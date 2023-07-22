# NAME

Tk_CoordsToWindow - Find window containing a point

# SYNOPSIS

**#include \<tk.h\>**

Tk_Window **Tk_CoordsToWindow**(*rootX, rootY, tkwin*)

# ARGUMENTS

X-coordinate (in root window coordinates).

Y-coordinate (in root window coordinates).

Token for window that identifies application.

# DESCRIPTION

**Tk_CoordsToWindow** locates the window that contains a given point.
The point is specified in root coordinates with *rootX* and *rootY* (if
a virtual-root window manager is in use then *rootX* and *rootY* are in
the coordinate system of the virtual root window). The return value from
the procedure is a token for the window that contains the given point.
If the point is not in any window, or if the containing window is not in
the same application as *tkwin*, then NULL is returned.

The containing window is decided using the same rules that determine
which window contains the mouse cursor: if a parent and a child both
contain the point then the child gets preference, and if two siblings
both contain the point then the highest one in the stacking order (i.e.
the one that\'s visible on the screen) gets preference.

# KEYWORDS

containing, coordinates, root window

<!---
Copyright (c) 1990-1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

