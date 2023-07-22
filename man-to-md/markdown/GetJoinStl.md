# NAME

Tk_GetJoinStyle, Tk_NameOfJoinStyle - translate between strings and join
styles

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetJoinStyle(***interp, string, joinPtr***)**

const char \* **Tk_NameOfJoinStyle(***join***)**

# ARGUMENTS

Interpreter to use for error reporting.

String containing name of join style - one of or - or a unique
abbreviation of one.

Pointer to location in which to store X join style corresponding to
*string*.

Join style: one of **JoinBevel**, **JoinMiter**, **JoinRound**.

# DESCRIPTION

**Tk_GetJoinStyle** places in *\*joinPtr* the X join style corresponding
to *string*, which will be one of **JoinBevel**, **JoinMiter**, or
**JoinRound**. Join styles are typically used in X graphics contexts to
indicate how adjacent line segments should be joined together. See the X
documentation for information on what each style implies.

Under normal circumstances the return value is **TCL_OK** and *interp*
is unused. If *string* does not contain a valid join style or an
abbreviation of one of these names, then an error message is stored in
interpreter *interp*\'s result, **TCL_ERROR** is returned, and
*\*joinPtr* is unmodified.

**Tk_NameOfJoinStyle** is the logical inverse of **Tk_GetJoinStyle**.
Given a join style such as **JoinBevel** it returns a
statically-allocated string corresponding to *join*. If *join* is not a
legal join style, then is returned.

# KEYWORDS

bevel, join style, miter, round

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

