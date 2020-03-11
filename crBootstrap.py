# 3rd
import logging  # NOQA: E402
#
# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
logging.basicConfig(filename="log.txt")  # NOQA: E402

# My
from crConfigHeader import *
from crEnvironmentHeader import *
from crCoreHeader import *

# Initialize
init_environment(message_config, magic_value_config)
init_core_get_catalog_node(message_config)
