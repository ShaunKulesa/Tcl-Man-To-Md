# NAME

Tk_AllocColorFromObj, Tk_GetColor, Tk_GetColorFromObj,
Tk_GetColorByValue, Tk_NameOfColor, Tk_FreeColorFromObj, Tk_FreeColor -
maintain database of colors

# SYNOPSIS

**#include \<tk.h\>**

XColor \* **Tk_AllocColorFromObj(***interp, tkwin, objPtr***)**

XColor \* **Tk_GetColor(***interp, tkwin, name***)**

XColor \* **Tk_GetColorFromObj(***tkwin, objPtr***)**

XColor \* **Tk_GetColorByValue(***tkwin, prefPtr***)**

const char \* **Tk_NameOfColor(***colorPtr***)**

GC **Tk_GCForColor(***colorPtr, drawable***)**

**Tk_FreeColorFromObj(***tkwin, objPtr***)**

**Tk_FreeColor(***colorPtr***)**

# ARGUMENTS

Interpreter to use for error reporting.

Token for window in which color will be used.

String value describes desired color; internal rep will be modified to
cache pointer to corresponding (XColor \*).

Same as *objPtr* except description of color is passed as a string and
resulting (XColor \*) is not cached.

Indicates red, green, and blue intensities of desired color.

Pointer to X color information. Must have been allocated by previous
call to **Tk_AllocColorFromObj**, **Tk_GetColor** or
**Tk_GetColorByValue**, except when passed to **Tk_NameOfColor**.

Drawable in which the result graphics context will be used. Must have
same screen and depth as the window for which the color was allocated.

# DESCRIPTION

These procedures manage the colors being used by a Tk application. They
allow colors to be shared whenever possible, so that colormap space is
preserved, and they pick closest available colors when colormap space is
exhausted.

Given a textual description of a color, **Tk_AllocColorFromObj** locates
a pixel value that may be used to render the color in a particular
window. The desired color is specified with a value whose string value
must have one of the following forms:

*colorname*

:   Any of the valid textual names for a color defined in the server\'s
    color database file, such as **red** or **PeachPuff**.

**\#***RGB*

:   

**\#***RRGGBB*

:   

**\#***RRRGGGBBB*

:   

**\#***RRRRGGGGBBBB*

:   A numeric specification of the red, green, and blue intensities to
    use to display the color. Each *R*, *G*, or *B* represents a single
    hexadecimal digit. The four forms permit colors to be specified with
    4-bit, 8-bit, 12-bit or 16-bit values. When fewer than 16 bits are
    provided for each color, they represent the most significant bits of
    the color, while the lower unfilled bits will be repeatedly
    replicated from the available higher bits. For example, #3a7 is the
    same as #3333aaaa7777.

**Tk_AllocColorFromObj** returns a pointer to an XColor structure; the
structure indicates the exact intensities of the allocated color (which
may differ slightly from those requested, depending on the limitations
of the screen) and a pixel value that may be used to draw with the color
in *tkwin*. If an error occurs in **Tk_AllocColorFromObj** (such as an
unknown color name) then NULL is returned and an error message is stored
in *interp*\'s result if *interp* is not NULL. If the colormap for
*tkwin* is full, **Tk_AllocColorFromObj** will use the closest existing
color in the colormap. **Tk_AllocColorFromObj** caches information about
the return value in *objPtr*, which speeds up future calls to procedures
such as **Tk_AllocColorFromObj** and **Tk_GetColorFromObj**.

**Tk_GetColor** is identical to **Tk_AllocColorFromObj** except that the
description of the color is specified with a string instead of a value.
This prevents **Tk_GetColor** from caching the return value, so
**Tk_GetColor** is less efficient than **Tk_AllocColorFromObj**.

**Tk_GetColorFromObj** returns the token for an existing color, given
the window and description used to create the color.
**Tk_GetColorFromObj** does not actually create the color; the color
must already have been created with a previous call to
**Tk_AllocColorFromObj** or **Tk_GetColor**. The return value is cached
in *objPtr*, which speeds up future calls to **Tk_GetColorFromObj** with
the same *objPtr* and *tkwin*.

**Tk_GetColorByValue** is similar to **Tk_GetColor** except that the
desired color is indicated with the *red*, *green*, and *blue* fields of
the structure pointed to by *colorPtr*.

This package maintains a database of all the colors currently in use. If
the same color is requested multiple times from **Tk_GetColor** or
**Tk_AllocColorFromObj** (e.g. by different windows), or if the same
intensities are requested multiple times from **Tk_GetColorByValue**,
then existing pixel values will be re-used. Re-using an existing pixel
avoids any interaction with the window server, which makes the
allocation much more efficient. These procedures also provide a portable
interface that works across all platforms. For this reason, you should
generally use **Tk_AllocColorFromObj**, **Tk_GetColor**, or
**Tk_GetColorByValue** instead of lower level procedures like
**XAllocColor**.

Since different calls to this package may return the same shared pixel
value, callers should never change the color of a pixel returned by the
procedures. If you need to change a color value dynamically, you should
use **XAllocColorCells** to allocate the pixel value for the color.

The procedure **Tk_NameOfColor** is roughly the inverse of
**Tk_GetColor**. If its *colorPtr* argument was created by
**Tk_AllocColorFromObj** or **Tk_GetColor** then the return value is the
string that was used to create the color. If *colorPtr* was created by a
call to **Tk_GetColorByValue**, or by any other mechanism, then the
return value is a string that could be passed to **Tk_GetColor** to
return the same color. Note: the string returned by **Tk_NameOfColor**
is only guaranteed to persist until the next call to **Tk_NameOfColor**.

**Tk_GCForColor** returns a graphics context whose **foreground** field
is the pixel allocated for *colorPtr* and whose other fields all have
default values. This provides an easy way to do basic drawing with a
color. The graphics context is cached with the color and will exist only
as long as *colorPtr* exists; it is freed when the last reference to
*colorPtr* is freed by calling **Tk_FreeColor**.

When a color is no longer needed **Tk_FreeColorFromObj** or
**Tk_FreeColor** should be called to release it. For
**Tk_FreeColorFromObj** the color to release is specified with the same
information used to create it; for **Tk_FreeColor** the color to release
is specified with a pointer to its XColor structure. There should be
exactly one call to **Tk_FreeColorFromObj** or **Tk_FreeColor** for each
call to **Tk_AllocColorFromObj**, **Tk_GetColor**, or
**Tk_GetColorByValue**.

# KEYWORDS

color, intensity, value, pixel value

<!---
Copyright (c) 1990-1991 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

