# This file exposes config "object" to global level
# And load them automatically
#
# The entire process is wrapped good,
# so the other modules don't need to worry about how to deal with it
from crConfig import environment_config
from crConfig import magic_value_config
from crConfig import message_config

from crConfig import config_init as _config_init

_config_init()
