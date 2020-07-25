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
import crGlobalVariable as _crGlobalVariable

# Config object placeholder
# The three are designed to be public
_crGlobalVariable.environment_config = _configparser.RawConfigParser()
_crGlobalVariable.magic_value_config = _configparser.RawConfigParser()
_crGlobalVariable.message_config = _configparser.RawConfigParser()

# Read config files


def _load_environment_config():
    environment_config_path = _plPath('environment.ini')

    if _osPath.exists(environment_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(environment_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _crGlobalVariable.environment_config.read(environment_config_path)

    # Apply locale
    _crGlobalVariable.environment_config = _crLocale.apply_locale_to_environment_config(_crGlobalVariable.environment_config)

    # Apply preprocessor(Not required yet)


def _load_message_config():
    message_config_path = _plPath(
        _crGlobalVariable.environment_config['message']['config_message_path'])

    if _osPath.exists(message_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(message_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _crGlobalVariable.message_config.read(message_config_path, encoding='utf-8')

    # Apply preprocessor
    _crGlobalVariable.message_config = _crMessageConfigPreprocess.apply_message_config_preprocessor(_crGlobalVariable.message_config)


def _load_magic_value_config():
    magic_value_config_path = _plPath(
        _crGlobalVariable.environment_config['dev']['magic_value_config_path'])

    if _osPath.exists(magic_value_config_path) is False:
        error_message = _crGlobalVariable.message_config['err']['software_broken'] \
            + str(magic_value_config_path)
        _crLog.crPrintCyan(error_message)
        raise _crException.CrFileNotFoundError(error_message)

    _crGlobalVariable.magic_value_config.read(magic_value_config_path)

    # Apply preprocessor(Not required yet)


# init_config
try:
    _load_environment_config()
    _load_message_config()
    _load_magic_value_config()
except:
    raise
