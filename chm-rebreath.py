# 3rd
import pathlib  # Path
import logging

from bs4 import BeautifulSoup  # HTML parsing

# My
import crMagicValue

from crEnvironmentHeader import *

# Initialize log file
# We do not dealing with external error, just print and crash
logging.basicConfig(filename=crMagicValue.logfileName)

# int main () {


def main():
    print(_getCatalogFilePath())


#}
main()
