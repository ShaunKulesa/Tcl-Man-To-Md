\

# NAME

Tcl_CancelEval, Tcl_Canceled - cancel Tcl scripts

# SYNOPSIS

    #include <tcl.h>
    int
    Tcl_CancelEval(interp, resultObjPtr, clientData, flags)

    int
    Tcl_Canceled(interp, flags)

# ARGUMENTS

Interpreter in which to cancel the script.

Error message to use in the cancellation, or NULL to use a default
message. If not NULL, this object will have its reference count
decremented before **Tcl_CancelEval** returns.

ORed combination of flag bits that specify additional options. For
**Tcl_CancelEval**, only **TCL_CANCEL_UNWIND** is currently supported.
For **Tcl_Canceled**, only **TCL_LEAVE_ERR_MSG** and
**TCL_CANCEL_UNWIND** are currently supported.

Currently reserved for future use. It should be set to NULL.

\

# DESCRIPTION

**Tcl_CancelEval** cancels or unwinds the script in progress soon after
the next invocation of asynchronous handlers, causing **TCL_ERROR** to
be the return code for that script. This function is thread-safe and may
be called from any thread in the process.

**Tcl_Canceled** checks if the script in progress has been canceled and
returns **TCL_ERROR** if it has. Otherwise, **TCL_OK** is returned.
Extensions can use this function to check to see if they should abort a
long running command. This function is thread sensitive and may only be
called from the thread the interpreter was created in.

## FLAG BITS

Any ORed combination of the following values may be used for the *flags*
argument to procedures such as **Tcl_CancelEval**:

**TCL_CANCEL_UNWIND**

:   This flag is used by **Tcl_CancelEval** and **Tcl_Canceled**. For
    **Tcl_CancelEval**, if this flag is set, the script in progress is
    canceled and the evaluation stack for the interpreter is unwound.
    For **Tcl_Canceled**, if this flag is set, the script in progress is
    considered to be canceled only if the evaluation stack for the
    interpreter is being unwound.

**TCL_LEAVE_ERR_MSG**

:   This flag is only used by **Tcl_Canceled**; it is ignored by other
    procedures. If an error is returned and this bit is set in *flags*,
    then an error message will be left in the interpreter\'s result,
    where it can be retrieved with **Tcl_GetObjResult** or
    **Tcl_GetStringResult**. If this flag bit is not set then no error
    message is left and the interpreter\'s result will not be modified.

# SEE ALSO

interp(n), Tcl_Eval(3), TIP 285

# KEYWORDS

cancel, unwind
