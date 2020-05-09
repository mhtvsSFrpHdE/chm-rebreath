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

    /** Toggle sidebar and related elements expand status
     * some element need to be hidden after fold
     * restore after expand
     */
    toggleSidebarExpandStatus: function () {
        // Fold or expand sidebar and catalog node list
        let sidebar = this.getSidebar();
        let catalogNodeList = this.getCatalogNodeList();

        // sidebar is expanded by default
        let sidebarFolded = sidebar.classList.contains("folded");
        if (sidebarFolded) {
            sidebar.classList.remove("folded");
            sidebar.classList.add("expanded");

            catalogNodeList.classList.remove("hide");
        }
        else {
            sidebar.classList.remove("expanded");
            sidebar.classList.add("folded");

            catalogNodeList.classList.add("hide");
        }
    },
    /** When click on menu button
     *
     * change the sidebar fold/expand status
     * change content area margin left to prevent overlapping
     */
    onclickMenuButton: function () {
    }
}
