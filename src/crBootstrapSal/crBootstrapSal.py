# Load project modules
import crConfigSal as _crConfig  # NOQA: E402
import crArgumentSal as crArgument  # NOQA: E402
import crInputSal as crInput  # NOQA: E402
import crCore  # NOQA: E402
import crEnvironmentSal as crEnvironment  # NOQA: E402
import crOutput  # NOQA: E402
import crUnpack  # NOQA: E402

# 3rd
from crBootstrap import *  # NOQA: E402

# The method will modify config files generated by crBootstrap,
# add custom preprocessor only for this specified project


def _apply_config_preprocessor():
    _crConfig.apply_config_preprocessor_sal()

# The method will use preprocessed config to initialize other module


def _init_any_other_module_requires_config():
    # Init basic module
    crInput.init_input_sal()
    crEnvironment.init_environment_sal()

    # crCore
    crCore.init_core_get_catalog_node()
    crCore.init_core_get_index_html()

    # crOutput
    crOutput.init_output()

    # crUnpack
    crUnpack.init_crUnpack()


# Run method
#
# Apply any exist config preprocessor
# Then use preprocessed config to initialize other module
_apply_config_preprocessor()
_init_any_other_module_requires_config()
