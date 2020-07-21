# Prepare everything about logging, config, international
# Result in one line `from crBootstrap import *` in the main method or file

# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
import logging as _logging  # NOQA: E402

_logging.basicConfig(filename="log.txt", level=logging.INFO)  # NOQA: E402
_logging.info("#========= Start =========#")  # NOQA: E402

# Load config
import crConfig as _crConfig  # NOQA: E402
environment_config, magic_value_config, message_config = _crConfig.get_config()

# Prepare command line arguments at the very beginning
from crArgumentParser import *
