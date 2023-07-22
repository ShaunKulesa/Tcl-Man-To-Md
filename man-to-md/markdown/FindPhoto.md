# NAME

Tk_FindPhoto, Tk_PhotoPutBlock, Tk_PhotoPutZoomedBlock,
Tk_PhotoGetImage, Tk_PhotoBlank, Tk_PhotoExpand, Tk_PhotoGetSize,
Tk_PhotoSetSize - manipulate the image data stored in a photo image.

# SYNOPSIS

**#include \<tk.h\>**

Tk_PhotoHandle **Tk_FindPhoto**(*interp, imageName*)

int **Tk_PhotoPutBlock**(*interp, handle, blockPtr, x, y, width,
height,compRule*)

int **Tk_PhotoPutZoomedBlock**(*interp, handle, blockPtr, x, y, width,
height,zoomX, zoomY, subsampleX, subsampleY, compRule*)

int **Tk_PhotoGetImage**(*handle, blockPtr*)

void **Tk_PhotoBlank**(*handle*)

int **Tk_PhotoExpand**(*interp, handle, width, height*)

void **Tk_PhotoGetSize**(*handle, widthPtr, heightPtr*)

int **Tk_PhotoSetSize**(*interp. handle, width, height*)

# ARGUMENTS

Interpreter in which image was created and in which error reporting is
to be done.

Name of the photo image.

Opaque handle identifying the photo image to be affected.

Specifies the address and storage layout of image data.

Specifies the X coordinate where the top-left corner of the block is to
be placed within the image.

Specifies the Y coordinate where the top-left corner of the block is to
be placed within the image.

Specifies the width of the image area to be affected (for
**Tk_PhotoPutBlock**) or the desired image width (for **Tk_PhotoExpand**
and **Tk_PhotoSetSize**).

Specifies the compositing rule used when combining transparent pixels in
a block of data with a photo image. Must be one of
**TK_PHOTO_COMPOSITE_OVERLAY** (which puts the block of data over the
top of the existing photo image, with the previous contents showing
through in the transparent bits) or **TK_PHOTO_COMPOSITE_SET** (which
discards the existing photo image contents in the rectangle covered by
the data block.)

Specifies the height of the image area to be affected (for
**Tk_PhotoPutBlock**) or the desired image height (for
**Tk_PhotoExpand** and **Tk_PhotoSetSize**).

Pointer to location in which to store the image width.

Pointer to location in which to store the image height.

Specifies the subsampling factor in the X direction for input image
data.

Specifies the subsampling factor in the Y direction for input image
data.

Specifies the zoom factor to be applied in the X direction to pixels
being written to the photo image.

Specifies the zoom factor to be applied in the Y direction to pixels
being written to the photo image.

# DESCRIPTION

**Tk_FindPhoto** returns an opaque handle that is used to identify a
particular photo image to the other procedures. The parameter is the
name of the image, that is, the name specified to the **image create**
photo command, or assigned by that command if no name was specified. If
*imageName* does not exist or is not a photo image, **Tk_FindPhoto**
returns NULL.

**Tk_PhotoPutBlock** is used to supply blocks of image data to be
displayed. The call affects an area of the image of size *width* x
*height* pixels, with its top-left corner at coordinates (*x*,*y*). All
of *width*, *height*, *x*, and *y* must be non-negative. If part of this
area lies outside the current bounds of the image, the image will be
expanded to include the area, unless the user has specified an explicit
image size with the **-width** and/or **-height** widget configuration
options (see photo(n)); in that case the area is silently clipped to the
image boundaries.

The *block* parameter is a pointer to a **Tk_PhotoImageBlock**
structure, defined as follows:

    typedef struct {
        unsigned char *pixelPtr;
        int width;
        int height;
        int pitch;
        int pixelSize;
        int offset[4];
    } Tk_PhotoImageBlock;

The *pixelPtr* field points to the first pixel, that is, the top-left
pixel in the block. The *width* and *height* fields specify the
dimensions of the block of pixels. The *pixelSize* field specifies the
address difference between two horizontally adjacent pixels. It should
be 4 for RGB and 2 for grayscale image data. Other values are possible,
if the offsets in the *offset* array are adjusted accordingly (e.g. for
red, green and blue data stored in different planes). Using such a
layout is strongly discouraged, though. Due to a bug, it might not work
correctly if an alpha channel is provided. (see the **BUGS** section
below). The *pitch* field specifies the address difference between two
vertically adjacent pixels. The *offset* array contains the offsets from
the address of a pixel to the addresses of the bytes containing the red,
green, blue and alpha (transparency) components. If the offsets for red,
green and blue are equal, the image is interpreted as grayscale. If they
differ, RGB data is assumed. Normally the offsets will be 0, 1, 2, 3 for
RGB data and 0, 0, 0, 1 for grayscale. It is possible to provide image
data without an alpha channel by setting the offset for alpha to a
negative value and adjusting the *pixelSize* field accordingly. This use
is discouraged, though (see the **BUGS** section below).

The *compRule* parameter to **Tk_PhotoPutBlock** specifies a compositing
rule that says what to do with transparent pixels. The value
**TK_PHOTO_COMPOSITE_OVERLAY** says that the previous contents of the
photo image should show through, and the value
**TK_PHOTO_COMPOSITE_SET** says that the previous contents of the photo
image should be completely ignored, and the values from the block be
copied directly across. The behavior in Tk8.3 and earlier was equivalent
to having **TK_PHOTO_COMPOSITE_OVERLAY** as a compositing rule.

The value given for the *width* and *height* parameters to
**Tk_PhotoPutBlock** do not have to correspond to the values specified
in *block*. If they are smaller, **Tk_PhotoPutBlock** extracts a
sub-block from the image data supplied. If they are larger, the data
given are replicated (in a tiled fashion) to fill the specified area.
These rules operate independently in the horizontal and vertical
directions.

**Tk_PhotoPutBlock** normally returns **TCL_OK**, though if it cannot
allocate sufficient memory to hold the resulting image, **TCL_ERROR** is
returned instead and, if the *interp* argument is non-NULL, an error
message is placed in the interpreter\'s result.

**Tk_PhotoPutZoomedBlock** works like **Tk_PhotoPutBlock** except that
the image can be reduced or enlarged for display. The *subsampleX* and
*subsampleY* parameters allow the size of the image to be reduced by
subsampling. **Tk_PhotoPutZoomedBlock** will use only pixels from the
input image whose X coordinates are multiples of *subsampleX*, and whose
Y coordinates are multiples of *subsampleY*. For example, an image of
512x512 pixels can be reduced to 256x256 by setting *subsampleX* and
*subsampleY* to 2.

The *zoomX* and *zoomY* parameters allow the image to be enlarged by
pixel replication. Each pixel of the (possibly subsampled) input image
will be written to a block *zoomX* pixels wide and *zoomY* pixels high
of the displayed image. Subsampling and zooming can be used together for
special effects.

**Tk_PhotoGetImage** can be used to retrieve image data from a photo
image. **Tk_PhotoGetImage** fills in the structure pointed to by the
*blockPtr* parameter with values that describe the address and layout of
the image data that the photo image has stored internally. The values
are valid until the image is destroyed or its size is changed.

It is possible to modify an image by writing directly to the data the
*pixelPtr* field points to. The size of the image cannot be changed this
way, though. Also, changes made by writing directly to *pixelPtr* will
not be immediately visible, but only after a call to **Tk_ImageChanged**
or after an event that causes the interested widgets to redraw
themselves. For these reasons usually it is preferable to make changes
to a copy of the image data and write it back with **Tk_PhotoPutBlock**
or **Tk_PhotoPutZoomedBlock**.

**Tk_PhotoGetImage** returns 1 for compatibility with the corresponding
procedure in the old photo widget.

**Tk_PhotoBlank** blanks the entire area of the photo image. Blank areas
of a photo image are transparent.

**Tk_PhotoExpand** requests that the widget\'s image be expanded to be
at least *width* x *height* pixels in size. The width and/or height are
unchanged if the user has specified an explicit image width or height
with the **-width** and/or **-height** configuration options,
respectively. If the image data are being supplied in many small blocks,
it is more efficient to use **Tk_PhotoExpand** or **Tk_PhotoSetSize** at
the beginning rather than allowing the image to expand in many small
increments as image blocks are supplied.

**Tk_PhotoExpand** normally returns **TCL_OK**, though if it cannot
allocate sufficient memory to hold the resulting image, **TCL_ERROR** is
returned instead and, if the *interp* argument is non-NULL, an error
message is placed in the interpreter\'s result.

**Tk_PhotoSetSize** specifies the size of the image, as if the user had
specified the given *width* and *height* values to the **-width** and
**-height** configuration options. A value of zero for *width* or
*height* does not change the image\'s width or height, but allows the
width or height to be changed by subsequent calls to
**Tk_PhotoPutBlock**, **Tk_PhotoPutZoomedBlock** or **Tk_PhotoExpand**.

**Tk_PhotoSetSize** normally returns **TCL_OK**, though if it cannot
allocate sufficient memory to hold the resulting image, **TCL_ERROR** is
returned instead and, if the *interp* argument is non-NULL, an error
message is placed in the interpreter\'s result.

**Tk_PhotoGetSize** returns the dimensions of the image in \**widthPtr*
and \**heightPtr*.

# PORTABILITY

In Tk 8.3 and earlier, **Tk_PhotoPutBlock** and
**Tk_PhotoPutZoomedBlock** had different signatures. If you want to
compile code that uses the old interface against 8.4 without updating
your code, compile it with the flag -DUSE_COMPOSITELESS_PHOTO_PUT_BLOCK.
Code linked using Stubs against older versions of Tk will continue to
work.

In Tk 8.4, **Tk_PhotoPutBlock**, **Tk_PhotoPutZoomedBlock**,
**Tk_PhotoExpand** and **Tk_PhotoSetSize** did not take an *interp*
argument or return any result code. If insufficient memory was available
for an image, Tk would panic. This behaviour is still supported if you
compile your extension with the additional flag
-DUSE_PANIC_ON_PHOTO_ALLOC_FAILURE. Code linked using Stubs against
older versions of Tk will continue to work.

# BUGS

The **Tk_PhotoImageBlock** structure used to provide image data to
**Tk_PhotoPutBlock** promises great flexibility in the layout of the
data (e.g. separate planes for the red, green, blue and alpha channels).
Unfortunately, the implementation fails to hold this promise. The
problem is that the *pixelSize* field is (incorrectly) used to determine
whether the image has an alpha channel. Currently, if the offset for the
alpha channel is greater or equal than *pixelSize*, **tk_PhotoPutblock**
assumes no alpha data is present and makes the image fully opaque. This
means that for layouts where the channels are separate (or any other
exotic layout where *pixelSize* has to be smaller than the alpha
offset), the alpha channel will not be read correctly. In order to be on
the safe side if this issue will be corrected in a future release, it is
strongly recommended you always provide alpha data - even if the image
has no transparency - and only use the \"standard\" layout with a
*pixelSize* of 2 for grayscale and 4 for RGB data with *offset*s of 0,
0, 0, 1 or 0, 1, 2, 3 respectively.

# CREDITS

The code for the photo image type was developed by Paul Mackerras, based
on his earlier photo widget code.

# KEYWORDS

photo, image

<!---
Copyright (c) 1994 The Australian National Universit
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

