# 3rd
import configparser

from pathlib import Path as plPath
from os import path as osPath

# My
from crLogHeader import *
from crLocaleHeader import *
from crEnvironmentHeader import *
from crMagicValueHeader import *
from crMessageHeader import *
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


def _load_message_config():
    global message_config

    message_config_path = plPath(
        environment_config['message']['config_message_path'])

    if osPath.exists(message_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(message_config_path)
        crPrintCyan(error_message)
        raise CrFileNotFoundError(error_message)

    message_config.read(message_config_path)


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


# init_config


def init_config():
    try:
        # Environment
        #
        _load_environment_config()
        # Apply locale
        global environment_config
        environment_config = get_environment_locale(environment_config)
        # Apply preprocessor
        environment_config = get_preprocessed_environment(environment_config)

        # Message
        #
        _load_message_config()
        # Apply preprocessor
        global message_config
        message_config = get_preprocessed_message(message_config)

        # Magic value
        #
        _load_magic_value_config()
        # Apply preprocessor
        global magic_value_config
        magic_value_config = get_preprocessed_magic_value(magic_value_config)
    except:
        raise
