def _preprocess_chm_file_search_pattern(magic_value_config):
    mdev = magic_value_config['dev']

    magic_value_config['dev']['chm_catalog_file_search_pattern'] = mdev['chm_catalog_file_search_pattern'] + \
        mdev['chm_catalog_file_extension']

    magic_value_config['dev']['chm_index_file_search_pattern'] = mdev['chm_index_file_search_pattern'] + \
        mdev['chm_index_file_extension']

    return magic_value_config

# Some magic value entry need to preprocess before use


def get_preprocessed_magic_value(magic_value_config):
    return _preprocess_chm_file_search_pattern(magic_value_config)
