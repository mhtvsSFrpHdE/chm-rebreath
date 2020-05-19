import crMagicValueSal as _crMagicValueSal


# Use python tuple(array) for shorter function call
# Transfer initialized SAL object as possible to prevent unnecessary double initialize
def init_config_sal(config_tuple, crEnvironmentSal):

    # Apply preprocessor
    environment_config_local = crEnvironmentSal.get_preprocessed_environment(config_tuple[0])
    magic_value_config_local = _crMagicValueSal.get_preprocessed_magic_value(config_tuple[1])

    return environment_config_local, magic_value_config_local, config_tuple[2]
