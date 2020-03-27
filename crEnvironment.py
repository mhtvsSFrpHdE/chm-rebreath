# 3rd
import os

from pathlib import Path as plPath  # Path
from os import path as osPath

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

# Create folder if not exist


def confirm_folder_exist(myFolder):
    folder_exist = False
    if osPath.exists(myFolder) is False:
        try:
            os.mkdir(myFolder)
            folder_exist = True
        except:
            error_message = message_config_local['err']['failed_to_create_output_folder']
            crPrintCyan(error_message)
            logging.exception(__name__)
            raise EnvironmentError(error_message)
    # else if myFolder already exist
    else:
        folder_exist = True

# Scan and get catalog file path


def get_catalog_chm_file_path():
    global magic_value_config_local
    global message_config_local

    catalog_file_path = None

    try:
        catalog_file_list = plPath(crDevInput.unpackedChmFolder) \
            .glob(magic_value_config_local['chm']['catalog_file_search_pattern'])
        catalog_file_list_count = 0

        for catalog_file in catalog_file_list:
            catalog_file_list_count = catalog_file_list_count + 1

            if catalog_file_list_count > 1:
                crPrintCyan(message_config_local['err']['multiple_catalog_file'])
                logging.exception(__name__)
                raise EnvironmentError(message_config_local['err']['multiple_catalog_file'])

            catalog_file_path = catalog_file

        if catalog_file_list_count is 0:
            crPrintCyan(message_config_local['err']['catalog_file_not_found'])
            logging.exception(__name__)
            raise EnvironmentError(message_config_local['err']['catalog_file_not_found'])
    except:
        logging.exception(__name__)
        raise

    return catalog_file_path

# Wrap the output folder with pathlib


def get_root_output_folder_path():
    output_folder = plPath(crDevInput.outputFolder)
    if osPath.exists(output_folder) is False:
        try:
            os.mkdir(output_folder)
        except:
            error_message = message_config_local['err']['failed_to_create_output_folder']
            crPrintCyan(error_message)
            logging.exception(__name__)
            raise EnvironmentError(error_message)

    return output_folder

# Combine serval information to catalog HTML full output path


def get_catalog_html_output_path(catalog_html_title):
    output_folder_path = get_root_output_folder_path()
    #
    # Catalog root node name  + `- Catalog` + `.html`
    output_file_path = output_folder_path.joinpath(
        catalog_html_title
        + message_config_local['html_catalog']['title']
        + magic_value_config_local['html']['file_extension'])

    return output_file_path

# Some entry need to preprocess before use


def get_preprocessed_environment(environment_config):
    mD = environment_config['data']
    mDC = environment_config['data_catalog']

    environment_config['data_catalog']['css_file_full_path'] = mD['root'] + mDC['root'] + mDC['css_file_name']
    environment_config['data_catalog']['js_file_full_path'] = mD['root'] + mDC['root'] + mDC['js_file_name']

    return environment_config
