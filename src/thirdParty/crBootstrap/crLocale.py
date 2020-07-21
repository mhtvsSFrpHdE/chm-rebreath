# Need to know the language a user using are

import locale as _locale

from os import path as _osPath
from pathlib import Path as _plPath

# Shortcut to getdefaultlocale()[0]
# Expected result: "en_US"


def get_system_language():

    return _locale.getdefaultlocale()[0]

# Preprocess config
# the config should not change by code after preprocess


def _my_locale_parser(config_environment):
    # Get current system language
    language_root = config_environment['language']['root_path']
    system_language = get_system_language()
    current_language = language_root + system_language + '/'  # language/en_US/

    # Confirm the language files are exists.
    # If not, use default fallback language
    current_language_exists = _osPath.exists(_plPath(current_language))
    if current_language_exists is False:
        current_language = config_environment['language']['fallback_path']

    # Apply language to path
    config_message_path = config_environment['message']['message_config_path']
    config_message_path = current_language + config_message_path  # language/en_US/message.xml

    # Put it back
    config_environment['message']['config_message_path'] = config_message_path

    return config_environment

# apply_locale_to_environment_config


def apply_locale_to_environment_config(config_environment):
    return _my_locale_parser(config_environment)
