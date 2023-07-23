# NAME

Tk_AllocBitmapFromObj, Tk_GetBitmap, Tk_GetBitmapFromObj,
Tk_DefineBitmap, Tk_NameOfBitmap, Tk_SizeOfBitmap, Tk_FreeBitmapFromObj,
Tk_FreeBitmap - maintain database of single-plane pixmaps

# SYNOPSIS

**#include \<tk.h\>**

Pixmap **Tk_AllocBitmapFromObj(***interp, tkwin, objPtr***)**

Pixmap **Tk_GetBitmap(***interp, tkwin, info***)**

Pixmap **Tk_GetBitmapFromObj(***tkwin, objPtr***)**

int **Tk_DefineBitmap(***interp, name, source, width, height***)**

const char \* **Tk_NameOfBitmap(***display, bitmap***)**

**Tk_SizeOfBitmap(***display, bitmap, widthPtr, heightPtr***)**

**Tk_FreeBitmapFromObj(***tkwin, objPtr***)**

**Tk_FreeBitmap(***display, bitmap***)**

# ARGUMENTS

Interpreter to use for error reporting; if NULL then no error message is
left after errors.

Token for window in which the bitmap will be used.

String value describes desired bitmap; internal rep will be modified to
cache pointer to corresponding Pixmap.

Same as *objPtr* except description of bitmap is passed as a string and
resulting Pixmap is not cached.

Name for new bitmap to be defined.

Data for bitmap, in standard bitmap format. Must be stored in static
memory whose value will never change.

Width of bitmap.

Height of bitmap.

Pointer to word to fill in with *bitmap*\'s width.

Pointer to word to fill in with *bitmap*\'s height.

Display for which *bitmap* was allocated.

Identifier for a bitmap allocated by **Tk_AllocBitmapFromObj** or
**Tk_GetBitmap**.

# DESCRIPTION

These procedures manage a collection of bitmaps (one-plane pixmaps)
being used by an application. The procedures allow bitmaps to be re-used
efficiently, thereby avoiding server overhead, and also allow bitmaps to
be named with character strings.

**Tk_AllocBitmapFromObj** returns a Pixmap identifier for a bitmap that
matches the description in *objPtr* and is suitable for use in *tkwin*.
It re-uses an existing bitmap, if possible, and creates a new one
otherwise. *ObjPtr*\'s value must have one of the following forms:

**@***fileName*

:   *FileName* must be the name of a file containing a bitmap
    description in the standard X11 format.

*name*

:   *Name* must be the name of a bitmap defined previously with a call
    to **Tk_DefineBitmap**. The following names are pre-defined by Tk:

    **error**

    :   The international symbol: a circle with a diagonal line across
        it.

    **gray75**

    :   75% gray: a checkerboard pattern where three out of four bits
        are on.

    **gray50**

    :   50% gray: a checkerboard pattern where every other bit is on.

    **gray25**

    :   25% gray: a checkerboard pattern where one out of every four
        bits is on.

    **gray12**

    :   12.5% gray: a pattern where one-eighth of the bits are on,
        consisting of every fourth pixel in every other row.

    **hourglass**

    :   An hourglass symbol.

    **info**

    :   A large letter

    **questhead**

    :   The silhouette of a human head, with a question mark in it.

    **question**

    :   A large question-mark.

    **warning**

    :   A large exclamation point.

    In addition, the following pre-defined names are available only on
    the **Macintosh** platform:

    **document**

    :   A generic document.

    **stationery**

    :   Document stationery.

    **edition**

    :   The *edition* symbol.

    **application**

    :   Generic application icon.

    **accessory**

    :   A desk accessory.

    **folder**

    :   Generic folder icon.

    **pfolder**

    :   A locked folder.

    **trash**

    :   A trash can.

    **floppy**

    :   A floppy disk.

    **ramdisk**

    :   A floppy disk with chip.

    **cdrom**

    :   A cd disk icon.

    **preferences**

    :   A folder with prefs symbol.

    **querydoc**

    :   A database document icon.

    **stop**

    :   A stop sign.

    **note**

    :   A face with balloon words.

    **caution**

    :   A triangle with an exclamation point.

Under normal conditions, **Tk_AllocBitmapFromObj** returns an identifier
for the requested bitmap. If an error occurs in creating the bitmap,
such as when *objPtr* refers to a non-existent file, then **None** is
returned and an error message is left in *interp*\'s result if *interp*
is not NULL. **Tk_AllocBitmapFromObj** caches information about the
return value in *objPtr*, which speeds up future calls to procedures
such as **Tk_AllocBitmapFromObj** and **Tk_GetBitmapFromObj**.

**Tk_GetBitmap** is identical to **Tk_AllocBitmapFromObj** except that
the description of the bitmap is specified with a string instead of an
object. This prevents **Tk_GetBitmap** from caching the return value, so
**Tk_GetBitmap** is less efficient than **Tk_AllocBitmapFromObj**.

**Tk_GetBitmapFromObj** returns the token for an existing bitmap, given
the window and description used to create the bitmap.
**Tk_GetBitmapFromObj** does not actually create the bitmap; the bitmap
must already have been created with a previous call to
**Tk_AllocBitmapFromObj** or **Tk_GetBitmap**. The return value is
cached in *objPtr*, which speeds up future calls to
**Tk_GetBitmapFromObj** with the same *objPtr* and *tkwin*.

**Tk_DefineBitmap** associates a name with in-memory bitmap data so that
the name can be used in later calls to **Tk_AllocBitmapFromObj** or
**Tk_GetBitmap**. The *nameId* argument gives a name for the bitmap; it
must not previously have been used in a call to **Tk_DefineBitmap**. The
arguments *source*, *width*, and *height* describe the bitmap.
**Tk_DefineBitmap** normally returns **TCL_OK**; if an error occurs
(e.g. a bitmap named *nameId* has already been defined) then
**TCL_ERROR** is returned and an error message is left in interpreter
*interp*\'s result. Note: **Tk_DefineBitmap** expects the memory pointed
to by *source* to be static: **Tk_DefineBitmap** does not make a private
copy of this memory, but uses the bytes pointed to by *source* later in
calls to **Tk_AllocBitmapFromObj** or **Tk_GetBitmap**.

Typically **Tk_DefineBitmap** is used by **#include**-ing a bitmap file
directly into a C program and then referencing the variables defined by
the file. For example, suppose there exists a file **stip.bitmap**,
which was created by the **bitmap** program and contains a stipple
pattern. The following code uses **Tk_DefineBitmap** to define a new
bitmap named **foo**:

    Pixmap bitmap;
    #include "stip.bitmap"
    Tk_DefineBitmap(interp, "foo", stip_bits,
        stip_width, stip_height);
    ...
    bitmap = Tk_GetBitmap(interp, tkwin, "foo");

This code causes the bitmap file to be read at compile-time and
incorporates the bitmap information into the program\'s executable
image. The same bitmap file could be read at run-time using
**Tk_GetBitmap**:

    Pixmap bitmap;
    bitmap = Tk_GetBitmap(interp, tkwin, "@stip.bitmap");

The second form is a bit more flexible (the file could be modified after
the program has been compiled, or a different string could be provided
to read a different file), but it is a little slower and requires the
bitmap file to exist separately from the program.

Tk maintains a database of all the bitmaps that are currently in use.
Whenever possible, it will return an existing bitmap rather than
creating a new one. When a bitmap is no longer used, Tk will release it
automatically. This approach can substantially reduce server overhead,
so **Tk_AllocBitmapFromObj** and **Tk_GetBitmap** should generally be
used in preference to Xlib procedures like **XReadBitmapFile**.

The bitmaps returned by **Tk_AllocBitmapFromObj** and **Tk_GetBitmap**
are shared, so callers should never modify them. If a bitmap must be
modified dynamically, then it should be created by calling Xlib
procedures such as **XReadBitmapFile** or **XCreatePixmap** directly.

The procedure **Tk_NameOfBitmap** is roughly the inverse of
**Tk_GetBitmap**. Given an X Pixmap argument, it returns the textual
description that was passed to **Tk_GetBitmap** when the bitmap was
created. *Bitmap* must have been the return value from a previous call
to **Tk_AllocBitmapFromObj** or **Tk_GetBitmap**.

**Tk_SizeOfBitmap** returns the dimensions of its *bitmap* argument in
the words pointed to by the *widthPtr* and *heightPtr* arguments. As
with **Tk_NameOfBitmap**, *bitmap* must have been created by
**Tk_AllocBitmapFromObj** or **Tk_GetBitmap**.

When a bitmap is no longer needed, **Tk_FreeBitmapFromObj** or
**Tk_FreeBitmap** should be called to release it. For
**Tk_FreeBitmapFromObj** the bitmap to release is specified with the
same information used to create it; for **Tk_FreeBitmap** the bitmap to
release is specified with its Pixmap token. There should be exactly one
call to **Tk_FreeBitmapFromObj** or **Tk_FreeBitmap** for each call to
**Tk_AllocBitmapFromObj** or **Tk_GetBitmap**.

# BUGS

In determining whether an existing bitmap can be used to satisfy a new
request, **Tk_AllocBitmapFromObj** and **Tk_GetBitmap** consider only
the immediate value of the string description. For example, when a file
name is passed to **Tk_GetBitmap**, **Tk_GetBitmap** will assume it is
safe to re-use an existing bitmap created from the same file name: it
will not check to see whether the file itself has changed, or whether
the current directory has changed, thereby causing the name to refer to
a different file.

# KEYWORDS

bitmap, pixmap

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

