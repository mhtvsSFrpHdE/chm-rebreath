## Why there are py files called "Header"?

This is not a usual python programming style.  
I didn't realize that a variable or function name start with "\_" will not be "imported".  
So I made a second py "Header" file to import what I really want to "can be imported".  
These legacy style will be removed as much as possible.

Some of them import same library but have different use, to prevent namespace conflicts,  
they still use header to export only necessary namespaces
