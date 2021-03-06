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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AuthorizationManagementClientConfiguration
from .operations import DenyAssignmentsOperations
from . import models


class AuthorizationManagementClient(SDKClient):
    """Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to get deny assignments. A deny assignment describes the set of actions on resources that are denied for Azure Active Directory users.

    :ivar config: Configuration for client.
    :vartype config: AuthorizationManagementClientConfiguration

    :ivar deny_assignments: DenyAssignments operations
    :vartype deny_assignments: azure.mgmt.authorization.v2018_07_01_preview.operations.DenyAssignmentsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = AuthorizationManagementClientConfiguration(credentials, subscription_id, base_url)
        super(AuthorizationManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-07-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.deny_assignments = DenyAssignmentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
