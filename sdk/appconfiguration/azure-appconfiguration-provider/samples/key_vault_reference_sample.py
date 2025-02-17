# ------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# -------------------------------------------------------------------------

from azure.appconfiguration.provider import load, AzureAppConfigurationKeyVaultOptions, SettingSelector
import os
from sample_utilities import get_authority, get_audience, get_credential, get_client_modifications

endpoint = os.environ.get("APPCONFIGURATION_ENDPOINT_STRING")
authority = get_authority(endpoint)
audience = get_audience(authority)
credential = get_credential(authority)
kwargs = get_client_modifications()

# Connection to Azure App Configuration using AAD and Resolving Key Vault References
key_vault_options = AzureAppConfigurationKeyVaultOptions(credential=credential)
selects = {SettingSelector(key_filter="*", label_filter="prod")}

config = load(endpoint=endpoint, credential=credential, key_vault_options=key_vault_options, selects=selects, **kwargs)

print(config["secret"])
