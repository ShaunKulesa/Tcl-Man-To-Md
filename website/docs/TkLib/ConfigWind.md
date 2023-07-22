# NAME

Tk_ConfigureWindow, Tk_MoveWindow, Tk_ResizeWindow, Tk_MoveResizeWindow,
Tk_SetWindowBorderWidth, Tk_ChangeWindowAttributes,
Tk_SetWindowBackground, Tk_SetWindowBackgroundPixmap,
Tk_SetWindowBorder, Tk_SetWindowBorderPixmap, Tk_SetWindowColormap,
Tk_DefineCursor, Tk_UndefineCursor - change window configuration or
attributes

# SYNOPSIS

**#include \<tk.h\>**

**Tk_ConfigureWindow**(*tkwin, valueMask, valuePtr*)

**Tk_MoveWindow**(*tkwin, x, y*)

**Tk_ResizeWindow**(*tkwin, width, height*)

**Tk_MoveResizeWindow**(*tkwin, x, y, width, height*)

**Tk_SetWindowBorderWidth**(*tkwin, borderWidth*)

**Tk_ChangeWindowAttributes**(*tkwin, valueMask, attsPtr*)

**Tk_SetWindowBackground**(*tkwin, pixel*)

**Tk_SetWindowBackgroundPixmap**(*tkwin, pixmap*)

**Tk_SetWindowBorder**(*tkwin, pixel*)

**Tk_SetWindowBorderPixmap**(*tkwin, pixmap*)

**Tk_SetWindowColormap**(*tkwin, colormap*)

**Tk_DefineCursor**(*tkwin, cursor*)

**Tk_UndefineCursor**(*tkwin*)

# ARGUMENTS

Token for window.

OR-ed mask of values like **CWX** or **CWBorderPixel**, indicating which
fields of *\*valuePtr* or *\*attsPtr* to use.

Points to a structure containing new values for the configuration
parameters selected by *valueMask*. Fields not selected by *valueMask*
are ignored.

New x-coordinate for *tkwin*\'s top left pixel (including border, if
any) within tkwin\'s parent.

New y-coordinate for *tkwin*\'s top left pixel (including border, if
any) within tkwin\'s parent.

New width for *tkwin* (interior, not including border).

New height for *tkwin* (interior, not including border).

New width for *tkwin*\'s border.

Points to a structure containing new values for the attributes given by
the *valueMask* argument. Attributes not selected by *valueMask* are
ignored.

New background or border color for window.

New pixmap to use for background or border of *tkwin*. WARNING: cannot
necessarily be deleted immediately, as for Xlib calls. See note below.

New colormap to use for *tkwin*.

New cursor to use for *tkwin*. If **None** is specified, then *tkwin*
will not have its own cursor; it will use the cursor of its parent.

# DESCRIPTION

These procedures are analogous to the X library procedures with similar
names, such as **XConfigureWindow**. Each one of the above procedures
calls the corresponding X procedure and also saves the configuration
information in Tk\'s local structure for the window. This allows the
information to be retrieved quickly by the application (using macros
such as **Tk_X** and **Tk_Height**) without having to contact the X
server. In addition, if no X window has actually been created for
*tkwin* yet, these procedures do not issue X operations or cause event
handlers to be invoked; they save the information in Tk\'s local
structure for the window; when the window is created later, the saved
information will be used to configure the window.

See the X library documentation for details on what these procedures do
and how they use their arguments.

In the procedures **Tk_ConfigureWindow**, **Tk_MoveWindow**,
**Tk_ResizeWindow**, **Tk_MoveResizeWindow**, and
**Tk_SetWindowBorderWidth**, if *tkwin* is an internal window then event
handlers interested in configure events are invoked immediately, before
the procedure returns. If *tkwin* is a top-level window then the event
handlers will be invoked later, after X has seen the request and
returned an event for it.

Applications using Tk should never call procedures like
**XConfigureWindow** directly; they should always use the corresponding
Tk procedures.

The size and location of a window should only be modified by the
appropriate geometry manager for that window and never by a window
itself (but see **Tk_MoveToplevelWindow** for moving a top-level
window).

You may not use **Tk_ConfigureWindow** to change the stacking order of a
window (*valueMask* may not contain the **CWSibling** or **CWStackMode**
bits). To change the stacking order, use the procedure
**Tk_RestackWindow**.

The procedure **Tk_SetWindowColormap** will automatically add *tkwin* to
the **TK_COLORMAP_WINDOWS** property of its nearest top-level ancestor
if the new colormap is different from that of *tkwin*\'s parent and
*tkwin* is not already in the **TK_COLORMAP_WINDOWS** property.

# BUGS

**Tk_SetWindowBackgroundPixmap** and **Tk_SetWindowBorderPixmap** differ
slightly from their Xlib counterparts in that the *pixmap* argument may
not necessarily be deleted immediately after calling one of these
procedures. This is because *tkwin*\'s window may not exist yet at the
time of the call, in which case *pixmap* is merely saved and used later
when *tkwin*\'s window is actually created. If you wish to delete
*pixmap*, then call **Tk_MakeWindowExist** first to be sure that
*tkwin*\'s window exists and *pixmap* has been passed to the X server.

A similar problem occurs for the *cursor* argument passed to
**Tk_DefineCursor**. The solution is the same as for pixmaps above: call
**Tk_MakeWindowExist** before freeing the cursor.

# SEE ALSO

Tk_MoveToplevelWindow, Tk_RestackWindow

# KEYWORDS

attributes, border, color, configure, height, pixel, pixmap, width,
window, x, y
