// https://www.w3schools.com/howto/howto_js_treeview.asp

  }
/** Initialize catalog div */
function initCatalogDiv() {
  // Find and expand root level catalog node list
  // They are all folded by default
  let rootCatalogNode = document.querySelector('.catalog_node_list.root');
  let rootCatalogNodeList = getTopLevelCatalogNodeList(rootCatalogNode);

  toggleCatalogNodeListExpandStatus(rootCatalogNodeList);
}

/** When html body have loaded */
function onloadHtmlBody() {
  initCatalogDiv();
}