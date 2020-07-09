# Prepare everything about logging, config, international
# Result in one line `from crBootstrap import *` in the main method or file

# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
import logging  # NOQA: E402

logging.basicConfig(filename="log.txt", level=logging.INFO)  # NOQA: E402
logging.info("#========= Start =========#")  # NOQA: E402

# Load config
from crConfig import *  # NOQA: E402

# Prepare command line arguments at the very beginning
from crArgumentParser import *
