// https://www.w3schools.com/howto/howto_js_treeview.asp

let catalog_list_namespace = {
  /** Export catalog node list element from given li element 
   *
   * @param {*} catalogNode A element matching .catalog_node
   */
  getCatalogNodeSubList: function (catalogNode) {
    return catalogNode.children[1];
  },

  /** Export catalog node title element from given li element
   * 
   * @param {*} catalogNode A element matching .catalog_node
  */
  getCatalogNodeTitle: function (catalogNode) {
    return catalogNode.children[0];
  },

  /** Toggle catalog node list expand status between folded and expanded
   * via remove or add class attribute
   * 
   * @param {*} catalogNodeTitle A element matching .catalog_node_url
   * @param {*} catalogNodeSubList A element matching .catalog_node_list
   */
  toggleCatalogNodeExpandStatus: function (catalogNodeTitle, catalogNodeSubList) {
    // The two status should sync together so use one condition
    let catalogNodeFolded = catalogNodeTitle.classList.contains("folded");

    // if catalogNode is Folded
    if (catalogNodeFolded) {
      catalogNodeTitle.classList.remove("folded");
      catalogNodeTitle.classList.add("expanded");

      catalogNodeSubList.classList.remove("folded");
      catalogNodeSubList.classList.add("expanded");
    }
    // else if catalogNode is Expanded
    else {
      catalogNodeTitle.classList.remove("expanded");
      catalogNodeTitle.classList.add("folded");

      catalogNodeSubList.classList.remove("expanded");
      catalogNodeSubList.classList.add("folded");
    }
  },

  /** Same as toggleCatalogNodeExpandStatus but for click event
   * the two situation have different entry point
   * 
   * @param {*} event click event object, should be span, the text
   */
  onclickToggleCatalogNodeExpandStatus: function (event) {
    let catalogNodeTitle = event.parentElement;
    let catalogNodeSubList = event.nextElementSibling;

    this.toggleCatalogNodeExpandStatus(catalogNodeTitle, catalogNodeSubList);
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

    this.onclickToggleCatalogNodeExpandStatus(event);
  },

  /** Initialize catalog div
   * 
   */
  initCatalogDiv: function () {
    // Find and expand root level catalog node list
    // They are all folded by default
    let rootCatalogNode = document.querySelector('.catalog_node_list.root');
    let rootCatalogNodeTitle = this.getCatalogNodeTitle(rootCatalogNode);
    let rootCatalogNodeSubList = this.getCatalogNodeSubList(rootCatalogNodeTitle);

    this.toggleCatalogNodeExpandStatus(rootCatalogNodeTitle, rootCatalogNodeSubList);
  }
}
