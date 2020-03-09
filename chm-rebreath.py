# 3rd
import logging  # NOQA: E402
#
# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
logging.basicConfig(filename="log.txt")  # NOQA: E402

from bs4 import BeautifulSoup  # HTML parsing

# My
from crConfigHeader import *
from crEnvironmentHeader import *

# Initialize
init_environment(message_config, magic_value_config)


# int main () {


def main():
    print(get_catalog_file_path())


#}
main()
