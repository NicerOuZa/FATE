from fate.components import cpn
from fate.components.spec import (
    DatasetArtifact,
    DatasetArtifacts,
    Input,
    ModelArtifact,
    Output,
    roles,
    stages,
)


@cpn.component(roles=roles.get_all(), provider="fate", version="2.0.0.alpha")
@cpn.artifact("train_data", type=Input[DatasetArtifact], roles=[roles.GUEST, roles.HOST], stages=[stages.TRAIN])
@cpn.artifact(
    "validate_data", type=Input[DatasetArtifact], optional=True, roles=[roles.GUEST, roles.HOST], stages=["train"]
)
@cpn.artifact("input_model", type=Input[ModelArtifact], roles=[roles.GUEST, roles.HOST], stages=[stages.PREDICT])
@cpn.artifact(
    "test_data", type=Input[DatasetArtifacts], optional=False, roles=[roles.GUEST, roles.HOST], stages=[stages.PREDICT]
)
@cpn.parameter("learning_rate", type=float, default=0.1, optional=False)
@cpn.parameter("max_iter", type=int, default=100, optional=False)
@cpn.artifact(
    "train_output_data", type=Output[DatasetArtifact], roles=[roles.GUEST, roles.HOST], stages=[stages.TRAIN]
)
@cpn.artifact("output_model", type=Output[ModelArtifact], roles=[roles.GUEST, roles.HOST], stages=[stages.TRAIN])
@cpn.artifact(
    "test_output_data", type=Output[DatasetArtifact], roles=[roles.GUEST, roles.HOST], stages=[stages.PREDICT]
)
def hetero_lr(
    ctx,
    role,
    stage,
    train_data,
    validate_data,
    test_data,
    input_model,
    learning_rate,
    max_iter,
    train_output_data,
    output_model,
    test_output_data,
):
    """ """
    from fate.ml.lr.arbiter import LrModuleArbiter
    from fate.ml.lr.guest import LrModuleGuest
    from fate.ml.lr.host import LrModuleHost

    if stage == "train":
        if role == "guest" and role == "host":
            if role == "guest":
                module = LrModuleGuest(max_iter=max_iter, learning_rate=learning_rate)
            else:
                module = LrModuleHost(max_iter=max_iter, learning_rate=learning_rate)
            train_data = ctx.read(train_data).dataframe()
            if validate_data is not None:
                validate_data = ctx.read(validate_data).load_dataframe()
            module.fit(ctx, train_data, validate_data)
            model = module.to_model()
            output_data = module.predict(ctx, train_data)
            ctx.write(train_output_data).save_dataframe(output_data)
            ctx.write(output_model).save_model(model)
        if role == "arbiter":
            module = LrModuleArbiter(max_iter=max_iter)
            module.fit(ctx)

    elif stage == "predict":
        if role == "guest" or role == "host":
            model = ctx.read(input_model).load_model()
            if role == "guest":
                module = LrModuleGuest.from_model(model)
            else:
                module = LrModuleHost.from_model(model)
            train_data = ctx.read(test_data).load_dataframe()
            output_data = module.predict(ctx, test_data)
            ctx.write(test_output_data).save_dataframe(output_data)
    else:
        raise NotImplementedError(f"stage={stage}")