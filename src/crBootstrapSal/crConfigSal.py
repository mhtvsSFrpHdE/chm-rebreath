import crMagicValueSal as _crMagicValueSal


# Use python tuple(array) for shorter function call
# Transfer initialized SAL object as possible to prevent unnecessary double initialize
def init_config_sal(config_tuple, crEnvironmentSal):

    # Apply preprocessor
    environment_config_local = crEnvironmentSal.apply_environment_config_preprocessor(config_tuple[0])
    magic_value_config_local = _crMagicValueSal.apply_magic_value_config_preprocessor(config_tuple[1])

    return environment_config_local, magic_value_config_local, config_tuple[2]
