# 3rd
from pathlib import Path as _plPath  # Path

# My
import crEnvironmentUtil as _crEnvironmentUtil

# Module scope config
_magic_value_config_local = None
_message_config_local = None

# Receive config


def init_environment_sal(magic_value_config, message_config):
    global _magic_value_config_local
    global _message_config_local

    _magic_value_config_local = magic_value_config
    _message_config_local = message_config

    _crEnvironmentUtil.init_environment(_message_config_local)

# Search in input folder and get catalog file path


def get_catalog_chm_file_full_path():
    global _magic_value_config_local
    global _message_config_local

    # Result placeholder
    catalog_file_full_path = None

    try:
        # Glob all potential catalog file
        # Call it a list, but see python generator for more information
        catalog_file_list = _plPath(crDevInput.unpackedChmFolder) \
            .glob(_magic_value_config_local['chm']['catalog_file_search_pattern'])

        # Expect only one catalog file
        catalog_file_list_count = 0

        # Explore the glob generator
        for catalog_file_glob_result in catalog_file_list:
            # Increase file count on every loop
            catalog_file_list_count = catalog_file_list_count + 1

            # Prevent more than one catalog file
            if catalog_file_list_count > 1:
                crPrintCyan(_message_config_local['err']['multiple_catalog_file'])
                raise CrNotImplementedError(_message_config_local['err']['multiple_catalog_file'])

            # Everything is fine, copy it as plPath
            catalog_file_full_path = _plPath(catalog_file_glob_result)

        # After explored the generator
        if catalog_file_list_count == 0:
            # Nothing found, raise error
            error_message = _message_config_local['err']['catalog_file_not_found']
            crPrintCyan(error_message)
            raise CrFileNotFoundError(error_message)
    except:
        raise

    return catalog_file_full_path

# get_root_output_folder_full_path


def get_root_output_folder_full_path():
    output_folder = _plPath(_crEnvironmentUtil.crDevInput.outputFolder)

    _crEnvironmentUtil.crCreateFolder(output_folder)

    return output_folder


# Combine serval information to generate catalog HTML full output path


def get_catalog_html_output_full_path(catalog_html_title):
    output_folder_path = get_root_output_folder_full_path()
    #
    # Catalog root node name  + `- Catalog` + `.html`
    output_file_path = output_folder_path.joinpath(
        catalog_html_title
        + _message_config_local['html_catalog']['title']
        + _magic_value_config_local['html']['file_extension'])

    return output_file_path

# apply_environment_config_preprocessor


def apply_environment_config_preprocessor(environment_config):
    # m = my
    mD = environment_config['data']
    mDC = environment_config['data_catalog_html_resource']

    # Copy data structure to output structure
    # Do this before preprocess data
    environment_config['output_catalog_html_resource'] = mDC

    # Generate full path for data_catalog folder
    environment_config['data_catalog_html_resource']['root_full_path'] = mD['root_path'] + mDC['root_path']

    return environment_config
