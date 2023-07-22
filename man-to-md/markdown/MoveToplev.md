# NAME

Tk_MoveToplevelWindow - Adjust the position of a top-level window

# SYNOPSIS

**#include \<tk.h\>**

**Tk_MoveToplevelWindow(***tkwin, x, y***)**

# ARGUMENTS

Token for top-level window to move.

New x-coordinate for the top-left pixel of *tkwin*\'s border, or the
top-left pixel of the decorative border supplied for *tkwin* by the
window manager, if there is one.

New y-coordinate for the top-left pixel of *tkwin*\'s border, or the
top-left pixel of the decorative border supplied for *tkwin* by the
window manager, if there is one.

# DESCRIPTION

In general, a window should never set its own position; this should be
done only by the geometry manger that is responsible for the window. For
top-level windows the window manager is effectively the geometry
manager; Tk provides interface code between the application and the
window manager to convey the application\'s desires to the geometry
manager. The desired size for a top-level window is conveyed using the
usual **Tk_GeometryRequest** mechanism. The procedure
**Tk_MoveToplevelWindow** may be used by an application to request a
particular position for a top-level window; this procedure is similar in
function to the **wm geometry** Tcl command except that negative offsets
cannot be specified. It is invoked by widgets such as menus that want to
appear at a particular place on the screen.

When **Tk_MoveToplevelWindow** is called it does not immediately pass on
the new desired location to the window manager; it defers this action
until all other outstanding work has been completed, using the
**Tcl_DoWhenIdle** mechanism.

# KEYWORDS

position, top-level window, window manager

<!---
Copyright (c) 1990-1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

