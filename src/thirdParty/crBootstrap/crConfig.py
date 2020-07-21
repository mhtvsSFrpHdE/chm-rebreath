# 3rd
import configparser as _configparser

from pathlib import Path as _plPath
from os import path as _osPath

# My
import crLog as _crLog
import crLocale as _crLocale
import crMagicValueConfigPreprocess as _crMagicValueConfigPreprocess
import crMessageConfigPreprocess as _crMessageConfigPreprocess
import crException as _crException

# Config object placeholder
# The three are designed to be public
_environment_config = _configparser.RawConfigParser()
_magic_value_config = _configparser.RawConfigParser()
_message_config = _configparser.RawConfigParser()

# Read config files


def _load_environment_config():
    global _environment_config

    environment_config_path = _plPath('environment.ini')

    if _osPath.exists(environment_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(environment_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _environment_config.read(environment_config_path)

    # Apply locale
    _environment_config = _crLocale.apply_locale_to_environment_config(_environment_config)

    # Apply preprocessor(Not required yet)


def _load_message_config():
    global _message_config

    message_config_path = _plPath(
        _environment_config['message']['config_message_path'])

    if _osPath.exists(message_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(message_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _message_config.read(message_config_path, encoding='utf-8')

    # Apply preprocessor
    _message_config = _crMessageConfigPreprocess.apply_message_config_preprocessor(_message_config)


def _load_magic_value_config():
    global _magic_value_config
    global _message_config

    magic_value_config_path = _plPath(
        _environment_config['dev']['magic_value_config_path'])

    if _osPath.exists(magic_value_config_path) is False:
        error_message = _message_config['err']['software_broken'] \
            + str(magic_value_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _magic_value_config.read(magic_value_config_path)

    # Apply preprocessor(Not required yet)

# Transfer config back


def get_config():
    return _environment_config, _magic_value_config, _message_config


# init_config
try:
    _load_environment_config()
    _load_message_config()
    _load_magic_value_config()
except:
    raise
