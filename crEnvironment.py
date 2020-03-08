# 3rd

# Environment
import pathlib  # Path

# Log
import logging

# My
import crDevInput  # Information used while development
import crMagicValue
import crMessage

from crLog import crPrintCyan

# Module scope config
magic_value_config_local = None
message_config_local = None

# Receive config


def environment_init(message_config, magic_value_config):
    global magic_value_config_local
    global message_config_local

    magic_value_config_local = magic_value_config
    message_config_local = message_config

# Scan and get catalog file path


def get_catalog_file_path(message, magic_value):
    catalog_file_path = None

    try:
        catalogFileList = pathlib.Path(crDevInput.unpackedChmFolder).glob(
            crMagicValue.chmCatalogFileSearchPattern)
        catalogFileListCount = 0

        for catalog_file in catalog_file_list:
            catalog_file_list_count = catalog_file_list_count + 1

            if catalogFileListCount > 1:
                crPrintCyan(crMessage.errMultipleCatalogFile)
                raise EnvironmentError(crMessage.errMultipleCatalogFile)

            catalog_file_path = catalog_file

        if catalogFileListCount is 0:
            crPrintCyan(crMessage.errCatalogFileNotFound)
            raise EnvironmentError(crMessage.errCatalogFileNotFound)
    except:
        logging.exception(__name__)
        raise

    return catalog_file_path
