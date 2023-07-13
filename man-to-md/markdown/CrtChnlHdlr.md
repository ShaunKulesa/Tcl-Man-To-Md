\

# NAME

Tcl_CreateChannelHandler, Tcl_DeleteChannelHandler - call a procedure
when a channel becomes readable or writable

# SYNOPSIS

    #include <tcl.h>

    void
    Tcl_CreateChannelHandler(channel, mask, proc, clientData)

    void
    Tcl_DeleteChannelHandler(channel, proc, clientData)

# ARGUMENTS

Tcl channel such as returned by **Tcl_CreateChannel**.

Conditions under which *proc* should be called: OR-ed combination of
**TCL_READABLE**, **TCL_WRITABLE** and **TCL_EXCEPTION**. Specify a zero
value to temporarily disable an existing handler.

Procedure to invoke whenever the channel indicated by *channel* meets
the conditions specified by *mask*.

Arbitrary one-word value to pass to *proc*.

\

# DESCRIPTION

**Tcl_CreateChannelHandler** arranges for *proc* to be called in the
future whenever input or output becomes possible on the channel
identified by *channel*, or whenever an exceptional condition exists for
*channel*. The conditions of interest under which *proc* will be invoked
are specified by the *mask* argument. See the manual entry for
**fileevent** for a precise description of what it means for a channel
to be readable or writable. *Proc* must conform to the following
prototype:

    typedef void Tcl_ChannelProc(
            ClientData clientData,
            int mask);

The *clientData* argument is the same as the value passed to
**Tcl_CreateChannelHandler** when the handler was created. Typically,
*clientData* points to a data structure containing application-specific
information about the channel. *Mask* is an integer mask indicating
which of the requested conditions actually exists for the channel; it
will contain a subset of the bits from the *mask* argument to
**Tcl_CreateChannelHandler** when the handler was created.

Each channel handler is identified by a unique combination of *channel*,
*proc* and *clientData*. There may be many handlers for a given channel
as long as they do not have the same *channel*, *proc*, and
*clientData*. If **Tcl_CreateChannelHandler** is invoked when there is
already a handler for *channel*, *proc*, and *clientData*, then no new
handler is created; instead, the *mask* is changed for the existing
handler.

**Tcl_DeleteChannelHandler** deletes a channel handler identified by
*channel*, *proc* and *clientData*; if no such handler exists, the call
has no effect.

Channel handlers are invoked via the Tcl event mechanism, so they are
only useful in applications that are event-driven. Note also that the
conditions specified in the *mask* argument to *proc* may no longer
exist when *proc* is invoked: for example, if there are two handlers for
**TCL_READABLE** on the same channel, the first handler could consume
all of the available input so that the channel is no longer readable
when the second handler is invoked. For this reason it may be useful to
use nonblocking I/O on channels for which there are event handlers.

# SEE ALSO

Notifier(3), Tcl_CreateChannel(3), Tcl_OpenFileChannel(3), vwait(n).

# KEYWORDS

blocking, callback, channel, events, handler, nonblocking.
