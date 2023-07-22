# NAME

Tcl_SaveInterpState, Tcl_RestoreInterpState, Tcl_DiscardInterpState,
Tcl_SaveResult, Tcl_RestoreResult, Tcl_DiscardResult - save and restore
an interpreter\'s state

# SYNOPSIS

**#include \<tcl.h\>**

Tcl_InterpState **Tcl_SaveInterpState**(*interp, status*)

int **Tcl_RestoreInterpState**(*interp, state*)

**Tcl_DiscardInterpState**(*state*)

**Tcl_SaveResult**(*interp, savedPtr*)

**Tcl_RestoreResult**(*interp, savedPtr*)

**Tcl_DiscardResult**(*savedPtr*)

# ARGUMENTS

Interpreter for which state should be saved.

Return code value to save as part of interpreter state.

Saved state token to be restored or discarded.

Pointer to location where interpreter result should be saved or
restored.

# DESCRIPTION

These routines allows a C procedure to take a snapshot of the current
state of an interpreter so that it can be restored after a call to
**Tcl_Eval** or some other routine that modifies the interpreter state.
There are two triplets of routines meant to work together.

The first triplet stores the snapshot of interpreter state in an opaque
token returned by **Tcl_SaveInterpState**. That token value may then be
passed back to one of **Tcl_RestoreInterpState** or
**Tcl_DiscardInterpState**, depending on whether the interp state is to
be restored. So long as one of the latter two routines is called, Tcl
will take care of memory management.

The second triplet stores the snapshot of only the interpreter result
(not its complete state) in memory allocated by the caller. These
routines are passed a pointer to **Tcl_SavedResult** that is used to
store enough information to restore the interpreter result.
**Tcl_SavedResult** can be allocated on the stack of the calling
procedure. These routines do not save the state of any error information
in the interpreter (e.g. the **-errorcode** or **-errorinfo** return
options, when an error is in progress).

Because the routines **Tcl_SaveInterpState**,
**Tcl_RestoreInterpState**, and **Tcl_DiscardInterpState** perform a
superset of the functions provided by the other routines, any new code
should only make use of the more powerful routines. The older, weaker
routines **Tcl_SaveResult**, **Tcl_RestoreResult**, and
**Tcl_DiscardResult** continue to exist only for the sake of existing
programs that may already be using them.

**Tcl_SaveInterpState** takes a snapshot of those portions of
interpreter state that make up the full result of script evaluation.
This include the interpreter result, the return code (passed in as the
*status* argument, and any return options, including **-errorinfo** and
**-errorcode** when an error is in progress. This snapshot is returned
as an opaque token of type **Tcl_InterpState**. The call to
**Tcl_SaveInterpState** does not itself change the state of the
interpreter. Unlike **Tcl_SaveResult**, it does not reset the
interpreter.

**Tcl_RestoreInterpState** accepts a **Tcl_InterpState** token
previously returned by **Tcl_SaveInterpState** and restores the state of
the interp to the state held in that snapshot. The return value of
**Tcl_RestoreInterpState** is the status value originally passed to
**Tcl_SaveInterpState** when the snapshot token was created.

**Tcl_DiscardInterpState** is called to release a **Tcl_InterpState**
token previously returned by **Tcl_SaveInterpState** when that snapshot
is not to be restored to an interp.

The **Tcl_InterpState** token returned by **Tcl_SaveInterpState** must
eventually be passed to either **Tcl_RestoreInterpState** or
**Tcl_DiscardInterpState** to avoid a memory leak. Once the
**Tcl_InterpState** token is passed to one of them, the token is no
longer valid and should not be used anymore.

**Tcl_SaveResult** moves the string and value results of *interp* into
the location specified by *statePtr*. **Tcl_SaveResult** clears the
result for *interp* and leaves the result in its normal empty
initialized state.

**Tcl_RestoreResult** moves the string and value results from *statePtr*
back into *interp*. Any result or error that was already in the
interpreter will be cleared. The *statePtr* is left in an uninitialized
state and cannot be used until another call to **Tcl_SaveResult**.

**Tcl_DiscardResult** releases the saved interpreter state stored at
**statePtr**. The state structure is left in an uninitialized state and
cannot be used until another call to **Tcl_SaveResult**.

Once **Tcl_SaveResult** is called to save the interpreter result, either
**Tcl_RestoreResult** or **Tcl_DiscardResult** must be called to
properly clean up the memory associated with the saved state.

# KEYWORDS

result, state, interp
