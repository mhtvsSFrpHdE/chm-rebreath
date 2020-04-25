// https://www.w3schools.com/howto/howto_js_treeview.asp

/** Export catalog node list element from given li element 
 *
 * @param {*} catalogNode A element matching .catalog_node
 */
function getCatalogNodeList(catalogNode) {
  return catalogNode.children[1];
}

/** Export catalog node list element from given li element,
 * but the one come directly with root element.
 *
 * @param {*} catalogNodeListRoot A element matching .catalog_node_list.root
 */
function getRootCatalogNodeList(catalogNodeListRoot) {
  let catalogNode = catalogNodeListRoot.children[0];
  return getCatalogNodeList(catalogNode);
}

/** Toggle catalog node list expand status between folded and expanded
 * via remove or add class attribute
 * 
 * @param {*} catalogNodeList A element matching .catalog_node_list
 */
function toggleCatalogNodeListExpandStatus(catalogNodeList) {
  // catalog node list is folded by default
  let catalogNodeFolded = catalogNodeList.classList.contains("folded");

  if (catalogNodeFolded) {
    catalogNodeList.classList.remove("folded");
    catalogNodeList.classList.add("expanded");
  }
  else {
    catalogNodeList.classList.remove("expanded");
    catalogNodeList.classList.add("folded");
  }
}

/** Initialize catalog div */
function initCatalogDiv() {
  // Find and expand root level catalog node list
  // They are all folded by default
  let rootCatalogNode = document.querySelector('.catalog_node_list.root');
  let rootCatalogNodeList = getRootCatalogNodeList(rootCatalogNode);

  toggleCatalogNodeListExpandStatus(rootCatalogNodeList);
}

/** When html body have loaded */
function onloadHtmlBody() {
  initCatalogDiv();
}