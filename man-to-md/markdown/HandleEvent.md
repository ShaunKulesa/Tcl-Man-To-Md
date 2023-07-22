# NAME

Tk_HandleEvent - invoke event handlers for window system events

# SYNOPSIS

**#include \<tk.h\>**

**Tk_HandleEvent**(*eventPtr*)

# ARGUMENTS

Pointer to X event to dispatch to relevant handler(s). It is important
that all unused fields of the structure be set to zero.

# DESCRIPTION

**Tk_HandleEvent** is a lower-level procedure that deals with window
events. It is called by **Tcl_ServiceEvent** (and indirectly by
**Tcl_DoOneEvent**), and in a few other cases within Tk. It makes
callbacks to any window event handlers (created by calls to
**Tk_CreateEventHandler**) that match *eventPtr* and then returns. In
some cases it may be useful for an application to bypass the Tk event
queue and call **Tk_HandleEvent** directly instead of calling
**Tcl_QueueEvent** followed by **Tcl_ServiceEvent**.

This procedure may be invoked recursively. For example, it is possible
to invoke **Tk_HandleEvent** recursively from a handler called by
**Tk_HandleEvent**. This sort of operation is useful in some modal
situations, such as when a notifier has been popped up and an
application wishes to wait for the user to click a button in the
notifier before doing anything else.

# KEYWORDS

callback, event, handler, window

<!---
Copyright (c) 1990-1992 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

