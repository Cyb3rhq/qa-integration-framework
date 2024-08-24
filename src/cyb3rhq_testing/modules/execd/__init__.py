# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import sys

from cyb3rhq_testing.constants.platforms import WINDOWS


if sys.platform == WINDOWS:
    PREFIX = r'.*execd.*'
else:
    PREFIX = r'.*cyb3rhq-execd.*'
