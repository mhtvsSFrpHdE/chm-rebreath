let catalog_node_list_getter_namespace = {
    /** Get catalog node list CONTAINER for later use
     */
    getCatalogNodeListContainer: function () {
        let catalogNodeList = document.querySelector('.catalog');
        return catalogNodeList;
    },


    /** Export catalog node sub list element from given li element 
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


    /** Export catalog node url from attribute
     * return url or false if there is no url out there
     * 
     * @param {*} event click event object, should be span, the text
     */
    getCatalogNodeUrl: function (event) {
        let catalogNodeUrl = event.getAttribute('crCatalogNodeUrl');

        // if not null
        if (catalogNodeUrl !== null) {
            return catalogNodeUrl;
        }
        // if null
        else {
            return false;
        }
    }
};