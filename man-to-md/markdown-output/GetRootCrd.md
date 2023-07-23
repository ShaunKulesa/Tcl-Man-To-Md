# NAME

Tk_GetRootCoords - Compute root-window coordinates of window

# SYNOPSIS

**#include \<tk.h\>**

**Tk_GetRootCoords**(*tkwin, xPtr, yPtr*)

# ARGUMENTS

Token for window.

Pointer to location in which to store root-window x-coordinate
corresponding to left edge of *tkwin*\'s border.

Pointer to location in which to store root-window y-coordinate
corresponding to top edge of *tkwin*\'s border.

# DESCRIPTION

This procedure scans through the structural information maintained by Tk
to compute the root-window coordinates corresponding to the upper-left
corner of *tkwin*\'s border. If *tkwin* has no border, then
**Tk_GetRootCoords** returns the root-window coordinates corresponding
to location (0,0) in *tkwin*. **Tk_GetRootCoords** is relatively
efficient, since it does not have to communicate with the X server.

# KEYWORDS

coordinates, root window

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

