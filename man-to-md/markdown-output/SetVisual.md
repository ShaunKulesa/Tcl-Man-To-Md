# NAME

Tk_SetWindowVisual - change visual characteristics of window

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_SetWindowVisual**(*tkwin, visual, depth, colormap*)

# ARGUMENTS

Token for window.

New visual type to use for *tkwin*.

Number of bits per pixel desired for *tkwin*.

New colormap for *tkwin*, which must be compatible with *visual* and
*depth*.

# DESCRIPTION

When Tk creates a new window it assigns it the default visual
characteristics (visual, depth, and colormap) for its screen.
**Tk_SetWindowVisual** may be called to change them.
**Tk_SetWindowVisual** must be called before the window has actually
been created in X (e.g. before **Tk_MapWindow** or
**Tk_MakeWindowExist** has been invoked for the window). The safest
thing is to call **Tk_SetWindowVisual** immediately after calling
**Tk_CreateWindow**. If *tkwin* has already been created before
**Tk_SetWindowVisual** is called then it returns 0 and does not make any
changes; otherwise it returns 1 to signify that the operation completed
successfully.

Note: **Tk_SetWindowVisual** should not be called if you just want to
change a window\'s colormap without changing its visual or depth; call
**Tk_SetWindowColormap** instead.

# KEYWORDS

colormap, depth, visual

<!---
Copyright (c) 1992 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

