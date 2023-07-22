# NAME

Tcl_SetErrno, Tcl_GetErrno, Tcl_ErrnoId, Tcl_ErrnoMsg - manipulate errno
to store and retrieve error codes

# SYNOPSIS

**#include \<tcl.h\>**

void **Tcl_SetErrno**(*errorCode*)

int **Tcl_GetErrno**()

const char \* **Tcl_ErrnoId**()

const char \* **Tcl_ErrnoMsg**(*errorCode*)

# ARGUMENTS

A POSIX error code such as **ENOENT**.

# DESCRIPTION

**Tcl_SetErrno** and **Tcl_GetErrno** provide portable access to the
**errno** variable, which is used to record a POSIX error code after
system calls and other operations such as **Tcl_Gets**. These procedures
are necessary because global variable accesses cannot be made across
module boundaries on some platforms.

**Tcl_SetErrno** sets the **errno** variable to the value of the
*errorCode* argument C procedures that wish to return error information
to their callers via **errno** should call **Tcl_SetErrno** rather than
setting **errno** directly.

**Tcl_GetErrno** returns the current value of **errno**. Procedures
wishing to access **errno** should call this procedure instead of
accessing **errno** directly.

**Tcl_ErrnoId** and **Tcl_ErrnoMsg** return string representations of
**errno** values. **Tcl_ErrnoId** returns a machine-readable textual
identifier such as that corresponds to the current value of **errno**.
**Tcl_ErrnoMsg** returns a human-readable string such as that
corresponds to the value of its *errorCode* argument. The *errorCode*
argument is typically the value returned by **Tcl_GetErrno**. The
strings returned by these functions are statically allocated and the
caller must not free or modify them.

# KEYWORDS

errno, error code, global variables
