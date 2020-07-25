from pathlib import Path as _plPath
from shutil import copytree as _copytree

import crGlobalLevel as _crGlobalLevel
import crLog as _crLog
from crEnvironmentUtil import crCreateFolder as _crCreateFolder

_environment_config_local = None
_message_config_local = None


def create_output_folder_structure(root_output_folder):
    _crCreateFolder(get_catalog_html_resource_output_full_path(root_output_folder))


def get_catalog_html_resource_output_full_path(root_output_folder):
    output_catalog_html_root_path = _plPath(_environment_config_local['output_catalog_html_resource']['root_path'])
    output_catalog_html_root_full_path = root_output_folder.joinpath(output_catalog_html_root_path)

    return output_catalog_html_root_full_path


def copy_catalog_html_resource(output_folder_path):
    try:
        data_catalog_html_resource_root_full_path = _plPath(_environment_config_local['data_catalog_html_resource']['root_full_path'])

        _copytree(data_catalog_html_resource_root_full_path, output_folder_path, dirs_exist_ok=True)
    except:
        error_message = _message_config_local['err']['failed_to_copy_file']
        _crLog.crPrintCyan(error_message)
        raise


def init_output():
    global _environment_config_local
    global _message_config_local

    _environment_config_local = _crGlobalLevel.environment_config
    _message_config_local = _crGlobalLevel.message_config
