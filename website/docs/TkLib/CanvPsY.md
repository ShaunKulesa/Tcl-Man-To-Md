# NAME

Tk_CanvasPsY, Tk_CanvasPsBitmap, Tk_CanvasPsColor, Tk_CanvasPsFont,
Tk_CanvasPsPath, Tk_CanvasPsStipple - utility procedures for generating
Postscript for canvases

# SYNOPSIS

**#include \<tk.h\>**

double **Tk_CanvasPsY**(*canvas, canvasY*)

int **Tk_CanvasPsBitmap**(*interp, canvas, bitmap, x, y, width, height*)

int **Tk_CanvasPsColor**(*interp, canvas, colorPtr*)

int **Tk_CanvasPsFont**(*interp, canvas, tkFont*)

**Tk_CanvasPsPath**(*interp, canvas, coordPtr, numPoints*)

int **Tk_CanvasPsStipple**(*interp, canvas, bitmap*)

# ARGUMENTS

A token that identifies a canvas widget for which Postscript is being
generated.

Y-coordinate in the space of the canvas.

A Tcl interpreter; Postscript is appended to its result, or the result
may be replaced with an error message.

Bitmap to use for generating Postscript.

X-coordinate within *bitmap* of left edge of region to output.

Y-coordinate within *bitmap* of top edge of region to output.

Width of region of bitmap to output, in pixels.

Height of region of bitmap to output, in pixels.

Information about color value to set in Postscript.

Font for which Postscript is to be generated.

Pointer to an array of coordinates for one or more points specified in
canvas coordinates. The order of values in *coordPtr* is x1, y1, x2, y2,
x3, y3, and so on.

Number of points at *coordPtr*.

# DESCRIPTION

These procedures are called by canvas type managers to carry out common
functions related to generating Postscript. Most of the procedures take
a *canvas* argument, which refers to a canvas widget for which
Postscript is being generated.

**Tk_CanvasPsY** takes as argument a y-coordinate in the space of a
canvas and returns the value that should be used for that point in the
Postscript currently being generated for *canvas*. Y coordinates require
transformation because Postscript uses an origin at the lower-left
corner whereas X uses an origin at the upper-left corner. Canvas x
coordinates can be used directly in Postscript without transformation.

**Tk_CanvasPsBitmap** generates Postscript to describe a region of a
bitmap. The Postscript is generated in proper image data format for
Postscript, i.e., as data between angle brackets, one bit per pixel. The
Postscript is appended to the result of interpreter *interp* and
**TCL_OK** is returned unless an error occurs, in which case
**TCL_ERROR** is returned and the interpreter result is overwritten with
an error message.

**Tk_CanvasPsColor** generates Postscript to set the current color to
correspond to its *colorPtr* argument, taking into account any color map
specified in the **postscript** command. It appends the Postscript to
the interpreter *interp*\'s result and returns **TCL_OK** unless an
error occurs, in which case **TCL_ERROR** is returned and the
interpreter\'s result is overwritten with an error message.

**Tk_CanvasPsFont** generates Postscript that sets the current font to
match *tkFont* as closely as possible. **Tk_CanvasPsFont** takes into
account any font map specified in the **postscript** command, and it
does the best it can at mapping X fonts to Postscript fonts. It appends
the Postscript to interpreter *interp*\'s result and returns **TCL_OK**
unless an error occurs, in which case **TCL_ERROR** is returned and the
interpreter\'s result is overwritten with an error message.

**Tk_CanvasPsPath** generates Postscript to set the current path to the
set of points given by *coordPtr* and *numPoints*. It appends the
resulting Postscript to the result of interpreter *interp*.

**Tk_CanvasPsStipple** generates Postscript that will fill the current
path in stippled fashion. It uses *bitmap* as the stipple pattern and
the current Postscript color; ones in the stipple bitmap are drawn in
the current color, and zeroes are not drawn at all. The Postscript is
appended to interpreter *interp*\'s result and **TCL_OK** is returned,
unless an error occurs, in which case **TCL_ERROR** is returned and the
interpreter\'s result is overwritten with an error message.

# KEYWORDS

bitmap, canvas, color, font, path, Postscript, stipple
