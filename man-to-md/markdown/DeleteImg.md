# NAME

Tk_DeleteImage - Destroy an image.

# SYNOPSIS

**#include \<tk.h\>**

**Tk_DeleteImage**(*interp, name*)

# ARGUMENTS

Interpreter for which the image was created.

Name of the image.

# DESCRIPTION

**Tk_DeleteImage** deletes the image given by *interp* and *name*, if
there is one. All instances of that image will redisplay as empty
regions. If the given image does not exist then the procedure has no
effect.

# KEYWORDS

delete image, image manager

<!---
Copyright (c) 1995-1996 Sun Microsystems, Inc
-->

