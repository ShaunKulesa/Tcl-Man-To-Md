# NAME

Tk_CanvasTkwin, Tk_CanvasGetCoord, Tk_CanvasDrawableCoords,
Tk_CanvasSetStippleOrigin, Tk_CanvasWindowCoords,
Tk_CanvasEventuallyRedraw, Tk_CanvasTagsOption - utility procedures for
canvas type managers

# SYNOPSIS

**#include \<tk.h\>**

Tk_Window **Tk_CanvasTkwin**(*canvas*)

int **Tk_CanvasGetCoord**(*interp, canvas, string, doublePtr*)

**Tk_CanvasDrawableCoords**(*canvas, x, y, drawableXPtr, drawableYPtr*)

**Tk_CanvasSetStippleOrigin**(*canvas, gc*)

**Tk_CanvasWindowCoords**(*canvas, x, y, screenXPtr, screenYPtr*)

**Tk_CanvasEventuallyRedraw**(*canvas, x1, y1, x2, y2*)

Tk_OptionParseProc \***Tk_CanvasTagsParseProc**;

Tk_OptionPrintProc \***Tk_CanvasTagsPrintProc**;

# ARGUMENTS

A token that identifies a canvas widget.

Interpreter to use for error reporting.

Textual description of a canvas coordinate.

Points to place to store a converted coordinate.

An x coordinate in the space of the canvas.

A y coordinate in the space of the canvas.

Pointer to a location in which to store an x coordinate in the space of
the drawable currently being used to redisplay the canvas.

Pointer to a location in which to store a y coordinate in the space of
the drawable currently being used to redisplay the canvas.

Graphics context to modify.

Points to a location in which to store the screen coordinate in the
canvas window that corresponds to *x*.

Points to a location in which to store the screen coordinate in the
canvas window that corresponds to *y*.

Left edge of the region that needs redisplay. Only pixels at or to the
right of this coordinate need to be redisplayed.

Top edge of the region that needs redisplay. Only pixels at or below
this coordinate need to be redisplayed.

Right edge of the region that needs redisplay. Only pixels to the left
of this coordinate need to be redisplayed.

Bottom edge of the region that needs redisplay. Only pixels above this
coordinate need to be redisplayed.

# DESCRIPTION

These procedures are called by canvas type managers to perform various
utility functions.

**Tk_CanvasTkwin** returns the Tk_Window associated with a particular
canvas.

**Tk_CanvasGetCoord** translates a string specification of a coordinate
(such as **2p** or **1.6c**) into a double-precision canvas coordinate.
If *string* is a valid coordinate description then **Tk_CanvasGetCoord**
stores the corresponding canvas coordinate at \**doublePtr* and returns
**TCL_OK**. Otherwise it stores an error message in the interpreter
result and returns **TCL_ERROR**.

**Tk_CanvasDrawableCoords** is called by type managers during redisplay
to compute where to draw things. Given *x* and *y* coordinates in the
space of the canvas, **Tk_CanvasDrawableCoords** computes the
corresponding pixel in the drawable that is currently being used for
redisplay; it returns those coordinates in \**drawableXPtr* and
\**drawableYPtr*. This procedure should not be invoked except during
redisplay.

**Tk_CanvasSetStippleOrigin** is also used during redisplay. It sets the
stipple origin in *gc* so that stipples drawn with *gc* in the current
offscreen pixmap will line up with stipples drawn with origin (0,0) in
the canvas\'s actual window. **Tk_CanvasSetStippleOrigin** is needed in
order to guarantee that stipple patterns line up properly when the
canvas is redisplayed in small pieces. Redisplays are carried out in
double-buffered fashion where a piece of the canvas is redrawn in an
offscreen pixmap and then copied back onto the screen. In this approach
the stipple origins in graphics contexts need to be adjusted during each
redisplay to compensate for the position of the off-screen pixmap
relative to the window. If an item is being drawn with stipples, its
type manager typically calls **Tk_CanvasSetStippleOrigin** just before
using *gc* to draw something; after it is finished drawing, the type
manager calls **XSetTSOrigin** to restore the origin in *gc* back to
(0,0) (the restore is needed because graphics contexts are shared, so
they cannot be modified permanently).

**Tk_CanvasWindowCoords** is similar to **Tk_CanvasDrawableCoords**
except that it returns coordinates in the canvas\'s window on the
screen, instead of coordinates in an off-screen pixmap.

**Tk_CanvasEventuallyRedraw** may be invoked by a type manager to inform
Tk that a portion of a canvas needs to be redrawn. The *x1*, *y1*, *x2*,
and *y2* arguments specify the region that needs to be redrawn, in
canvas coordinates. Type managers rarely need to invoke
**Tk_CanvasEventuallyRedraw**, since Tk can normally figure out when an
item has changed and make the redisplay request on its behalf (this
happens, for example whenever Tk calls a *configureProc* or
*scaleProc*). The only time that a type manager needs to call
**Tk_CanvasEventuallyRedraw** is if an item has changed on its own
without being invoked through one of the procedures in its Tk_ItemType;
this could happen, for example, in an image item if the image is
modified using image commands.

**Tk_CanvasTagsParseProc** and **Tk_CanvasTagsPrintProc** are procedures
that handle the **-tags** option for canvas items. The code of a canvas
type manager will not call these procedures directly, but will use their
addresses to create a **Tk_CustomOption** structure for the **-tags**
option. The code typically looks like this:

    static const Tk_CustomOption tagsOption = {Tk_CanvasTagsParseProc,
        Tk_CanvasTagsPrintProc, NULL
    };

    static const Tk_ConfigSpec configSpecs[] = {
        ...
        {TK_CONFIG_CUSTOM, "-tags", NULL, NULL,
            NULL, 0, TK_CONFIG_NULL_OK, &tagsOption},
        ...
    };

# KEYWORDS

canvas, focus, item type, redisplay, selection, type manager
