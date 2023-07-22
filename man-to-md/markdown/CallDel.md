# NAME

Tcl_CallWhenDeleted, Tcl_DontCallWhenDeleted - Arrange for callback when
interpreter is deleted

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_CallWhenDeleted**(*interp*, *proc*, *clientData*)

**Tcl_DontCallWhenDeleted**(*interp*, *proc*, *clientData*)

# ARGUMENTS

Interpreter with which to associated callback.

Procedure to call when *interp* is deleted.

Arbitrary one-word value to pass to *proc*.

# DESCRIPTION

**Tcl_CallWhenDeleted** arranges for *proc* to be called by
**Tcl_DeleteInterp** if/when *interp* is deleted at some future time.
*Proc* will be invoked just before the interpreter is deleted, but the
interpreter will still be valid at the time of the call. *Proc* should
have arguments and result that match the type **Tcl_InterpDeleteProc**:

    typedef void Tcl_InterpDeleteProc(
            ClientData clientData,
            Tcl_Interp *interp);

The *clientData* and *interp* parameters are copies of the *clientData*
and *interp* arguments given to **Tcl_CallWhenDeleted**. Typically,
*clientData* points to an application-specific data structure that
*proc* uses to perform cleanup when an interpreter is about to go away.
*Proc* does not return a value.

**Tcl_DontCallWhenDeleted** cancels a previous call to
**Tcl_CallWhenDeleted** with the same arguments, so that *proc* will not
be called after all when *interp* is deleted. If there is no deletion
callback that matches *interp*, *proc*, and *clientData* then the call
to **Tcl_DontCallWhenDeleted** has no effect.

Note that if the callback is being used to delete a resource that *must*
be released on exit, **Tcl_CreateExitHandler** should be used to ensure
that a callback is received even if the application terminates without
deleting the interpreter.

# SEE ALSO

Tcl_CreateExitHandler(3), Tcl_CreateThreadExitHandler(3)

# KEYWORDS

callback, cleanup, delete, interpreter

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

