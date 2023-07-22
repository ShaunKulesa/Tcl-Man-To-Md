# NAME

Tk_AllocFontFromObj, Tk_GetFont, Tk_GetFontFromObj, Tk_NameOfFont,
Tk_FreeFontFromObj, Tk_FreeFont - maintain database of fonts

# SYNOPSIS

**#include \<tk.h\>**

Tk_Font **Tk_AllocFontFromObj(***interp, tkwin, objPtr***)**

Tk_Font **Tk_GetFont(***interp, tkwin, string***)**

Tk_Font **Tk_GetFontFromObj(***tkwin, objPtr***)**

const char \* **Tk_NameOfFont(***tkfont***)**

Tk_Font **Tk_FreeFontFromObj(***tkwin, objPtr***)**

void **Tk_FreeFont(***tkfont***)**

# ARGUMENTS

Interpreter to use for error reporting. If **NULL**, then no error
messages are left after errors.

Token for window in which font will be used.

Gives name or description of font. See documentation for the **font**
command for details on acceptable formats. Internal rep will be modified
to cache corresponding Tk_Font.

Same as *objPtr* except description of font is passed as a string and
resulting Tk_Font is not cached.

Opaque font token.

# DESCRIPTION

**Tk_AllocFontFromObj** finds the font indicated by *objPtr* and returns
a token that represents the font. The return value can be used in
subsequent calls to procedures such as **Tk_GetFontMetrics**,
**Tk_MeasureChars**, and **Tk_FreeFont**. The Tk_Font token will remain
valid until **Tk_FreeFontFromObj** or **Tk_FreeFont** is called to
release it. *ObjPtr* can contain either a symbolic name or a font
description; see the documentation for the **font** command for a
description of the valid formats. If **Tk_AllocFontFromObj** is
unsuccessful (because, for example, *objPtr* did not contain a valid
font specification) then it returns **NULL** and leaves an error message
in *interp*\'s result if *interp* is not **NULL**.
**Tk_AllocFontFromObj** caches information about the return value in
*objPtr*, which speeds up future calls to procedures such as
**Tk_AllocFontFromObj** and **Tk_GetFontFromObj**.

**Tk_GetFont** is identical to **Tk_AllocFontFromObj** except that the
description of the font is specified with a string instead of an object.
This prevents **Tk_GetFont** from caching the matching Tk_Font, so
**Tk_GetFont** is less efficient than **Tk_AllocFontFromObj**.

**Tk_GetFontFromObj** returns the token for an existing font, given the
window and description used to create the font. **Tk_GetFontFromObj**
does not actually create the font; the font must already have been
created with a previous call to **Tk_AllocFontFromObj** or
**Tk_GetFont**. The return value is cached in *objPtr*, which speeds up
future calls to **Tk_GetFontFromObj** with the same *objPtr* and
*tkwin*.

**Tk_AllocFontFromObj** and **Tk_GetFont** maintain a database of all
fonts they have allocated. If the same font is requested multiple times
(e.g. by different windows or for different purposes), then a single
Tk_Font will be shared for all uses. The underlying resources will be
freed automatically when no-one is using the font anymore.

The procedure **Tk_NameOfFont** is roughly the inverse of
**Tk_GetFont**. Given a *tkfont* that was created by **Tk_GetFont** (or
**Tk_AllocFontFromObj**), the return value is the *string* argument that
was passed to **Tk_GetFont** to create the font. The string returned by
**Tk_NameOfFont** is only guaranteed to persist until the *tkfont* is
deleted. The caller must not modify this string.

When a font is no longer needed, **Tk_FreeFontFromObj** or
**Tk_FreeFont** should be called to release it. For
**Tk_FreeFontFromObj** the font to release is specified with the same
information used to create it; for **Tk_FreeFont** the font to release
is specified with its Tk_Font token. There should be exactly one call to
**Tk_FreeFontFromObj** or **Tk_FreeFont** for each call to
**Tk_AllocFontFromObj** or **Tk_GetFont**.

# SEE ALSO

Tk_FontId(3)

# KEYWORDS

font
