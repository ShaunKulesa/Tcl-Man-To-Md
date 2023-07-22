# NAME

Tk_CreateClientMessageHandler, Tk_DeleteClientMessageHandler - associate
procedure callback with ClientMessage type X events

# SYNOPSIS

**#include \<tk.h\>**

**Tk_CreateClientMessageHandler**(*proc*)

**Tk_DeleteClientMessageHandler**(*proc*)

# ARGUMENTS

Procedure to invoke whenever a ClientMessage X event occurs on any
display.

# DESCRIPTION

**Tk_CreateClientMessageHandler** arranges for *proc* to be invoked in
the future whenever a ClientMessage X event occurs that is not handled
by **WM_PROTOCOL**. **Tk_CreateClientMessageHandler** is intended for
use by applications which need to watch X ClientMessage events, such as
drag and drop applications.

The callback to *proc* will be made by **Tk_HandleEvent**; this
mechanism only works in programs that dispatch events through
**Tk_HandleEvent** (or through other Tk procedures that call
**Tk_HandleEvent**, such as **Tcl_DoOneEvent** or **Tk_MainLoop**).

*Proc* should have arguments and result that match the type
**Tk_ClientMessageProc**:

    typedef int Tk_ClientMessageProc(
            Tk_Window tkwin,
            XEvent *eventPtr);

The *tkwin* parameter to *proc* is the Tk window which is associated
with this event. *EventPtr* is a pointer to the X event.

Whenever an X ClientMessage event is processed by **Tk_HandleEvent**,
the *proc* is called if it was not handled as a **WM_PROTOCOL**. The
return value from *proc* is normally 0. A non-zero return value
indicates that the event is not to be handled further; that is, *proc*
has done all processing that is to be allowed for the event.

If there are multiple ClientMessage event handlers, each one is called
for each event, in the order in which they were established.

**Tk_DeleteClientMessageHandler** may be called to delete a
previously-created ClientMessage event handler: it deletes each handler
it finds that matches the *proc* argument. If no such handler exists,
then **Tk_DeleteClientMessageHandler** returns without doing anything.
Although Tk supports it, it\'s probably a bad idea to have more than one
callback with the same *proc* argument.

# KEYWORDS

bind, callback, event, handler
