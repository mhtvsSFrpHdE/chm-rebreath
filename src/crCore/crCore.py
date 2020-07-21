# The "Header" style at here will not be removed
# There are too many namespace either public or private in these files
# With a header we can just export the required namespace,
# and ignore any other public namespace to reduce time consume

# On another hand, crCore is a couple of files
# This header collect them as a full concept

# This file exposes project feature code for use,
# that all code not related to infrastructure

from crCoreGetCatalogNode import get_catalog_node
from crCoreGetCatalogNode import init_core_get_catalog_node

from crCoreGetIndexHtml import get_index_html_text
from crCoreGetIndexHtml import init_core_get_index_html
