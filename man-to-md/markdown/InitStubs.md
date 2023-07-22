# NAME

Tcl_InitStubs - initialize the Tcl stubs mechanism

# SYNOPSIS

**#include \<tcl.h\>**

const char \* **Tcl_InitStubs**(*interp, version, exact*)

# ARGUMENTS

Tcl interpreter handle.

A version string consisting of one or more decimal numbers separated by
dots.

Non-zero means that only the particular version specified by *version*
is acceptable. Zero means that versions newer than *version* are also
acceptable as long as they have the same major version number as
*version*.

# INTRODUCTION

The Tcl stubs mechanism defines a way to dynamically bind extensions to
a particular Tcl implementation at run time. This provides two
significant benefits to Tcl users:

1)  Extensions that use the stubs mechanism can be loaded into multiple
    versions of Tcl without being recompiled or relinked.

2)  Extensions that use the stubs mechanism can be dynamically loaded
    into statically-linked Tcl applications.

The stubs mechanism accomplishes this by exporting function tables that
define an interface to the Tcl API. The extension then accesses the Tcl
API through offsets into the function table, so there are no direct
references to any of the Tcl library\'s symbols. This redirection is
transparent to the extension, so an extension writer can continue to use
all public Tcl functions as documented.

The stubs mechanism requires no changes to applications incorporating
Tcl interpreters. Only developers creating C-based Tcl extensions need
to take steps to use the stubs mechanism with their extensions.

Enabling the stubs mechanism for an extension requires the following
steps:

1)  Call **Tcl_InitStubs** in the extension before calling any other Tcl
    functions.

2)  Define the **USE_TCL_STUBS** symbol. Typically, you would include
    the **-DUSE_TCL_STUBS** flag when compiling the extension.

3)  Link the extension with the Tcl stubs library instead of the
    standard Tcl library. For example, to use the Tcl 8.6 ABI on Unix
    platforms, the library name is *libtclstub8.6.a*; on Windows
    platforms, the library name is *tclstub86.lib*.

If the extension also requires the Tk API, it must also call
**Tk_InitStubs** to initialize the Tk stubs interface and link with the
Tk stubs libraries. See the **Tk_InitStubs** page for more information.

# DESCRIPTION

**Tcl_InitStubs** attempts to initialize the stub table pointers and
ensure that the correct version of Tcl is loaded. In addition to an
interpreter handle, it accepts as arguments a version number and a
Boolean flag indicating whether the extension requires an exact version
match or not. If *exact* is 0, then the extension is indicating that
newer versions of Tcl are acceptable as long as they have the same major
version number as *version*; non-zero means that only the specified
*version* is acceptable. **Tcl_InitStubs** returns a string containing
the actual version of Tcl satisfying the request, or NULL if the Tcl
version is not acceptable, does not support stubs, or any other error
condition occurred.

# SEE ALSO

Tk_InitStubs

# KEYWORDS

stubs

<!---
Copyright (c) 1998-1999 Scriptics Corporatio
-->

