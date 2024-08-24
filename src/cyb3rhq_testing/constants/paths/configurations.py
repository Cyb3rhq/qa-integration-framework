"""
Copyright (C) 2015-2023, Cyb3rhq Inc.
Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os
import sys

from cyb3rhq_testing.constants.platforms import WINDOWS

from . import CYB3RHQ_PATH
from cyb3rhq_testing.constants.paths.api import CYB3RHQ_API_FOLDER_PATH, CYB3RHQ_API_SECURITY_FOLDER_PATH


if sys.platform == WINDOWS:
    BASE_CONF_PATH = CYB3RHQ_PATH
else:
    BASE_CONF_PATH = os.path.join(CYB3RHQ_PATH, 'etc')

CYB3RHQ_CLIENT_KEYS_PATH = os.path.join(BASE_CONF_PATH, 'client.keys')
SHARED_CONFIGURATIONS_PATH = os.path.join(BASE_CONF_PATH, 'shared')
CYB3RHQ_CONF_PATH = os.path.join(BASE_CONF_PATH, 'ossec.conf')
CYB3RHQ_LOCAL_INTERNAL_OPTIONS = os.path.join(BASE_CONF_PATH, 'local_internal_options.conf')
ACTIVE_RESPONSE_CONFIGURATION = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
AR_CONF = os.path.join(SHARED_CONFIGURATIONS_PATH, 'ar.conf')
CUSTOM_RULES_PATH = os.path.join(BASE_CONF_PATH, 'rules')
CUSTOM_RULES_FILE = os.path.join(CUSTOM_RULES_PATH, 'local_rules.xml')
CUSTOM_DECODERS_PATH = os.path.join(BASE_CONF_PATH, 'decoders')
CUSTOM_DECODERS_FILE = os.path.join(CUSTOM_DECODERS_PATH, 'local_decoder.xml')
DEFAULT_AUTHD_PASS_PATH = os.path.join(BASE_CONF_PATH, 'authd.pass')

# Cyb3rhq API configurations path
CYB3RHQ_API_CONFIGURATION_PATH = os.path.join(CYB3RHQ_API_FOLDER_PATH, 'configuration', 'api.yaml')
CYB3RHQ_SECURITY_CONFIGURATION_PATH = os.path.join(CYB3RHQ_API_SECURITY_FOLDER_PATH, 'security.yaml')
