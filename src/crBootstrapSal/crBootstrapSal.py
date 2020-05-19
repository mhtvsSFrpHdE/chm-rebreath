import crConfigSal as _crConfigSal  # NOQA: E402
import crCoreHeader as crCore  # NOQA: E402
import crEnvironmentSalHeader as crEnvironmentSal  # NOQA: E402
import crOutputHeader as crOutput  # NOQA: E402

# The method will modify config files generated by crBootstrap to add custom preprocessor


def init_bootstrap_sal(environment_config, magic_value_config, message_config):
    crEnvironmentSal.init_environment_sal(magic_value_config, message_config)

    crCore.init_core_get_catalog_node(environment_config, message_config)
    crCore.init_core_get_index_html(environment_config, message_config)

    crOutput.init_output(environment_config, message_config)

    # Create modified config
    myConfigGroup = environment_config, magic_value_config, message_config
    environment_config_local, magic_value_config_local, message_config_local = _crConfigSal.init_config_sal(myConfigGroup, crEnvironmentSal)

    return environment_config_local, magic_value_config_local, message_config_local
