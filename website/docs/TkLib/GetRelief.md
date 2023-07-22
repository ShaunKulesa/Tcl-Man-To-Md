# NAME

Tk_GetReliefFromObj, Tk_GetRelief, Tk_NameOfRelief - translate between
strings and relief values

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetReliefFromObj(***interp, objPtr, reliefPtr***)**

int **Tk_GetRelief(***interp, name, reliefPtr***)**

const char \* **Tk_NameOfRelief(***relief***)**

# ARGUMENTS

Interpreter to use for error reporting.

String value contains name of relief, one of or (or any unique
abbreviation thereof on input); the internal rep will be modified to
cache corresponding relief value.

Same as *objPtr* except description of relief is passed as a string.

Pointer to location in which to store relief value corresponding to
*objPtr* or *name*.

Name of the relief.

Relief value (one of **TK_RELIEF_FLAT**, **TK_RELIEF_RAISED**,
**TK_RELIEF_SUNKEN**, **TK_RELIEF_GROOVE**, **TK_RELIEF_SOLID**, or
**TK_RELIEF_RIDGE**).

# DESCRIPTION

**Tk_GetReliefFromObj** places in *\*reliefPtr* the relief value
corresponding to the value of *objPtr*. This value will be one of
**TK_RELIEF_FLAT**, **TK_RELIEF_RAISED**, **TK_RELIEF_SUNKEN**,
**TK_RELIEF_GROOVE**, **TK_RELIEF_SOLID**, or **TK_RELIEF_RIDGE**. Under
normal circumstances the return value is **TCL_OK** and *interp* is
unused. If *objPtr* does not contain one of the valid relief names or an
abbreviation of one of them, then **TCL_ERROR** is returned,
*\*reliefPtr* is unmodified, and an error message is stored in
*interp*\'s result if *interp* is not NULL. **Tk_GetReliefFromObj**
caches information about the return value in *objPtr*, which speeds up
future calls to **Tk_GetReliefFromObj** with the same *objPtr*.

**Tk_GetRelief** is identical to **Tk_GetReliefFromObj** except that the
description of the relief is specified with a string instead of an
object. This prevents **Tk_GetRelief** from caching the return value, so
**Tk_GetRelief** is less efficient than **Tk_GetReliefFromObj**.

**Tk_NameOfRelief** is the logical inverse of **Tk_GetRelief**. Given a
relief value it returns the corresponding string (**flat**, **raised**,
**sunken**, **groove**, **solid**, or **ridge**). If *relief* is not a
legal relief value, then is returned.

# KEYWORDS

name, relief, string
