# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: queries.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import primitive_pb2 as primitive__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rqueries.proto\x12\x0eiroha.protocol\x1a\x0fprimitive.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa9\x01\n\x08Ordering\x12\x38\n\x08sequence\x18\x01 \x03(\x0b\x32&.iroha.protocol.Ordering.FieldOrdering\x1a\x63\n\rFieldOrdering\x12$\n\x05\x66ield\x18\x01 \x01(\x0e\x32\x15.iroha.protocol.Field\x12,\n\tdirection\x18\x02 \x01(\x0e\x32\x19.iroha.protocol.Direction\"\xf3\x02\n\x10TxPaginationMeta\x12\x11\n\tpage_size\x18\x01 \x01(\r\x12\x17\n\rfirst_tx_hash\x18\x02 \x01(\tH\x00\x12*\n\x08ordering\x18\x03 \x01(\x0b\x32\x18.iroha.protocol.Ordering\x12\x33\n\rfirst_tx_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x12\x32\n\x0clast_tx_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x02\x12\x19\n\x0f\x66irst_tx_height\x18\x06 \x01(\x04H\x03\x12\x18\n\x0elast_tx_height\x18\x07 \x01(\x04H\x04\x42\x13\n\x11opt_first_tx_hashB\x13\n\x11opt_first_tx_timeB\x12\n\x10opt_last_tx_timeB\x15\n\x13opt_first_tx_heightB\x14\n\x12opt_last_tx_height\"X\n\x13\x41ssetPaginationMeta\x12\x11\n\tpage_size\x18\x01 \x01(\r\x12\x18\n\x0e\x66irst_asset_id\x18\x02 \x01(\tH\x00\x42\x14\n\x12opt_first_asset_id\" \n\nGetAccount\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\x1a\n\x08GetBlock\x12\x0e\n\x06height\x18\x01 \x01(\x04\"$\n\x0eGetSignatories\x12\x12\n\naccount_id\x18\x01 \x01(\t\"g\n\x16GetAccountTransactions\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x39\n\x0fpagination_meta\x18\x02 \x01(\x0b\x32 .iroha.protocol.TxPaginationMeta\"~\n\x1bGetAccountAssetTransactions\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x10\n\x08\x61sset_id\x18\x02 \x01(\t\x12\x39\n\x0fpagination_meta\x18\x03 \x01(\x0b\x32 .iroha.protocol.TxPaginationMeta\"$\n\x0fGetTransactions\x12\x11\n\ttx_hashes\x18\x01 \x03(\t\"d\n\x10GetAccountAssets\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12<\n\x0fpagination_meta\x18\x02 \x01(\x0b\x32#.iroha.protocol.AssetPaginationMeta\"p\n\x1b\x41\x63\x63ountDetailPaginationMeta\x12\x11\n\tpage_size\x18\x01 \x01(\r\x12>\n\x0f\x66irst_record_id\x18\x02 \x01(\x0b\x32%.iroha.protocol.AccountDetailRecordId\"\xba\x01\n\x10GetAccountDetail\x12\x14\n\naccount_id\x18\x01 \x01(\tH\x00\x12\r\n\x03key\x18\x02 \x01(\tH\x01\x12\x10\n\x06writer\x18\x03 \x01(\tH\x02\x12\x44\n\x0fpagination_meta\x18\x04 \x01(\x0b\x32+.iroha.protocol.AccountDetailPaginationMetaB\x10\n\x0eopt_account_idB\t\n\x07opt_keyB\x0c\n\nopt_writer\" \n\x0cGetAssetInfo\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\"\n\n\x08GetRoles\"%\n\x12GetRolePermissions\x12\x0f\n\x07role_id\x18\x01 \x01(\t\"S\n\x16GetPendingTransactions\x12\x39\n\x0fpagination_meta\x18\x01 \x01(\x0b\x32 .iroha.protocol.TxPaginationMeta\"\n\n\x08GetPeers\"[\n\x10QueryPayloadMeta\x12\x14\n\x0c\x63reated_time\x18\x01 \x01(\x04\x12\x1a\n\x12\x63reator_account_id\x18\x02 \x01(\t\x12\x15\n\rquery_counter\x18\x03 \x01(\x04\"$\n\x11GetEngineReceipts\x12\x0f\n\x07tx_hash\x18\x01 \x01(\t\"\x8f\x08\n\x05Query\x12.\n\x07payload\x18\x01 \x01(\x0b\x32\x1d.iroha.protocol.Query.Payload\x12,\n\tsignature\x18\x02 \x01(\x0b\x32\x19.iroha.protocol.Signature\x1a\xa7\x07\n\x07Payload\x12.\n\x04meta\x18\x01 \x01(\x0b\x32 .iroha.protocol.QueryPayloadMeta\x12\x31\n\x0bget_account\x18\x03 \x01(\x0b\x32\x1a.iroha.protocol.GetAccountH\x00\x12\x39\n\x0fget_signatories\x18\x04 \x01(\x0b\x32\x1e.iroha.protocol.GetSignatoriesH\x00\x12J\n\x18get_account_transactions\x18\x05 \x01(\x0b\x32&.iroha.protocol.GetAccountTransactionsH\x00\x12U\n\x1eget_account_asset_transactions\x18\x06 \x01(\x0b\x32+.iroha.protocol.GetAccountAssetTransactionsH\x00\x12;\n\x10get_transactions\x18\x07 \x01(\x0b\x32\x1f.iroha.protocol.GetTransactionsH\x00\x12>\n\x12get_account_assets\x18\x08 \x01(\x0b\x32 .iroha.protocol.GetAccountAssetsH\x00\x12>\n\x12get_account_detail\x18\t \x01(\x0b\x32 .iroha.protocol.GetAccountDetailH\x00\x12-\n\tget_roles\x18\n \x01(\x0b\x32\x18.iroha.protocol.GetRolesH\x00\x12\x42\n\x14get_role_permissions\x18\x0b \x01(\x0b\x32\".iroha.protocol.GetRolePermissionsH\x00\x12\x36\n\x0eget_asset_info\x18\x0c \x01(\x0b\x32\x1c.iroha.protocol.GetAssetInfoH\x00\x12J\n\x18get_pending_transactions\x18\r \x01(\x0b\x32&.iroha.protocol.GetPendingTransactionsH\x00\x12-\n\tget_block\x18\x0e \x01(\x0b\x32\x18.iroha.protocol.GetBlockH\x00\x12-\n\tget_peers\x18\x0f \x01(\x0b\x32\x18.iroha.protocol.GetPeersH\x00\x12@\n\x13get_engine_receipts\x18\x10 \x01(\x0b\x32!.iroha.protocol.GetEngineReceiptsH\x00\x42\x07\n\x05query\"k\n\x0b\x42locksQuery\x12.\n\x04meta\x18\x01 \x01(\x0b\x32 .iroha.protocol.QueryPayloadMeta\x12,\n\tsignature\x18\x02 \x01(\x0b\x32\x19.iroha.protocol.Signature*(\n\x05\x46ield\x12\x10\n\x0ckCreatedTime\x10\x00\x12\r\n\tkPosition\x10\x01*,\n\tDirection\x12\x0e\n\nkAscending\x10\x00\x12\x0f\n\x0bkDescending\x10\x01\x42\x1aZ\x18iroha.generated/protocolb\x06proto3')

_FIELD = DESCRIPTOR.enum_types_by_name['Field']
Field = enum_type_wrapper.EnumTypeWrapper(_FIELD)
_DIRECTION = DESCRIPTOR.enum_types_by_name['Direction']
Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
kCreatedTime = 0
kPosition = 1
kAscending = 0
kDescending = 1


_ORDERING = DESCRIPTOR.message_types_by_name['Ordering']
_ORDERING_FIELDORDERING = _ORDERING.nested_types_by_name['FieldOrdering']
_TXPAGINATIONMETA = DESCRIPTOR.message_types_by_name['TxPaginationMeta']
_ASSETPAGINATIONMETA = DESCRIPTOR.message_types_by_name['AssetPaginationMeta']
_GETACCOUNT = DESCRIPTOR.message_types_by_name['GetAccount']
_GETBLOCK = DESCRIPTOR.message_types_by_name['GetBlock']
_GETSIGNATORIES = DESCRIPTOR.message_types_by_name['GetSignatories']
_GETACCOUNTTRANSACTIONS = DESCRIPTOR.message_types_by_name['GetAccountTransactions']
_GETACCOUNTASSETTRANSACTIONS = DESCRIPTOR.message_types_by_name['GetAccountAssetTransactions']
_GETTRANSACTIONS = DESCRIPTOR.message_types_by_name['GetTransactions']
_GETACCOUNTASSETS = DESCRIPTOR.message_types_by_name['GetAccountAssets']
_ACCOUNTDETAILPAGINATIONMETA = DESCRIPTOR.message_types_by_name['AccountDetailPaginationMeta']
_GETACCOUNTDETAIL = DESCRIPTOR.message_types_by_name['GetAccountDetail']
_GETASSETINFO = DESCRIPTOR.message_types_by_name['GetAssetInfo']
_GETROLES = DESCRIPTOR.message_types_by_name['GetRoles']
_GETROLEPERMISSIONS = DESCRIPTOR.message_types_by_name['GetRolePermissions']
_GETPENDINGTRANSACTIONS = DESCRIPTOR.message_types_by_name['GetPendingTransactions']
_GETPEERS = DESCRIPTOR.message_types_by_name['GetPeers']
_QUERYPAYLOADMETA = DESCRIPTOR.message_types_by_name['QueryPayloadMeta']
_GETENGINERECEIPTS = DESCRIPTOR.message_types_by_name['GetEngineReceipts']
_QUERY = DESCRIPTOR.message_types_by_name['Query']
_QUERY_PAYLOAD = _QUERY.nested_types_by_name['Payload']
_BLOCKSQUERY = DESCRIPTOR.message_types_by_name['BlocksQuery']
Ordering = _reflection.GeneratedProtocolMessageType('Ordering', (_message.Message,), {

  'FieldOrdering' : _reflection.GeneratedProtocolMessageType('FieldOrdering', (_message.Message,), {
    'DESCRIPTOR' : _ORDERING_FIELDORDERING,
    '__module__' : 'queries_pb2'
    # @@protoc_insertion_point(class_scope:iroha.protocol.Ordering.FieldOrdering)
    })
  ,
  'DESCRIPTOR' : _ORDERING,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Ordering)
  })
_sym_db.RegisterMessage(Ordering)
_sym_db.RegisterMessage(Ordering.FieldOrdering)

TxPaginationMeta = _reflection.GeneratedProtocolMessageType('TxPaginationMeta', (_message.Message,), {
  'DESCRIPTOR' : _TXPAGINATIONMETA,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.TxPaginationMeta)
  })
_sym_db.RegisterMessage(TxPaginationMeta)

AssetPaginationMeta = _reflection.GeneratedProtocolMessageType('AssetPaginationMeta', (_message.Message,), {
  'DESCRIPTOR' : _ASSETPAGINATIONMETA,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AssetPaginationMeta)
  })
_sym_db.RegisterMessage(AssetPaginationMeta)

GetAccount = _reflection.GeneratedProtocolMessageType('GetAccount', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNT,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccount)
  })
_sym_db.RegisterMessage(GetAccount)

GetBlock = _reflection.GeneratedProtocolMessageType('GetBlock', (_message.Message,), {
  'DESCRIPTOR' : _GETBLOCK,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetBlock)
  })
_sym_db.RegisterMessage(GetBlock)

GetSignatories = _reflection.GeneratedProtocolMessageType('GetSignatories', (_message.Message,), {
  'DESCRIPTOR' : _GETSIGNATORIES,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetSignatories)
  })
_sym_db.RegisterMessage(GetSignatories)

GetAccountTransactions = _reflection.GeneratedProtocolMessageType('GetAccountTransactions', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTTRANSACTIONS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountTransactions)
  })
_sym_db.RegisterMessage(GetAccountTransactions)

GetAccountAssetTransactions = _reflection.GeneratedProtocolMessageType('GetAccountAssetTransactions', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTASSETTRANSACTIONS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountAssetTransactions)
  })
_sym_db.RegisterMessage(GetAccountAssetTransactions)

GetTransactions = _reflection.GeneratedProtocolMessageType('GetTransactions', (_message.Message,), {
  'DESCRIPTOR' : _GETTRANSACTIONS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetTransactions)
  })
_sym_db.RegisterMessage(GetTransactions)

GetAccountAssets = _reflection.GeneratedProtocolMessageType('GetAccountAssets', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTASSETS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountAssets)
  })
_sym_db.RegisterMessage(GetAccountAssets)

AccountDetailPaginationMeta = _reflection.GeneratedProtocolMessageType('AccountDetailPaginationMeta', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDETAILPAGINATIONMETA,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.AccountDetailPaginationMeta)
  })
_sym_db.RegisterMessage(AccountDetailPaginationMeta)

GetAccountDetail = _reflection.GeneratedProtocolMessageType('GetAccountDetail', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTDETAIL,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAccountDetail)
  })
_sym_db.RegisterMessage(GetAccountDetail)

GetAssetInfo = _reflection.GeneratedProtocolMessageType('GetAssetInfo', (_message.Message,), {
  'DESCRIPTOR' : _GETASSETINFO,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetAssetInfo)
  })
_sym_db.RegisterMessage(GetAssetInfo)

GetRoles = _reflection.GeneratedProtocolMessageType('GetRoles', (_message.Message,), {
  'DESCRIPTOR' : _GETROLES,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetRoles)
  })
_sym_db.RegisterMessage(GetRoles)

GetRolePermissions = _reflection.GeneratedProtocolMessageType('GetRolePermissions', (_message.Message,), {
  'DESCRIPTOR' : _GETROLEPERMISSIONS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetRolePermissions)
  })
_sym_db.RegisterMessage(GetRolePermissions)

GetPendingTransactions = _reflection.GeneratedProtocolMessageType('GetPendingTransactions', (_message.Message,), {
  'DESCRIPTOR' : _GETPENDINGTRANSACTIONS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetPendingTransactions)
  })
_sym_db.RegisterMessage(GetPendingTransactions)

GetPeers = _reflection.GeneratedProtocolMessageType('GetPeers', (_message.Message,), {
  'DESCRIPTOR' : _GETPEERS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetPeers)
  })
_sym_db.RegisterMessage(GetPeers)

QueryPayloadMeta = _reflection.GeneratedProtocolMessageType('QueryPayloadMeta', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPAYLOADMETA,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.QueryPayloadMeta)
  })
_sym_db.RegisterMessage(QueryPayloadMeta)

GetEngineReceipts = _reflection.GeneratedProtocolMessageType('GetEngineReceipts', (_message.Message,), {
  'DESCRIPTOR' : _GETENGINERECEIPTS,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.GetEngineReceipts)
  })
_sym_db.RegisterMessage(GetEngineReceipts)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {
    'DESCRIPTOR' : _QUERY_PAYLOAD,
    '__module__' : 'queries_pb2'
    # @@protoc_insertion_point(class_scope:iroha.protocol.Query.Payload)
    })
  ,
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.Query)
  })
_sym_db.RegisterMessage(Query)
_sym_db.RegisterMessage(Query.Payload)

BlocksQuery = _reflection.GeneratedProtocolMessageType('BlocksQuery', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKSQUERY,
  '__module__' : 'queries_pb2'
  # @@protoc_insertion_point(class_scope:iroha.protocol.BlocksQuery)
  })
_sym_db.RegisterMessage(BlocksQuery)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\030iroha.generated/protocol'
  _FIELD._serialized_start=2959
  _FIELD._serialized_end=2999
  _DIRECTION._serialized_start=3001
  _DIRECTION._serialized_end=3045
  _ORDERING._serialized_start=84
  _ORDERING._serialized_end=253
  _ORDERING_FIELDORDERING._serialized_start=154
  _ORDERING_FIELDORDERING._serialized_end=253
  _TXPAGINATIONMETA._serialized_start=256
  _TXPAGINATIONMETA._serialized_end=627
  _ASSETPAGINATIONMETA._serialized_start=629
  _ASSETPAGINATIONMETA._serialized_end=717
  _GETACCOUNT._serialized_start=719
  _GETACCOUNT._serialized_end=751
  _GETBLOCK._serialized_start=753
  _GETBLOCK._serialized_end=779
  _GETSIGNATORIES._serialized_start=781
  _GETSIGNATORIES._serialized_end=817
  _GETACCOUNTTRANSACTIONS._serialized_start=819
  _GETACCOUNTTRANSACTIONS._serialized_end=922
  _GETACCOUNTASSETTRANSACTIONS._serialized_start=924
  _GETACCOUNTASSETTRANSACTIONS._serialized_end=1050
  _GETTRANSACTIONS._serialized_start=1052
  _GETTRANSACTIONS._serialized_end=1088
  _GETACCOUNTASSETS._serialized_start=1090
  _GETACCOUNTASSETS._serialized_end=1190
  _ACCOUNTDETAILPAGINATIONMETA._serialized_start=1192
  _ACCOUNTDETAILPAGINATIONMETA._serialized_end=1304
  _GETACCOUNTDETAIL._serialized_start=1307
  _GETACCOUNTDETAIL._serialized_end=1493
  _GETASSETINFO._serialized_start=1495
  _GETASSETINFO._serialized_end=1527
  _GETROLES._serialized_start=1529
  _GETROLES._serialized_end=1539
  _GETROLEPERMISSIONS._serialized_start=1541
  _GETROLEPERMISSIONS._serialized_end=1578
  _GETPENDINGTRANSACTIONS._serialized_start=1580
  _GETPENDINGTRANSACTIONS._serialized_end=1663
  _GETPEERS._serialized_start=1665
  _GETPEERS._serialized_end=1675
  _QUERYPAYLOADMETA._serialized_start=1677
  _QUERYPAYLOADMETA._serialized_end=1768
  _GETENGINERECEIPTS._serialized_start=1770
  _GETENGINERECEIPTS._serialized_end=1806
  _QUERY._serialized_start=1809
  _QUERY._serialized_end=2848
  _QUERY_PAYLOAD._serialized_start=1913
  _QUERY_PAYLOAD._serialized_end=2848
  _BLOCKSQUERY._serialized_start=2850
  _BLOCKSQUERY._serialized_end=2957
# @@protoc_insertion_point(module_scope)