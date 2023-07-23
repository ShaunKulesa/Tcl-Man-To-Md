# NAME

Tk_ImageChanged - notify widgets that image needs to be redrawn

# SYNOPSIS

**#include \<tk.h\>**

**Tk_ImageChanged**(*model, x, y, width, height, imageWidth,
imageHeight*)

# ARGUMENTS

Token for image, which was passed to image\'s *createProc* when the
image was created.

X-coordinate of upper-left corner of region that needs redisplay
(measured from upper-left corner of image).

Y-coordinate of upper-left corner of region that needs redisplay
(measured from upper-left corner of image).

Width of region that needs to be redrawn, in pixels.

Height of region that needs to be redrawn, in pixels.

Current width of image, in pixels.

Current height of image, in pixels.

# DESCRIPTION

An image manager calls **Tk_ImageChanged** for an image whenever
anything happens that requires the image to be redrawn. As a result of
calling **Tk_ImageChanged**, any widgets using the image are notified so
that they can redisplay themselves appropriately. The *model* argument
identifies the image, and *x*, *y*, *width*, and *height* specify a
rectangular region within the image that needs to be redrawn.
*imageWidth* and *imageHeight* specify the image\'s (new) size.

*Tk_ImageModel* is synonym for *Tk_ImageMaster*

An image manager should call **Tk_ImageChanged** during its *createProc*
to specify the image\'s initial size and to force redisplay if there are
existing instances for the image. If any of the pixel values in the
image should change later on, **Tk_ImageChanged** should be called again
with *x*, *y*, *width*, and *height* values that cover all the pixels
that changed. If the size of the image should change, then
**Tk_ImageChanged** must be called to indicate the new size, even if no
pixels need to be redisplayed.

# SEE ALSO

Tk_CreateImageType

# KEYWORDS

images, redisplay, image size changes

<!---
Copyright (c) 1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

