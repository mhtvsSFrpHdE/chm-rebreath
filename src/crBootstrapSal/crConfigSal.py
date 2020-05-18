from crEnvironmentSalHeader import *

def init_config_sal(environment_config):

    # Apply preprocessor
    environment_config_local = get_preprocessed_environment(environment_config)

    return environment_config_local