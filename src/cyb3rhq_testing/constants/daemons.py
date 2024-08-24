# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

AGENT_DAEMON = 'cyb3rhq-agentd'
AGENTLESS_DAEMON = 'cyb3rhq-agentlessd'
ANALYSISD_DAEMON = 'cyb3rhq-analysisd'
API_DAEMON = 'cyb3rhq-apid'
AUTHD_DAEMON = 'cyb3rhq-authd'
CLUSTER_DAEMON = 'cyb3rhq-clusterd'
CSYSLOG_DAEMON = 'cyb3rhq-csyslogd'
EXEC_DAEMON = 'cyb3rhq-execd'
INTEGRATOR_DAEMON = 'cyb3rhq-integratord'
MAIL_DAEMON = 'cyb3rhq-maild'
MODULES_DAEMON = 'cyb3rhq-modulesd'
MONITOR_DAEMON = 'cyb3rhq-monitord'
LOGCOLLECTOR_DAEMON = 'cyb3rhq-logcollector'
REMOTE_DAEMON = 'cyb3rhq-remoted'
SYSCHECK_DAEMON = 'cyb3rhq-syscheckd'
CYB3RHQ_DB_DAEMON = 'cyb3rhq-db'

CYB3RHQ_AGENT_DAEMONS = [AGENT_DAEMON,
                       EXEC_DAEMON,
                       MODULES_DAEMON,
                       LOGCOLLECTOR_DAEMON,
                       SYSCHECK_DAEMON]

CYB3RHQ_MANAGER_DAEMONS = [AGENTLESS_DAEMON,
                         ANALYSISD_DAEMON,
                         API_DAEMON,
                         CLUSTER_DAEMON,
                         CSYSLOG_DAEMON,
                         EXEC_DAEMON,
                         INTEGRATOR_DAEMON,
                         LOGCOLLECTOR_DAEMON,
                         MAIL_DAEMON,
                         MODULES_DAEMON,
                         MONITOR_DAEMON,
                         REMOTE_DAEMON,
                         SYSCHECK_DAEMON,
                         CYB3RHQ_DB_DAEMON]

API_DAEMONS_REQUIREMENTS = [API_DAEMON,
                            CYB3RHQ_DB_DAEMON,
                            EXEC_DAEMON,
                            ANALYSISD_DAEMON,
                            REMOTE_DAEMON,
                            MODULES_DAEMON]

CYB3RHQ_AGENT = 'cyb3rhq-agent'
CYB3RHQ_MANAGER = 'cyb3rhq-manager'

CYB3RHQ_AGENT_WIN = 'cyb3rhq-agent.exe'
