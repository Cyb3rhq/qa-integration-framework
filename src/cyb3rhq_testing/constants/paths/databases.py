# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import os
from . import CYB3RHQ_PATH


CVE_DB_PATH = os.path.join(CYB3RHQ_PATH, 'queue', 'vulnerabilities', 'cve.db')
CPE_HELPER_PATH = os.path.join(CYB3RHQ_PATH, 'queue', 'vulnerabilities', 'dictionaries', 'cpe_helper.json')
