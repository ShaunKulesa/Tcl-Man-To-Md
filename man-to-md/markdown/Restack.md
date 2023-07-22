# NAME

Tk_RestackWindow - Change a window\'s position in the stacking order

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_RestackWindow**(*tkwin, aboveBelow, other*)

# ARGUMENTS

Token for window to restack.

Indicates new position of *tkwin* relative to *other*; must be **Above**
or **Below**.

*Tkwin* will be repositioned just above or below this window. Must be a
sibling of *tkwin* or a descendant of a sibling. If NULL then *tkwin* is
restacked above or below all siblings.

# DESCRIPTION

**Tk_RestackWindow** changes the stacking order of *window* relative to
its siblings. If *other* is specified as NULL then *window* is
repositioned at the top or bottom of its stacking order, depending on
whether *aboveBelow* is **Above** or **Below**. If *other* has a
non-NULL value then *window* is repositioned just above or below
*other*.

The *aboveBelow* argument must have one of the symbolic values **Above**
or **Below**. Both of these values are defined by the include file
\<X11/Xlib.h\>.

# KEYWORDS

above, below, obscure, stacking order

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

