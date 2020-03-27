# Prepare everything about environment, logging, config, international
# Result in one line `from crBootstrap import *` in the main method or file


# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
import logging  # NOQA: E402

logging.basicConfig(filename="log.txt", level=logging.INFO)  # NOQA: E402
logging.info("#========= Start =========#")  # NOQA: E402

# Prepare command line arguments at the very beginning
from crArgumentParserHeader import *

init_argument_parser()


# Other modules
from crConfigHeader import *  # NOQA: E402
from crEnvironmentHeader import *  # NOQA: E402
from crCoreHeader import *  # NOQA: E402
from crOutputHeader import *  # NOQA: E402

# Some module require config file to initialize,
# call the init method here
init_environment(message_config, magic_value_config)
init_core_get_catalog_node(environment_config, message_config)
init_core_get_catalog_html(environment_config, message_config)
init_output(environment_config, message_config)
