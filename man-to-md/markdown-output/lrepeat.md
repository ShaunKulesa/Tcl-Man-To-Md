# NAME

lrepeat - Build a list by repeating elements

# SYNOPSIS

**lrepeat ***count *?*element \...*?

# DESCRIPTION

The **lrepeat** command creates a list of size *count \* number of*
elements by repeating *count* times the sequence of elements *element
\...*. *count* must be a non-negative integer, *element* can be any Tcl
value. Note that **lrepeat 1 element \...** is identical to **list
element \...**.

# EXAMPLES

    lrepeat 3 a
          → a a a
    lrepeat 3 [lrepeat 3 0]
          → {0 0 0} {0 0 0} {0 0 0}
    lrepeat 3 a b c
          → a b c a b c a b c
    lrepeat 3 [lrepeat 2 a] b c
          → {a a} b c {a a} b c {a a} b c

# SEE ALSO

list(n), lappend(n), linsert(n), llength(n), lset(n)

# KEYWORDS

element, index, list

<!---
Copyright (c) 2003 Simon Geard.  All rights reserved
-->

