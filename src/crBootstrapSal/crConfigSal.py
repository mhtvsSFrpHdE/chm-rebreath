from crEnvironmentSalHeader import *
from crMagicValueSalHeader import *


def init_config_sal(environment_config, magic_value_config, message_config):

    # Apply preprocessor
    environment_config_local = get_preprocessed_environment(environment_config)
    magic_value_config_local = get_preprocessed_magic_value(magic_value_config)

    return environment_config_local, magic_value_config_local, message_config
