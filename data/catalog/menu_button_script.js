let menu_button_script_namespace = {
    /** Toggle sidebar and related elements expand status
     * some element need to be hidden after fold
     * restore after expand
     */
    toggleSidebarExpandStatus: function () {
        // Fold or expand sidebar and catalog node list
        let sidebar = sidebar_getter_namespace.getSidebar();
        let catalogNodeListContainer = catalog_node_list_getter_namespace.getCatalogNodeListContainer();

        // sidebar is expanded by default
        let sidebarFolded = sidebar.classList.contains("folded");
        if (sidebarFolded) {
            sidebar.classList.remove("folded");
            sidebar.classList.add("expanded");

            catalogNodeListContainer.classList.remove("hide");
        }
        else {
            sidebar.classList.remove("expanded");
            sidebar.classList.add("folded");

            catalogNodeListContainer.classList.add("hide");
        }
    },

    /** Update content area margin left dynamically by matching sidebar width
     * in order to prevent content overlap
     */
    updateContentAreaMargin: function () {
        let sidebarWidth = `${sidebar_getter_namespace.getSidebar().offsetWidth}px`;
        let contentArea = content_area_getter_namespace.getContentArea();

        contentArea.style.marginLeft = sidebarWidth;
    },

    /** When click on menu button
     *
     * change the sidebar fold/expand status
     * change content area margin left to prevent overlapping
     */
    onclickMenuButton: function () {
        this.toggleSidebarExpandStatus();
        this.updateContentAreaMargin();
    }
}
