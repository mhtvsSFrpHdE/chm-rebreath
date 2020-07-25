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
    _crEnvironmentSal.init_environment_sal()

    # Apply preprocessor
    _crEnvironmentSal.apply_environment_config_preprocessor()
    _crMagicValueSal.apply_magic_value_config_preprocessor()
