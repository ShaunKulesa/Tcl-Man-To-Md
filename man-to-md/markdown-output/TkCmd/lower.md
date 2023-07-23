# NAME

lower - Change a window\'s position in the stacking order

# SYNOPSIS

**lower ***window *?*belowThis*?

# DESCRIPTION

If the *belowThis* argument is omitted then the command lowers *window*
so that it is below all of its siblings in the stacking order (it will
be obscured by any siblings that overlap it and will not obscure any
siblings). If *belowThis* is specified then it must be the path name of
a window that is either a sibling of *window* or the descendant of a
sibling of *window*. In this case the **lower** command will insert
*window* into the stacking order just below *belowThis* (or the ancestor
of *belowThis* that is a sibling of *window*); this could end up either
raising or lowering *window*.

All **toplevel** windows may be restacked with respect to each other,
whatever their relative path names, but the window manager is not
obligated to strictly honor requests to restack.

# SEE ALSO

raise

# KEYWORDS

lower, obscure, stacking order

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

