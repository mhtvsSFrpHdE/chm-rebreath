def _my_message_preprocessor(message_config):
    mErr = message_config['err']

    # TODO: use a loop to replace all the symbols

    # .ini config doesn't support space at end of the line,
    # they will cap by three double quotes
    message_config['err']['software_broken'] = mErr['software_broken'].strip(
        '"""')

    # %nl% is next line, refer to \n
    message_config['err']['chm_catalog_multiple_sub_node_ul'] = mErr['chm_catalog_multiple_sub_node_ul'].strip(
        '"""').replace("<nl>", "\n")

    return message_config

# Some message entry need to preprocess before use


def get_preprocessed_message(message_config):
    return _my_message_preprocessor(message_config)
