# NAME

Ttk_MakeBox, Ttk_PadBox, Ttk_ExpandBox, Ttk_PackBox, Ttk_StickBox,
Ttk_PlaceBox, Ttk_BoxContains, Ttk_MakePadding, Ttk_UniformPadding,
Ttk_AddPadding, Ttk_RelievePadding, Ttk_GetPaddingFromObj,
Ttk_GetBorderFromObj, Ttk_GetStickyFromObj - Tk themed geometry
utilities

# SYNOPSIS

**#include \<tkTheme.h\>**

Ttk_Box **Ttk_MakeBox**(int *x*, int *y*, int *width*, int *height*);

Ttk_Box **Ttk_PadBox**(Ttk_Box *parcel*, Ttk_Padding *padding*);

Ttk_Box **Ttk_ExpandBox**(Ttk_Box *parcel*, Ttk_Padding *padding*);

Ttk_Box **Ttk_PackBox**(Ttk_Box \**cavity*, int *width*, int *height*,
Ttk_Side *side*);

Ttk_Box **Ttk_StickBox**(Ttk_Box *parcel*, int *width*, int *height*,
unsigned *sticky*);

Ttk_Box **Ttk_PlaceBox**(Ttk_Box \**cavity*, int *width*, int *height*,
Ttk_Side *side*, unsigned *sticky*);

Ttk_Box **Ttk_AnchorBox**(Ttk_Box *parcel*, int *width*, int *height*,
Tk_Anchor *anchor*);

Ttk_Padding **Ttk_MakePadding**(short *left*, short *top*, short
*right*, short *bottom*);

Ttk_Padding **Ttk_UniformPadding**(short *border*);

Ttk_Padding **Ttk_AddPadding**(Ttk_Padding *padding1*, Ttk_Padding
*padding2*;

Ttk_Padding **Ttk_RelievePadding**(Ttk_Padding *padding*, int *relief*);

int **Ttk_BoxContains**(Ttk_Box *box*, int *x*, int *y*);

int **Ttk_GetPaddingFromObj**(Tcl_Interp \**interp*, Tk_Window *tkwin*,
Tcl_Obj \**objPtr*, Ttk_Padding \**padding_rtn*);

int **Ttk_GetBorderFromObj**(Tcl_Interp \**interp*, Tcl_Obj \**objPtr*,
Ttk_Padding \**padding_rtn*);

int **Ttk_GetStickyFromObj**(Tcl_Interp \**interp*, Tcl_Obj \**objPtr*,
int \**sticky_rtn*);

# ARGUMENTS

One of the symbolic constants **TK_ANCHOR_N**, **TK_ANCHOR_NE**, etc.
See *Tk_GetAnchorFromObj(3)*.

A rectangular region from which a parcel is allocated.

Extra padding (in pixels) to add uniformly to each side of a region.

Extra padding (in pixels) to add to the bottom of a region.

Specifies a rectangular region.

A rectangular region.

The height in pixels of a region.

Used to store error messages.

Extra padding (in pixels) to add to the left side of a region.

String value contains a symbolic name to be converted to an enumerated
value or bitmask. Internal rep may be be modified to cache corresponding
value.

Extra padding to add on the inside of a region.

Padding present in the inside of a region.

A rectangular region, allocated from a cavity.

One of the standard Tk relief options (**TK_RELIEF_RAISED**,
**TK_RELIEF_SUNKEN**, etc.). See **Tk_GetReliefFromObj**.

Extra padding (in pixels) to add to the right side of a region.

One of **TTK_SIDE_LEFT**, **TTK_SIDE_TOP**, **TTK_SIDE_RIGHT**, or
**TTK_SIDE_BOTTOM**.

A bitmask containing one or more of the bits **TTK_STICK_W** (west, or
left), **TTK_STICK_E** (east, or right), **TTK_STICK_N** (north, or
top), and **TTK_STICK_S** (south, or bottom). **TTK_FILL_X** is defined
as a synonym for (**TTK_STICK_W**\|**TTK_STICK_E**), **TTK_FILL_Y** is a
synonym for (**TTK_STICK_N**\|**TTK_STICK_S**), and **TTK_FILL_BOTH** is
a synonym for (**TTK_FILL_X**\|**TTK_FILL_Y**). See also: *grid(n)*.

Window whose screen geometry determines the conversion between absolute
units and pixels.

Extra padding at the top of a region.

The width in pixels of a region.

X coordinate of upper-left corner of region.

Y coordinate of upper-left corner of region.

# BOXES

The **Ttk_Box** structure represents a rectangular region of a window:

    typedef struct {
        int x;
        int y;
        int width;
        int height;
    } Ttk_Box;

All coordinates are relative to the window.

**Ttk_MakeBox** is a convenience routine that constructs a **Ttk_Box**
structure representing a region *width* pixels wide, *height* pixels
tall, at the specified *x, y* coordinates.

**Ttk_PadBox** returns a new box located inside the specified *parcel*,
shrunken according to the left, top, right, and bottom margins specified
by *padding*.

**Ttk_ExpandBox** is the inverse of **Ttk_PadBox**: it returns a new box
surrounding the specified *parcel*, expanded according to the left, top,
right, and bottom margins specified by *padding*.

**Ttk_PackBox** allocates a parcel *width* by *height* pixels wide on
the specified *side* of the *cavity*, and shrinks the *cavity*
accordingly.

**Ttk_StickBox** places a box with the requested *width* and *height*
inside the *parcel* according to the *sticky* bits.

**Ttk_PlaceBox** combines **Ttk_PackBox** and **Ttk_StickBox**: it
allocates a parcel on the specified *side* of the *cavity*, places a box
of the requested size inside the parcel according to *sticky*, and
shrinks the *cavity*.

**Ttk_AnchorBox** places a box with the requested *width* and *height*
inside the *parcel* according to the specified *anchor* option.

**Ttk_BoxContains** tests if the specified *x, y* coordinate lies within
the rectangular region *box*.

# PADDDING

The **Ttk_Padding** structure is used to represent borders, internal
padding, and external margins:

    typedef struct {
        short left;
        short top;
        short right;
        short bottom;
    } Ttk_Padding;

**Ttk_MakePadding** is a convenience routine that constructs a
**Ttk_Padding** structure with the specified left, top, right, and
bottom components.

**Ttk_UniformPadding** constructs a **Ttk_Padding** structure with all
components equal to the specified *border*.

**Ttk_AddPadding** adds two **Ttk_Padding**s together and returns a
combined padding containing the sum of the individual padding
components.

**Ttk_RelievePadding** adds an extra 2 pixels of padding to *padding*
according to the specified *relief*. If *relief* is
**TK_RELIEF_SUNKEN**, adds two pixels at the top and left so the inner
region is shifted down and to the left. If it is **TK_RELIEF_RAISED**,
adds two pixels at the bottom and right so the inner region is shifted
up and to the right. Otherwise, adds 1 pixel on all sides. This is
typically used in element geometry procedures to simulate a look for
pushbuttons.

# CONVERSION ROUTINES

**Ttk_GetPaddingFromObj** converts the string in *objPtr* to a
**Ttk_Padding** structure. The string representation is a list of up to
four length specifications If fewer than four elements are specified,
*bottom* defaults to *top*, *right* defaults to *left*, and *top*
defaults to *left*. See **Tk_GetPixelsFromObj(3)** for the syntax of
length specifications.

**Ttk_GetBorderFromObj** is the same as **Ttk_GetPaddingFromObj** except
that the lengths are specified as integers (i.e., resolution-dependent
values like *3m* are not allowed).

**Ttk_GetStickyFromObj** converts the string in *objPtr* to a *sticky*
bitmask. The string contains zero or more of the characters **n**,
**s**, **e**, or **w**.

# SEE ALSO

Tk_GetReliefFromObj(3), Tk_GetPixelsFromObj(3), Tk_GetAnchorFromObj(3)

# KEYWORDS

geometry, padding, margins, box, region, sticky, relief
