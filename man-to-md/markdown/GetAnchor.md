# NAME

Tk_GetAnchorFromObj, Tk_GetAnchor, Tk_NameOfAnchor - translate between
strings and anchor positions

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetAnchorFromObj(***interp, objPtr, anchorPtr***)**

int **Tk_GetAnchor(***interp, string, anchorPtr***)**

const char \* **Tk_NameOfAnchor(***anchor***)**

# ARGUMENTS

Interpreter to use for error reporting, or NULL.

String value contains name of anchor point: or internal rep will be
modified to cache corresponding Tk_Anchor. In the case of on input, a
non-empty abbreviation of it may also be used on input.

Same as *objPtr* except description of anchor point is passed as a
string.

Pointer to location in which to store anchor position corresponding to
*objPtr* or *string*.

Anchor position, e.g. **TCL_ANCHOR_CENTER**.

# DESCRIPTION

**Tk_GetAnchorFromObj** places in *\*anchorPtr* an anchor position
(enumerated type **Tk_Anchor**) corresponding to *objPtr*\'s value. The
result will be one of **TK_ANCHOR_N**, **TK_ANCHOR_NE**,
**TK_ANCHOR_E**, **TK_ANCHOR_SE**, **TK_ANCHOR_S**, **TK_ANCHOR_SW**,
**TK_ANCHOR_W**, **TK_ANCHOR_NW**, or **TK_ANCHOR_CENTER**. Anchor
positions are typically used for indicating a point on an object that
will be used to position the object, e.g. **TK_ANCHOR_N** means position
the top center point of the object at a particular place.

Under normal circumstances the return value is **TCL_OK** and *interp*
is unused. If *string* does not contain a valid anchor position or an
abbreviation of one of these names, **TCL_ERROR** is returned,
*\*anchorPtr* is unmodified, and an error message is stored in
*interp*\'s result if *interp* is not NULL. **Tk_GetAnchorFromObj**
caches information about the return value in *objPtr*, which speeds up
future calls to **Tk_GetAnchorFromObj** with the same *objPtr*.

**Tk_GetAnchor** is identical to **Tk_GetAnchorFromObj** except that the
description of the anchor is specified with a string instead of an
object. This prevents **Tk_GetAnchor** from caching the return value, so
**Tk_GetAnchor** is less efficient than **Tk_GetAnchorFromObj**.

**Tk_NameOfAnchor** is the logical inverse of **Tk_GetAnchor**. Given an
anchor position such as **TK_ANCHOR_N** it returns a
statically-allocated string corresponding to *anchor*. If *anchor* is
not a legal anchor value, then is returned.

# KEYWORDS

anchor position

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

