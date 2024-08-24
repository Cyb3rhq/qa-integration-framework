# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
from cyb3rhq_testing.constants.paths.variables import AGENTD_STATE


def parse_state_file():
    """Parse state file

    Returns:
        state info
    """
    state = {}
    with open(AGENTD_STATE) as state_file:
        for line in state_file:
            line = line.rstrip('\n')
            # Remove empty lines or comments
            if not line or line.startswith('#'):
                continue
            (key, value) = line.split('=', 1)
            # Remove value's quotes
            state[key] = value.strip("'")

    return state
