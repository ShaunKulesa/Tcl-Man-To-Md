# NAME

list - Create a list

# SYNOPSIS

**list **?*arg arg \...*?

# DESCRIPTION

This command returns a list comprised of all the *arg*s, or an empty
string if no *arg*s are specified. Braces and backslashes get added as
necessary, so that the **lindex** command may be used on the result to
re-extract the original arguments, and also so that **eval** may be used
to execute the resulting list, with *arg1* comprising the command\'s
name and the other *arg*s comprising its arguments. **List** produces
slightly different results than **concat**: **concat** removes one level
of grouping before forming the list, while **list** works directly from
the original arguments.

# EXAMPLE

The command

    list a b "c d e  " "  f {g h}"

will return

    a b {c d e  } {  f {g h}}

while **concat** with the same arguments will return

    a b c d e f {g h}

# SEE ALSO

lappend(n), lindex(n), linsert(n), llength(n), lrange(n), lrepeat(n),
lreplace(n), lsearch(n), lset(n), lsort(n)

# KEYWORDS

element, list, quoting

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
Copyright (c) 2001 Kevin B. Kenny <kennykb@acm.org>.  All rights reserved
-->

