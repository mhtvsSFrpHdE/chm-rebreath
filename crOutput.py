from pathlib import Path as plPath
from shutil import copyfile

from crLogHeader import *
from crEnvironmentHeader import confirm_folder_exist

environment_config_local = None
message_config_local = None

def copy_catalog_html_resource(output_folder_path):
    try:
        css_file_name = plPath(environment_config_local['data_catalog']['css_file_name'])
        css_file_path = plPath(environment_config_local['data_catalog']['css_file_full_path'])
        css_output_file_path = output_folder_path.joinpath(css_file_name)
        copyfile(css_file_path, css_output_file_path)

        js_file_name = plPath(environment_config_local['data_catalog']['js_file_name'])
        js_file_path = plPath(environment_config_local['data_catalog']['js_file_full_path'])
        js_output_file_path = output_folder_path.joinpath(js_file_name)
        copyfile(js_file_path, js_output_file_path)
    except:
        error_message = message_config_local['err']['failed_to_copy_file']
        crPrintCyan(error_message)
        logging.exception(__name__)
        raise EnvironmentError(error_message)

def init_output(environment_config, message_config):
    global environment_config_local
    global message_config_local

    environment_config_local = environment_config
    message_config_local = message_config
