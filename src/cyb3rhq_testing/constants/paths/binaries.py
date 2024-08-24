# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from cyb3rhq_testing.constants.platforms import WINDOWS

from . import CYB3RHQ_PATH

if sys.platform == WINDOWS:
    BIN_PATH = CYB3RHQ_PATH
    AGENT_AUTH_PATH = os.path.join(CYB3RHQ_PATH, 'agent-auth.exe')
else:
    BIN_PATH = os.path.join(CYB3RHQ_PATH, 'bin')
    AGENT_AUTH_PATH= os.path.join(BIN_PATH, 'agent-auth')

CYB3RHQ_CONTROL_PATH = os.path.join(BIN_PATH, 'cyb3rhq-control')
AGENT_AUTH_PATH = os.path.join(BIN_PATH, 'agent-auth')
ACTIVE_RESPONSE_BIN_PATH = os.path.join(CYB3RHQ_PATH, 'active-response', 'bin')
ACTIVE_RESPONSE_FIREWALL_DROP = os.path.join(ACTIVE_RESPONSE_BIN_PATH, 'firewall-drop')
MANAGE_AGENTS_BINARY = os.path.join(BIN_PATH, 'manage_agents')
AGENT_GROUPS_BINARY = os.path.join(BIN_PATH, 'agent_groups')
