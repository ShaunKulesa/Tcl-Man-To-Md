# NAME

Tk_GetImage, Tk_RedrawImage, Tk_SizeOfImage, Tk_FreeImage - use an image
in a widget

# SYNOPSIS

**#include \<tk.h\>**

Tk_Image **Tk_GetImage**(*interp, tkwin, name, changeProc, clientData*)

**Tk_RedrawImage**(*image, imageX, imageY, width, height, drawable,
drawableX, drawableY*)

**Tk_SizeOfImage**(*image, widthPtr, heightPtr*)

**Tk_FreeImage**(*image*)

# ARGUMENTS

Place to leave error message.

Window in which image will be used.

Name of image.

Procedure for Tk to invoke whenever image content or size changes.

One-word value for Tk to pass to *changeProc*.

Token for image instance; must have been returned by a previous call to
**Tk_GetImage**.

X-coordinate of upper-left corner of region of image to redisplay
(measured in pixels from the image\'s upper-left corner).

Y-coordinate of upper-left corner of region of image to redisplay
(measured in pixels from the image\'s upper-left corner).

Width of region of image to redisplay.

Height of region of image to redisplay.

Where to display image. Must either be window specified to
**Tk_GetImage** or a pixmap compatible with that window.

Where to display image in *drawable*: this is the x-coordinate in
*drawable* where x-coordinate *imageX* of the image should be displayed.

Where to display image in *drawable*: this is the y-coordinate in
*drawable* where y-coordinate *imageY* of the image should be displayed.

Store width of *image* (in pixels) here.

Store height of *image* (in pixels) here.

# DESCRIPTION

These procedures are invoked by widgets that wish to display images.
**Tk_GetImage** is invoked by a widget when it first decides to display
an image. *name* gives the name of the desired image and *tkwin*
identifies the window where the image will be displayed. **Tk_GetImage**
looks up the image in the table of existing images and returns a token
for a new instance of the image. If the image does not exist then
**Tk_GetImage** returns NULL and leaves an error message in interpreter
*interp*\'s result.

When a widget wishes to actually display an image it must call
**Tk_RedrawImage**, identifying the image (*image*), a region within the
image to redisplay (*imageX*, *imageY*, *width*, and *height*), and a
place to display the image (*drawable*, *drawableX*, and *drawableY*).
Tk will then invoke the appropriate image manager, which will display
the requested portion of the image before returning.

A widget can find out the dimensions of an image by calling
**Tk_SizeOfImage**: the width and height will be stored in the locations
given by *widthPtr* and *heightPtr*, respectively.

When a widget is finished with an image (e.g., the widget is being
deleted or it is going to use a different image instead of the current
one), it must call **Tk_FreeImage** to release the image instance. The
widget should never again use the image token after passing it to
**Tk_FreeImage**. There must be exactly one call to **Tk_FreeImage** for
each call to **Tk_GetImage**.

If the contents or size of an image changes, then any widgets using the
image will need to find out about the changes so that they can redisplay
themselves. The *changeProc* and *clientData* arguments to
**Tk_GetImage** are used for this purpose. *changeProc* will be called
by Tk whenever a change occurs in the image; it must match the following
prototype:

    typedef void Tk_ImageChangedProc(
            ClientData clientData,
            int x,
            int y,
            int width,
            int height,
            int imageWidth,
            int imageHeight);

The *clientData* argument to *changeProc* is the same as the
*clientData* argument to **Tk_GetImage**. It is usually a pointer to the
widget record for the widget or some other data structure managed by the
widget. The arguments *x*, *y*, *width*, and *height* identify a region
within the image that must be redisplayed; they are specified in pixels
measured from the upper-left corner of the image. The arguments
*imageWidth* and *imageHeight* give the image\'s (new) size.

# SEE ALSO

Tk_CreateImageType

# KEYWORDS

images, redisplay
