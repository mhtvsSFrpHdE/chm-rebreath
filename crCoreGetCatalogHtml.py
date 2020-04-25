# 3rd
from yattag import Doc  # Generate HTML

# My
from crLogHeader import *
from crLocaleHeader import *

# Read these code from bottom to top is suggested
#
# Module scope config
environment_config_local = None
message_config_local = None

# Empty HTML template
#
# doc, tag, text = Doc().tagtext()
# doc.asis("<!DOCTYPE html>")
# with tag("html"):
#     with tag("head"):
#         doc.stag("meta", charset="utf-8")
#         with tag("title"):
#     with tag("body"):
#         with tag("p"):


# Format system language to HTML language


def _get_html_language():
    return get_system_language().replace('_', '-')

# Generate content_url a tag


def _get_content_url_tag(catalog_node, doc, tag, text):
    # Url can be None, preset default values may required
    #
    # If have content url:
    if catalog_node.have_content_url:
        with tag("a", href=catalog_node.content_url, target="_blank", klass="catalog_node_url have_url"):
            text(catalog_node.catalog_name)
    #
    # else if no content url:
    else:
        # A tag but without url
        with tag("a", klass="catalog_node_url no_url"):
            text(catalog_node.catalog_name)


# Convert catalog node to HTML object recurse
#
# This code example comes from
# https://www.w3schools.com/howto/howto_js_treeview.asp


def _process_catalog_node(catalog_node, doc, tag, text):
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
                    _process_catalog_node(child, doc, tag, text)


# Fill information into the standard HTML document structure
def get_catalog_html_text(catalog_node):
    global message_config_local

    catalog_html_resource_root_path = environment_config_local['output_catalog_html_resource']['root_path']
    catalog_style_path = catalog_html_resource_root_path + environment_config_local['data_catalog_html_resource']['css_file_name']
    catalog_script_path = catalog_html_resource_root_path + environment_config_local['output_catalog_html_resource']['js_file_name']

    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")
    with tag("html", lang=_get_html_language()):

        # Head & Meta
        with tag("head"):
            doc.stag("meta", charset="utf-8")
            # Title
            with tag("title"):
                text(catalog_node.catalog_name +
                     message_config_local['html_catalog']['title'])

            # CSS
            doc.stag("link", rel="stylesheet", href=catalog_style_path)

            # JavaScript
            with tag("script", "defer", src=catalog_script_path):
                pass

        # Body & onLoad method
        with tag("body", onLoad="catalogOnLoad()"):
            # Catalog scope
            with tag("div", klass="catalog"):
                # Root unordered list
                with tag("ul", klass="catalog_node_list root"):
                    _process_catalog_node(catalog_node, doc, tag, text)

    return doc.getvalue()


# Receive config


def init_core_get_catalog_html(environment_config, message_config):
    global environment_config_local
    global message_config_local

    message_config_local = message_config
    environment_config_local = environment_config
