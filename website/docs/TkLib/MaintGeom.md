# NAME

Tk_MaintainGeometry, Tk_UnmaintainGeometry - maintain geometry of one
window relative to another

# SYNOPSIS

**#include \<tk.h\>**

**Tk_MaintainGeometry**(*window, container, x, y, width, height*)

**Tk_UnmaintainGeometry**(*window, container*)

# ARGUMENTS

Window whose geometry is to be controlled.

Window relative to which *window*\'s geometry will be controlled.

Desired x-coordinate of *window* in *container*, measured in pixels from
the inside of *container*\'s left border to the outside of *window*\'s
left border.

Desired y-coordinate of *window* in *container*, measured in pixels from
the inside of *container*\'s top border to the outside of *window*\'s
top border.

Desired width for *window*, in pixels.

Desired height for *window*, in pixels.

# DESCRIPTION

**Tk_MaintainGeometry** and **Tk_UnmaintainGeometry** make it easier for
geometry managers to deal with windows whose containers are not their
parents. Three problems arise if the container for a window is not its
parent:

\[1\]

:   The x- and y-position of the window must be translated from the
    coordinate system of the container to that of the parent before
    positioning the window.

\[2\]

:   If the container window, or any of its ancestors up to the window\'s
    parent, is moved, then the window must be repositioned within its
    parent in order to maintain the correct position relative to the
    container.

\[3\]

:   If the container or one of its ancestors is mapped or unmapped, then
    the window must be mapped or unmapped to correspond.

None of these problems is an issue if the parent and container are the
same. For example, if the container or one of its ancestors is unmapped,
the window is automatically removed by the screen by X.

**Tk_MaintainGeometry** deals with these problems for windows whose
containers are not their parents, as well as handling the simpler case
of windows whose container are their parents. **Tk_MaintainGeometry** is
typically called by a window manager once it has decided where a window
should be positioned relative to its container. **Tk_MaintainGeometry**
translates the coordinates to the coordinate system of *window*\'s
parent and then moves and resizes the window appropriately. Furthermore,
it remembers the desired position and creates event handlers to monitor
the container and all of its ancestors up to (but not including) the
window\'s parent. If any of these windows is moved, mapped, or unmapped,
the window will be adjusted so that it is mapped only when the container
is mapped and its geometry relative to the container remains as
specified by *x*, *y*, *width*, and *height*.

When a window manager relinquishes control over a window, or if it
decides that it does not want the window to appear on the screen under
any conditions, it calls **Tk_UnmaintainGeometry**.
**Tk_UnmaintainGeometry** unmaps the window and cancels any previous
calls to **Tk_MaintainGeometry** for the *container*-*window* pair, so
that the window\'s geometry and mapped state are no longer maintained
automatically. **Tk_UnmaintainGeometry** need not be called by a
geometry manager if the window, the container, or any of the
container\'s ancestors is destroyed: Tk will call it automatically.

If **Tk_MaintainGeometry** is called repeatedly for the same
*container*-*window* pair, the information from the most recent call
supersedes any older information. If **Tk_UnmaintainGeometry** is called
for a *container*-*window* pair that is is not currently managed, the
call has no effect.

# KEYWORDS

geometry manager, map, container, parent, position, window, unmap
