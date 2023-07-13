\

# NAME

Tcl_CommandComplete - Check for unmatched braces in a Tcl command

# SYNOPSIS

    #include <tcl.h>

    int
    Tcl_CommandComplete(cmd)

# ARGUMENTS

Command string to test for completeness.

\

# DESCRIPTION

**Tcl_CommandComplete** takes a Tcl command string as argument and
determines whether it contains one or more complete commands (i.e. there
are no unclosed quotes, braces, brackets, or variable references). If
the command string is complete then it returns 1; otherwise it returns
0.

# KEYWORDS

complete command, partial command
