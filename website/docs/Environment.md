\

# NAME

Tcl_PutEnv - procedures to manipulate the environment

# SYNOPSIS

    #include <tcl.h>

    int
    Tcl_PutEnv(assignment)

# ARGUMENTS

Info about environment variable in the format The *assignment* argument
is in the system encoding.

\

# DESCRIPTION

**Tcl_PutEnv** sets an environment variable. The information is passed
in a single string of the form This procedure is intended to be a
stand-in for the UNIX **putenv** system call. All Tcl-based applications
using **putenv** should redefine it to **Tcl_PutEnv** so that they will
interface properly to the Tcl runtime.

# SEE ALSO

env(n)

# KEYWORDS

environment, variable
