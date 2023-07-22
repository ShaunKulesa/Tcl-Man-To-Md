# NAME

Tk_ParseArgv - process command-line options

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_ParseArgv**(*interp, tkwin, argcPtr, argv, argTable, flags*)

# ARGUMENTS

Interpreter to use for returning error messages.

Window to use when arguments specify Tk options. If NULL, then no Tk
options will be processed.

Pointer to number of arguments in argv; gets modified to hold number of
unprocessed arguments that remain after the call.

Command line arguments passed to main program. Modified to hold
unprocessed arguments that remain after the call.

Array of argument descriptors, terminated by element with type
**TK_ARGV_END**.

If non-zero, then it specifies one or more flags that control the
parsing of arguments. Different flags may be OR\'ed together. The flags
currently defined are **TK_ARGV_DONT_SKIP_FIRST_ARG**,
**TK_ARGV_NO_ABBREV**, **TK_ARGV_NO_LEFTOVERS**, and
**TK_ARGV_NO_DEFAULTS**.

# DESCRIPTION

**Tk_ParseArgv** processes an array of command-line arguments according
to a table describing the kinds of arguments that are expected. Each of
the arguments in *argv* is processed in turn: if it matches one of the
entries in *argTable*, the argument is processed according to that entry
and discarded. The arguments that do not match anything in *argTable*
are copied down to the beginning of *argv* (retaining their original
order) and returned to the caller. At the end of the call
**Tk_ParseArgv** sets *\*argcPtr* to hold the number of arguments that
are left in *argv*, and *argv\[\*argcPtr\]* will hold the value NULL.
Normally, **Tk_ParseArgv** assumes that *argv\[0\]* is a command name,
so it is treated like an argument that does not match *argTable* and
returned to the caller; however, if the **TK_ARGV_DONT_SKIP_FIRST_ARG**
bit is set in *flags* then *argv\[0\]* will be processed just like the
other elements of *argv*.

**Tk_ParseArgv** normally returns the value **TCL_OK**. If an error
occurs while parsing the arguments, then **TCL_ERROR** is returned and
**Tk_ParseArgv** will leave an error message in the result of
interpreter *interp* in the standard Tcl fashion. In the event of an
error return, *\*argvPtr* will not have been modified, but *argv* could
have been partially modified. The possible causes of errors are
explained below.

The *argTable* array specifies the kinds of arguments that are expected;
each of its entries has the following structure:

    typedef struct {
        const char *key;
        int type;
        char *src;
        char *dst;
        const char *help;
    } Tk_ArgvInfo;

The *key* field is a string such as or that is compared with the values
in *argv*. *Type* indicates how to process an argument that matches
*key* (more on this below). *Src* and *dst* are additional values used
in processing the argument. Their exact usage depends on *type*, but
typically *src* indicates a value and *dst* indicates where to store the
value. The **char \*** declarations for *src* and *dst* are
placeholders: the actual types may be different. Lastly, *help* is a
string giving a brief description of this option; this string is printed
when users ask for help about command-line options.

When processing an argument in *argv*, **Tk_ParseArgv** compares the
argument to each of the *key*\'s in *argTable*. **Tk_ParseArgv** selects
the first specifier whose *key* matches the argument exactly, if such a
specifier exists. Otherwise **Tk_ParseArgv** selects a specifier for
which the argument is a unique abbreviation. If the argument is a unique
abbreviation for more than one specifier, then an error is returned. If
there is no matching entry in *argTable*, then the argument is skipped
and returned to the caller.

Once a matching argument specifier is found, **Tk_ParseArgv** processes
the argument according to the *type* field of the specifier. The
argument that matched *key* is called in the descriptions below. As part
of the processing, **Tk_ParseArgv** may also use the next argument in
*argv* after the matching argument, which is called The legal values for
*type*, and the processing that they cause, are as follows:

**TK_ARGV_END**

:   Marks the end of the table. The last entry in *argTable* must have
    this type; all of its other fields are ignored and it will never
    match any arguments.

**TK_ARGV_CONSTANT**

:   *Src* is treated as an integer and *dst* is treated as a pointer to
    an integer. *Src* is stored at *\*dst*. The matching argument is
    discarded.

**TK_ARGV_INT**

:   The following argument must contain an integer string in the format
    accepted by **strtol** (e.g. and prefixes may be used to specify
    octal or hexadecimal numbers, respectively). *Dst* is treated as a
    pointer to an integer; the following argument is converted to an
    integer value and stored at *\*dst*. *Src* is ignored. The matching
    and following arguments are discarded from *argv*.

**TK_ARGV_FLOAT**

:   The following argument must contain a floating-point number in the
    format accepted by **strtol**. *Dst* is treated as the address of a
    double-precision floating point value; the following argument is
    converted to a double-precision value and stored at *\*dst*. The
    matching and following arguments are discarded from *argv*.

**TK_ARGV_STRING**

:   In this form, *dst* is treated as a pointer to a (char \*);
    **Tk_ParseArgv** stores at *\*dst* a pointer to the following
    argument, and discards the matching and following arguments from
    *argv*. *Src* is ignored.

**TK_ARGV_UID**

:   This form is similar to **TK_ARGV_STRING**, except that the argument
    is turned into a Tk_Uid by calling **Tk_GetUid**. *Dst* is treated
    as a pointer to a Tk_Uid; **Tk_ParseArgv** stores at *\*dst* the
    Tk_Uid corresponding to the following argument, and discards the
    matching and following arguments from *argv*. *Src* is ignored.

**TK_ARGV_CONST_OPTION**

:   This form causes a Tk option to be set (as if the **option** command
    had been invoked). The *src* field is treated as a pointer to a
    string giving the value of an option, and *dst* is treated as a
    pointer to the name of the option. The matching argument is
    discarded. If *tkwin* is NULL, then argument specifiers of this type
    are ignored (as if they did not exist).

**TK_ARGV_OPTION_VALUE**

:   This form is similar to **TK_ARGV_CONST_OPTION**, except that the
    value of the option is taken from the following argument instead of
    from *src*. *Dst* is used as the name of the option. *Src* is
    ignored. The matching and following arguments are discarded. If
    *tkwin* is NULL, then argument specifiers of this type are ignored
    (as if they did not exist).

**TK_ARGV_OPTION_NAME_VALUE**

:   In this case the following argument is taken as the name of a Tk
    option and the argument after that is taken as the value for that
    option. Both *src* and *dst* are ignored. All three arguments are
    discarded from *argv*. If *tkwin* is NULL, then argument specifiers
    of this type are ignored (as if they did not exist).

**TK_ARGV_HELP**

:   When this kind of option is encountered, **Tk_ParseArgv** uses the
    *help* fields of *argTable* to format a message describing all the
    valid arguments. The message is placed in interpreter *interp*\'s
    result and **Tk_ParseArgv** returns **TCL_ERROR**. When this
    happens, the caller normally prints the help message and aborts. If
    the *key* field of a **TK_ARGV_HELP** specifier is NULL, then the
    specifier will never match any arguments; in this case the specifier
    simply provides extra documentation, which will be included when
    some other **TK_ARGV_HELP** entry causes help information to be
    returned.

**TK_ARGV_REST**

:   This option is used by programs or commands that allow the last
    several of their options to be the name and/or options for some
    other program. If a **TK_ARGV_REST** argument is found, then
    **Tk_ParseArgv** does not process any of the remaining arguments; it
    returns them all at the beginning of *argv* (along with any other
    unprocessed arguments). In addition, **Tk_ParseArgv** treats *dst*
    as the address of an integer value, and stores at *\*dst* the index
    of the first of the **TK_ARGV_REST** options in the returned *argv*.
    This allows the program to distinguish the **TK_ARGV_REST** options
    from other unprocessed options that preceded the **TK_ARGV_REST**.

**TK_ARGV_FUNC**

:   For this kind of argument, *src* is treated as the address of a
    procedure, which is invoked to process the following argument. The
    procedure should have the following structure:

        int
        func(dst, key, nextArg)
            char *dst;
            char *key;
            char *nextArg;
        {
        }

    The *dst* and *key* parameters will contain the corresponding fields
    from the *argTable* entry, and *nextArg* will point to the following
    argument from *argv* (or NULL if there are not any more arguments
    left in *argv*). If *func* uses *nextArg* (so that **Tk_ParseArgv**
    should discard it), then it should return 1. Otherwise it should
    return 0 and **TkParseArgv** will process the following argument in
    the normal fashion. In either event the matching argument is
    discarded.

**TK_ARGV_GENFUNC**

:   This form provides a more general procedural escape. It treats *src*
    as the address of a procedure, and passes that procedure all of the
    remaining arguments. The procedure should have the following form:

        int
        genfunc(dst, interp, key, argc, argv)
            char *dst;
            Tcl_Interp *interp;
            char *key;
            int argc;
            char **argv;
        {
        }

    The *dst* and *key* parameters will contain the corresponding fields
    from the *argTable* entry. *Interp* will be the same as the *interp*
    argument to **Tcl_ParseArgv**. *Argc* and *argv* refer to all of the
    options after the matching one. *Genfunc* should behave in a fashion
    similar to **Tk_ParseArgv**: parse as many of the remaining
    arguments as it can, then return any that are left by compacting
    them to the beginning of *argv* (starting at *argv*\[0\]). *Genfunc*
    should return a count of how many arguments are left in *argv*;
    **Tk_ParseArgv** will process them. If *genfunc* encounters an error
    then it should leave an error message in interpreter *interp*\'s
    result, in the usual Tcl fashion, and return -1; when this happens
    **Tk_ParseArgv** will abort its processing and return **TCL_ERROR**.

## FLAGS

**TK_ARGV_DONT_SKIP_FIRST_ARG**

:   **Tk_ParseArgv** normally treats *argv\[0\]* as a program or command
    name, and returns it to the caller just as if it had not matched
    *argTable*. If this flag is given, then *argv\[0\]* is not given
    special treatment.

**TK_ARGV_NO_ABBREV**

:   Normally, **Tk_ParseArgv** accepts unique abbreviations for *key*
    values in *argTable*. If this flag is given then only exact matches
    will be acceptable.

**TK_ARGV_NO_LEFTOVERS**

:   Normally, **Tk_ParseArgv** returns unrecognized arguments to the
    caller. If this bit is set in *flags* then **Tk_ParseArgv** will
    return an error if it encounters any argument that does not match
    *argTable*. The only exception to this rule is *argv\[0\]*, which
    will be returned to the caller with no errors as long as
    **TK_ARGV_DONT_SKIP_FIRST_ARG** is not specified.

**TK_ARGV_NO_DEFAULTS**

:   Normally, **Tk_ParseArgv** searches an internal table of standard
    argument specifiers in addition to *argTable*. If this bit is set in
    *flags*, then **Tk_ParseArgv** will use only *argTable* and not its
    default table.

# EXAMPLE

Here is an example definition of an *argTable* and some sample command
lines that use the options. Note the effect on *argc* and *argv*;
arguments processed by **Tk_ParseArgv** are eliminated from *argv*, and
*argc* is updated to reflect reduced number of arguments.

    /*
     * Define and set default values for globals.
     */
    int debugFlag = 0;
    int numReps = 100;
    char defaultFileName[] = "out";
    char *fileName = defaultFileName;
    Boolean exec = FALSE;

    /*
     * Define option descriptions.
     */
    Tk_ArgvInfo argTable[] = {
        {"-X", TK_ARGV_CONSTANT, (char *) 1, (char *) &debugFlag,
            "Turn on debugging printfs"},
        {"-N", TK_ARGV_INT, NULL, (char *) &numReps,
            "Number of repetitions"},
        {"-of", TK_ARGV_STRING, NULL, (char *) &fileName,
            "Name of file for output"},
        {"x", TK_ARGV_REST, NULL, (char *) &exec,
            "File to exec, followed by any arguments (must be last argument)."},
        {NULL, TK_ARGV_END, NULL, NULL,
            NULL}
    };

    main(argc, argv)
        int argc;
        char *argv[];
    {
        ...

        if (Tk_ParseArgv(interp, tkwin, &argc, argv, argTable, 0) != TCL_OK) {
            fprintf(stderr, "%s\n", Tcl_GetString(Tcl_GetObjResult(interp)));
            exit(1);
        }

        /*
         * Remainder of the program.
         */
    }

Note that default values can be assigned to variables named in
*argTable*: the variables will only be overwritten if the particular
arguments are present in *argv*. Here are some example command lines and
their effects.

    prog -N 200 infile        # just sets the numReps variable to 200
    prog -of out200 infile    # sets fileName to reference "out200"
    prog -XN 10 infile        # sets the debug flag, also sets numReps

In all of the above examples, *argc* will be set by **Tk_ParseArgv** to
2, *argv*\[0\] will be *argv*\[1\] will be and *argv*\[2\] will be NULL.

# KEYWORDS

arguments, command line, options
