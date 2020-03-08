# 3rd
import configparser
import logging

from pathlib import Path as plPath

# My
from crLog import crPrintCyan
from crLocaleHeader import *
from crMagicValueHeader import *
from crMessageHeader import *

environment_config = configparser.ConfigParser()
magic_value_config = configparser.ConfigParser()
message_config = configparser.ConfigParser()

# Read config files


def _load_environment_config():
    global environment_config

    environment_config_path = plPath('environment.ini')

    if osPath.exists(environment_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(environment_config_path)
        crPrintCyan(error_message)
        raise EnvironmentError(error_message)

    environment_config.read(environment_config_path)


def _load_message_config():
    global message_config

    message_config_path = plPath(
        environment_config['message']['config_message_path'])

    if osPath.exists(message_config_path) is False:
        # Message config not yet loaded
        error_message = "Config file missing: " + str(message_config_path)
        crPrintCyan(error_message)
        raise EnvironmentError(error_message)

    message_config.read(message_config_path)


def _load_magic_value_config():
    global magic_value_config
    global message_config

    magic_value_config_path = plPath(
        environment_config['dev']['configPathMagicValue'])

    if osPath.exists(magic_value_config_path) is False:
        error_message = message_config['err']['software_broken'] + \
            str(magic_value_config_path)
        crPrintCyan(error_message)
        raise EnvironmentError(error_message)

    magic_value_config.read(magic_value_config_path)


# Wrap


def config_init():
    try:
        # Environment
        #
        _load_environment_config()
        # Apply locale
        global environment_config
        environment_config = get_environment_locale(environment_config)

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
        logging.exception(__name__)
        raise
