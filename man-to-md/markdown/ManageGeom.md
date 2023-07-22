# NAME

Tk_ManageGeometry - arrange to handle geometry requests for a window

# SYNOPSIS

**#include \<tk.h\>**

**Tk_ManageGeometry**(*tkwin, mgrPtr, clientData*)

# ARGUMENTS

Token for window to be managed.

Pointer to data structure containing information about the geometry
manager, or NULL to indicate that *tkwin*\'s geometry should not be
managed anymore. The data structure pointed to by *mgrPtr* must be
static: Tk keeps a reference to it as long as the window is managed.

Arbitrary one-word value to pass to geometry manager callbacks.

# DESCRIPTION

**Tk_ManageGeometry** arranges for a particular geometry manager,
described by the *mgrPtr* argument, to control the geometry of a
particular content window, given by *tkwin*. If *tkwin* was previously
managed by some other geometry manager, the previous manager loses
control in favor of the new one. If *mgrPtr* is NULL, geometry
management is cancelled for *tkwin*.

The structure pointed to by *mgrPtr* contains information about the
geometry manager:

    typedef struct {
        const char *name;
        Tk_GeomRequestProc *requestProc;
        Tk_GeomLostSlaveProc *lostSlaveProc;
    } Tk_GeomMgr;

The *name* field is the textual name for the geometry manager, such as
**pack** or **place**; this value will be returned by the command
**winfo manager**.

*requestProc* is a procedure in the geometry manager that will be
invoked whenever **Tk_GeometryRequest** is called by the content window
to change its desired geometry. *requestProc* should have arguments and
results that match the type **Tk_GeomRequestProc**:

    typedef void Tk_GeomRequestProc(
            ClientData clientData,
            Tk_Window tkwin);

The parameters to *requestProc* will be identical to the corresponding
parameters passed to **Tk_ManageGeometry**. *clientData* usually points
to a data structure containing application-specific information about
how to manage *tkwin*\'s geometry.

The *lostSlaveProc* field of *mgrPtr* points to another procedure in the
geometry manager. Tk will invoke *lostSlaveProc* if some other manager
calls **Tk_ManageGeometry** to claim *tkwin* away from the current
geometry manager. *lostSlaveProc* is not invoked if
**Tk_ManageGeometry** is called with a NULL value for *mgrPtr*
(presumably the current geometry manager has made this call, so it
already knows that the window is no longer managed), nor is it called if
*mgrPtr* is the same as the window\'s current geometry manager.
*lostSlaveProc* should have arguments and results that match the
following prototype:

    typedef void Tk_GeomLostSlaveProc(
            ClientData clientData,
            Tk_Window tkwin);

The parameters to *lostSlaveProc* will be identical to the corresponding
parameters passed to **Tk_ManageGeometry**.

# KEYWORDS

callback, geometry, managed, request, unmanaged

<!---
Copyright (c) 1990-1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

