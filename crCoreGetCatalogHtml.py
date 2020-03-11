# My
from crLogHeader import *

# Read these code from bottom to top is suggested
#
# Module scope config
message_config_local = None

# Receive config


def init_core_get_catalog_html(message_config):
    global message_config_local

    message_config_local = message_config