# 3rd
import pathlib  # Path

# My
from crLogHeader import *
import crDevInput  # Information used while development

# Module scope config
magic_value_config_local = None
message_config_local = None

# Receive config


def init_environment(message_config, magic_value_config):
    global magic_value_config_local
    global message_config_local

    magic_value_config_local = magic_value_config
    message_config_local = message_config

# Scan and get catalog file path


def get_catalog_file_path():
    global magic_value_config_local
    global message_config_local

    catalog_file_path = None

    try:
        catalog_file_list = pathlib.Path(crDevInput.unpackedChmFolder).glob(
            magic_value_config_local['dev']['chm_catalog_file_search_pattern'])
        catalog_file_list_count = 0

        for catalog_file in catalog_file_list:
            catalog_file_list_count = catalog_file_list_count + 1

            if catalog_file_list_count > 1:
                crPrintCyan(
                    message_config_local['err']['multiple_catalog_file'])
                raise EnvironmentError(
                    message_config_local['err']['multiple_catalog_file'])

            catalog_file_path = catalog_file

        if catalog_file_list_count is 0:
            crPrintCyan(message_config_local['err']['catalog_file_not_found'])
            raise EnvironmentError(
                message_config_local['err']['catalog_file_not_found'])
    except:
        logging.exception(__name__)
        raise

    return catalog_file_path
