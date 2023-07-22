# NAME

Tcl_OOInitStubs - initialize library access to TclOO functionality

# SYNOPSIS

**#include \<tclOO.h\>**

const char \* **Tcl_OOInitStubs**(*interp*)

# ARGUMENTS

The Tcl interpreter that the TclOO API is integrated with and whose C
interface is going to be used.

# DESCRIPTION

When an extension library is going to use the C interface exposed by
TclOO, it should use **Tcl_OOInitStubs** to initialize its access to
that interface from within its *\****\_Init** (or *\****\_SafeInit**)
function, passing in the *interp* that was passed into that routine as
context. If the result of calling **Tcl_OOInitStubs** is NULL, the
initialization failed and an error message will have been left in the
interpreter\'s result. Otherwise, the initialization succeeded and the
TclOO API may thereafter be used; the version of the TclOO API is
returned.

When using this function, either the C #define symbol
**USE_TCLOO_STUBS** should be defined and your library code linked
against the Tcl stub library, or that #define symbol should *not* be
defined and your library code linked against the Tcl main library
directly.

# BACKWARD COMPATIBILITY NOTE

If you are linking against the Tcl 8.5 forward compatibility package for
TclOO, *only* the stub-enabled configuration is supported and you should
also link against the TclOO independent stub library; that library is an
integrated part of the main Tcl stub library in Tcl 8.6.

# KEYWORDS

stubs

# SEE ALSO

Tcl_InitStubs(3)

<!---
Copyright (c) 2012 Donal K. Fellow
-->

