\

# NAME

throw - Generate a machine-readable error

# SYNOPSIS

**throw*** type message*

\

# DESCRIPTION

This command causes the current evaluation to be unwound with an error.
The error created is described by the *type* and *message* arguments:
*type* must contain a list of words describing the error in a form that
is machine-readable (and which will form the error-code part of the
result dictionary), and *message* should contain text that is intended
for display to a human being.

The stack will be unwound until the error is trapped by a suitable
**catch** or **try** command. If it reaches the event loop without being
trapped, it will be reported through the **bgerror** mechanism. If it
reaches the top level of script evaluation in **tclsh**, it will be
printed on the console before, in the non-interactive case, causing an
exit (the behavior in other programs will depend on the details of how
Tcl is embedded and used).

By convention, the words in the *type* argument should go from most
general to most specific.

# EXAMPLES

The following produces an error that is identical to that produced by
**expr** when trying to divide a value by zero.

    throw {ARITH DIVZERO {divide by zero}} {divide by zero}

# SEE ALSO

catch(n), error(n), errorCode(n), errorInfo(n), return(n), try(n)

# KEYWORDS

error, exception
