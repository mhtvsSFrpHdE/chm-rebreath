let page_canvas_script_namespace = {
    /** Update content iframe url 
     * 
     * @param {*} event click event object, should be span, the text
     */
    updatePageCanvasUrl: function (event) {
        let pageCanvas = page_canvas_getter_namespace.getPageCanvas();
        let catalogNodeUrl = catalog_node_list_getter_namespace.getCatalogNodeUrl(event);

        if (catalogNodeUrl !== false) {
            pageCanvas.src = catalogNodeUrl;
        }
    }
};