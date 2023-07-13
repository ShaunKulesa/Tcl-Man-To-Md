\

# NAME

Tcl_WrongNumArgs - generate standard error message for wrong number of
arguments

# SYNOPSIS

    #include <tcl.h>

    Tcl_WrongNumArgs(interp, objc, objv, message)

# ARGUMENTS

Interpreter in which error will be reported: error message gets stored
in its result value.

Number of leading arguments from *objv* to include in error message.

Arguments to command that had the wrong number of arguments.

Additional error information to print after leading arguments from
*objv*. This typically gives the acceptable syntax of the command. This
argument may be NULL.

\

# DESCRIPTION

**Tcl_WrongNumArgs** is a utility procedure that is invoked by command
procedures when they discover that they have received the wrong number
of arguments. **Tcl_WrongNumArgs** generates a standard error message
and stores it in the result value of *interp*. The message includes the
*objc* initial elements of *objv* plus *message*. For example, if *objv*
consists of the values **foo** and **bar**, *objc* is 1, and *message*
is then *interp*\'s result value will be set to the following string:

    wrong # args: should be "foo fileName count"

If *objc* is 2, the result will be set to the following string:

    wrong # args: should be "foo bar fileName count"

*Objc* is usually 1, but may be 2 or more for commands like **string**
and the Tk widget commands, which use the first argument as a
subcommand.

Some of the values in the *objv* array may be abbreviations for a
subcommand. The command **Tcl_GetIndexFromObj** will convert the
abbreviated string value into an *indexObject*. If an error occurs in
the parsing of the subcommand we would like to use the full subcommand
name rather than the abbreviation. If the **Tcl_WrongNumArgs** command
finds any *indexObjects* in the *objv* array it will use the full
subcommand name in the error message instead of the abbreviated name
that was originally passed in. Using the above example, let us assume
that *bar* is actually an abbreviation for *barfly* and the value is now
an *indexObject* because it was passed to **Tcl_GetIndexFromObj**. In
this case the error message would be:

    wrong # args: should be "foo barfly fileName count"

# SEE ALSO

Tcl_GetIndexFromObj(3)

# KEYWORDS

command, error message, wrong number of arguments
