# NAME

Tk_AllocCursorFromObj, Tk_GetCursor, Tk_GetCursorFromObj,
Tk_GetCursorFromData, Tk_NameOfCursor, Tk_FreeCursorFromObj,
Tk_FreeCursor - maintain database of cursors

# SYNOPSIS

**#include \<tk.h\>**

Tk_Cursor **Tk_AllocCursorFromObj(***interp, tkwin, objPtr***)**

Tk_Cursor **Tk_GetCursor(***interp, tkwin, name***)**

Tk_Cursor **Tk_GetCursorFromObj(***tkwin, objPtr***)**

Tk_Cursor **Tk_GetCursorFromData(***interp, tkwin, source, mask, width,
height, xHot, yHot, fg, bg***)**

const char \* **Tk_NameOfCursor(***display, cursor***)**

**Tk_FreeCursorFromObj(***tkwin, objPtr***)**

**Tk_FreeCursor(***display, cursor***)**

# ARGUMENTS

Interpreter to use for error reporting.

Token for window in which the cursor will be used.

Description of cursor; see below for possible values. Internal rep will
be modified to cache pointer to corresponding Tk_Cursor.

Same as *objPtr* except description of cursor is passed as a string and
resulting Tk_Cursor is not cached.

Data for cursor cursor, in standard cursor format.

Data for mask cursor, in standard cursor format.

Width of *source* and *mask*.

Height of *source* and *mask*.

X-location of cursor hot-spot.

Y-location of cursor hot-spot.

Textual description of foreground color for cursor.

Textual description of background color for cursor.

Display for which *cursor* was allocated.

Opaque Tk identifier for cursor. If passed to **Tk_FreeCursor**, must
have been returned by some previous call to **Tk_GetCursor** or
**Tk_GetCursorFromData**.

# DESCRIPTION

These procedures manage a collection of cursors being used by an
application. The procedures allow cursors to be re-used efficiently,
thereby avoiding server overhead, and also allow cursors to be named
with character strings.

**Tk_AllocCursorFromObj** takes as argument an object describing a
cursor, and returns an opaque Tk identifier for a cursor corresponding
to the description. It re-uses an existing cursor if possible and
creates a new one otherwise. **Tk_AllocCursorFromObj** caches
information about the return value in *objPtr*, which speeds up future
calls to procedures such as **Tk_AllocCursorFromObj** and
**Tk_GetCursorFromObj**. If an error occurs in creating the cursor, such
as when *objPtr* refers to a non-existent file, then **None** is
returned and an error message will be stored in *interp*\'s result if
*interp* is not NULL. *ObjPtr* must contain a standard Tcl list with one
of the following forms:

*name* \[*fgColor* \[*bgColor*\]\]

:   *Name* is the name of a cursor in the standard X cursor cursor,
    i.e., any of the names defined in **cursorcursor.h**, without the
    **XC\_**. Some example values are **X_cursor**, **hand2**, or
    **left_ptr**. Appendix B of by Scheifler & Gettys has illustrations
    showing what each of these cursors looks like. If *fgColor* and
    *bgColor* are both specified, they give the foreground and
    background colors to use for the cursor (any of the forms acceptable
    to **Tk_GetColor** may be used). If only *fgColor* is specified,
    then there will be no background color: the background will be
    transparent. If no colors are specified, then the cursor will use
    black for its foreground color and white for its background color.

    The Macintosh version of Tk supports all of the X cursors and will
    also accept any of the standard Mac cursors including **ibeam**,
    **crosshair**, **watch**, **plus**, and **arrow**. In addition, Tk
    will load Macintosh cursor resources of the types **crsr** (color)
    and **CURS** (black and white) by the name of the resource. The
    application and all its open dynamic library\'s resource files will
    be searched for the named cursor. If there are conflicts color
    cursors will always be loaded in preference to black and white
    cursors.

**@***sourceName maskName fgColor bgColor*

:   In this form, *sourceName* and *maskName* are the names of files
    describing cursors for the cursor\'s source bits and mask. Each file
    must be in standard X11 cursor format. *FgColor* and *bgColor*
    indicate the colors to use for the cursor, in any of the forms
    acceptable to **Tk_GetColor**. This form of the command will not
    work on Macintosh or Windows computers.

**@***sourceName fgColor*

:   This form is similar to the one above, except that the source is
    used as mask also. This means that the cursor\'s background is
    transparent. This form of the command will not work on Macintosh or
    Windows computers.

**@***sourceName*

:   This form only works on Windows, and will load a Windows system
    cursor (**.ani** or **.cur**) from the file specified in
    *sourceName*.

**Tk_GetCursor** is identical to **Tk_AllocCursorFromObj** except that
the description of the cursor is specified with a string instead of an
object. This prevents **Tk_GetCursor** from caching the return value, so
**Tk_GetCursor** is less efficient than **Tk_AllocCursorFromObj**.

**Tk_GetCursorFromObj** returns the token for an existing cursor, given
the window and description used to create the cursor.
**Tk_GetCursorFromObj** does not actually create the cursor; the cursor
must already have been created with a previous call to
**Tk_AllocCursorFromObj** or **Tk_GetCursor**. The return value is
cached in *objPtr*, which speeds up future calls to
**Tk_GetCursorFromObj** with the same *objPtr* and *tkwin*.

**Tk_GetCursorFromData** allows cursors to be created from in-memory
descriptions of their source and mask cursors. *Source* points to
standard cursor data for the cursor\'s source bits, and *mask* points to
standard cursor data describing which pixels of *source* are to be drawn
and which are to be considered transparent. *Width* and *height* give
the dimensions of the cursor, *xHot* and *yHot* indicate the location of
the cursor\'s hot-spot (the point that is reported when an event
occurs), and *fg* and *bg* describe the cursor\'s foreground and
background colors textually (any of the forms suitable for
**Tk_GetColor** may be used). Typically, the arguments to
**Tk_GetCursorFromData** are created by including a cursor file directly
into the source code for a program, as in the following example:

    Tk_Cursor cursor;
    #include "source.cursor"
    #include "mask.cursor"
    cursor = Tk_GetCursorFromData(interp, tkwin, source_bits,
        mask_bits, source_width, source_height, source_x_hot,
        source_y_hot, Tk_GetUid("red"), Tk_GetUid("blue"));

Under normal conditions **Tk_GetCursorFromData** will return an
identifier for the requested cursor. If an error occurs in creating the
cursor then **None** is returned and an error message will be stored in
*interp*\'s result.

**Tk_AllocCursorFromObj**, **Tk_GetCursor**, and
**Tk_GetCursorFromData** maintain a database of all the cursors they
have created. Whenever possible, a call to **Tk_AllocCursorFromObj**,
**Tk_GetCursor**, or **Tk_GetCursorFromData** will return an existing
cursor rather than creating a new one. This approach can substantially
reduce server overhead, so the Tk procedures should generally be used in
preference to Xlib procedures like **XCreateFontCursor** or
**XCreatePixmapCursor**, which create a new cursor on each call. The Tk
procedures are also more portable than the lower-level X procedures.

The procedure **Tk_NameOfCursor** is roughly the inverse of
**Tk_GetCursor**. If its *cursor* argument was created by
**Tk_GetCursor**, then the return value is the *name* argument that was
passed to **Tk_GetCursor** to create the cursor. If *cursor* was created
by a call to **Tk_GetCursorFromData**, or by any other mechanism, then
the return value is a hexadecimal string giving the X identifier for the
cursor. Note: the string returned by **Tk_NameOfCursor** is only
guaranteed to persist until the next call to **Tk_NameOfCursor**. Also,
this call is not portable except for cursors returned by
**Tk_GetCursor**.

When a cursor returned by **Tk_AllocCursorFromObj**, **Tk_GetCursor**,
or **Tk_GetCursorFromData** is no longer needed,
**Tk_FreeCursorFromObj** or **Tk_FreeCursor** should be called to
release it. For **Tk_FreeCursorFromObj** the cursor to release is
specified with the same information used to create it; for
**Tk_FreeCursor** the cursor to release is specified with its Tk_Cursor
token. There should be exactly one call to **Tk_FreeCursor** for each
call to **Tk_AllocCursorFromObj**, **Tk_GetCursor**, or
**Tk_GetCursorFromData**.

# BUGS

In determining whether an existing cursor can be used to satisfy a new
request, **Tk_AllocCursorFromObj**, **Tk_GetCursor**, and
**Tk_GetCursorFromData** consider only the immediate values of their
arguments. For example, when a file name is passed to **Tk_GetCursor**,
**Tk_GetCursor** will assume it is safe to re-use an existing cursor
created from the same file name: it will not check to see whether the
file itself has changed, or whether the current directory has changed,
thereby causing the name to refer to a different file. Similarly,
**Tk_GetCursorFromData** assumes that if the same *source* pointer is
used in two different calls, then the pointers refer to the same data;
it does not check to see if the actual data values have changed.

# KEYWORDS

cursor
