let menu_button_namespace = {
    /** Get sidebar for later use
     * 
     */
    getSidebar: function () {
        let sidebar = document.querySelector('.sidebar');
        return sidebar;
    },

    /** Get catalog node list for later use
     * the root level one
     */
    getCatalogNodeList: function () {
        let catalogNodeList = document.querySelector('.catalog');
        return catalogNodeList;
    },

    /** When click on menu button
     * should change the sidebar fold/expand status
     * some element need to be hidden after fold
     * restore after expand
     */
    onclickMenuButton: function () {
        let sidebar = this.getSidebar();
        let catalogNodeList = this.getCatalogNodeList();
        // Menu button is expanded by default
        let menuButtonFolded = sidebar.classList.contains("folded");


        if (menuButtonFolded) {
            sidebar.classList.remove("folded");
            sidebar.classList.add("expanded");

            catalogNodeList.classList.remove("hide");
        }
        else {
            sidebar.classList.remove("expanded");
            sidebar.classList.add("folded");

            catalogNodeList.classList.add("hide");
        }
    }
}
