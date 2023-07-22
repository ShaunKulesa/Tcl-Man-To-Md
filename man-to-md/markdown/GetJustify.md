# NAME

Tk_GetJustifyFromObj, Tk_GetJustify, Tk_NameOfJustify - translate
between strings and justification styles

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetJustifyFromObj(***interp, objPtr, justifyPtr***)**

int **Tk_GetJustify(***interp, string, justifyPtr***)**

const char \* **Tk_NameOfJustify(***justify***)**

# ARGUMENTS

Interpreter to use for error reporting, or NULL.

String value contains name of justification style - one of or - or a
unique abbreviation of one. The internal rep will be modified to cache
corresponding justify value.

Same as *objPtr* except description of justification style is passed as
a string.

Pointer to location in which to store justify value corresponding to
*objPtr* or *string*.

Justification style (one of the values listed below).

# DESCRIPTION

**Tk_GetJustifyFromObj** places in *\*justifyPtr* the justify value
corresponding to *objPtr*\'s value. This value will be one of the
following:

**TK_JUSTIFY_LEFT**

:   Means that the text on each line should start at the left edge of
    the line; as a result, the right edges of lines may be ragged.

**TK_JUSTIFY_RIGHT**

:   Means that the text on each line should end at the right edge of the
    line; as a result, the left edges of lines may be ragged.

**TK_JUSTIFY_CENTER**

:   Means that the text on each line should be centered; as a result,
    both the left and right edges of lines may be ragged.

Under normal circumstances the return value is **TCL_OK** and *interp*
is unused. If *objPtr* does not contain a valid justification style or
an abbreviation of one of these names, **TCL_ERROR** is returned,
*\*justifyPtr* is unmodified, and an error message is stored in
*interp*\'s result if *interp* is not NULL. **Tk_GetJustifyFromObj**
caches information about the return value in *objPtr*, which speeds up
future calls to **Tk_GetJustifyFromObj** with the same *objPtr*.

**Tk_GetJustify** is identical to **Tk_GetJustifyFromObj** except that
the description of the justification is specified with a string instead
of an object. This prevents **Tk_GetJustify** from caching the return
value, so **Tk_GetJustify** is less efficient than
**Tk_GetJustifyFromObj**.

**Tk_NameOfJustify** is the logical inverse of **Tk_GetJustify**. Given
a justify value it returns a statically-allocated string corresponding
to *justify*. If *justify* is not a legal justify value, then is
returned.

# KEYWORDS

center, fill, justification, string

<!---
Copyright (c) 1990-1994 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

