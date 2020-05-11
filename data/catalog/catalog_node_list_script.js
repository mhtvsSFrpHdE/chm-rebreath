// https://www.w3schools.com/howto/howto_js_treeview.asp

let catalog_node_list_script_namespace = {
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
    toggleCatalogNodeExpandStatusOnClickEntry: function (event) {
        // Check if this one have sub node
        let haveSubNode = event.parentElement.classList.contains("have_sub_node");
        // If not, stop execute
        if (haveSubNode === false) return;

        // Or toggle this sub node
        let catalogNodeTitle = event.parentElement;
        let catalogNodeSubList = event.nextElementSibling;

        this.toggleCatalogNodeExpandStatus(catalogNodeTitle, catalogNodeSubList);
    },


    /** When click on every catalog node title text
     * 
     * Update page canvas url if available
     * 
     * Locate the sub node list and toggle its expand status
     * if it's parent element can tell it have sub node
     * 
     * @param {*} event Element which fired event
     */
    onclickCatalogNode: function (event) {
        // Update content iframe url
        page_canvas_script_namespace.updatePageCanvasUrl(event);

        // These are sub node related
        this.toggleCatalogNodeExpandStatusOnClickEntry(event);
    },


    /** Initialize catalog div
     * 
     */
    initCatalogDiv: function () {
        // Find and expand root level catalog node list
        // They are all folded by default
        let rootCatalogNode = document.querySelector('.catalog_node_list.root');
        let rootCatalogNodeTitle = catalog_node_list_getter_namespace.getCatalogNodeTitle(rootCatalogNode);
        let rootCatalogNodeSubList = catalog_node_list_getter_namespace.getCatalogNodeSubList(rootCatalogNodeTitle);

        this.toggleCatalogNodeExpandStatus(rootCatalogNodeTitle, rootCatalogNodeSubList);
    }
}
