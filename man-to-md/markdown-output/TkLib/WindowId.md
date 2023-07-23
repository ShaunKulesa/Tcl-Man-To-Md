# NAME

Tk_WindowId, Tk_Parent, Tk_Display, Tk_DisplayName, Tk_ScreenNumber,
Tk_Screen, Tk_X, Tk_Y, Tk_Width, Tk_Height, Tk_Changes, Tk_Attributes,
Tk_IsContainer, Tk_IsEmbedded, Tk_IsMapped, Tk_IsTopLevel, Tk_ReqWidth,
Tk_ReqHeight, Tk_MinReqWidth, Tk_MinReqHeight, Tk_InternalBorderLeft,
Tk_InternalBorderRight, Tk_InternalBorderTop, Tk_InternalBorderBottom,
Tk_Visual, Tk_Depth, Tk_Colormap, Tk_Interp - retrieve information from
Tk\'s local data structure

# SYNOPSIS

**#include \<tk.h\>**

Window **Tk_WindowId**(*tkwin*)

Tk_Window **Tk_Parent**(*tkwin*)

Display \* **Tk_Display**(*tkwin*)

const char \* **Tk_DisplayName**(*tkwin*)

int **Tk_ScreenNumber**(*tkwin*)

Screen \* **Tk_Screen**(*tkwin*)

int **Tk_X**(*tkwin*)

int **Tk_Y**(*tkwin*)

int **Tk_Width**(*tkwin*)

int **Tk_Height**(*tkwin*)

XWindowChanges \* **Tk_Changes**(*tkwin*)

XSetWindowAttributes \* **Tk_Attributes**(*tkwin*)

int **Tk_IsContainer**(*tkwin*)

int **Tk_IsEmbedded**(*tkwin*)

int **Tk_IsMapped**(*tkwin*)

int **Tk_IsTopLevel**(*tkwin*)

int **Tk_ReqWidth**(*tkwin*)

int **Tk_ReqHeight**(*tkwin*)

int **Tk_MinReqWidth**(*tkwin*)

int **Tk_MinReqHeight**(*tkwin*)

int **Tk_InternalBorderLeft**(*tkwin*)

int **Tk_InternalBorderRight**(*tkwin*)

int **Tk_InternalBorderTop**(*tkwin*)

int **Tk_InternalBorderBottom**(*tkwin*)

Visual \* **Tk_Visual**(*tkwin*)

int **Tk_Depth**(*tkwin*)

Colormap **Tk_Colormap**(*tkwin*)

Tcl_Interp \* **Tk_Interp**(*tkwin*)

# ARGUMENTS

Token for window.

# DESCRIPTION

**Tk_WindowId** and the other names listed above are all macros that
return fields from Tk\'s local data structure for *tkwin*. None of these
macros requires any interaction with the server; it is safe to assume
that all are fast.

**Tk_WindowId** returns the X identifier for *tkwin*, or **NULL** if no
X window has been created for *tkwin* yet.

**Tk_Parent** returns Tk\'s token for the logical parent of *tkwin*. The
parent is the token that was specified when *tkwin* was created, or NULL
for main windows.

**Tk_Interp** returns the Tcl interpreter associated with a *tkwin* or
NULL if there is an error.

**Tk_Display** returns a pointer to the Xlib display structure
corresponding to *tkwin*. **Tk_DisplayName** returns an ASCII string
identifying *tkwin*\'s display. **Tk_ScreenNumber** returns the index of
*tkwin*\'s screen among all the screens of *tkwin*\'s display.
**Tk_Screen** returns a pointer to the Xlib structure corresponding to
*tkwin*\'s screen.

**Tk_X**, **Tk_Y**, **Tk_Width**, and **Tk_Height** return information
about *tkwin\'s* location within its parent and its size. The location
information refers to the upper-left pixel in the window, or its border
if there is one. The width and height information refers to the interior
size of the window, not including any border. **Tk_Changes** returns a
pointer to a structure containing all of the above information plus a
few other fields. **Tk_Attributes** returns a pointer to an
XSetWindowAttributes structure describing all of the attributes of the
*tkwin*\'s window, such as background pixmap, event mask, and so on (Tk
keeps track of all this information as it is changed by the
application). Note: it is essential that applications use Tk procedures
like **Tk_ResizeWindow** instead of X procedures like **XResizeWindow**,
so that Tk can keep its data structures up-to-date.

**Tk_IsContainer** returns a non-zero value if *tkwin* is a container,
and that some other application may be embedding itself inside *tkwin*.

**Tk_IsEmbedded** returns a non-zero value if *tkwin* is not a
free-standing window, but rather is embedded in some other application.

**Tk_IsMapped** returns a non-zero value if *tkwin* is mapped and zero
if *tkwin* is not mapped.

**Tk_IsTopLevel** returns a non-zero value if *tkwin* is a top-level
window (its X parent is the root window of the screen) and zero if
*tkwin* is not a top-level window.

**Tk_ReqWidth** and **Tk_ReqHeight** return information about the
window\'s requested size. These values correspond to the last call to
**Tk_GeometryRequest** for *tkwin*.

**Tk_MinReqWidth** and **Tk_MinReqHeight** return information about the
window\'s minimum requested size. These values correspond to the last
call to **Tk_SetMinimumRequestSize** for *tkwin*.

**Tk_InternalBorderLeft**, **Tk_InternalBorderRight**,
**Tk_InternalBorderTop** and **Tk_InternalBorderBottom** return the
width of one side of the internal border that has been requested for
*tkwin*, or 0 if no internal border was requested. The return value is
simply the last value passed to **Tk_SetInternalBorder** or
**Tk_SetInternalBorderEx** for *tkwin*.

**Tk_Visual**, **Tk_Depth**, and **Tk_Colormap** return information
about the visual characteristics of a window. **Tk_Visual** returns the
visual type for the window, **Tk_Depth** returns the number of bits per
pixel, and **Tk_Colormap** returns the current colormap for the window.
The visual characteristics are normally set from the defaults for the
window\'s screen, but they may be overridden by calling
**Tk_SetWindowVisual**.

# KEYWORDS

attributes, colormap, depth, display, height, geometry manager,
identifier, mapped, requested size, screen, top-level, visual, width,
window, x, y

<!---
Copyright (c) 1990-1993 The Regents of the University of California
Copyright (c) 1994-1997 Sun Microsystems, Inc
-->

