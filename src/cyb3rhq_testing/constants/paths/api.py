"""
Copyright (C) 2015-2023, Cyb3rhq Inc.
Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os

from . import CYB3RHQ_PATH

# API paths that do not fit in `configurations`

# Folders
CYB3RHQ_API_FOLDER_PATH = os.path.join(CYB3RHQ_PATH, 'api')
CYB3RHQ_API_CONFIGURATION_FOLDER_PATH = os.path.join(CYB3RHQ_API_FOLDER_PATH, 'configuration')
CYB3RHQ_API_SECURITY_FOLDER_PATH = os.path.join(CYB3RHQ_API_CONFIGURATION_FOLDER_PATH, 'security')
CYB3RHQ_API_SCRIPTS_FOLDER_PATH = os.path.join(CYB3RHQ_API_FOLDER_PATH, 'scripts')

# API scripts paths
CYB3RHQ_API_SCRIPT = os.path.join(CYB3RHQ_API_SCRIPTS_FOLDER_PATH, 'cyb3rhq_apid.py')

# Databases paths
RBAC_DATABASE_PATH = os.path.join(CYB3RHQ_API_SECURITY_FOLDER_PATH, 'rbac.db')

# SSL paths
CYB3RHQ_API_CERTIFICATE = os.path.join(CYB3RHQ_API_CONFIGURATION_FOLDER_PATH, 'ssl', 'server.crt')
