def _preprocess_chm_file_search_pattern(magic_value_config):
    # m = my
    mChm = magic_value_config['chm']

    # Merge search pattern and file extension
    # Example: *.hhc
    magic_value_config['chm']['catalog_file_search_pattern'] = mChm['catalog_file_search_pattern'] + mChm['catalog_file_extension']
    magic_value_config['chm']['index_file_search_pattern'] = mChm['index_file_search_pattern'] + mChm['index_file_extension']

    return magic_value_config

# get_preprocessed_magic_value


def get_preprocessed_magic_value(magic_value_config):
    return _preprocess_chm_file_search_pattern(magic_value_config)
