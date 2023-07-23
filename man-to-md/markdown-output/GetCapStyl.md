# NAME

Tk_GetCapStyle, Tk_NameOfCapStyle - translate between strings and cap
styles

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetCapStyle(***interp, string, capPtr***)**

const char \* **Tk_NameOfCapStyle(***cap***)**

# ARGUMENTS

Interpreter to use for error reporting.

String containing name of cap style - one of or - or a unique
abbreviation of one.

Pointer to location in which to store X cap style corresponding to
*string*.

Cap style: one of **CapButt**, **CapProjecting**, or **CapRound**.

# DESCRIPTION

**Tk_GetCapStyle** places in *\*capPtr* the X cap style corresponding to
*string*. This will be one of the values **CapButt**, **CapProjecting**,
or **CapRound**. Cap styles are typically used in X graphics contexts to
indicate how the end-points of lines should be capped. See the X
documentation for information on what each style implies.

Under normal circumstances the return value is **TCL_OK** and *interp*
is unused. If *string* does not contain a valid cap style or an
abbreviation of one of these names, then an error message is stored in
interpreter *interp*\'s result, **TCL_ERROR** is returned, and
*\*capPtr* is unmodified.

**Tk_NameOfCapStyle** is the logical inverse of **Tk_GetCapStyle**.
Given a cap style such as **CapButt** it returns a statically-allocated
string corresponding to *cap*. If *cap* is not a legal cap style, then
is returned.

# KEYWORDS

butt, cap style, projecting, round

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

