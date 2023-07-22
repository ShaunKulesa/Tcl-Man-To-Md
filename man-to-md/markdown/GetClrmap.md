# NAME

Tk_GetColormap, Tk_PreserveColormap, Tk_FreeColormap - allocate and free
colormaps

# SYNOPSIS

**#include \<tk.h\>**

Colormap **Tk_GetColormap(***interp, tkwin, string***)**

**Tk_PreserveColormap(***display, colormap***)**

**Tk_FreeColormap(***display, colormap***)**

# ARGUMENTS

Interpreter to use for error reporting.

Token for window in which colormap will be used.

Selects a colormap: either **new** or the name of a window with the same
screen and visual as *tkwin*.

Display for which *colormap* was allocated.

Colormap to free or preserve; must have been returned by a previous call
to **Tk_GetColormap** or **Tk_GetVisual**.

# DESCRIPTION

These procedures are used to manage colormaps. **Tk_GetColormap**
returns a colormap suitable for use in *tkwin*. If its *string* argument
is **new** then a new colormap is created; otherwise *string* must be
the name of another window with the same screen and visual as *tkwin*,
and the colormap from that window is returned. If *string* does not make
sense, or if it refers to a window on a different screen from *tkwin* or
with a different visual than *tkwin*, then **Tk_GetColormap** returns
**None** and leaves an error message in *interp*\'s result.

**Tk_PreserveColormap** increases the internal reference count for a
colormap previously returned by **Tk_GetColormap**, which allows the
colormap to be stored in several locations without knowing which order
they will be released.

**Tk_FreeColormap** should be called when a colormap returned by
**Tk_GetColormap** is no longer needed. Tk maintains a reference count
for each colormap returned by **Tk_GetColormap**, so there should
eventually be one call to **Tk_FreeColormap** for each call to
**Tk_GetColormap** and each call to **Tk_PreserveColormap**. When a
colormap\'s reference count becomes zero, Tk releases the X colormap.

**Tk_GetVisual** and **Tk_GetColormap** work together, in that a new
colormap created by **Tk_GetVisual** may later be returned by
**Tk_GetColormap**. The reference counting mechanism for colormaps
includes both procedures, so callers of **Tk_GetVisual** must also call
**Tk_FreeColormap** to release the colormap. If **Tk_GetColormap** is
called with a *string* value of **new** then the resulting colormap will
never be returned by **Tk_GetVisual**; however, it can be used in other
windows by calling **Tk_GetColormap** with the original window\'s name
as *string*.

# KEYWORDS

colormap, visual

<!---
Copyright (c) 1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

