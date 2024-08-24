"""
Copyright (C) 2015-2023, Cyb3rhq Inc.
Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
import os

from . import CYB3RHQ_PATH


# Paths that are mainly used by the Analysisd module but serves to other modules too
DEFAULT_RULESET_PATH = os.path.join(CYB3RHQ_PATH, 'ruleset')
DEFAULT_RULES_PATH = os.path.join(DEFAULT_RULESET_PATH, 'rules')
DEFAULT_DECODERS_PATH = os.path.join(DEFAULT_RULESET_PATH, 'decoders')
CIS_RULESET_PATH = os.path.join(DEFAULT_RULESET_PATH, 'sca')
