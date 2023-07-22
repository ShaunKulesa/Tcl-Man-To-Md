# NAME

Tk_InternAtom, Tk_GetAtomName - manage cache of X atoms

# SYNOPSIS

**#include \<tk.h\>**

Atom **Tk_InternAtom(***tkwin, name*)

const char \* **Tk_GetAtomName(***tkwin, atom*)

# ARGUMENTS

Token for window. Used to map atom or name relative to a particular
display.

String name for which atom is desired.

Atom for which corresponding string name is desired.

# DESCRIPTION

These procedures are similar to the Xlib procedures **XInternAtom** and
**XGetAtomName**. **Tk_InternAtom** returns the atom identifier
associated with string given by *name*; the atom identifier is only
valid for the display associated with *tkwin*. **Tk_GetAtomName**
returns the string associated with *atom* on *tkwin*\'s display. The
string returned by **Tk_GetAtomName** is in Tk\'s storage: the caller
need not free this space when finished with the string, and the caller
should not modify the contents of the returned string. If there is no
atom *atom* on *tkwin*\'s display, then **Tk_GetAtomName** returns the
string

Tk caches the information returned by **Tk_InternAtom** and
**Tk_GetAtomName** so that future calls for the same information can be
serviced from the cache without contacting the server. Thus
**Tk_InternAtom** and **Tk_GetAtomName** are generally much faster than
their Xlib counterparts, and they should be used in place of the Xlib
procedures.

# KEYWORDS

atom, cache, display

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

