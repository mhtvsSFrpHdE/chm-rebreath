# Read these code from bottom to top is suggested


# Generate content_url a tag


def _get_content_url_tag(catalog_node, doc, tag, text):
    # Url can be None, preset default values may required
    #
    # If have content url:
    if catalog_node.have_content_url:
        with tag("span", crCatalogNodeContentUrl=catalog_node.content_url, klass="catalog_node_url have_url", onclick="catalog_list_namespace.onclickCatalogNode(this)"):
            text(catalog_node.catalog_name)
    #
    # else if no content url:
    else:
        # A tag but without url
        with tag("span", klass="catalog_node_url no_url", onclick="onclickCatalogNode(this)"):
            text(catalog_node.catalog_name)


# Convert catalog node to HTML object recurse
#
# This code example comes from
# https://www.w3schools.com/howto/howto_js_treeview.asp


def process_catalog_node(catalog_node, doc, tag, text):
    # A catalog node have two status
    if catalog_node.have_sub_node == False:
        # li with no_sub_node class
        with tag("li", klass="catalog_node no_sub_node"):
            # Name & Url
            _get_content_url_tag(catalog_node, doc, tag, text)
    #
    # else if catalog_node.have_sub_node:
    else:
        # li with have_sub_node class
        with tag("li", klass="catalog_node have_sub_node"):
            # Name & Url
            _get_content_url_tag(catalog_node, doc, tag, text)

            # Create its sub-node
            with tag("ul", klass="catalog_node_list sub folded"):
                for child in catalog_node.sub_node_list:
                    process_catalog_node(child, doc, tag, text)
