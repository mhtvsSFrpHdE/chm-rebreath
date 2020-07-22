# Load project modules
import crConfigSal as _crConfigSal  # NOQA: E402
import crCore  # NOQA: E402
import crEnvironmentSal  # NOQA: E402
import crOutput  # NOQA: E402
import crUnpack  # NOQA: E402

# 3rd
from crBootstrap import *  # NOQA: E402

# The method will modify config files generated by crBootstrap,
# add custom preprocessor only for this specified project


def _apply_config_preprocessor():
    # Get access to root level config
    global environment_config
    global magic_value_config
    global message_config

    environment_config, magic_value_config, message_config = _crConfigSal.apply_config_preprocessor_sal(environment_config, magic_value_config, message_config)

# The method will use preprocessed config to initialize other module


def _init_any_other_module_requires_config():
    # Init basic module
    crEnvironmentSal.init_environment_sal(magic_value_config, message_config)

    # crCore
    crCore.init_core_get_catalog_node(environment_config, message_config)
    crCore.init_core_get_index_html(environment_config, message_config)

    # crOutput
    crOutput.init_output(environment_config, message_config)

    # crUnpack
    crUnpack.init_crUnpack(environment_config)


# Run method
#
# Apply any exist config preprocessor
# Then use preprocessed config to initialize other module
_apply_config_preprocessor()
_init_any_other_module_requires_config()

# Prepare command line arguments
import crArgumentSal as crArgument  # NOQA: E402
