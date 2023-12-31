# NAME

Tcl_Preserve, Tcl_Release, Tcl_EventuallyFree - avoid freeing storage
while it is being used

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_Preserve**(*clientData*)

**Tcl_Release**(*clientData*)

**Tcl_EventuallyFree**(*clientData, freeProc*)

# ARGUMENTS

Token describing structure to be freed or reallocated. Usually a pointer
to memory for structure.

Procedure to invoke to free *clientData*.

# DESCRIPTION

These three procedures help implement a simple reference count mechanism
for managing storage. They are designed to solve a problem having to do
with widget deletion, but are also useful in many other situations. When
a widget is deleted, its widget record (the structure holding
information specific to the widget) must be returned to the storage
allocator. However, it is possible that the widget record is in active
use by one of the procedures on the stack at the time of the deletion.
This can happen, for example, if the command associated with a button
widget causes the button to be destroyed: an X event causes an
event-handling C procedure in the button to be invoked, which in turn
causes the button\'s associated Tcl command to be executed, which in
turn causes the button to be deleted, which in turn causes the button\'s
widget record to be de-allocated. Unfortunately, when the Tcl command
returns, the button\'s event-handling procedure will need to reference
the button\'s widget record. Because of this, the widget record must not
be freed as part of the deletion, but must be retained until the
event-handling procedure has finished with it. In other situations where
the widget is deleted, it may be possible to free the widget record
immediately.

**Tcl_Preserve** and **Tcl_Release** implement short-term reference
counts for their *clientData* argument. The *clientData* argument
identifies an object and usually consists of the address of a structure.
The reference counts guarantee that an object will not be freed until
each call to **Tcl_Preserve** for the object has been matched by calls
to **Tcl_Release**. There may be any number of unmatched
**Tcl_Preserve** calls in effect at once.

**Tcl_EventuallyFree** is invoked to free up its *clientData* argument.
It checks to see if there are unmatched **Tcl_Preserve** calls for the
object. If not, then **Tcl_EventuallyFree** calls *freeProc*
immediately. Otherwise **Tcl_EventuallyFree** records the fact that
*clientData* needs eventually to be freed. When all calls to
**Tcl_Preserve** have been matched with calls to **Tcl_Release** then
*freeProc* will be called by **Tcl_Release** to do the cleanup.

All the work of freeing the object is carried out by *freeProc*.
*FreeProc* must have arguments and result that match the type
**Tcl_FreeProc**:

    typedef void Tcl_FreeProc(
            char *blockPtr);

The *blockPtr* argument to *freeProc* will be the same as the
*clientData* argument to **Tcl_EventuallyFree**. The type of *blockPtr*
(**char \***) is different than the type of the *clientData* argument to
**Tcl_EventuallyFree** for historical reasons, but the value is the
same.

When the *clientData* argument to **Tcl_EventuallyFree** refers to
storage allocated and returned by a prior call to **Tcl_Alloc**,
**ckalloc**, or another function of the Tcl library, then the *freeProc*
argument should be given the special value of **TCL_DYNAMIC**.

This mechanism can be used to solve the problem described above by
placing **Tcl_Preserve** and **Tcl_Release** calls around actions that
may cause undesired storage re-allocation. The mechanism is intended
only for short-term use (i.e. while procedures are pending on the
stack); it will not work efficiently as a mechanism for long-term
reference counts. The implementation does not depend in any way on the
internal structure of the objects being freed; it keeps the reference
counts in a separate structure.

# SEE ALSO

Tcl_Interp, Tcl_Alloc

# KEYWORDS

free, reference count, storage

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

