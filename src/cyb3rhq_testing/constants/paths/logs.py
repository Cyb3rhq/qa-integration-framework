# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from cyb3rhq_testing.constants.platforms import WINDOWS

from . import CYB3RHQ_PATH


BASE_LOGS_PATH = os.path.join(CYB3RHQ_PATH, 'logs')

if sys.platform == WINDOWS:
    BASE_LOGS_PATH = CYB3RHQ_PATH
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-response', 'active-responses.log')
else:
    ACTIVE_RESPONSE_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'active-responses.log')

CYB3RHQ_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'ossec.log')
ALERTS_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.log')
ALERTS_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'alerts', 'alerts.json')
ARCHIVES_LOG_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.log')
ARCHIVES_JSON_PATH = os.path.join(BASE_LOGS_PATH, 'archives', 'archives.json')

# API logs paths
CYB3RHQ_API_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.log')
CYB3RHQ_API_JSON_LOG_FILE_PATH = os.path.join(BASE_LOGS_PATH, 'api.json')

CYB3RHQ_CLUSTER_LOGS_PATH = os.path.join(BASE_LOGS_PATH, 'cluster.log')

MACOS_LOG_COMMAND_PATH = '/usr/bin/log'
