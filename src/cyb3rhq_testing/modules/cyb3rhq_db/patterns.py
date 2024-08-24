# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

from . import CYB3RHQ_DB_PREFIX

BACKUP_CREATION_CALLBACK = r'.*Created Global database backup "(backup/db/global.db-backup.*.gz)"'
WRONG_INTERVAL_CALLBACK = r".*Invalid value for element ('interval':.*)"
WRONG_MAX_FILES_CALLBACK = r".*Invalid value for element ('max_files':.*)"
