# NAME

Tcl_SplitPath, Tcl_JoinPath, Tcl_GetPathType - manipulate
platform-dependent file paths

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_SplitPath**(*path, argcPtr, argvPtr*)

char \* **Tcl_JoinPath**(*argc, argv, resultPtr*)

Tcl_PathType **Tcl_GetPathType**(*path*)

# ARGUMENTS

File path in a form appropriate for the current platform (see the
**filename** manual entry for acceptable forms for path names).

Filled in with number of path elements in *path*.

*\*argvPtr* will be filled in with the address of an array of pointers
to the strings that are the extracted elements of *path*. There will be
*\*argcPtr* valid entries in the array, followed by a NULL entry.

Number of elements in *argv*.

Array of path elements to merge together into a single path.

A pointer to an initialized **Tcl_DString** to which the result of
**Tcl_JoinPath** will be appended.

# DESCRIPTION

These procedures have been superseded by the Tcl-value-aware procedures
in the **FileSystem** man page, which are more efficient.

These procedures may be used to disassemble and reassemble file paths in
a platform independent manner: they provide C-level access to the same
functionality as the **file split**, **file join**, and **file
pathtype** commands.

**Tcl_SplitPath** breaks a path into its constituent elements, returning
an array of pointers to the elements using *argcPtr* and *argvPtr*. The
area of memory pointed to by *\*argvPtr* is dynamically allocated; in
addition to the array of pointers, it also holds copies of all the path
elements. It is the caller\'s responsibility to free all of this
storage. For example, suppose that you have called **Tcl_SplitPath**
with the following code:

    int argc;
    char *path;
    char **argv;
    ...
    Tcl_SplitPath(string, &argc, &argv);

Then you should eventually free the storage with a call like the
following:

    Tcl_Free((char *) argv);

**Tcl_JoinPath** is the inverse of **Tcl_SplitPath**: it takes a
collection of path elements given by *argc* and *argv* and generates a
result string that is a properly constructed path. The result string is
appended to *resultPtr*. *ResultPtr* must refer to an initialized
**Tcl_DString**.

If the result of **Tcl_SplitPath** is passed to **Tcl_JoinPath**, the
result will refer to the same location, but may not be in the same form.
This is because **Tcl_SplitPath** and **Tcl_JoinPath** eliminate
duplicate path separators and return a normalized form for each
platform.

**Tcl_GetPathType** returns the type of the specified *path*, where
**Tcl_PathType** is one of **TCL_PATH_ABSOLUTE**, **TCL_PATH_RELATIVE**,
or **TCL_PATH_VOLUME_RELATIVE**. See the **filename** manual entry for a
description of the path types for each platform.

# KEYWORDS

file, filename, join, path, split, type

<!---
Copyright (c) 1996 Sun Microsystems, Inc
-->

