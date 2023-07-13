\

# NAME

lseq - Build a numeric sequence returned as a list

# SYNOPSIS

**lseq ***start *?(**..**\|**to**)? *end* ??**by**? *step*?

**lseq ***start ***count** *count* ??**by**? *step*?

**lseq ***count* ?**by ***step*?

\

# DESCRIPTION

The **lseq** command creates a sequence of numeric values using the
given parameters *start*, *end*, and *step*. The *operation* argument
\"**..**\" or \"**to**\" defines the range. The \"**count**\" option is
used to define a count of the number of elements in the list. A short
form use of the command, with a single count value, will create a range
from 0 to count-1.

The **lseq** command can produce both increasing and decreasing
sequences. When both *start* and *end* are provided without a *step*
value, then if *start* \<= *end*, the sequence will be increasing and if
*start* \> *end* it will be decreasing. If a *step* vale is included,
it\'s sign should agree with the direction of the sequence (descending
-\> negative and ascending -\> positive), otherwise an empty list is
returned. For example:

    % lseq 1 to 5    ;# increasing
    → 1 2 3 4 5

    % lseq 5 to 1    ;# decreasing
    → 5 4 3 2 1

    % lseq 6 to 1 by 2   ;# decreasing, step wrong sign, empty list

    % lseq 1 to 5 by 0   ;# all step sizes of 0 produce an empty list

The numeric arguments, *start*, *end*, *step*, and *count*, may also be
a valid expression. The expression will be evaluated and the numeric
result will be used. An expression that does not evaluate to a number
will produce an invalid argument error.

*Start* defines the initial value and *end* defines the limit, not
necessarily the last value. **lseq** produces a list with *count*
elements, and if *count* is not supplied, it is computed as

        count = int( (end - start + step) / step )

The numeric arguments, *start*, *end*, *step*, and *count*, can also be
a valid expression. the **lseq** command will evaluate the expression
(as if with **expr**) and use the numeric result, or return an error as
with any invalid argument value; a non-numeric expression result will
result in an error.

# EXAMPLES

    lseq 3
    → 0 1 2

    lseq 3 0
    → 3 2 1 0

    lseq 10 .. 1 by -2
    → 10 8 6 4 2

    set l [lseq 0 -5]
    → 0 -1 -2 -3 -4 -5

    foreach i [lseq [llength $l]] {
        puts l($i)=[lindex $l $i]
    }
    → l(0)=0
    → l(1)=-1
    → l(2)=-2
    → l(3)=-3
    → l(4)=-4
    → l(5)=-5

    foreach i [lseq {[llength $l]-1} 0] {
        puts l($i)=[lindex $l $i]
    }
    → l(5)=-5
    → l(4)=-4
    → l(3)=-3
    → l(2)=-2
    → l(1)=-1
    → l(0)=0

    set i 17
             → 17
    if {$i in [lseq 0 50]} { # equivalent to: (0 <= $i && $i <= 50)
        puts "Ok"
    } else {
        puts "outside :("
    }
    → Ok

    set sqrs [lmap i [lseq 1 10] { expr {$i*$i} }]
    → 1 4 9 16 25 36 49 64 81 100

# SEE ALSO

foreach(n), list(n), lappend(n), lassign(n), lindex(n), linsert(n),
llength(n), lmap(n), lpop(n), lrange(n), lremove(n), lreplace(n),
lreverse(n), lsearch(n), lset(n), lsort(n)

# KEYWORDS

element, index, list
