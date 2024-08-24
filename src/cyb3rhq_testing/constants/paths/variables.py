# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
import sys

from cyb3rhq_testing.constants.platforms import WINDOWS

from . import CYB3RHQ_PATH


VAR_PATH = os.path.join(CYB3RHQ_PATH, 'var')
VAR_RUN_PATH = os.path.join(VAR_PATH, 'run')

ANALYSISD_STATE = os.path.join(VAR_RUN_PATH, 'cyb3rhq-analysisd.state')

if sys.platform == WINDOWS:
    VERSION_FILE = os.path.join(CYB3RHQ_PATH, 'VERSION')
    AGENTD_STATE = os.path.join(CYB3RHQ_PATH, 'cyb3rhq-agent.state')
else:
    VERSION_FILE = ''
    AGENTD_STATE = os.path.join(VAR_RUN_PATH, 'cyb3rhq-agentd.state')

VAR_MULTIGROUPS_PATH = os.path.join(VAR_PATH, 'multigroups')
