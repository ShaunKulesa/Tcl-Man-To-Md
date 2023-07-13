\

# NAME

Tcl_SourceRCFile - source the Tcl rc file

# SYNOPSIS

    #include <tcl.h>

    void
    Tcl_SourceRCFile(interp)

# ARGUMENTS

Tcl interpreter to source rc file into.

\

# DESCRIPTION

**Tcl_SourceRCFile** is used to source the Tcl rc file at startup. It is
typically invoked by Tcl_Main or Tk_Main. The name of the file sourced
is obtained from the global variable **tcl_rcFileName** in the
interpreter given by *interp*. If this variable is not defined, or if
the file it indicates cannot be found, no action is taken.

# KEYWORDS

application-specific initialization, main program, rc file
