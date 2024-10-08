"""
Copyright (C) 2015-2023, Cyb3rhq Inc.
Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
# Regular expressions
API_STARTED_MSG = r'.*Listening on \{host}:{port}.+'
API_TIMEOUT_ERROR_MSG = r'.*ERROR.*Timeout executing API request.*'
API_LOGIN_REQUEST_MSG = r'.*INFO.*{user}.*{host}.*{login_route}.*'

# Plain messages
API_LOGIN_ERROR_MSG = 'Could not get the login token.'
