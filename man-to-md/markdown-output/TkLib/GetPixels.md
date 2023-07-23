# NAME

Tk_GetPixelsFromObj, Tk_GetPixels, Tk_GetMMFromObj, Tk_GetScreenMM -
translate between strings and screen units

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetPixelsFromObj(***interp, tkwin, objPtr, intPtr***)**

int **Tk_GetPixels(***interp, tkwin, string, intPtr***)**

int **Tk_GetMMFromObj(***interp, tkwin, objPtr, doublePtr***)**

int **Tk_GetScreenMM(***interp, tkwin, string, doublePtr***)**

# ARGUMENTS

Interpreter to use for error reporting.

Window whose screen geometry determines the conversion between absolute
units and pixels.

String value specifies a distance on the screen; internal rep will be
modified to cache converted distance.

Same as *objPtr* except specification of distance is passed as a string.

Pointer to location in which to store converted distance in pixels.

Pointer to location in which to store converted distance in millimeters.

# DESCRIPTION

These procedures take as argument a specification of distance on the
screen (*objPtr* or *string*) and compute the corresponding distance
either in integer pixels or floating-point millimeters. In either case,
*objPtr* or *string* specifies a screen distance as a floating-point
number followed by one of the following characters that indicates units:

\<none\>

:   The number specifies a distance in pixels.

**c**

:   The number specifies a distance in centimeters on the screen.

**i**

:   The number specifies a distance in inches on the screen.

**m**

:   The number specifies a distance in millimeters on the screen.

**p**

:   The number specifies a distance in printer\'s points (1/72 inch) on
    the screen.

**Tk_GetPixelsFromObj** converts the value of *objPtr* to the nearest
even number of pixels and stores that value at *\*intPtr*. It returns
**TCL_OK** under normal circumstances. If an error occurs (e.g. *objPtr*
contains a number followed by a character that is not one of the ones
above) then **TCL_ERROR** is returned and an error message is left in
*interp*\'s result if *interp* is not NULL. **Tk_GetPixelsFromObj**
caches information about the return value in *objPtr*, which speeds up
future calls to **Tk_GetPixelsFromObj** with the same *objPtr*.

**Tk_GetPixels** is identical to **Tk_GetPixelsFromObj** except that the
screen distance is specified with a string instead of an object. This
prevents **Tk_GetPixels** from caching the return value, so
**Tk_GetPixels** is less efficient than **Tk_GetPixelsFromObj**.

**Tk_GetMMFromObj** and **Tk_GetScreenMM** are similar to
**Tk_GetPixelsFromObj** and **Tk_GetPixels** (respectively) except that
they convert the screen distance to millimeters and store a
double-precision floating-point result at *\*doublePtr*.

# KEYWORDS

centimeters, convert, inches, millimeters, pixels, points, screen units

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

