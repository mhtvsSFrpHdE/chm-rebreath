# 3rd
import logging  # NOQA: E402
#
# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
logging.basicConfig(filename="log.txt")  # NOQA: E402

from bs4 import BeautifulSoup  # HTML parsing

# My
from crConfigHeader import *
from crEnvironment import *

# Initialize environment
environment_init(message_config, magic_value_config)


# int main () {


def main():
    print(magic_value_config['dev']['config_version'])


#}
main()
