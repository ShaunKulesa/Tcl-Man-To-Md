# NAME

Tk_CreateEventHandler, Tk_DeleteEventHandler - associate procedure
callback with an X event

# SYNOPSIS

**#include \<tk.h\>**

**Tk_CreateEventHandler**(*tkwin, mask, proc, clientData*)

**Tk_DeleteEventHandler**(*tkwin, mask, proc, clientData*)

# ARGUMENTS

Token for window in which events may occur.

Bit-mask of events (such as **ButtonPressMask**) for which *proc* should
be called.

Procedure to invoke whenever an event in *mask* occurs in the window
given by *tkwin*.

Arbitrary one-word value to pass to *proc*.

# DESCRIPTION

**Tk_CreateEventHandler** arranges for *proc* to be invoked in the
future whenever one of the event types specified by *mask* occurs in the
window specified by *tkwin*. The callback to *proc* will be made by
**Tk_HandleEvent**; this mechanism only works in programs that dispatch
events through **Tk_HandleEvent** (or through other Tk procedures that
call **Tk_HandleEvent**, such as **Tcl_DoOneEvent** or **Tk_MainLoop**).

*Proc* should have arguments and result that match the type
**Tk_EventProc**:

    typedef void Tk_EventProc(
            ClientData clientData,
            XEvent *eventPtr);

The *clientData* parameter to *proc* is a copy of the *clientData*
argument given to **Tk_CreateEventHandler** when the callback was
created. Typically, *clientData* points to a data structure containing
application-specific information about the window in which the event
occurred. *EventPtr* is a pointer to the X event, which will be one of
the ones specified in the *mask* argument to **Tk_CreateEventHandler**.

**Tk_DeleteEventHandler** may be called to delete a previously-created
event handler: it deletes the first handler it finds that is associated
with *tkwin* and matches the *mask*, *proc*, and *clientData* arguments.
If no such handler exists, then **Tk_HandleEvent** returns without doing
anything. Although Tk supports it, it\'s probably a bad idea to have
more than one callback with the same *mask*, *proc*, and *clientData*
arguments. When a window is deleted all of its handlers will be deleted
automatically; in this case there is no need to call
**Tk_DeleteEventHandler**.

If multiple handlers are declared for the same type of X event on the
same window, then the handlers will be invoked in the order they were
created.

# KEYWORDS

bind, callback, event, handler

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

