# NAME

Tcl_CreateCloseHandler, Tcl_DeleteCloseHandler - arrange for callbacks
when channels are closed

# SYNOPSIS

**#include \<tcl.h\>**

void **Tcl_CreateCloseHandler**(*channel, proc, clientData*)

void **Tcl_DeleteCloseHandler**(*channel, proc, clientData*)

# ARGUMENTS

The channel for which to create or delete a close callback.

The procedure to call as the callback.

Arbitrary one-word value to pass to *proc*.

# DESCRIPTION

**Tcl_CreateCloseHandler** arranges for *proc* to be called when
*channel* is closed with **Tcl_Close** or **Tcl_UnregisterChannel**, or
using the Tcl **close** command. *Proc* should match the following
prototype:

    typedef void Tcl_CloseProc(
            ClientData clientData);

The *clientData* is the same as the value provided in the call to
**Tcl_CreateCloseHandler**.

**Tcl_DeleteCloseHandler** removes a close callback for *channel*. The
*proc* and *clientData* identify which close callback to remove;
**Tcl_DeleteCloseHandler** does nothing if its *proc* and *clientData*
arguments do not match the *proc* and *clientData* for a close handler
for *channel*.

# SEE ALSO

close(n), Tcl_Close(3), Tcl_UnregisterChannel(3)

# KEYWORDS

callback, channel closing
