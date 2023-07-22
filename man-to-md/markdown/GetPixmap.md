# NAME

Tk_GetPixmap, Tk_FreePixmap - allocate and free pixmaps

# SYNOPSIS

**#include \<tk.h\>**

Pixmap **Tk_GetPixmap(***display, d, width, height, depth***)**

**Tk_FreePixmap(***display, pixmap***)**

# ARGUMENTS

X display for the pixmap.

Pixmap or window where the new pixmap will be used for drawing.

Width of pixmap.

Height of pixmap.

Number of bits per pixel in pixmap.

Pixmap to destroy.

# DESCRIPTION

These procedures are identical to the Xlib procedures **XCreatePixmap**
and **XFreePixmap**, except that they have extra code to manage X
resource identifiers so that identifiers for deleted pixmaps can be
reused in the future. It is important for Tk applications to use these
procedures rather than **XCreatePixmap** and **XFreePixmap**; otherwise
long-running applications may run out of resource identifiers.

**Tk_GetPixmap** creates a pixmap suitable for drawing in *d*, with
dimensions given by *width*, *height*, and *depth*, and returns its
identifier. **Tk_FreePixmap** destroys the pixmap given by *pixmap* and
makes its resource identifier available for reuse.

# KEYWORDS

pixmap, resource identifier

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

