# 3rd
import configparser

from pathlib import Path as plPath
from os import path as osPath

# My
from crLog import *
from crLocale import *
from crMagicValueConfigPreprocess import *
from crMessageConfigPreprocess import *
from crException import *

# Config object placeholder
environment_config = configparser.RawConfigParser()
magic_value_config = configparser.RawConfigParser()
message_config = configparser.RawConfigParser()

# Read config files


def _load_environment_config():
    global environment_config

    environment_config_path = plPath('environment.ini')

    if osPath.exists(environment_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(environment_config_path)
        crPrintCyan(error_message)
        raise CrFileNotFoundError(error_message)

    environment_config.read(environment_config_path)

    # Apply locale
    environment_config = apply_locale_to_environment_config(environment_config)

    # Apply preprocessor(Not required yet)
    #environment_config = apply_environment_config_preprocessor(environment_config)


def _load_message_config():
    global message_config

    message_config_path = plPath(
        environment_config['message']['config_message_path'])

    if osPath.exists(message_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(message_config_path)
        crPrintCyan(error_message)
        raise CrFileNotFoundError(error_message)

    message_config.read(message_config_path, encoding='utf-8')

    # Apply preprocessor
    message_config = apply_message_config_preprocessor(message_config)


def _load_magic_value_config():
    global magic_value_config
    global message_config

    magic_value_config_path = plPath(
        environment_config['dev']['magic_value_config_path'])

    if osPath.exists(magic_value_config_path) is False:
        error_message = message_config['err']['software_broken'] \
            + str(magic_value_config_path)
        crPrintCyan(error_message)
        raise CrFileNotFoundError(error_message)

    magic_value_config.read(magic_value_config_path)

    # Apply preprocessor(Not required yet)
    #magic_value_config = apply_magic_value_config_preprocessor(magic_value_config)


# init_config
try:
    _load_environment_config()
    _load_message_config()
    _load_magic_value_config()
except:
    raise
