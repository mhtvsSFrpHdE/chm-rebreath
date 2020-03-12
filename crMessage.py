# Some message entry need to preprocess before use
#
# NEEDHELP: use a loop to replace all the symbols
#
# Update: too bad, failed to use loop to update the values
# It seems configparser doesn't support iterate through it and update value
# Perhaps a stackoverflow can help


def get_preprocessed_message(message_config):
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
