def _my_message_preprocessor(message_config):
    mErr = message_config['err']

    # .ini config doesn't support space at end of the line,
    # they will cap by three double quotes
    message_config['err']['software_broken'] = mErr['software_broken'].strip(
        '"""')

    return message_config

# Some message entry need to preprocess before use


def get_preprocessed_message(message_config):
    return _my_message_preprocessor(message_config)
