# NAME

llength - Count the number of elements in a list

# SYNOPSIS

**llength ***list*

# DESCRIPTION

Treats *list* as a list and returns a decimal string giving the number
of elements in it.

# EXAMPLES

The result is the number of elements:

    % llength {a b c d e}
    5
    % llength {a b c}
    3
    % llength {}
    0

Elements are not guaranteed to be exactly words in a dictionary sense of
course, especially when quoting is used:

    % llength {a b {c d} e}
    4
    % llength {a b { } c d e}
    6

An empty list is not necessarily an empty string:

    % set var { }; puts "[string length $var],[llength $var]"
    1,0

# SEE ALSO

list(n), lappend(n), lindex(n), linsert(n), lsearch(n), lset(n),
lsort(n), lrange(n), lreplace(n)

# KEYWORDS

element, list, length

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
Copyright (c) 2001 Kevin B. Kenny <kennykb@acm.org>.  All rights reserved
-->

