# NAME

Tk_Alloc3DBorderFromObj, Tk_Get3DBorder, Tk_Get3DBorderFromObj,
Tk_Draw3DRectangle, Tk_Fill3DRectangle, Tk_Draw3DPolygon,
Tk_Fill3DPolygon, Tk_3DVerticalBevel, Tk_3DHorizontalBevel,
Tk_SetBackgroundFromBorder, Tk_NameOf3DBorder, Tk_3DBorderColor,
Tk_3DBorderGC, Tk_Free3DBorderFromObj, Tk_Free3DBorder - draw borders
with three-dimensional appearance

# SYNOPSIS

**#include \<tk.h\>**

Tk_3DBorder **Tk_Alloc3DBorderFromObj(***interp, tkwin, objPtr***)**

Tk_3DBorder **Tk_Get3DBorder(***interp, tkwin, colorName***)**

Tk_3DBorder **Tk_Get3DBorderFromObj(***tkwin, objPtr***)**

void **Tk_Draw3DRectangle(***tkwin, drawable, border, x, y, width,
height, borderWidth, relief***)**

void **Tk_Fill3DRectangle(***tkwin, drawable, border, x, y, width,
height, borderWidth, relief***)**

void **Tk_Draw3DPolygon(***tkwin, drawable, border, pointPtr, numPoints,
polyBorderWidth, leftRelief***)**

void **Tk_Fill3DPolygon(***tkwin, drawable, border, pointPtr, numPoints,
polyBorderWidth, leftRelief***)**

void **Tk_3DVerticalBevel**(*tkwin, drawable, border, x, y, width,
height, leftBevel, relief***)**

void **Tk_3DHorizontalBevel**(*tkwin, drawable, border, x, y, width,
height, leftIn, rightIn, topBevel, relief***)**

void **Tk_SetBackgroundFromBorder(***tkwin, border***)**

const char \* **Tk_NameOf3DBorder(***border***)**

XColor \* **Tk_3DBorderColor(***border***)**

GC \* **Tk_3DBorderGC(***tkwin, border, which***)**

**Tk_Free3DBorderFromObj(***tkwin, objPtr***)**

**Tk_Free3DBorder(***border***)**

# ARGUMENTS

Interpreter to use for error reporting.

Token for window (for all procedures except **Tk_Get3DBorder**, must be
the window for which the border was allocated).

Pointer to value whose value describes color corresponding to background
(flat areas). Illuminated edges will be brighter than this and shadowed
edges will be darker than this.

Same as *objPtr* except value is supplied as a string rather than a
value.

X token for window or pixmap; indicates where graphics are to be drawn.
Must either be the X window for *tkwin* or a pixmap with the same screen
and depth as *tkwin*.

Token for border previously allocated in call to **Tk_Get3DBorder**.

X-coordinate of upper-left corner of rectangle describing border or
bevel, in pixels.

Y-coordinate of upper-left corner of rectangle describing border or
bevel, in pixels.

Width of rectangle describing border or bevel, in pixels.

Height of rectangle describing border or bevel, in pixels.

Width of border in pixels. Positive means border is inside rectangle
given by *x*, *y*, *width*, *height*, negative means border is outside
rectangle.

Indicates 3-D position of interior of value relative to exterior; should
be **TK_RELIEF_RAISED**, **TK_RELIEF_SUNKEN**, **TK_RELIEF_GROOVE**,
**TK_RELIEF_SOLID**, or **TK_RELIEF_RIDGE** (may also be
**TK_RELIEF_FLAT** for **Tk_Fill3DRectangle**).

Pointer to array of points describing the set of vertices in a polygon.
The polygon need not be closed (it will be closed automatically if it is
not).

Number of points at *\*pointPtr*.

Width of border in pixels. If positive, border is drawn to left of
trajectory given by *pointPtr*; if negative, border is drawn to right of
trajectory. If *leftRelief* is **TK_RELIEF_GROOVE** or
**TK_RELIEF_RIDGE** then the border is centered on the trajectory.

Height of left side of polygon\'s path relative to right.
**TK_RELIEF_RAISED** means left side should appear higher and
**TK_RELIEF_SUNKEN** means right side should appear higher;
**TK_RELIEF_GROOVE** and **TK_RELIEF_RIDGE** mean the obvious things.
For **Tk_Fill3DPolygon**, **TK_RELIEF_FLAT** may also be specified to
indicate no difference in height.

Non-zero means this bevel forms the left side of the value; zero means
it forms the right side.

Non-zero means that the left edge of the horizontal bevel angles in, so
that the bottom of the edge is farther to the right than the top. Zero
means the edge angles out, so that the bottom is farther to the left
than the top.

Non-zero means that the right edge of the horizontal bevel angles in, so
that the bottom of the edge is farther to the left than the top. Zero
means the edge angles out, so that the bottom is farther to the right
than the top.

Non-zero means this bevel forms the top side of the value; zero means it
forms the bottom side.

Specifies which of the border\'s graphics contexts is desired. Must be
**TK_3D_FLAT_GC**, **TK_3D_LIGHT_GC**, or **TK_3D_DARK_GC**.

# DESCRIPTION

These procedures provide facilities for drawing window borders in a way
that produces a three-dimensional appearance.
**Tk_Alloc3DBorderFromObj** allocates colors and Pixmaps needed to draw
a border in the window given by the *tkwin* argument. The value of
*objPtr* is a standard Tk color name that determines the border colors.
The color indicated by *objPtr* will not actually be used in the border;
it indicates the background color for the window (i.e. a color for flat
surfaces). The illuminated portions of the border will appear brighter
than indicated by *objPtr*, and the shadowed portions of the border will
appear darker than *objPtr*.

**Tk_Alloc3DBorderFromObj** returns a token that may be used in later
calls to **Tk_Draw3DRectangle**. If an error occurs in allocating
information for the border (e.g. a bogus color name was given) then NULL
is returned and an error message is left as the result of interpreter
*interp*. If it returns successfully, **Tk_Alloc3DBorderFromObj** caches
information about the return value in *objPtr*, which speeds up future
calls to **Tk_Alloc3DBorderFromObj** with the same *objPtr* and *tkwin*.

**Tk_Get3DBorder** is identical to **Tk_Alloc3DBorderFromObj** except
that the color is specified with a string instead of a value. This
prevents **Tk_Get3DBorder** from caching the return value, so
**Tk_Get3DBorder** is less efficient than **Tk_Alloc3DBorderFromObj**.

**Tk_Get3DBorderFromObj** returns the token for an existing border,
given the window and color name used to create the border.
**Tk_Get3DBorderFromObj** does not actually create the border; it must
already have been created with a previous call to
**Tk_Alloc3DBorderFromObj** or **Tk_Get3DBorder**. The return value is
cached in *objPtr*, which speeds up future calls to
**Tk_Get3DBorderFromObj** with the same *objPtr* and *tkwin*.

Once a border structure has been created, **Tk_Draw3DRectangle** may be
invoked to draw the border. The *tkwin* argument specifies the window
for which the border was allocated, and *drawable* specifies a window or
pixmap in which the border is to be drawn. *Drawable* need not refer to
the same window as *tkwin*, but it must refer to a compatible pixmap or
window: one associated with the same screen and with the same depth as
*tkwin*. The *x*, *y*, *width*, and *height* arguments define the
bounding box of the border region within *drawable* (usually *x* and *y*
are zero and *width* and *height* are the dimensions of the window), and
*borderWidth* specifies the number of pixels actually occupied by the
border. The *relief* argument indicates which of several
three-dimensional effects is desired: **TK_RELIEF_RAISED** means that
the interior of the rectangle should appear raised relative to the
exterior of the rectangle, and **TK_RELIEF_SUNKEN** means that the
interior should appear depressed. **TK_RELIEF_GROOVE** and
**TK_RELIEF_RIDGE** mean that there should appear to be a groove or
ridge around the exterior of the rectangle.

**Tk_Fill3DRectangle** is somewhat like **Tk_Draw3DRectangle** except
that it first fills the rectangular area with the background color (one
corresponding to the color used to create *border*). Then it calls
**Tk_Draw3DRectangle** to draw a border just inside the outer edge of
the rectangular area. The argument *relief* indicates the desired effect
(**TK_RELIEF_FLAT** means no border should be drawn; all that happens is
to fill the rectangle with the background color).

The procedure **Tk_Draw3DPolygon** may be used to draw more complex
shapes with a three-dimensional appearance. The *pointPtr* and
*numPoints* arguments define a trajectory, *polyBorderWidth* indicates
how wide the border should be (and on which side of the trajectory to
draw it), and *leftRelief* indicates which side of the trajectory should
appear raised. **Tk_Draw3DPolygon** draws a border around the given
trajectory using the colors from *border* to produce a three-dimensional
appearance. If the trajectory is non-self-intersecting, the appearance
will be a raised or sunken polygon shape. The trajectory may be
self-intersecting, although it\'s not clear how useful this is.

**Tk_Fill3DPolygon** is to **Tk_Draw3DPolygon** what
**Tk_Fill3DRectangle** is to **Tk_Draw3DRectangle**: it fills the
polygonal area with the background color from *border*, then calls
**Tk_Draw3DPolygon** to draw a border around the area (unless
*leftRelief* is **TK_RELIEF_FLAT**; in this case no border is drawn).

The procedures **Tk_3DVerticalBevel** and **Tk_3DHorizontalBevel**
provide lower-level drawing primitives that are used by procedures such
as **Tk_Draw3DRectangle**. These procedures are also useful in their own
right for drawing rectilinear border shapes. **Tk_3DVerticalBevel**
draws a vertical beveled edge, such as the left or right side of a
rectangle, and **Tk_3DHorizontalBevel** draws a horizontal beveled edge,
such as the top or bottom of a rectangle. Each procedure takes *x*, *y*,
*width*, and *height* arguments that describe the rectangular area of
the beveled edge (e.g., *width* is the border width for
**Tk_3DVerticalBevel**). The *leftBorder* and *topBorder* arguments
indicate the position of the border relative to the of the value, and
*relief* indicates the relief of the inside of the value relative to the
outside. **Tk_3DVerticalBevel** just draws a rectangular region.
**Tk_3DHorizontalBevel** draws a trapezoidal region to generate mitered
corners; it should be called after **Tk_3DVerticalBevel** (otherwise
**Tk_3DVerticalBevel** will overwrite the mitering in the corner). The
*leftIn* and *rightIn* arguments to **Tk_3DHorizontalBevel** describe
the mitering at the corners; a value of 1 means that the bottom edge of
the trapezoid will be shorter than the top, 0 means it will be longer.
For example, to draw a rectangular border the top bevel should be drawn
with 1 for both *leftIn* and *rightIn*, and the bottom bevel should be
drawn with 0 for both arguments.

The procedure **Tk_SetBackgroundFromBorder** will modify the background
pixel and/or pixmap of *tkwin* to produce a result compatible with
*border*. For color displays, the resulting background will just be the
color specified when *border* was created; for monochrome displays, the
resulting background will be a light stipple pattern, in order to
distinguish the background from the illuminated portion of the border.

Given a token for a border, the procedure **Tk_NameOf3DBorder** will
return the color name that was used to create the border.

The procedure **Tk_3DBorderColor** returns the XColor structure that
will be used for flat surfaces drawn for its *border* argument by
procedures like **Tk_Fill3DRectangle**. The return value corresponds to
the color name that was used to create the border. The XColor, and its
associated pixel value, will remain allocated as long as *border*
exists.

The procedure **Tk_3DBorderGC** returns one of the X graphics contexts
that are used to draw the border. The argument *which* selects which one
of the three possible GC\'s: **TK_3D_FLAT_GC** returns the context used
for flat surfaces, **TK_3D_LIGHT_GC** returns the context for light
shadows, and **TK_3D_DARK_GC** returns the context for dark shadows.

When a border is no longer needed, **Tk_Free3DBorderFromObj** or
**Tk_Free3DBorder** should be called to release the resources associated
with it. For **Tk_Free3DBorderFromObj** the border to release is
specified with the window and color name used to create the border; for
**Tk_Free3DBorder** the border to release is specified with the
Tk_3DBorder token for the border. There should be exactly one call to
**Tk_Free3DBorderFromObj** or **Tk_Free3DBorder** for each call to
**Tk_Alloc3DBorderFromObj** or **Tk_Get3DBorder**.

# KEYWORDS

3D, background, border, color, depressed, illumination, value, polygon,
raised, shadow, three-dimensional effect

<!---
Copyright (c) 1990-1993 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

