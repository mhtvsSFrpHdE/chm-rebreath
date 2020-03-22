# Some message entry need to preprocess before use


def _get_preprocessed_message_early_implementation_code_backup(message_config):
    # Try to make process close together and short the method name
    # Use namespace to avoid conflict
    def ps(myString):
        # .ini config doesn't support space at end of the line,
        # they will cap by three double quotes
        #
        # %nl% is next line, refer to \n
        return myString.strip('"""').replace("%nl%", "\n")

    mErr = message_config['err']
    message_config['err']['software_broken'] = ps(mErr['software_broken'])
    message_config['err']['chm_catalog_multiple_sub_node_ul'] = ps(
        mErr['chm_catalog_multiple_sub_node_ul'])

    mHtml = message_config['html_catalog']
    message_config['html_catalog']['title'] = ps(mHtml['title'])

    return message_config


def get_preprocessed_message(message_config):
    # Try to make process close together and short the method name
    # Use namespace to avoid conflict
    # Full name: preprocess_string
    def ps(myString):
        # .ini config doesn't support space at end of the line,
        # they will cap by three double quotes
        #
        # %nl% is next line, refer to \n
        return myString.strip('"""').replace("%nl%", "\n")

    for group_name in message_config.sections():
        for key_name in message_config[group_name]:
            message_config[group_name][key_name] = ps(
                message_config[group_name][key_name])

    return message_config
