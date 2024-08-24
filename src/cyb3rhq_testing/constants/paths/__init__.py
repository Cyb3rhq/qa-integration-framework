# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import sys
import os

from cyb3rhq_testing.constants.platforms import MACOS, WINDOWS

TEMP_FILE_PATH = '/tmp'

if sys.platform == WINDOWS:
    CYB3RHQ_PATH = os.path.join("C:", os.sep, "Program Files (x86)", "ossec-agent")
    ROOT_PREFIX = os.path.join('c:', os.sep)

elif sys.platform == MACOS:
    CYB3RHQ_PATH = os.path.join("/", "Library", "Ossec")
    ROOT_PREFIX = os.path.join('/', 'private', 'var', 'root')

else:
    CYB3RHQ_PATH = os.path.join("/", "var", "ossec")
    ROOT_PREFIX = os.sep
