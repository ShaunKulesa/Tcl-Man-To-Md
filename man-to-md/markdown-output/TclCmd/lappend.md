# NAME

lappend - Append list elements onto a variable

# SYNOPSIS

**lappend ***varName *?*value value value \...*?

# DESCRIPTION

This command treats the variable given by *varName* as a list and
appends each of the *value* arguments to that list as a separate
element, with spaces between elements. If *varName* does not exist, it
is created as a list with elements given by the *value* arguments.
**Lappend** is similar to **append** except that the *value*s are
appended as list elements rather than raw text. This command provides a
relatively efficient way to build up large lists. For example, is much
more efficient than when **\$a** is long.

# EXAMPLE

Using **lappend** to build up a list of numbers.

    % set var 1
    1
    % lappend var 2
    1 2
    % lappend var 3 4 5
    1 2 3 4 5

# SEE ALSO

list(n), lindex(n), linsert(n), llength(n), lset(n), lsort(n), lrange(n)

# KEYWORDS

append, element, list, variable

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
Copyright (c) 2001 Kevin B. Kenny <kennykb@acm.org>.  All rights reserved
-->

