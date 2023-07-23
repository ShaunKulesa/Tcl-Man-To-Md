# NAME

Tk_OwnSelection - make a window the owner of the primary selection

# SYNOPSIS

**#include \<tk.h\>**

**Tk_OwnSelection**(*tkwin, selection, proc, clientData*)

# ARGUMENTS

Window that is to become new selection owner.

The name of the selection to be owned, such as XA_PRIMARY.

Procedure to invoke when *tkwin* loses selection ownership later.

Arbitrary one-word value to pass to *proc*.

# DESCRIPTION

**Tk_OwnSelection** arranges for *tkwin* to become the new owner of the
selection specified by the atom *selection*. After this call completes,
future requests for the selection will be directed to handlers created
for *tkwin* using **Tk_CreateSelHandler**. When *tkwin* eventually loses
the selection ownership, *proc* will be invoked so that the window can
clean itself up (e.g. by unhighlighting the selection). *Proc* should
have arguments and result that match the type **Tk_LostSelProc**:

    typedef void Tk_LostSelProc(
            ClientData clientData);

The *clientData* parameter to *proc* is a copy of the *clientData*
argument given to **Tk_OwnSelection**, and is usually a pointer to a
data structure containing application-specific information about
*tkwin*.

# KEYWORDS

own, selection owner

<!---
Copyright (c) 1990-1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

