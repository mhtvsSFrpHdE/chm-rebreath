# 3rd
from yattag import Doc  # Generate HTML

# My
from crLogHeader import *

# Read these code from bottom to top is suggested
#
# Module scope config
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

# Convert catalog node to HTML object rescue

# This code example comes from
# https://www.w3schools.com/howto/howto_js_treeview.asp


def _process_catalog_node(catalog_node, doc, tag, text):
    with tag("li"):
        with tag("span", klass="caret"):
            text(catalog_node.catalog_name)
        if catalog_node.have_sub_node:
            with tag("ul", klass="nested"):
                for child in catalog_node.sub_node_list:
                    _process_catalog_node(child, doc, tag, text)


# Wrap


def get_catalog_html_text(catalog_node):
    global message_config_local

    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")
    with tag("html"):
        with tag("head"):
            doc.stag("meta", charset="utf-8")
            with tag("title"):
                text(catalog_node.catalog_name +
                     message_config_local['html_catalog']['title'])
        with tag("body"):
            with tag("div"):
                _process_catalog_node(catalog_node, doc, tag, text)

    return doc.getvalue()

# Receive config


def init_core_get_catalog_html(message_config):
    global message_config_local

    message_config_local = message_config
