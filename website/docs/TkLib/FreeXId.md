# NAME

Tk_FreeXId - make X resource identifier available for reuse

# SYNOPSIS

**#include \<tk.h\>**

**Tk_FreeXId(***display, id***)**

# ARGUMENTS

Display for which *id* was allocated.

Identifier of X resource (window, font, pixmap, cursor, graphics
context, or colormap) that is no longer in use.

# DESCRIPTION

The default allocator for resource identifiers provided by Xlib is very
simple-minded and does not allow resource identifiers to be re-used. If
a long-running application reaches the end of the resource id space, it
will generate an X protocol error and crash. Tk replaces the default id
allocator with its own allocator, which allows identifiers to be reused.
In order for this to work, **Tk_FreeXId** must be called to tell the
allocator about resources that have been freed. Tk automatically calls
**Tk_FreeXId** whenever it frees a resource, so if you use procedures
like **Tk_GetFont**, **Tk_GetGC**, and **Tk_GetPixmap** then you need
not call **Tk_FreeXId**. However, if you allocate resources directly
from Xlib, for example by calling **XCreatePixmap**, then you should
call **Tk_FreeXId** when you call the corresponding Xlib free procedure,
such as **XFreePixmap**. If you do not call **Tk_FreeXId** then the
resource identifier will be lost, which could cause problems if the
application runs long enough to lose all of the available identifiers.

# KEYWORDS

resource identifier
