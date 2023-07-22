# NAME

Tk_CreateItemType, Tk_GetItemTypes - define new kind of canvas item

# SYNOPSIS

**#include \<tk.h\>**

**Tk_CreateItemType**(*typePtr*)

Tk_ItemType \* **Tk_GetItemTypes**()

# ARGUMENTS

Structure that defines the new type of canvas item.

# INTRODUCTION

**Tk_CreateItemType** is invoked to define a new kind of canvas item
described by the *typePtr* argument. An item type corresponds to a
particular value of the *type* argument to the **create** widget command
for canvases, and the code that implements a canvas item type is called
a *type manager*. Tk defines several built-in item types, such as
**rectangle** and **text** and **image**, but **Tk_CreateItemType**
allows additional item types to be defined. Once **Tk_CreateItemType**
returns, the new item type may be used in new or existing canvas widgets
just like the built-in item types.

**Tk_GetItemTypes** returns a pointer to the first in the list of all
item types currently defined for canvases. The entries in the list are
linked together through their *nextPtr* fields, with the end of the list
marked by a NULL *nextPtr*.

You may find it easier to understand the rest of this manual entry by
looking at the code for an existing canvas item type such as bitmap (in
the file tkCanvBmap.c) or text (tkCanvText.c). The easiest way to create
a new type manager is to copy the code for an existing type and modify
it for the new type.

Tk provides a number of utility procedures for the use of canvas type
managers, such as **Tk_CanvasCoords** and **Tk_CanvasPsColor**; these
are described in separate manual entries.

# DATA STRUCTURES

A type manager consists of a collection of procedures that provide a
standard set of operations on items of that type. The type manager deals
with three kinds of data structures. The first data structure is a
Tk_ItemType; it contains information such as the name of the type and
pointers to the standard procedures implemented by the type manager:

    typedef struct Tk_ItemType {
        const char *name;
        int itemSize;
        Tk_ItemCreateProc *createProc;
        const Tk_ConfigSpec *configSpecs;
        Tk_ItemConfigureProc *configProc;
        Tk_ItemCoordProc *coordProc;
        Tk_ItemDeleteProc *deleteProc;
        Tk_ItemDisplayProc *displayProc;
        int alwaysRedraw;
        Tk_ItemPointProc *pointProc;
        Tk_ItemAreaProc *areaProc;
        Tk_ItemPostscriptProc *postscriptProc;
        Tk_ItemScaleProc *scaleProc;
        Tk_ItemTranslateProc *translateProc;
        Tk_ItemIndexProc *indexProc;
        Tk_ItemCursorProc *icursorProc;
        Tk_ItemSelectionProc *selectionProc;
        Tk_ItemInsertProc *insertProc;
        Tk_ItemDCharsProc *dCharsProc;
        Tk_ItemType *nextPtr;
    } Tk_ItemType;

The fields of a Tk_ItemType structure are described in more detail later
in this manual entry. When **Tk_CreateItemType** is called, its
*typePtr* argument must point to a structure with all of the fields
initialized except *nextPtr*, which Tk sets to link all the types
together into a list. The structure must be in permanent memory (either
statically allocated or dynamically allocated but never freed); Tk
retains a pointer to this structure.

The second data structure manipulated by a type manager is an *item
record*. For each item in a canvas there exists one item record. All of
the items of a given type generally have item records with the same
structure, but different types usually have different formats for their
item records. The first part of each item record is a header with a
standard structure defined by Tk via the type Tk_Item; the rest of the
item record is defined by the type manager. A type manager must define
its item records with a Tk_Item as the first field. For example, the
item record for bitmap items is defined as follows:

    typedef struct BitmapItem {
        Tk_Item header;
        double x, y;
        Tk_Anchor anchor;
        Pixmap bitmap;
        XColor *fgColor;
        XColor *bgColor;
        GC gc;
    } BitmapItem;

The *header* substructure contains information used by Tk to manage the
item, such as its identifier, its tags, its type, and its bounding box.
The fields starting with *x* belong to the type manager: Tk will never
read or write them. The type manager should not need to read or write
any of the fields in the header except for four fields whose names are
*x1*, *y1*, *x2*, and *y2*. These fields give a bounding box for the
items using integer canvas coordinates: the item should not cover any
pixels with x-coordinate lower than *x1* or y-coordinate lower than
*y1*, nor should it cover any pixels with x-coordinate greater than or
equal to *x2* or y-coordinate greater than or equal to *y2*. It is up to
the type manager to keep the bounding box up to date as the item is
moved and reconfigured.

Whenever Tk calls a procedure in a type manager it passes in a pointer
to an item record. The argument is always passed as a pointer to a
Tk_Item; the type manager will typically cast this into a pointer to its
own specific type, such as BitmapItem.

The third data structure used by type managers has type Tk_Canvas; it
serves as an opaque handle for the canvas widget as a whole. Type
managers need not know anything about the contents of this structure. A
Tk_Canvas handle is typically passed in to the procedures of a type
manager, and the type manager can pass the handle back to library
procedures such as Tk_CanvasTkwin to fetch information about the canvas.

# TK_ITEMTYPE FIELDS

## NAME

This section and the ones that follow describe each of the fields in a
Tk_ItemType structure in detail. The *name* field provides a string name
for the item type. Once **Tk_CreateImageType** returns, this name may be
used in **create** widget commands to create items of the new type. If
there already existed an item type by this name then the new item type
replaces the old one.

## FLAGS (IN ALWAYSREDRAW)

The *typePtr-\>alwaysRedraw* field (so named for historic reasons)
contains a collection of flag bits that modify how the canvas core
interacts with the item. The following bits are defined:

**1**

:   Indicates that the item should always be redrawn when any part of
    the canvas is redrawn, rather than only when the bounding box of the
    item overlaps the area being redrawn. This is used by window items,
    for example, which need to unmap subwindows that are not on the
    screen.

**TK_CONFIG_OBJS**

:   Indicates that operations which would otherwise take a string (or
    array of strings) actually take a Tcl_Obj reference (or an array of
    such references). The operations to which this applies are the
    *configProc*, the *coordProc*, the *createProc*, the *indexProc* and
    the *insertProc*.

**TK_MOVABLE_POINTS**

:   

Indicates that the item supports the *dCharsProc*, *indexProc* and
*insertProc* with the same semantics as Tk\'s built-in line and polygon
types, and that hence individual coordinate points can be moved. Must
not be set if any of the above methods is NULL.

## ITEMSIZE

*typePtr-\>itemSize* gives the size in bytes of item records of this
type, including the Tk_Item header. Tk uses this size to allocate memory
space for items of the type. All of the item records for a given type
must have the same size. If variable length fields are needed for an
item (such as a list of points for a polygon), the type manager can
allocate a separate object of variable length and keep a pointer to it
in the item record.

## CREATEPROC

*typePtr-\>createProc* points to a procedure for Tk to call whenever a
new item of this type is created. *typePtr-\>createProc* must match the
following prototype:

    typedef int Tk_ItemCreateProc(
            Tcl_Interp *interp,
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int objc,
            Tcl_Obj *const objv[]);

The *interp* argument is the interpreter in which the canvas\'s
**create** widget command was invoked, and *canvas* is a handle for the
canvas widget. *itemPtr* is a pointer to a newly-allocated item of size
*typePtr-\>itemSize*. Tk has already initialized the item\'s header (the
first **sizeof(Tk_ItemType)** bytes). The *objc* and *objv* arguments
describe all of the arguments to the **create** command after the *type*
argument. Note that if **TK_CONFIG_OBJS** is not set in the
*typePtr-\>alwaysRedraw* field, the *objv* parameter will actually
contain a pointer to an array of constant strings. For example, in the
widget command:

    .c create rectangle 10 20 50 50 -fill black

*objc* will be **6** and *objv*\[0\] will contain the integer object
**10**.

*createProc* should use *objc* and *objv* to initialize the
type-specific parts of the item record and set an initial value for the
bounding box in the item\'s header. It should return a standard Tcl
completion code and leave an error message in the interpreter result if
an error occurs. If an error occurs Tk will free the item record, so
*createProc* must be sure to leave the item record in a clean state if
it returns an error (e.g., it must free any additional memory that it
allocated for the item).

## CONFIGSPECS

Each type manager must provide a standard table describing its
configuration options, in a form suitable for use with
**Tk_ConfigureWidget**. This table will normally be used by
*typePtr-\>createProc* and *typePtr-\>configProc*, but Tk also uses it
directly to retrieve option information in the **itemcget** and
**itemconfigure** widget commands. *typePtr-\>configSpecs* must point to
the configuration table for this type. Note: Tk provides a custom option
type **tk_CanvasTagsOption** for implementing the **-tags** option; see
an existing type manager for an example of how to use it in
*configSpecs*.

## CONFIGPROC

*typePtr-\>configProc* is called by Tk whenever the **itemconfigure**
widget command is invoked to change the configuration options for a
canvas item. This procedure must match the following prototype:

    typedef int Tk_ItemConfigureProc(
            Tcl_Interp *interp,
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int objc,
            Tcl_Obj *const objv[],
            int flags);

The *interp* argument identifies the interpreter in which the widget
command was invoked, *canvas* is a handle for the canvas widget, and
*itemPtr* is a pointer to the item being configured. *objc* and *objv*
contain the configuration options. Note that if **TK_CONFIG_OBJS** is
not set in the *typePtr-\>alwaysRedraw* field, the *objv* parameter will
actually contain a pointer to an array of constant strings. For example,
if the following command is invoked:

    .c itemconfigure 2 -fill red -outline black

*objc* is **4** and *objv* contains the string objects **-fill** through
**black**. *objc* will always be an even value. The *flags* argument
contains flags to pass to **Tk_ConfigureWidget**; currently this value
is always **TK_CONFIG_ARGV_ONLY** when Tk invokes
*typePtr-\>configProc*, but the type manager\'s *createProc* procedure
will usually invoke *configProc* with different flag values.

*typePtr-\>configProc* returns a standard Tcl completion code and leaves
an error message in the interpreter result if an error occurs. It must
update the item\'s bounding box to reflect the new configuration
options.

## COORDPROC

*typePtr-\>coordProc* is invoked by Tk to implement the **coords**
widget command for an item. It must match the following prototype:

    typedef int Tk_ItemCoordProc(
            Tcl_Interp *interp,
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int objc,
            Tcl_Obj *const objv[]);

The arguments *interp*, *canvas*, and *itemPtr* all have the standard
meanings, and *objc* and *objv* describe the coordinate arguments. Note
that if **TK_CONFIG_OBJS** is not set in the *typePtr-\>alwaysRedraw*
field, the *objv* parameter will actually contain a pointer to an array
of constant strings. For example, if the following widget command is
invoked:

    .c coords 2 30 90

*objc* will be **2** and **objv** will contain the integer objects
**30** and **90**.

The *coordProc* procedure should process the new coordinates, update the
item appropriately (e.g., it must reset the bounding box in the item\'s
header), and return a standard Tcl completion code. If an error occurs,
*coordProc* must leave an error message in the interpreter result.

## DELETEPROC

*typePtr-\>deleteProc* is invoked by Tk to delete an item and free any
resources allocated to it. It must match the following prototype:

    typedef void Tk_ItemDeleteProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            Display *display);

The *canvas* and *itemPtr* arguments have the usual interpretations, and
*display* identifies the X display containing the canvas. *deleteProc*
must free up any resources allocated for the item, so that Tk can free
the item record. *deleteProc* should not actually free the item record;
this will be done by Tk when *deleteProc* returns.

## DISPLAYPROC

*typePtr-\>displayProc* is invoked by Tk to redraw an item on the
screen. It must match the following prototype:

    typedef void Tk_ItemDisplayProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            Display *display,
            Drawable dst,
            int x,
            int y,
            int width,
            int height);

The *canvas* and *itemPtr* arguments have the usual meaning. *display*
identifies the display containing the canvas, and *dst* specifies a
drawable in which the item should be rendered; typically this is an
off-screen pixmap, which Tk will copy into the canvas\'s window once all
relevant items have been drawn. *x*, *y*, *width*, and *height* specify
a rectangular region in canvas coordinates, which is the area to be
redrawn; only information that overlaps this area needs to be redrawn.
Tk will not call *displayProc* unless the item\'s bounding box overlaps
the redraw area, but the type manager may wish to use the redraw area to
optimize the redisplay of the item.

Because of scrolling and the use of off-screen pixmaps for
double-buffered redisplay, the item\'s coordinates in *dst* will not
necessarily be the same as those in the canvas. *displayProc* should
call **Tk_CanvasDrawableCoords** to transform coordinates from those of
the canvas to those of *dst*.

Normally an item\'s *displayProc* is only invoked if the item overlaps
the area being displayed. However, if bit zero of
*typePtr-\>alwaysRedraw* is 1, (i.e.  then *displayProc* is invoked
during every redisplay operation, even if the item does not overlap the
area of redisplay; this is useful for cases such as window items, where
the subwindow needs to be unmapped when it is off the screen.

## POINTPROC

*typePtr-\>pointProc* is invoked by Tk to find out how close a given
point is to a canvas item. Tk uses this procedure for purposes such as
locating the item under the mouse or finding the closest item to a given
point. The procedure must match the following prototype:

    typedef double Tk_ItemPointProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            double *pointPtr);

*canvas* and *itemPtr* have the usual meaning. *pointPtr* points to an
array of two numbers giving the x and y coordinates of a point.
*pointProc* must return a real value giving the distance from the point
to the item, or 0 if the point lies inside the item.

## AREAPROC

*typePtr-\>areaProc* is invoked by Tk to find out the relationship
between an item and a rectangular area. It must match the following
prototype:

    typedef int Tk_ItemAreaProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            double *rectPtr);

*canvas* and *itemPtr* have the usual meaning. *rectPtr* points to an
array of four real numbers; the first two give the x and y coordinates
of the upper left corner of a rectangle, and the second two give the x
and y coordinates of the lower right corner. *areaProc* must return -1
if the item lies entirely outside the given area, 0 if it lies partially
inside and partially outside the area, and 1 if it lies entirely inside
the area.

## POSTSCRIPTPROC

*typePtr-\>postscriptProc* is invoked by Tk to generate Postscript for
an item during the **postscript** widget command. If the type manager is
not capable of generating Postscript then *typePtr-\>postscriptProc*
should be NULL. The procedure must match the following prototype:

    typedef int Tk_ItemPostscriptProc(
            Tcl_Interp *interp,
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int prepass);

The *interp*, *canvas*, and *itemPtr* arguments all have standard
meanings; *prepass* will be described below. If *postscriptProc*
completes successfully, it should append Postscript for the item to the
information in the interpreter result (e.g. by calling
**Tcl_AppendResult**, not **Tcl_SetResult**) and return **TCL_OK**. If
an error occurs, *postscriptProc* should clear the result and replace
its contents with an error message; then it should return **TCL_ERROR**.

Tk provides a collection of utility procedures to simplify
*postscriptProc*. For example, **Tk_CanvasPsColor** will generate
Postscript to set the current color to a given Tk color and
**Tk_CanvasPsFont** will set up font information. When generating
Postscript, the type manager is free to change the graphics state of the
Postscript interpreter, since Tk places **gsave** and **grestore**
commands around the Postscript for the item. The type manager can use
canvas x coordinates directly in its Postscript, but it must call
**Tk_CanvasPsY** to convert y coordinates from the space of the canvas
(where the origin is at the upper left) to the space of Postscript
(where the origin is at the lower left).

In order to generate Postscript that complies with the Adobe Document
Structuring Conventions, Tk actually generates Postscript in two passes.
It calls each item\'s *postscriptProc* in each pass. The only purpose of
the first pass is to collect font information (which is done by
**Tk_CanvasPsFont**); the actual Postscript is discarded. Tk sets the
*prepass* argument to *postscriptProc* to 1 during the first pass; the
type manager can use *prepass* to skip all Postscript generation except
for calls to **Tk_CanvasPsFont**. During the second pass *prepass* will
be 0, so the type manager must generate complete Postscript.

## SCALEPROC

*typePtr-\>scaleProc* is invoked by Tk to rescale a canvas item during
the **scale** widget command. The procedure must match the following
prototype:

    typedef void Tk_ItemScaleProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            double originX,
            double originY,
            double scaleX,
            double scaleY);

The *canvas* and *itemPtr* arguments have the usual meaning. *originX*
and *originY* specify an origin relative to which the item is to be
scaled, and *scaleX* and *scaleY* give the x and y scale factors. The
item should adjust its coordinates so that a point in the item that used
to have coordinates *x* and *y* will have new coordinates *x′* and *y′*,
where

    x′ = originX + scaleX × (x − originX)
    y′ = originY + scaleY × (y − originY)

*scaleProc* must also update the bounding box in the item\'s header.

## TRANSLATEPROC

*typePtr-\>translateProc* is invoked by Tk to translate a canvas item
during the **move** widget command. The procedure must match the
following prototype:

    typedef void Tk_ItemTranslateProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            double deltaX,
            double deltaY);

The *canvas* and *itemPtr* arguments have the usual meaning, and
*deltaX* and *deltaY* give the amounts that should be added to each x
and y coordinate within the item. The type manager should adjust the
item\'s coordinates and update the bounding box in the item\'s header.

## INDEXPROC

*typePtr-\>indexProc* is invoked by Tk to translate a string index
specification into a numerical index, for example during the **index**
widget command. It is only relevant for item types that support
indexable text or coordinates; *typePtr-\>indexProc* may be specified as
NULL for non-textual item types if they do not support detailed
coordinate addressing. The procedure must match the following prototype:

    typedef int Tk_ItemIndexProc(
            Tcl_Interp *interp,
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            Tcl_Obj *indexObj,
            int *indexPtr);

The *interp*, *canvas*, and *itemPtr* arguments all have the usual
meaning. *indexObj* contains a textual description of an index, and
*indexPtr* points to an integer value that should be filled in with a
numerical index. Note that if **TK_CONFIG_OBJS** is not set in the
*typePtr-\>alwaysRedraw* field, the *indexObj* parameter will actually
contain a pointer to a constant string. It is up to the type manager to
decide what forms of index are supported (e.g., numbers, **insert**,
**sel.first**, **end**, etc.). *indexProc* should return a Tcl
completion code and set the interpreter result in the event of an error.

## ICURSORPROC

*typePtr-\>icursorProc* is invoked by Tk during the **icursor** widget
command to set the position of the insertion cursor in a textual item.
It is only relevant for item types that support an insertion cursor;
*typePtr-\>icursorProc* may be specified as NULL for item types that do
not support an insertion cursor. The procedure must match the following
prototype:

    typedef void Tk_ItemCursorProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int index);

*canvas* and *itemPtr* have the usual meanings, and *index* is an index
into the item\'s text, as returned by a previous call to
*typePtr-\>insertProc*. The type manager should position the insertion
cursor in the item just before the character given by *index*. Whether
or not to actually display the insertion cursor is determined by other
information provided by **Tk_CanvasGetTextInfo**.

## SELECTIONPROC

*typePtr-\>selectionProc* is invoked by Tk during selection retrievals;
it must return part or all of the selected text in the item (if any). It
is only relevant for item types that support text;
*typePtr-\>selectionProc* may be specified as NULL for non-textual item
types. The procedure must match the following prototype:

    typedef int Tk_ItemSelectionProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int offset,
            char *buffer,
            int maxBytes);

*canvas* and *itemPtr* have the usual meanings. *offset* is an offset in
bytes into the selection where 0 refers to the first byte of the
selection; it identifies the first character that is to be returned in
this call. *buffer* points to an area of memory in which to store the
requested bytes, and *maxBytes* specifies the maximum number of bytes to
return. *selectionProc* should extract up to *maxBytes* characters from
the selection and copy them to *maxBytes*; it should return a count of
the number of bytes actually copied, which may be less than *maxBytes*
if there are not *offset+maxBytes* bytes in the selection.

## INSERTPROC

*typePtr-\>insertProc* is invoked by Tk during the **insert** widget
command to insert new text or coordinates into a canvas item. It is only
relevant for item types that support the **insert** method;
*typePtr-\>insertProc* may be specified as NULL for other item types.
The procedure must match the following prototype:

    typedef void Tk_ItemInsertProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int index,
            Tcl_Obj *obj);

*canvas* and *itemPtr* have the usual meanings. *index* is an index into
the item\'s text, as returned by a previous call to
*typePtr-\>insertProc*, and *obj* contains new text to insert just
before the character given by *index*. Note that if **TK_CONFIG_OBJS**
is not set in the *typePtr-\>alwaysRedraw* field, the *obj* parameter
will actually contain a pointer to a constant string to be inserted. If
the item supports modification of the coordinates list by this

The type manager should insert the text and recompute the bounding box
in the item\'s header.

## DCHARSPROC

*typePtr-\>dCharsProc* is invoked by Tk during the **dchars** widget
command to delete a range of text from a canvas item or a range of
coordinates from a pathed item. It is only relevant for item types that
support text; *typePtr-\>dCharsProc* may be specified as NULL for
non-textual item types that do not want to support coordinate deletion.
The procedure must match the following prototype:

    typedef void Tk_ItemDCharsProc(
            Tk_Canvas canvas,
            Tk_Item *itemPtr,
            int first,
            int last);

*canvas* and *itemPtr* have the usual meanings. *first* and *last* give
the indices of the first and last bytes to be deleted, as returned by
previous calls to *typePtr-\>indexProc*. The type manager should delete
the specified characters and update the bounding box in the item\'s
header.

# SEE ALSO

Tk_CanvasPsY, Tk_CanvasTextInfo, Tk_CanvasTkwin

# KEYWORDS

canvas, focus, item type, selection, type manager

<!---
Copyright (c) 1994-1995 Sun Microsystems, Inc
-->

