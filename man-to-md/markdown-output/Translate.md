# NAME

Tcl_TranslateFileName - convert file name to native form and replace
tilde with home directory

# SYNOPSIS

**#include \<tcl.h\>**

char \* **Tcl_TranslateFileName**(*interp*, *name*, *bufferPtr*)

# ARGUMENTS

Interpreter in which to report an error, if any.

File name, which may start with a

If needed, this dynamic string is used to store the new file name. At
the time of the call it should be uninitialized or free. The caller must
eventually call **Tcl_DStringFree** to free up anything stored here.

# DESCRIPTION

This utility procedure translates a file name to a platform-specific
form which, after being converted to the appropriate encoding, is
suitable for passing to the local operating system. In particular, it
converts network names into native form and does tilde substitution.

However, with the advent of the newer **Tcl_FSGetNormalizedPath** and
**Tcl_FSGetNativePath**, there is no longer any need to use this
procedure. In particular, **Tcl_FSGetNativePath** performs all the
necessary translation and encoding conversion, is virtual-filesystem
aware, and caches the native result for faster repeated calls. Finally
**Tcl_FSGetNativePath** does not require you to free anything
afterwards.

If **Tcl_TranslateFileName** has to do tilde substitution or translate
the name then it uses the dynamic string at *\*bufferPtr* to hold the
new string it generates. After **Tcl_TranslateFileName** returns a
non-NULL result, the caller must eventually invoke **Tcl_DStringFree**
to free any information placed in *\*bufferPtr*. The caller need not
know whether or not **Tcl_TranslateFileName** actually used the string;
**Tcl_TranslateFileName** initializes *\*bufferPtr* even if it does not
use it, so the call to **Tcl_DStringFree** will be safe in either case.

If an error occurs (e.g. because there was no user by the given name)
then NULL is returned and an error message will be left in the
interpreter\'s result. When an error occurs, **Tcl_TranslateFileName**
frees the dynamic string itself so that the caller need not call
**Tcl_DStringFree**.

The caller is responsible for making sure that the interpreter\'s result
has its default empty value when **Tcl_TranslateFileName** is invoked.

# SEE ALSO

filename(n)

# KEYWORDS

file name, home directory, tilde, translate, user

<!---
Copyright (c) 1989-1993 The Regents of the University of California
Copyright (c) 1994-1998 Sun Microsystems, Inc
-->

