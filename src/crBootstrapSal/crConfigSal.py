# After apply config preprocessor, there is no need to use method in this file again
# `import crConfigSal as _crConfig` as private is recommended

# My
import crGlobalVariable as _crGlobalVariable

# Get preprocessor
import crEnvironmentSal as _crEnvironmentSal
import crMagicValueSal as _crMagicValueSal

# Add feature to crConfig but only for this specified project
# they are not universal feature that suit any project


def apply_config_preprocessor_sal():
    # Init module
    _crEnvironmentSal.init_environment_sal(_crGlobalVariable.magic_value_config, _crGlobalVariable.message_config)

    # Apply preprocessor
    environment_config_local = _crEnvironmentSal.apply_environment_config_preprocessor(_crGlobalVariable.environment_config)
    magic_value_config_local = _crMagicValueSal.apply_magic_value_config_preprocessor(_crGlobalVariable.magic_value_config)

    # Transfer back modified config
    _crGlobalVariable.environment_config = environment_config_local
    _crGlobalVariable.magic_value_config = magic_value_config_local
