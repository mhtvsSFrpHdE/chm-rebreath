# Python import search path
import sys
sys.path.append('./src/thirdParty/crBootstrap')
sys.path.append('./src/thirdParty/cstpw')
sys.path.append('./src/crBootstrapSal')
sys.path.append('./src/crCore')
sys.path.append('./src/crOutput')
sys.path.append('./src/crUnpack')

# 3rd
from bs4 import BeautifulSoup  # NOQA: E402 HTML parsing

# My
from crBootstrapSal import *  # NOQA: E402
import crGlobalLevel as _crGlobalLevel  # NOQA: E402

# All returned path musb be pathlib path

# int main () {


def main():
    # Catalog node placeholder
    catalog_node = None

    # Open
    with open(crEnvironment.get_catalog_chm_file_full_path(), "rb") as chm_catalog_file:
        mySoup = BeautifulSoup(chm_catalog_file, "html5lib")
        catalog_node = crCore.get_catalog_node(mySoup)

    # TODO: Test purpose code, move to other place later
    catalog_html_text = crCore.get_index_html_text(catalog_node)
    root_output_folder_full_path = crEnvironment.get_root_output_folder_full_path()
    crOutput.create_output_folder_structure(root_output_folder_full_path)

    catalog_html_output_full_path = crEnvironment.get_catalog_html_output_full_path(catalog_node.catalog_name)
    catalog_html_resource_output_full_path = crOutput.get_catalog_html_resource_output_full_path(root_output_folder_full_path)

    with open(catalog_html_output_full_path, "w+", encoding="utf-8") as catalog_html_file:
        catalog_html_file.write(catalog_html_text)

    crOutput.copy_catalog_html_resource(catalog_html_resource_output_full_path)


# }

# main()
crInput.get_runtime_input(crArgument.commandline_arguments)
crUnpack.unpack_chm_file()

# If any error occurred during execute
# This statements is false
# (Will not add to log file)
_crGlobalLevel.crLog.logging.info("#========= End properly after main() =#")  # NOQA: E402
