from .._tensor import Tensor
from ..types import Shape
from ._ops import _get_dispatch_info, dispatch_signature2


def matmul(a: Tensor, b: Tensor) -> Tensor:
    """
    If both arguments are 2-D they are multiplied like conventional matrices.
    If either argument is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly.
    If the first argument is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed.
    If the second argument is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed.
    """
    _is_distributed, _device, _dtype = _get_dispatch_info([a, b])

    # both local
    from ..storage._helper import local_ops_helper

    local_ops = local_ops_helper(_device, _dtype)

    if not _is_distributed:
        storage = local_ops.matmul(a.storage, b.storage)
        return Tensor(storage)

    bc_shape_a = a.shape[:-2]
    bc_shape_b = b.shape[:-2]
    bs_shape = Shape.broadcast_shape([bc_shape_a, bc_shape_b], raise_exception=False)
    if bs_shape is None:
        raise ValueError("matmul: shape broadcast failed")

    if bc_shape_a.d_axis is not None:
        # distributed along bc part: (...,d,...,m, k) x (...,d,...,k, n) -> (...,d,..., m, n)
        # join and matmul
        return dispatch_signature2("matmul", a, b, [], {}, bc_shape_validate=False)

    mul_shape_a = a.shape[-2:]
    mul_shape_b = b.shape[-2:]
    if mul_shape_a.size[-1] != mul_shape_b.size[0]:
        raise ValueError("matmul: dimension mismatch: should be (..., n) x (...,n,?)")

    if mul_shape_a.is_d_axis(-2):
        raise ValueError(f"not supported distributed axis position (...,d,?) for left tensor {a}")
    if mul_shape_b.is_d_axis(-1):
        raise ValueError("not supported distributed axis position (...,?,d) for right tensor {b}")

    out_storage = a.storage.blocks.join(
        b.storage.blocks,
        apply_transpose(
            local_ops.matmul,
            a.storage.transposed,
            b.storage.transposed,
        ),
    ).reduce(local_ops.add)
    return Tensor(out_storage)


def apply_transpose(func, lf, rf):
    def _wrap(a, b):
        if lf:
            a = a.transpose()
        if rf:
            b = b.transpose()
        return func(a, b)

    return _wrap