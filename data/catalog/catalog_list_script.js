// https://www.w3schools.com/howto/howto_js_treeview.asp

let catalog_list_namespace = {
  /** Export catalog node list element from given li element 
   *
   * @param {*} catalogNode A element matching .catalog_node
   */
  getCatalogNodeSubList: function (catalogNode) {
    return catalogNode.children[1];
  },

  /** Export catalog node list element from given li element,
   * but the one come directly with root element.
   *
   * @param {*} catalogNodeListRoot A element matching .catalog_node_list.root
   */
  getRootCatalogNodeList: function (catalogNodeListRoot) {
    let catalogNode = catalogNodeListRoot.children[0];
    return this.getCatalogNodeList(catalogNode);
  },

  /** Toggle catalog node list expand status between folded and expanded
   * via remove or add class attribute
   * 
   * @param {*} catalogNodeSubList A element matching .catalog_node_list
   */
  toggleCatalogNodeListExpandStatus: function (catalogNodeList) {
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
  },

  /** When click on every catalog node title text
   * If it's parent element can tell it have sub node
   * locate the sub node list and toggle its expand status
   * 
   * @param {*} event Element which fired event
   */
  onclickCatalogNode: function (event) {
    // Check if this one have sub node
    let haveSubNode = event.parentElement.classList.contains("have_sub_node");
    // If not, stop execute
    if (haveSubNode === false) return;

    let catalogNodeList = event.nextElementSibling;

    this.toggleCatalogNodeListExpandStatus(catalogNodeList);
  },

  /** Initialize catalog div
   * 
   */
  initCatalogDiv: function () {
    // Find and expand root level catalog node list
    // They are all folded by default
    let rootCatalogNode = document.querySelector('.catalog_node_list.root');
    let rootCatalogNodeSubList = this.getCatalogNodeSubList(rootCatalogNodeTitle);

    this.toggleCatalogNodeListExpandStatus(rootCatalogNodeList);
  }
}
