# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: onehot-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='onehot-meta.proto',
  package='com.webank.ai.fate.common.mlmodel.buffer',
  syntax='proto3',
  serialized_pb=_b('\n\x11onehot-meta.proto\x12(com.webank.ai.fate.common.mlmodel.buffer\"\x1a\n\nOneHotMeta\x12\x0c\n\x04\x63ols\x18\x01 \x03(\tB\x11\x42\x0fOneHotMetaProtob\x06proto3')
)




_ONEHOTMETA = _descriptor.Descriptor(
  name='OneHotMeta',
  full_name='com.webank.ai.fate.common.mlmodel.buffer.OneHotMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cols', full_name='com.webank.ai.fate.common.mlmodel.buffer.OneHotMeta.cols', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['OneHotMeta'] = _ONEHOTMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OneHotMeta = _reflection.GeneratedProtocolMessageType('OneHotMeta', (_message.Message,), dict(
  DESCRIPTOR = _ONEHOTMETA,
  __module__ = 'onehot_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.common.mlmodel.buffer.OneHotMeta)
  ))
_sym_db.RegisterMessage(OneHotMeta)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\017OneHotMetaProto'))
# @@protoc_insertion_point(module_scope)
