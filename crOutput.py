from pathlib import Path as plPath
from shutil import copyfile

from crException import *
from crLogHeader import *
from crEnvironmentHeader import crCreateFolder

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
        css_output_file_name = plPath(environment_config_local['output_catalog_html_resource']['css_file_name'])
        css_data_file_path = plPath(environment_config_local['data_catalog_html_resource']['css_file_full_path'])
        css_output_file_path = output_folder_path.joinpath(css_output_file_name)

        copyfile(css_data_file_path, css_output_file_path)

        js_output_file_name = plPath(environment_config_local['output_catalog_html_resource']['js_file_name'])
        js_data_file_path = plPath(environment_config_local['data_catalog_html_resource']['js_file_full_path'])
        js_output_file_path = output_folder_path.joinpath(js_output_file_name)

        copyfile(js_data_file_path, js_output_file_path)
    except:
        error_message = message_config_local['err']['failed_to_copy_file']
        crPrintCyan(error_message)
        raise CrEnvironmentError(error_message)


def init_output(environment_config, message_config):
    global environment_config_local
    global message_config_local

    environment_config_local = environment_config
    message_config_local = message_config
