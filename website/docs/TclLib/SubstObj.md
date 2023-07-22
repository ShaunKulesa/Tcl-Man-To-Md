# NAME

Tcl_SubstObj - perform substitutions on Tcl values

# SYNOPSIS

**#include \<tcl.h\>**

Tcl_Obj \* **Tcl_SubstObj**(*interp, objPtr, flags*)

# ARGUMENTS

Interpreter in which to execute Tcl scripts and lookup variables. If an
error occurs, the interpreter\'s result is modified to hold an error
message.

A Tcl value containing the string to perform substitutions on.

ORed combination of flag bits that specify which substitutions to
perform. The flags **TCL_SUBST_COMMANDS**, **TCL_SUBST_VARIABLES** and
**TCL_SUBST_BACKSLASHES** are currently supported, and **TCL_SUBST_ALL**
is provided as a convenience for the common case where all substitutions
are desired.

# DESCRIPTION

The **Tcl_SubstObj** function is used to perform substitutions on
strings in the fashion of the **subst** command. It gets the value of
the string contained in *objPtr* and scans it, copying characters and
performing the chosen substitutions as it goes to an output value which
is returned as the result of the function. In the event of an error
occurring during the execution of a command or variable substitution,
the function returns NULL and an error message is left in *interp*\'s
result.

Three kinds of substitutions are supported. When the
**TCL_SUBST_BACKSLASHES** bit is set in *flags*, sequences that look
like backslash substitutions for Tcl commands are replaced by their
corresponding character.

When the **TCL_SUBST_VARIABLES** bit is set in *flags*, sequences that
look like variable substitutions for Tcl commands are replaced by the
contents of the named variable.

When the **TCL_SUBST_COMMANDS** bit is set in *flags*, sequences that
look like command substitutions for Tcl commands are replaced by the
result of evaluating that script. Where an uncaught occurs during the
evaluation of a command substitution, an empty string is substituted for
the command. Where an uncaught occurs during the evaluation of a command
substitution, the result of the whole substitution on *objPtr* will be
truncated at the point immediately before the start of the command
substitution, and no characters will be added to the result or
substitutions performed after that point.

# SEE ALSO

subst(n)

# KEYWORDS

backslash substitution, command substitution, variable substitution
