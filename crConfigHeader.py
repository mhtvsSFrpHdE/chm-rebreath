# This file exposes config "object" to global level
# And load them automatically
#
# The entire process is wrapped good,
# so the other modules don't need to worry about how to deal with it
from crConfig import environment_config
from crConfig import magic_value_config
from crConfig import message_config

from crConfig import init_config as _init_config

_init_config()
