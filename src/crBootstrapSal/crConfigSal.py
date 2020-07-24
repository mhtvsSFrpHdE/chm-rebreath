# After apply config preprocessor, there is no need to use method in this file again
# `import crConfigSal as _crConfig` as private is recommended

# Get preprocessor
import crEnvironmentSal as _crEnvironmentSal
import crMagicValueSal as _crMagicValueSal

# Add feature to crConfig but only for this specified project
# they are not universal feature that suit any project


def apply_config_preprocessor_sal(environment_config, magic_value_config, message_config):
    # Init module
    _crEnvironmentSal.init_environment_sal(magic_value_config, message_config)

    # Apply preprocessor
    environment_config_local = _crEnvironmentSal.apply_environment_config_preprocessor(environment_config)
    magic_value_config_local = _crMagicValueSal.apply_magic_value_config_preprocessor(magic_value_config)

    # Return modified config and unmodified config
    return environment_config_local, magic_value_config_local, message_config
