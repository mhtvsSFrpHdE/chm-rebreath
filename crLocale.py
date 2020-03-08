import locale

from os import path as osPath
from pathlib import Path as plPath

# Preprocess config
# the config should not change by code after preprocess


def _my_locale_parser(config_environment):
    # Check system language
    language_root = config_environment['language']['root']
    system_language = locale.getdefaultlocale()[0]
    language_current = language_root + system_language + '/'  # language/en_US/

    current_language_exists = osPath.exists(plPath(language_current))
    if current_language_exists is True:
        language_current = config_environment['language']['fallback']
    #

    # Apply language to path
    #
    # config_message_path
    # Get
    config_message_path = config_environment['message']['message_config_path']
    # Apply
    config_message_path = language_current + \
        config_message_path  # language/en_US/message.xml

    # Put it back
    config_environment['message']['config_message_path'] = config_message_path

    return config_environment

# Wrap the process


def get_environment_locale(config_environment):
    return _my_locale_parser(config_environment)
