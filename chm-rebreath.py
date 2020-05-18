# Python import search path
import sys
sys.path.append('./src/crBootstrap')
sys.path.append('./src/crBootstrapSal')
sys.path.append('./src/crCore')
sys.path.append('./src/crOutput')

# 3rd
from bs4 import BeautifulSoup  # HTML parsing

# My
from crBootstrap import *
from crBootstrapSalHeader import *
from crLogHeader import *

# These three variable are imported by crBootstrap
# Then apply project dependent preprocessors by crBootstrapSal
environment_config, magic_value_config, message_config = init_bootstrap_sal(environment_config, magic_value_config, message_config)

# All returned path musb be pathlib path

# int main () {


def main():
    # Catalog node placeholder
    catalog_node = None

    # Open 
    with open(get_catalog_chm_file_full_path(), "rb") as chm_catalog_file:
        mySoup = BeautifulSoup(chm_catalog_file, "html5lib")
        catalog_node = get_catalog_node(mySoup)

    # TODO: Test purpose code, move to other place later
    catalog_html_text = get_index_html_text(catalog_node)
    root_output_folder_full_path = get_root_output_folder_full_path()
    create_output_folder_structure(root_output_folder_full_path)
    
    catalog_html_output_full_path = get_catalog_html_output_full_path(catalog_node.catalog_name)
    catalog_html_resource_output_full_path = get_catalog_html_resource_output_full_path(root_output_folder_full_path)

    with open(catalog_html_output_full_path, "w+", encoding="utf-8") as catalog_html_file:
        catalog_html_file.write(catalog_html_text)

    copy_catalog_html_resource(catalog_html_resource_output_full_path)


# }

main()

# This statements is false
# If any error occurred before
logging.info("#========= End properly after main() =#")  # NOQA: E402
