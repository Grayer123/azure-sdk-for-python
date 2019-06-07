# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .mongo_db_object_info import MongoDbObjectInfo


class MongoDbCollectionInfo(MongoDbObjectInfo):
    """Describes a supported collection within a MongoDB database.

    All required parameters must be populated in order to send to Azure.

    :param average_document_size: Required. The average document size, or -1
     if the average size is unknown
    :type average_document_size: long
    :param data_size: Required. The estimated total data size, in bytes, or -1
     if the size is unknown.
    :type data_size: long
    :param document_count: Required. The estimated total number of documents,
     or -1 if the document count is unknown
    :type document_count: long
    :param name: Required. The unqualified name of the database or collection
    :type name: str
    :param qualified_name: Required. The qualified name of the database or
     collection. For a collection, this is the database-qualified name.
    :type qualified_name: str
    :param database_name: Required. The name of the database containing the
     collection
    :type database_name: str
    :param is_capped: Required. Whether the collection is a capped collection
     (i.e. whether it has a fixed size and acts like a circular buffer)
    :type is_capped: bool
    :param is_system_collection: Required. Whether the collection is system
     collection
    :type is_system_collection: bool
    :param is_view: Required. Whether the collection is a view of another
     collection
    :type is_view: bool
    :param shard_key: The shard key on the collection, or null if the
     collection is not sharded
    :type shard_key: ~azure.mgmt.datamigration.models.MongoDbShardKeyInfo
    :param supports_sharding: Required. Whether the database has sharding
     enabled. Note that the migration task will enable sharding on the target
     if necessary.
    :type supports_sharding: bool
    :param view_of: The name of the collection that this is a view of, if
     IsView is true
    :type view_of: str
    """

    _validation = {
        'average_document_size': {'required': True},
        'data_size': {'required': True},
        'document_count': {'required': True},
        'name': {'required': True},
        'qualified_name': {'required': True},
        'database_name': {'required': True},
        'is_capped': {'required': True},
        'is_system_collection': {'required': True},
        'is_view': {'required': True},
        'supports_sharding': {'required': True},
    }

    _attribute_map = {
        'average_document_size': {'key': 'averageDocumentSize', 'type': 'long'},
        'data_size': {'key': 'dataSize', 'type': 'long'},
        'document_count': {'key': 'documentCount', 'type': 'long'},
        'name': {'key': 'name', 'type': 'str'},
        'qualified_name': {'key': 'qualifiedName', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'is_capped': {'key': 'isCapped', 'type': 'bool'},
        'is_system_collection': {'key': 'isSystemCollection', 'type': 'bool'},
        'is_view': {'key': 'isView', 'type': 'bool'},
        'shard_key': {'key': 'shardKey', 'type': 'MongoDbShardKeyInfo'},
        'supports_sharding': {'key': 'supportsSharding', 'type': 'bool'},
        'view_of': {'key': 'viewOf', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(MongoDbCollectionInfo, self).__init__(**kwargs)
        self.database_name = kwargs.get('database_name', None)
        self.is_capped = kwargs.get('is_capped', None)
        self.is_system_collection = kwargs.get('is_system_collection', None)
        self.is_view = kwargs.get('is_view', None)
        self.shard_key = kwargs.get('shard_key', None)
        self.supports_sharding = kwargs.get('supports_sharding', None)
        self.view_of = kwargs.get('view_of', None)