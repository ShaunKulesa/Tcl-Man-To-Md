\

# NAME

Tcl_InitSubsystems - initialize the Tcl library.

# SYNOPSIS

    #include <tcl.h>

    const char *
    Tcl_InitSubsystems(void)

# DESCRIPTION

The **Tcl_InitSubsystems** procedure initializes the Tcl library. This
procedure is typically invoked as the very first thing in the
application\'s main program.

The result of **Tcl_InitSubsystems** is the full Tcl version with build
information (e.g., **9.0.0+abcdef\...abcdef.gcc-1002**).

**Tcl_InitSubsystems** is very similar in use to **Tcl_FindExecutable**.
It can be used when Tcl is used as utility library, no other encodings
than utf-8, iso8859-1 or utf-16 are used, and no interest exists in the
value of **info nameofexecutable**. The system encoding will not be
extracted from the environment, but falls back to utf-8.

# KEYWORDS

binary, executable file
