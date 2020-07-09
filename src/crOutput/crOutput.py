from pathlib import Path as plPath
from shutil import copytree

from crExceptionSal import *
from crLog import *
from crEnvironmentUtil import crCreateFolder

environment_config_local = None
message_config_local = None


def create_output_folder_structure(root_output_folder):
    crCreateFolder(get_catalog_html_resource_output_full_path(root_output_folder))


def get_catalog_html_resource_output_full_path(root_output_folder):
    output_catalog_html_root_path = plPath(environment_config_local['output_catalog_html_resource']['root_path'])
    output_catalog_html_root_full_path = root_output_folder.joinpath(output_catalog_html_root_path)

    return output_catalog_html_root_full_path


def copy_catalog_html_resource(output_folder_path):
    try:
        data_catalog_html_resource_root_full_path = plPath(environment_config_local['data_catalog_html_resource']['root_full_path'])

        copytree(data_catalog_html_resource_root_full_path, output_folder_path, dirs_exist_ok=True)
    except:
        error_message = message_config_local['err']['failed_to_copy_file']
        crPrintCyan(error_message)
        raise


def init_output(environment_config, message_config):
    global environment_config_local
    global message_config_local

    environment_config_local = environment_config
    message_config_local = message_config
