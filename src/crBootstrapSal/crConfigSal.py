import crEnvironmentSalHeader as _crEnvironmentSal
import crMagicValueSal as _crMagicValueSal


def init_config_sal(environment_config, magic_value_config, message_config):

    # Apply preprocessor
    environment_config_local = _crEnvironmentSal.get_preprocessed_environment(environment_config)
    magic_value_config_local = _crMagicValueSal.get_preprocessed_magic_value(magic_value_config)

    return environment_config_local, magic_value_config_local, message_config
