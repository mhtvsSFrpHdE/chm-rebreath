# Preprocess message


def _preprocess_message_config(message_config):
    mErr = message_config['err']
    mHtml = message_config['html_catalog']
    # Try to make process close together and short the method name
    # Use namespace to avoid conflict
    def ps(myString):
        # .ini config doesn't support space at end of the line,
        # they will cap by three double quotes
        #
        # %nl% is next line, refer to \n
        return myString.strip('"""').replace("%nl%", "\n")

    message_config['err']['software_broken'] = mErr['software_broken'].strip(
        '"""')
    message_config['html_catalog']['title'] = mHtml['title'].strip('"""')

    message_config['err']['chm_catalog_multiple_sub_node_ul'] = mErr['chm_catalog_multiple_sub_node_ul'].strip(
        '"""').replace("%nl%", "\n")

    return message_config

# Some message entry need to preprocess before use
#
# TODO: use a loop to replace all the symbols
#
# Update: too bad, failed to use loop to update the values
# It seems configparser doesn't support iterate through it and update value
# Perhaps a stackoverflow can help


def get_preprocessed_message(message_config):
    return _preprocess_message_config(message_config)
