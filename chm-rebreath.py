# 3rd
from bs4 import BeautifulSoup  # HTML parsing

# My
from crBootstrap import *

# int main () {


def main():
    with open(get_catalog_file_path(), "rb") as chm_catalog_file:
        mySoup = BeautifulSoup(chm_catalog_file, "html5lib")
        catalog_node = get_catalog_node(mySoup)

        get_catalog_html_text(catalog_node)


#}
main()
