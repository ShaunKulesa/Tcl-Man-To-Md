\

# NAME

Tcl_NRCreateCommand, Tcl_NRCallObjProc, Tcl_NREvalObj, Tcl_NREvalObjv,
Tcl_NRCmdSwap, Tcl_NRExprObj, Tcl_NRAddCallback - Non-Recursive
(stackless) evaluation of Tcl scripts.

# SYNOPSIS

    #include <tcl.h>

    Tcl_Command
    Tcl_NRCreateCommand(interp, cmdName, proc, nreProc, clientData,
                        deleteProc)

    int
    Tcl_NRCallObjProc(interp, nreProc, clientData, objc, objv)

    int
    Tcl_NREvalObj(interp, objPtr, flags)

    int
    Tcl_NREvalObjv(interp, objc, objv, flags)

    int
    Tcl_NRCmdSwap(interp, cmd, objc, objv, flags)

    int
    Tcl_NRExprObj(interp, objPtr, resultPtr)

    void
    Tcl_NRAddCallback(interp, postProcPtr, data0, data1, data2, data3)

# ARGUMENTS

The relevant Interpreter.

Name of the command to create.

Called in order to evaluate a command. Is often just a small wrapper
that uses **Tcl_NRCallObjProc** to call *nreProc* using a new
trampoline. Behaves in the same way as the *proc* argument to
**Tcl_CreateObjCommand**(3) (*q.v.*).

Called instead of *proc* when a trampoline is already in use.

Arbitrary one-word value passed to *proc*, *nreProc*, *deleteProc* and
*objProc*.

Called before *cmdName* is deleted from the interpreter, allowing for
command-specific cleanup. May be NULL.

Number of items in *objv*.

Words in the command.

A script or expression to evaluate.

As described for *Tcl_EvalObjv*.

Token to use instead of one derived from the first word of *objv* in
order to evaluate a command.

Pointer to an unshared Tcl_Obj where the result of the evaluation is
stored if the return code is TCL_OK.

A function to push.

*data0* through *data3* are four one-word values that will be passed to
the function designated by *postProcPtr* when it is invoked.

\

# DESCRIPTION

These functions provide an interface to the function stack that an
interpreter iterates through to evaluate commands. The routine behind a
command is implemented by an initial function and any additional
functions that the routine pushes onto the stack as it progresses. The
interpreter itself pushes functions onto the stack to react to the end
of a routine and to exercise other forms of control such as switching
between in-progress stacks and the evaluation of other scripts at
additional levels without adding frames to the C stack. To execute a
routine, the initial function for the routine is called and then a small
bit of code called a *trampoline* iteratively takes functions off the
stack and calls them, using the value of the last call as the value of
the routine.

**Tcl_NRCallObjProc** calls *nreProc* using a new trampoline.

**Tcl_NRCreateCommand**, an alternative to **Tcl_CreateObjCommand**,
resolves *cmdName*, which may contain namespace qualifiers, relative to
the current namespace, creates a command by that name, and returns a
token for the command which may be used in subsequent calls to
**Tcl_GetCommandName**. Except for a few cases noted below any existing
command by the same name is first deleted. If *interp* is in the process
of being deleted **Tcl_NRCreateCommand** does not create any command,
does not delete any command, and returns NULL.

**Tcl_NREvalObj** pushes a function that is like **Tcl_EvalObjEx** but
consumes no space on the C stack.

**Tcl_NREvalObjv** pushes a function that is like **Tcl_EvalObjv** but
consumes no space on the C stack.

**Tcl_NRCmdSwap** is like **Tcl_NREvalObjv**, but uses *cmd*, a token
previously returned by **Tcl_CreateObjCommand** or
**Tcl_GetCommandFromObj**, instead of resolving the first word of
*objv*.

**Tcl_NRExprObj** pushes a function that evaluates *objPtr* as an
expression in the same manner as **Tcl_ExprObj** but without consuming
space on the C stack.

All of the functions return **TCL_OK** if the evaluation of the script,
command, or expression has been scheduled successfully. Otherwise (for
example if the command name cannot be resolved), they return
**TCL_ERROR** and store a message as the interpreter\'s result.

**Tcl_NRAddCallback** pushes *postProcPtr*. The signature for
**Tcl_NRPostProc** is:

    typedef int
    Tcl_NRPostProc(
            ClientData data[],
            Tcl_Interp *interp,
            int result);

*data* is a pointer to an array containing *data0* through *data3*.
*result* is the value returned by the previous function implementing
part the routine.

# EXAMPLE

The following command uses **Tcl_EvalObjEx**, which consumes space on
the C stack, to evalute a script:

    int
    TheCmdOldObjProc(
        ClientData clientData,
        Tcl_Interp *interp,
        int objc,
        Tcl_Obj *const objv[])
    {
        int result;
        Tcl_Obj *objPtr;

        ... preparation ...

        result = Tcl_EvalObjEx(interp, objPtr, 0);

        ... postprocessing ...

        return result;
    }
    Tcl_CreateObjCommand(interp, "theCommand",
            TheCmdOldObjProc, clientData, TheCmdDeleteProc);

To avoid consuming space on the C stack, *TheCmdOldObjProc* is renamed
to *TheCmdNRObjProc* and the postprocessing step is split into a
separate function, *TheCmdPostProc*, which is pushed onto the function
stack. *Tcl_EvalObjEx* is replaced with *Tcl_NREvalObj*, which uses a
trampoline instead of consuming space on the C stack. A new version of
*TheCmdOldObjProc* is just a a wrapper that uses **Tcl_NRCallObjProc**
to call *TheCmdNRObjProc*:

    int
    TheCmdOldObjProc(
        ClientData clientData,
        Tcl_Interp *interp,
        int objc,
        Tcl_Obj *const objv[])
    {
        return Tcl_NRCallObjProc(interp, TheCmdNRObjProc,
                clientData, objc, objv);
    }

    int
    TheCmdNRObjProc
        ClientData clientData,
        Tcl_Interp *interp,
        int objc,
        Tcl_Obj *const objv[])
    {
        Tcl_Obj *objPtr;

        ... preparation ...

        Tcl_NRAddCallback(interp, TheCmdPostProc,
                data0, data1, data2, data3);
        /* data0 .. data3 are up to four one-word items to
         * pass to the postprocessing procedure */

        return Tcl_NREvalObj(interp, objPtr, 0);
    }

    int
    TheCmdNRPostProc(
        ClientData data[],
        Tcl_Interp *interp,
        int result)
    {
        /* data[0] .. data[3] are the four words of data
         * passed to Tcl_NRAddCallback */

        ... postprocessing ...

        return result;
    }

Any function comprising a routine can push other functions, making it
possible implement looping and sequencing constructs using the function
stack.

# SEE ALSO

Tcl_CreateCommand(3), Tcl_CreateObjCommand(3), Tcl_EvalObjEx(3),
Tcl_GetCommandFromObj(3), Tcl_ExprObj(3)

# KEYWORDS

stackless, nonrecursive, execute, command, global, value, result, script

# COPYRIGHT

Copyright © 2008 Kevin B. Kenny. Copyright © 2018 Nathan Coulter.
