\

# NAME

Tcl_Init - find and source initialization script

# SYNOPSIS

    #include <tcl.h>

    int
    Tcl_Init(interp)

# ARGUMENTS

Interpreter to initialize.

\

# DESCRIPTION

**Tcl_Init** is a helper procedure that finds and **source**s the
**init.tcl** script, which should exist somewhere on the Tcl library
path.

**Tcl_Init** is typically called from **Tcl_AppInit** procedures.

# SEE ALSO

Tcl_AppInit, Tcl_Main

# KEYWORDS

application, initialization, interpreter
