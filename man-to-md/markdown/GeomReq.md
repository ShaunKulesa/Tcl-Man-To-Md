# NAME

Tk_GeometryRequest, Tk_SetMinimumRequestSize, Tk_SetInternalBorder,
Tk_SetInternalBorderEx - specify desired geometry or internal border for
a window

# SYNOPSIS

**#include \<tk.h\>**

**Tk_GeometryRequest**(*tkwin, reqWidth, reqHeight*)

**Tk_SetMinimumRequestSize**(*tkwin, minWidth, minHeight*)

**Tk_SetInternalBorder**(*tkwin, width*)

**Tk_SetInternalBorderEx**(*tkwin, left, right, top, bottom*)

# ARGUMENTS

Window for which geometry is being requested.

Desired width for *tkwin*, in pixel units.

Desired height for *tkwin*, in pixel units.

Desired minimum requested width for *tkwin*, in pixel units.

Desired minimum requested height for *tkwin*, in pixel units.

Space to leave for internal border for *tkwin*, in pixel units.

Space to leave for left side of internal border for *tkwin*, in pixel
units.

Space to leave for right side of internal border for *tkwin*, in pixel
units.

Space to leave for top side of internal border for *tkwin*, in pixel
units.

Space to leave for bottom side of internal border for *tkwin*, in pixel
units.

# DESCRIPTION

**Tk_GeometryRequest** is called by widget code to indicate its
preference for the dimensions of a particular window. The arguments to
**Tk_GeometryRequest** are made available to the geometry manager for
the window, which then decides on the actual geometry for the window.
Although geometry managers generally try to satisfy requests made to
**Tk_GeometryRequest**, there is no guarantee that this will always be
possible. Widget code should not assume that a geometry request will be
satisfied until it receives a **ConfigureNotify** event indicating that
the geometry change has occurred. Widget code should never call
procedures like **Tk_ResizeWindow** directly. Instead, it should invoke
**Tk_GeometryRequest** and leave the final geometry decisions to the
geometry manager.

If *tkwin* is a top-level window, then the geometry information will be
passed to the window manager using the standard ICCCM protocol.

**Tk_SetInternalBorder** is called by widget code to indicate that the
widget has an internal border. This means that the widget draws a
decorative border inside the window instead of using the standard X
borders, which are external to the window\'s area. For example, internal
borders are used to draw 3-D effects. *Width* specifies the width of the
border in pixels. Geometry managers will use this information to avoid
placing any children of *tkwin* overlapping the outermost *width* pixels
of *tkwin*\'s area.

**Tk_SetInternalBorderEx** works like **Tk_SetInternalBorder** but lets
you specify different widths for different sides of the window.

**Tk_SetMinimumRequestSize** is called by widget code to indicate that a
geometry manager should request at least this size for the widget. This
allows a widget to have some control over its size when a propagating
geometry manager is used inside it.

The information specified in calls to **Tk_GeometryRequest**,
**Tk_SetMinimumRequestSize**, **Tk_SetInternalBorder** and
**Tk_SetInternalBorderEx** can be retrieved using the macros
**Tk_ReqWidth**, **Tk_ReqHeight**, **Tk_MinReqWidth**,
**Tk_MinReqHeight**, **Tk_MinReqWidth**, **Tk_InternalBorderLeft**,
**Tk_InternalBorderRight**, **Tk_InternalBorderTop** and
**Tk_InternalBorderBottom**. See the **Tk_WindowId** manual entry for
details.

# KEYWORDS

geometry, request

<!---
Copyright (c) 1990-1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

