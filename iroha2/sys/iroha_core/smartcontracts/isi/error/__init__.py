from .....rust import Enum, Struct, Tuple, Dict
FindError = Enum[("Asset", "iroha_data_model.asset.Id"), ("AssetDefinition", "iroha_data_model.asset.DefinitionId"), ("Account", "iroha_data_model.account.Id"), ("Domain", "iroha_data_model.domain.Id"), ("MetadataKey", "iroha_data_model.Name"), ("Block", "iroha_core.smartcontracts.isi.error.ParentHashNotFound"), ("Transaction", "iroha_crypto.hash.HashOf"), ("Context", str), ("Peer", "iroha_data_model.peer.Id"), ("Trigger", "iroha_data_model.trigger.Id"), ("Role", "iroha_data_model.role.Id")] 
ParentHashNotFound = Tuple["iroha_crypto.hash.HashOf"]