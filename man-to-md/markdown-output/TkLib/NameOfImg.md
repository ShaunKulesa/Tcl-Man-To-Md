# NAME

Tk_NameOfImage - Return name of image.

# SYNOPSIS

**#include \<tk.h\>**

const char \* **Tk_NameOfImage**(*imageMaster*)

# ARGUMENTS

Token for image, which was passed to image manager\'s *createProc* when
the image was created.

# DESCRIPTION

This procedure is invoked by image managers to find out the name of an
image. Given the token for the image, it returns the string name for the
image.

*Tk_ImageModel* is synonym for *Tk_ImageMaster*

# KEYWORDS

image manager, image name

<!---
Copyright (c) 1995-1996 Sun Microsystems, Inc
-->

