# My
from crLogHeader import *

# Receive a BeautifulSoup soup object,
# then try to parse it to a rescue catalog node
#
# Read these code from bottom to top is suggested
#
# # Module scope config
message_config_local = None

# Define structure of chm catalog
# Chm catalog divided into two status, have sub-node or not
#
# This status can't be known by itself,
# need to set by the external iterator
#
# All the sub-node is stored in an ordered list


class CrChmCatalogNode():
    # Scan object tag and export name and URL
    # The URL can be None but it doesn't mean that it doesn't contain sub-node
    # About this, check the raw HTML unpacked from chm file for details
    def __init__(self, myObject):
        self.catalog_name = None
        self.content_url = None

        self.have_sub_node = False
        self.sub_node_list = []

        for child in myObject:
            if child.name != "param":
                continue

            if child['name'] == "Name":
                self.catalog_name = child['value']
            elif child['name'] == "Local":
                self.content_url = child['value']


# In the future, this variable may use fo store multiple root nodes,
# or implemented by another solution, just a hint.
catalog_node_list = []

# Scan li tag that contains node, find object tag or other ul tags
# "OBJECT" refer to a catalog node that doesn't have sub-node
# "ul" refer to a catalog, but with sub-node exists
#
# Also detect sub-node node at here


def _process_catalog_li(myLi):
    catalog_node = None
    # Although CrChmCatalogNode has sub-node boolean,
    # but in an iterator it not always initialize for use at the very beginning
    # So here to use a separate boolean to store the status
    have_sub_node = False
    # Call it a list, but for now,
    # the sub-node list supports exactly one sub-node(ul object)
    # Array here allow it possible to hold more than one value once detected,
    # so later can raise an error about it
    sub_node_list = []

    # Scan sub-nodes
    for child in myLi:
        # When child.name == "li",
        # enter a new iteration until a object and it's ul found
        #
        # When child.name == "ul",
        # add it's contents to the sub-node list for later expand
        # The ul tag will contains many li tag,
        # when expand, do iteration for each one(see "li" above)
        #
        # When child.name == "object",
        # create it from the CrChmCatalogNode class
        #
        # The object and ul combined as a pair,
        # and should never appears with a li tag at the same time
        # So the scan can be done with one loop
        # Otherwise, check chm define for more information
        #
        if child.name == "li":
            catalog_node = _process_catalog_li(child)
        #
        elif child.name == "object":
            catalog_node = CrChmCatalogNode(child)
        #
        elif child.name == "ul":
            sub_node_list.append(child)

    # Calculate sub-node list length and raise an error if necessary
    sub_node_list_length = len(sub_node_list)
    if sub_node_list_length > 1:
        error_message = message_config_local['err']['chm_catalog_multiple_sub_node_ul'] + str(
            sub_node_list)
        crPrintCyan(error_message)
        raise NotImplementedError(error_message)
    # Update sub-node status,
    # to make sure there is only one sub-node ul in the current version
    elif sub_node_list_length == 1:
        have_sub_node = True

    if have_sub_node:
        # Copy sub-node status to the class instance
        catalog_node.have_sub_node = True

        # Scan sub-node_list to find li
        # The li refers to this sub-node would also have it's sub-node,
        # in this case, require an iteration to complete
        for child in sub_node_list[0]:
            if child.name == "li":
                catalog_node.sub_node_list.append(_process_catalog_li(child))

    return catalog_node


# Scan root catalog node, find every li tag
# Refer to catalog object or it's sub-node


def _process_catalog_ul(myUl):
    for child in myUl:
        if child.name == "li":
            catalog_node = _process_catalog_li(child)

    return catalog_node

# Scan soup, find ul tag
# Refer to the root node of catalog


def _process_my_soup(mySoup):
    catalog_node = None

    # For now, it can support only one root node
    # Count root node here for later raise an error
    ulCount = 0
    for child in mySoup.body.contents:
        # Filter all ul tag
        if child.name != "ul":
            continue

        ulCount = ulCount + 1
        if ulCount > 1:
            error_message = message_config_local['err']['chm_catalog_multiple_sub_node_ul'] + str(
                child)
            crPrintCyan(error_message)
            raise NotImplementedError(error_message)
        else:
            # Process ul tag found
            catalog_node = _process_catalog_ul(child)

    return catalog_node

# Wrap


def get_catalog_node(mySoup):
    catalog_node = None

    try:
        catalog_node = _process_my_soup(mySoup)
    except:
        logging.exception(__name__)
        raise
    return catalog_node

# Receive config


def init_core_get_catalog_node(message_config):
    global message_config_local

    message_config_local = message_config
