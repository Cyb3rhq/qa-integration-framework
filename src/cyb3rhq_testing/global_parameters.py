# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
import sys

from collections import defaultdict

from cyb3rhq_testing.constants.platforms import LINUX, MACOS, WINDOWS


class GlobalParameters:
    """Class to allocate all global parameters for testing"""

    def __init__(self):
        timeouts = defaultdict(lambda: 10)
        timeouts[LINUX] = 5
        timeouts[MACOS] = 5
        timeouts[WINDOWS] = 60
        self._default_timeout = timeouts[sys.platform]

    @property
    def default_timeout(self):
        """Getter method for the default timeout property

        Returns:
            int: representing the default timeout in seconds
        """
        return self._default_timeout

    @default_timeout.setter
    def default_timeout(self, value):
        """Setter method for the default timeout property

        Args:
            value (int): New value for the default timeout. Must be in seconds.
        """
        self._default_timeout = value

    @property
    def current_configuration(self):
        """Getter method for the current configuration property

        Returns:
            dict: A dictionary containing the current configuration.
        """
        return self._current_configuration

    @current_configuration.setter
    def current_configuration(self, value):
        """Setter method for the current configuration property

        Args:
            value (dict): New value for the current configuration.
        """
        self._current_configuration = value
