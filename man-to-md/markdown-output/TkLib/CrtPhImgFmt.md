# NAME

Tk_CreatePhotoImageFormat - define new file format for photo images

# SYNOPSIS

**#include \<tk.h\>**

**Tk_CreatePhotoImageFormat**(*formatPtr*)

# ARGUMENTS

Structure that defines the new file format.

# DESCRIPTION

**Tk_CreatePhotoImageFormat** is invoked to define a new file format for
image data for use with photo images. The code that implements an image
file format is called an image file format handler, or handler for
short. The photo image code maintains a list of handlers that can be
used to read and write data to or from a file. Some handlers may also
support reading image data from a string or converting image data to a
string format. The user can specify which handler to use with the
**-format** image configuration option or the **-format** option to the
**read** and **write** photo image subcommands.

An image file format handler consists of a collection of procedures plus
a Tk_PhotoImageFormat structure, which contains the name of the image
file format and pointers to six procedures provided by the handler to
deal with files and strings in this format. The Tk_PhotoImageFormat
structure contains the following fields:

    typedef struct Tk_PhotoImageFormat {
        const char *name;
        Tk_ImageFileMatchProc *fileMatchProc;
        Tk_ImageStringMatchProc *stringMatchProc;
        Tk_ImageFileReadProc *fileReadProc;
        Tk_ImageStringReadProc *stringReadProc;
        Tk_ImageFileWriteProc *fileWriteProc;
        Tk_ImageStringWriteProc *stringWriteProc;
    } Tk_PhotoImageFormat;

The handler need not provide implementations of all six procedures. For
example, the procedures that handle string data would not be provided
for a format in which the image data are stored in binary, and could
therefore contain null characters. If any procedure is not implemented,
the corresponding pointer in the Tk_PhotoImageFormat structure should be
set to NULL. The handler must provide the *fileMatchProc* procedure if
it provides the *fileReadProc* procedure, and the *stringMatchProc*
procedure if it provides the *stringReadProc* procedure.

## NAME

*formatPtr-\>name* provides a name for the image type. Once
**Tk_CreatePhotoImageFormat** returns, this name may be used in the
**-format** photo image configuration and subcommand option. The manual
page for the photo image (photo(n)) describes how image file formats are
chosen based on their names and the value given to the **-format**
option. The first character of *formatPtr-\>name* must not be an
uppercase character from the ASCII character set (that is, one of the
characters **A**-**Z**). Such names are used only for legacy interface
support (see below).

## FILEMATCHPROC

*formatPtr-\>fileMatchProc* provides the address of a procedure for Tk
to call when it is searching for an image file format handler suitable
for reading data in a given file. *formatPtr-\>fileMatchProc* must match
the following prototype:

    typedef int Tk_ImageFileMatchProc(
            Tcl_Channel chan,
            const char *fileName,
            Tcl_Obj *format,
            int *widthPtr,
            int *heightPtr,
            Tcl_Interp *interp);

The *fileName* argument is the name of the file containing the image
data, which is open for reading as *chan*. The *format* argument
contains the value given for the **-format** option, or NULL if the
option was not specified. If the data in the file appears to be in the
format supported by this handler, the *formatPtr-\>fileMatchProc*
procedure should store the width and height of the image in \**widthPtr*
and \**heightPtr* respectively, and return 1. Otherwise it should return
0.

## STRINGMATCHPROC

*formatPtr-\>stringMatchProc* provides the address of a procedure for Tk
to call when it is searching for an image file format handler for
suitable for reading data from a given string.
*formatPtr-\>stringMatchProc* must match the following prototype:

    typedef int Tk_ImageStringMatchProc(
            Tcl_Obj *data,
            Tcl_Obj *format,
            int *widthPtr,
            int *heightPtr,
            Tcl_Interp *interp);

The *data* argument points to the object containing the image data. The
*format* argument contains the value given for the **-format** option,
or NULL if the option was not specified. If the data in the string
appears to be in the format supported by this handler, the
*formatPtr-\>stringMatchProc* procedure should store the width and
height of the image in \**widthPtr* and \**heightPtr* respectively, and
return 1. Otherwise it should return 0.

## FILEREADPROC

*formatPtr-\>fileReadProc* provides the address of a procedure for Tk to
call to read data from an image file into a photo image.
*formatPtr-\>fileReadProc* must match the following prototype:

    typedef int Tk_ImageFileReadProc(
            Tcl_Interp *interp,
            Tcl_Channel chan,
            const char *fileName,
            Tcl_Obj *format,
            PhotoHandle imageHandle,
            int destX, int destY,
            int width, int height,
            int srcX, int srcY);

The *interp* argument is the interpreter in which the command was
invoked to read the image; it should be used for reporting errors. The
image data is in the file named *fileName*, which is open for reading as
*chan*. The *format* argument contains the value given for the
**-format** option, or NULL if the option was not specified. The image
data in the file, or a subimage of it, is to be read into the photo
image identified by the handle *imageHandle*. The subimage of the data
in the file is of dimensions *width* x *height* and has its top-left
corner at coordinates (*srcX*,*srcY*). It is to be stored in the photo
image with its top-left corner at coordinates (*destX*,*destY*) using
the **Tk_PhotoPutBlock** procedure. The return value is a standard Tcl
return value.

## STRINGREADPROC

*formatPtr-\>stringReadProc* provides the address of a procedure for Tk
to call to read data from a string into a photo image.
*formatPtr-\>stringReadProc* must match the following prototype:

    typedef int Tk_ImageStringReadProc(
            Tcl_Interp *interp,
            Tcl_Obj *data,
            Tcl_Obj *format,
            PhotoHandle imageHandle,
            int destX, int destY,
            int width, int height,
            int srcX, int srcY);

The *interp* argument is the interpreter in which the command was
invoked to read the image; it should be used for reporting errors. The
*data* argument points to the image data in object form. The *format*
argument contains the value given for the **-format** option, or NULL if
the option was not specified. The image data in the string, or a
subimage of it, is to be read into the photo image identified by the
handle *imageHandle*. The subimage of the data in the string is of
dimensions *width* x *height* and has its top-left corner at coordinates
(*srcX*,*srcY*). It is to be stored in the photo image with its top-left
corner at coordinates (*destX*,*destY*) using the **Tk_PhotoPutBlock**
procedure. The return value is a standard Tcl return value.

## FILEWRITEPROC

*formatPtr-\>fileWriteProc* provides the address of a procedure for Tk
to call to write data from a photo image to a file.
*formatPtr-\>fileWriteProc* must match the following prototype:

    typedef int Tk_ImageFileWriteProc(
            Tcl_Interp *interp,
            const char *fileName,
            Tcl_Obj *format,
            Tk_PhotoImageBlock *blockPtr);

The *interp* argument is the interpreter in which the command was
invoked to write the image; it should be used for reporting errors. The
image data to be written are in memory and are described by the
Tk_PhotoImageBlock structure pointed to by *blockPtr*; see the manual
page FindPhoto(3) for details. The *fileName* argument points to the
string giving the name of the file in which to write the image data. The
*format* argument contains the value given for the **-format** option,
or NULL if the option was not specified. The format string can contain
extra characters after the name of the format. If appropriate, the
*formatPtr-\>fileWriteProc* procedure may interpret these characters to
specify further details about the image file. The return value is a
standard Tcl return value.

## STRINGWRITEPROC

*formatPtr-\>stringWriteProc* provides the address of a procedure for Tk
to call to translate image data from a photo image into a string.
*formatPtr-\>stringWriteProc* must match the following prototype:

    typedef int Tk_ImageStringWriteProc(
            Tcl_Interp *interp,
            Tcl_Obj *format,
            Tk_PhotoImageBlock *blockPtr);

The *interp* argument is the interpreter in which the command was
invoked to convert the image; it should be used for reporting errors.
The image data to be converted are in memory and are described by the
Tk_PhotoImageBlock structure pointed to by *blockPtr*; see the manual
page FindPhoto(3) for details. The data for the string should be put in
the interpreter *interp* result. The *format* argument contains the
value given for the **-format** option, or NULL if the option was not
specified. The format string can contain extra characters after the name
of the format. If appropriate, the *formatPtr-\>stringWriteProc*
procedure may interpret these characters to specify further details
about the image file. The return value is a standard Tcl return value.

# LEGACY INTERFACE SUPPORT

In Tk 8.2 and earlier, the definition of all the function pointer types
stored in fields of a **Tk_PhotoImageFormat** struct were incompatibly
different. Legacy programs and libraries dating from those days may
still contain code that defines extended Tk photo image formats using
the old interface. The Tk header file will still support this legacy
interface if the code is compiled with the macro **USE_OLD_IMAGE**
defined. Alternatively, the legacy interfaces are used if the first
character of *formatPtr-\>name* is an uppercase ASCII character
(**A**-**Z**), and explicit casts are used to forgive the type mismatch.
For example,

    static Tk_PhotoImageFormat myFormat = {
        "MyFormat",
        (Tk_ImageFileMatchProc *) FileMatch,
        NULL,
        (Tk_ImageFileReadProc *) FileRead,
        NULL,
        NULL,
        NULL
    };

would define a minimal **Tk_PhotoImageFormat** that operates provide
only file reading capability, where **FileMatch** and **FileRead** are
written according to the legacy interfaces of Tk 8.2 or earlier.

Any stub-enabled extension providing an extended photo image format via
the legacy interface enabled by the **USE_OLD_IMAGE** macro that is
compiled against Tk 8.5 headers and linked against the Tk 8.5 stub
library will produce a file that can be loaded only into interps with Tk
8.5 or later; that is, the normal stub-compatibility rules. If a
developer needs to generate from such code a file that is loadable into
interps with Tk 8.4 or earlier, they must use Tk 8.4 headers and stub
libraries to do so.

Any new code written today should not make use of the legacy interfaces.
Expect their support to go away in Tk 9.

# SEE ALSO

Tk_FindPhoto, Tk_PhotoPutBlock

# KEYWORDS

photo image, image file

<!---
Copyright (c) 1994 The Australian National Universit
Copyright (c) 1994-1997 Sun Microsystems, Inc
-->

