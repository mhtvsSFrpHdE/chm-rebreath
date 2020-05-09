# 3rd
from yattag import Doc  # Generate HTML

# My
from crLogHeader import *
from crLocaleHeader import *
from crCoreGetCatalogHtml import process_catalog_node

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


# Fill information into the standard HTML document structure
def get_index_html_text(catalog_node):
    global message_config_local

    catalog_html_resource_root_path = environment_config_local['output_catalog_html_resource']['root_path']

    catalog_style_path = catalog_html_resource_root_path + 'style.css'
    catalog_list_script_path = catalog_html_resource_root_path + 'catalog_list_script.js'
    menu_button_script_path = catalog_html_resource_root_path + 'menu_button_script.js'
    html_body_script_path = catalog_html_resource_root_path + 'html_body_script.js'

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
            with tag("script", "defer", src=catalog_list_script_path):
                pass
            with tag("script", "defer", src=menu_button_script_path):
                pass
            with tag("script", "defer", src=html_body_script_path):
                pass

        # Body & onLoad method
        with tag("body", onload="onloadHtmlBody()"):
            # Catalog scope
            with tag("div", klass="sidebar expanded"):
                # Menu button
                with tag("p"):
                    with tag("img", src="catalog/icon/menu-24px.svg", klass="menu_button", onclick="menu_button_namespace.onclickMenuButton()"):
                        pass
                doc.stag("br")
                # Root unordered list
                with tag("div", klass="catalog"):
                    with tag("ul", klass="catalog_node_list root"):
                        process_catalog_node(catalog_node, doc, tag, text)
            
            # Content area
            with tag("div", klass="content"):
                with tag("iframe", klass="page_canvas"):
                    pass

    return doc.getvalue()

# Receive config


def init_core_get_index_html(environment_config, message_config):
    global environment_config_local
    global message_config_local

    message_config_local = message_config
    environment_config_local = environment_config
