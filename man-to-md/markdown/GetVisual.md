# NAME

Tk_GetVisual - translate from string to visual

# SYNOPSIS

**#include \<tk.h\>**

Visual \* **Tk_GetVisual(***interp, tkwin, string, depthPtr,
colormapPtr***)**

# ARGUMENTS

Interpreter to use for error reporting.

Token for window in which the visual will be used.

String that identifies the desired visual. See below for valid formats.

Depth of returned visual gets stored here.

If non-NULL then a suitable colormap for visual is found and its
identifier is stored here.

# DESCRIPTION

**Tk_GetVisual** takes a string description of a visual and finds a
suitable X Visual for use in *tkwin*, if there is one. It returns a
pointer to the X Visual structure for the visual and stores the number
of bits per pixel for it at *\*depthPtr*. If *string* is unrecognizable
or if no suitable visual could be found, then NULL is returned and
**Tk_GetVisual** leaves an error message in interpreter *interp*\'s
result. If *colormap* is non-NULL then **Tk_GetVisual** also locates an
appropriate colormap for use with the result visual and stores its X
identifier at *\*colormapPtr*.

The *string* argument specifies the desired visual in one of the
following ways:

*class depth*

:   The string consists of a class name followed by an integer depth,
    with any amount of white space (including none) in between. *class*
    selects what sort of visual is desired and must be one of
    **directcolor**, **grayscale**, **greyscale**, **pseudocolor**,
    **staticcolor**, **staticgray**, **staticgrey**, or **truecolor**,
    or a unique abbreviation. *depth* specifies how many bits per pixel
    are needed for the visual. If possible, **Tk_GetVisual** will return
    a visual with this depth; if there is no visual of the desired depth
    then **Tk_GetVisual** looks first for a visual with greater depth,
    then one with less depth.

**default**

:   Use the default visual for *tkwin*\'s screen.

*pathName*

:   Use the visual for the window given by *pathName*. *pathName* must
    be the name of a window on the same screen as *tkwin*.

*number*

:   Use the visual whose X identifier is *number*.

**best** ?*depth*?

:   Choose the visual, using the following rules, in decreasing order of
    priority:

    (a) a visual that has exactly the desired depth is best, followed by
        a visual with greater depth than requested (but as little extra
        as possible), followed by a visual with less depth than
        requested (but as great a depth as possible);

    (b) if no *depth* is specified, then the deepest available visual is
        chosen;

    (c) **pseudocolor** is better than **truecolor** or **directcolor**,
        which are better than **staticcolor**, which is better than
        **staticgray** or **grayscale**;

    (d) the default visual for the screen is better than any other
        visual.

# CREDITS

The idea for **Tk_GetVisual**, and the first implementation, came from
Paul Mackerras.

# KEYWORDS

colormap, screen, visual

<!---
Copyright (c) 1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

