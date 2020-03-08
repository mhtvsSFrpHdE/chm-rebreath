# 3rd
import configparser

from pathlib import Path as plPath

# My
from crLocaleHeader import *
from crMagicValueHeader import *

environment_config = configparser.ConfigParser()
magic_value_config = configparser.ConfigParser()
message_config = configparser.ConfigParser()

# Read config files


def _load_environment_config():
    global environment_config

    # Congratulations, this should be the only hardcoded variable
    environment_config_path = plPath('environment.ini')
    environment_config.read(environment_config_path)


def _load_message_config():
    global message_config

    message_config_path = plPath(
        environment_config['message']['config_message_path'])
    message_config.read(message_config_path)


def _load_magic_value_config():
    global magic_value_config

    magic_value_config_path = plPath(
        environment_config['dev']['configPathMagicValue'])
    magic_value_config.read(magic_value_config_path)




# Wrap


def config_init():
    # Environment
    #
    _load_environment_config()
    # Apply locale
    global environment_config
    environment_config = get_environment_locale(environment_config)

    # Magic value
    #
    _load_magic_value_config()
    # Apply preprocessor
    global magic_value_config
    magic_value_config = get_preprocessed_magic_value(magic_value_config)
