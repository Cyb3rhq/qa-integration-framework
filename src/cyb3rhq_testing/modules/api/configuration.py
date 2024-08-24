"""
Copyright (C) 2015-2023, Cyb3rhq Inc.
Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
This program is free software; you can redistribute it and/or modify it under the terms of GPLv2
"""
from pathlib import Path

from cyb3rhq_testing.constants.paths.configurations import CYB3RHQ_API_CONFIGURATION_PATH, CYB3RHQ_SECURITY_CONFIGURATION_PATH
from cyb3rhq_testing.constants.api import CONFIGURATION_TYPES
from cyb3rhq_testing.utils.file import read_yaml, append_content_to_yaml, remove_file, truncate_file, write_file


def check_configuration_type(configuration_type: str) -> None:
    """Check if the configuration type is allowed.

    Args:
        configuration_type (str): Configuration type.

    Raises:
        RuntimeError: When the configuration type is not allowed.
    """
    if configuration_type not in CONFIGURATION_TYPES:
        raise RuntimeError(f"The chosen option is not allowed, use one of these: {CONFIGURATION_TYPES}")


def set_target_configuration_file(configuration_type: str) -> str:
    """Set the target configuration filepath where the actions will be performed.

    Args:
        configuration_type (str): Configuration type.

    Returns:
        cyb3rhq_api_configuration_path (str): Path to the chosen Cyb3rhq API configuration file.
    """
    check_configuration_type(configuration_type)
    configuration_files = {'base': CYB3RHQ_API_CONFIGURATION_PATH, 'security': CYB3RHQ_SECURITY_CONFIGURATION_PATH}
    cyb3rhq_api_configuration_path = configuration_files[configuration_type]

    return cyb3rhq_api_configuration_path


def get_configuration(configuration_type: str = 'base') -> dict:
    """Get current content from the chosen Cyb3rhq API configuration file.

    Args:
        configuration_type (str): Choose file from which the configuration will be obtained.

    Returns:
        current_configuration (dict): Current content of the `api.yaml` file.
    """
    target_file = set_target_configuration_file(configuration_type)

    return read_yaml(target_file) if Path(target_file).exists() else None


def append_configuration(cyb3rhq_api_configuration_content: dict, configuration_type: str = 'base') -> None:
    """Write a new configuration at the end of the Cyb3rhq API configuration file.

    Args:
        configuration_type (str): Choose configuration file to be removed.
        cyb3rhq_api_configuration_content (dict): Content to be written in the given file.
    """
    target_file = set_target_configuration_file(configuration_type)
    if not Path(target_file).exists():
        write_file(target_file)

    if cyb3rhq_api_configuration_content is None:
        truncate_file(target_file)
    else:
        append_content_to_yaml(target_file, cyb3rhq_api_configuration_content)


def delete_configuration_file(configuration_type: str = 'base') -> None:
    """Delete chosen Cyb3rhq API configuration file.

    Args:
        configuration_type (str): Choose configuration file to be removed.
    """
    remove_file(set_target_configuration_file(configuration_type))
