\

# NAME

Tcl_SaveInterpState, Tcl_RestoreInterpState, Tcl_DiscardInterpState -
Save and restore the state of an an interpreter.

# SYNOPSIS

    #include <tcl.h>

    Tcl_InterpState
    Tcl_SaveInterpState(interp, status)

    int
    Tcl_RestoreInterpState(interp, state)

    Tcl_DiscardInterpState(state)

# ARGUMENTS

The interpreter for the operation.

The return code for the state.

A token for saved state.

\

# DESCRIPTION

These routines save the state of an interpreter before a call to a
routine such as **Tcl_Eval**, and restore the state afterwards.

**Tcl_SaveInterpState** saves the parts of *interp* that comprise the
result of a script, including the resulting value, the return code
passed as *status*, and any options such as **-errorinfo** and
**-errorcode**. It returns a token for the saved state. The interpreter
result is not reset and no interpreter state is changed.

**Tcl_RestoreInterpState** restores the state indicated by *state* and
returns the *status* originally passed in the corresponding call to
**Tcl_SaveInterpState**.

If a saved state is not restored, **Tcl_DiscardInterpState** must be
called to release it. A token used to discard or restore state must not
be used again.

# KEYWORDS

result, state, interp
