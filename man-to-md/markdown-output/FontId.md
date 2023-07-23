# NAME

Tk_FontId, Tk_GetFontMetrics, Tk_PostscriptFontName - accessor functions
for fonts

# SYNOPSIS

**#include \<tk.h\>**

Font **Tk_FontId(***tkfont***)**

**Tk_GetFontMetrics(***tkfont, fmPtr***)**

int **Tk_PostscriptFontName(***tkfont, dsPtr***)**

# ARGUMENTS

Opaque font token being queried. Must have been returned by a previous
call to **Tk_GetFont**.

Pointer to structure in which the font metrics for *tkfont* will be
stored. See **DATA STRUCTURES** below for details.

Pointer to an initialized **Tcl_DString** to which the name of the
Postscript font that corresponds to *tkfont* will be appended.

# DESCRIPTION

Given a *tkfont*, **Tk_FontId** returns the token that should be
selected into an XGCValues structure in order to construct a graphics
context that can be used to draw text in the specified font.

**Tk_GetFontMetrics** computes the ascent, descent, and linespace of the
*tkfont* in pixels and stores those values in the structure pointer to
by *fmPtr*. These values can be used in computations such as to space
multiple lines of text, to align the baselines of text in different
fonts, and to vertically align text in a given region. See the
documentation for the **font** command for definitions of the terms
ascent, descent, and linespace, used in font metrics.

**Tk_PostscriptFontName** maps a *tkfont* to the corresponding
Postscript font name that should be used when printing. The return value
is the size in points of the *tkfont* and the Postscript font name is
appended to *dsPtr*. *DsPtr* must refer to an initialized
**Tcl_DString**. Given a Postscript printer, the following screen font
families should print correctly:

> **Avant Garde**, **Arial**, **Bookman**, **Courier**, **Courier New**,
> **Geneva**, **Helvetica**, **Monaco**, **New Century Schoolbook**,
> **New York**, **Palatino**, **Symbol**, **Times**, **Times New
> Roman**, **Zapf Chancery**, and **Zapf Dingbats**.

Any other font families may not print correctly because the computed
Postscript font name may be incorrect or not exist on the printer.

# DATA STRUCTURES

The **Tk_FontMetrics** data structure is used by **Tk_GetFontMetrics**
to return information about a font and is defined as follows:

    typedef struct Tk_FontMetrics {
        int ascent;
        int descent;
        int linespace;
    } Tk_FontMetrics;

The *ascent* field is the amount in pixels that the tallest letter
sticks up above the baseline, plus any extra blank space added by the
designer of the font.

The *descent* is the largest amount in pixels that any letter sticks
below the baseline, plus any extra blank space added by the designer of
the font.

The *linespace* is the sum of the ascent and descent. How far apart two
lines of text in the same font should be placed so that none of the
characters in one line overlap any of the characters in the other line.

# SEE ALSO

font(n), MeasureChar(3)

# KEYWORDS

font, measurement, Postscript

<!---
Copyright (c) 1996 Sun Microsystems, Inc
-->

