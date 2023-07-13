\

# NAME

lreplace - Replace elements in a list with new elements

# SYNOPSIS

**lreplace ***list first last *?*element element \...*?

\

# DESCRIPTION

**lreplace** returns a new list formed by replacing zero or more
elements of *list* with the *element* arguments. *first* and *last* are
index values specifying the first and last elements of the range to
replace. The index values *first* and *last* are interpreted the same as
index values for the command **string index**, supporting simple index
arithmetic and indices relative to the end of the list. 0 refers to the
first element of the list, and **end** refers to the last element of the
list.

If either *first* or *last* is less than zero, it is considered to refer
to before the first element of the list. This allows **lreplace** to
prepend elements to *list*.

If either *first* or *last* indicates a position greater than the index
of the last element of the list, it is treated as if it is an index one
greater than the last element. This allows **lreplace** to append
elements to *list*.

If *last* is less than *first*, then any specified elements will be
inserted into the list before the element specified by *first* with no
elements being deleted.

The *element* arguments specify zero or more new elements to be added to
the list in place of those that were deleted. Each *element* argument
will become a separate element of the list. If no *element* arguments
are specified, then the elements between *first* and *last* are simply
deleted.

# EXAMPLES

Replacing an element of a list with another:

    % lreplace {a b c d e} 1 1 foo
    a foo c d e

Replacing two elements of a list with three:

    % lreplace {a b c d e} 1 2 three more elements
    a three more elements d e

Deleting the last element from a list in a variable:

    % set var {a b c d e}
    a b c d e
    % set var [lreplace $var end end]
    a b c d

A procedure to delete a given element from a list:

    proc lremove {listVariable value} {
        upvar 1 $listVariable var
        set idx [lsearch -exact $var $value]
        set var [lreplace $var $idx $idx]
    }

Appending elements to the list; note that **end+2** will initially be
treated as if it is **6** here, but both that and **12345** are greater
than the index of the final item so they behave identically:

    % set var {a b c d e}
    a b c d e
    % set var [lreplace $var 12345 end+2 f g h i]
    a b c d e f g h i

# SEE ALSO

list(n), lappend(n), lindex(n), linsert(n), llength(n), lsearch(n),
lset(n), lrange(n), lsort(n), string(n)

# KEYWORDS

element, list, replace
