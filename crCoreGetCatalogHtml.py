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

# Wrap


def get_catalog_html_text(catalog_node):
    global message_config_local

    doc, tag, text = Doc().tagtext()
    doc.asis("<!DOCTYPE html>")
    with tag("html"):
        with tag("head"):
            doc.stag("meta", charset="utf-8")
            with tag("title"):
                text("Hello World")
        with tag("body"):
            with tag("p"):
                text("Hello World")

    return doc.getvalue()

# Receive config


def init_core_get_catalog_html(message_config):
    global message_config_local

    message_config_local = message_config
