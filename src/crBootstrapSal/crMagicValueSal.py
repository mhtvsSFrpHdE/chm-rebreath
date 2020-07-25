import crGlobalLevel as _crGlobalLevel

def _preprocess_chm_file_search_pattern(magic_value_config):
    # m = my
    mChm = magic_value_config['chm']

    # Merge search pattern and file extension
    # Example: *.hhc
    magic_value_config['chm']['catalog_file_search_pattern'] = mChm['catalog_file_search_pattern'] + mChm['catalog_file_extension']
    magic_value_config['chm']['index_file_search_pattern'] = mChm['index_file_search_pattern'] + mChm['index_file_extension']

    return magic_value_config

# apply_magic_value_config_preprocessor


def apply_magic_value_config_preprocessor():
    return _preprocess_chm_file_search_pattern(_crGlobalLevel.magic_value_config)
