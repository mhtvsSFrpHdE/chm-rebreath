# Try to make process close together and short the method name
#
# I DON'T WANT BELOW THESE TRASH UNLESS NECESSARY
#
# # If you do hope use three double quotes(why?),
# # try replace " by &dq&, for example: """ -> &dq&&dq&&dq&
# myString.replace("&dq&", '"')
#
# # To show symbol directly, break each & with &/,
# # they will be remove to keep symbol together
# # For example: &nl& but don't want a line break -> &/ + &nl + &/ + & -> &/&nl&/&
# myString = myString.replace("&/", "")


def _preprocess_message_string(myString):
    # .ini config doesn't support space at end of the line,
    # they will cap by three double quotes
    # '""" """' -> ' '

    # &nl& is next line, refer to \n in python CODE
    # '&nl&' -> '\n'
    return myString.strip('"""').replace("&nl&", "\n")

# apply_message_config_preprocessor


def apply_message_config_preprocessor(message_config):

    for group_name in message_config.sections():
        for key_name in message_config[group_name]:
            message_config[group_name][key_name] = _preprocess_message_string(
                message_config[group_name][key_name])

    return message_config
