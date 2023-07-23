# NAME

Tk_MeasureChars, Tk_TextWidth, Tk_DrawChars, Tk_UnderlineChars -
routines to measure and display simple single-line strings.

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_MeasureChars(***tkfont, string, numBytes, maxPixels, flags,
lengthPtr***)**

int **Tk_TextWidth(***tkfont, string, numBytes***)**

**Tk_DrawChars(***display, drawable, gc, tkfont, string, numBytes, x,
y***)**

**Tk_UnderlineChars(***display, drawable, gc, tkfont, string, x, y,
firstByte, lastByte***)**

# ARGUMENTS

Token for font in which text is to be drawn or measured. Must have been
returned by a previous call to **Tk_GetFont**.

Text to be measured or displayed. Need not be null terminated. Any
non-printing meta-characters in the string (such as tabs, newlines, and
other control characters) will be measured or displayed in a
platform-dependent manner.

The maximum number of bytes to consider when measuring or drawing
*string*. Must be greater than or equal to 0.

If *maxPixels* is \>= 0, it specifies the longest permissible line
length in pixels. Characters from *string* are processed only until this
many pixels have been covered. If *maxPixels* is \< 0, then the line
length is unbounded and the *flags* argument is ignored.

Various flag bits OR-ed together: **TK_PARTIAL_OK** means include a
character as long as any part of it fits in the length given by
*maxPixels*; otherwise, a character must fit completely to be
considered. **TK_WHOLE_WORDS** means stop on a word boundary, if
possible. If **TK_AT_LEAST_ONE** is set, it means return at least one
character even if no characters could fit in the length given by
*maxPixels*. If **TK_AT_LEAST_ONE** is set and **TK_WHOLE_WORDS** is
also set, it means that if not even one word fits on the line, return
the first few letters of the word that did fit; if not even one letter
of the word fit, then the first letter will still be returned.

Filled with the number of pixels occupied by the number of characters
returned as the result of **Tk_MeasureChars**.

Display on which to draw.

Window or pixmap in which to draw.

Graphics context for drawing characters. The font selected into this GC
must be the same as the *tkfont*.

Coordinates at which to place the left edge of the baseline when
displaying *string*.

The index of the first byte of the first character to underline in the
*string*. Underlining begins at the left edge of this character.

The index of the first byte of the last character up to which the
underline will be drawn. The character specified by *lastByte* will not
itself be underlined.

# DESCRIPTION

These routines are for measuring and displaying simple single-font,
single-line strings. To measure and display single-font, multi-line,
justified text, refer to the documentation for **Tk_ComputeTextLayout**.
There is no programming interface in the core of Tk that supports
multi-font, multi-line text; support for that behavior must be built on
top of simpler layers. Note that the interfaces described here are
byte-oriented not character-oriented, so index values coming from Tcl
scripts need to be converted to byte offsets using the
**Tcl_UtfAtIndex** and related routines.

A glyph is the displayable picture of a letter, number, or some other
symbol. Not all character codes in a given font have a glyph. Characters
such as tabs, newlines/returns, and control characters that have no
glyph are measured and displayed by these procedures in a
platform-dependent manner; under X, they are replaced with backslashed
escape sequences, while under Windows and Macintosh hollow or solid
boxes may be substituted. Refer to the documentation for
**Tk_ComputeTextLayout** for a programming interface that supports the
platform-independent expansion of tab characters into columns and
newlines/returns into multi-line text.

**Tk_MeasureChars** is used both to compute the length of a given string
and to compute how many characters from a string fit in a given amount
of space. The return value is the number of bytes from *string* that fit
in the space specified by *maxPixels* subject to the conditions
described by *flags*. If all characters fit, the return value will be
*numBytes*. *\*lengthPtr* is filled with the computed width, in pixels,
of the portion of the string that was measured. For example, if the
return value is 5, then *\*lengthPtr* is filled with the distance
between the left edge of *string*\[0\] and the right edge of
*string*\[4\].

**Tk_TextWidth** is a wrapper function that provides a simpler interface
to the **Tk_MeasureChars** function. The return value is how much space
in pixels the given *string* needs.

**Tk_DrawChars** draws the *string* at the given location in the given
*drawable*.

**Tk_UnderlineChars** underlines the given range of characters in the
given *string*. It does not draw the characters (which are assumed to
have been displayed previously by **Tk_DrawChars**); it just draws the
underline. This procedure is used to underline a few characters without
having to construct an underlined font. To produce natively underlined
text, the appropriate underlined font should be constructed and used.

# SEE ALSO

font(n), FontId(3)

# KEYWORDS

font, measurement

<!---
Copyright (c) 1996 Sun Microsystems, Inc
-->

