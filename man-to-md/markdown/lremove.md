\

# NAME

lremove - Remove elements from a list by index

# SYNOPSIS

**lremove ***list* ?*index \...*?

\

# DESCRIPTION

**lremove** returns a new list formed by simultaneously removing zero or
more elements of *list* at each of the indices given by an arbitrary
number of *index* arguments. The indices may be in any order and may be
repeated; the element at index will only be removed once. The index
values are interpreted the same as index values for the command **string
index**, supporting simple index arithmetic and indices relative to the
end of the list. 0 refers to the first element of the list, and **end**
refers to the last element of the list.

# EXAMPLES

Removing the third element of a list:

    % lremove {a b c d e} 2
    a b d e

Removing two elements from a list:

    % lremove {a b c d e} end-1 1
    a c e

Removing the same element indicated in two different ways:

    % lremove {a b c d e} 2 end-2
    a b d e

# SEE ALSO

list(n), lappend(n), lassign(n), ledit(n), lindex(n), linsert(n),
llength(n), lmap(n), lpop(n), lrange(n), lrepeat(n), lreplace(n),
lreverse(n), lsearch(n), lseq(n), lset(n), lsort(n)

# KEYWORDS

element, list, remove
