# NAME

tailcall - Replace the current procedure with another command

# SYNOPSIS

**tailcall ***command* ?*arg \...*?

# DESCRIPTION

The **tailcall** command replaces the currently executing procedure,
lambda application, or method with another command. The *command*, which
will have *arg \...* passed as arguments if they are supplied, will be
looked up in the current namespace context, not in the caller\'s. Apart
from that difference in resolution, it is equivalent to:

    return [uplevel 1 [list command ?arg ...?]]

This command may not be invoked from within an **uplevel** into a
procedure or inside a **catch** inside a procedure or lambda.

# EXAMPLE

Compute the factorial of a number.

    proc factorial {n {accum 1}} {
        if {$n < 2} {
            return $accum
        }
        tailcall factorial [expr {$n - 1}] [expr {$accum * $n}]
    }

Print the elements of a list with alternating lines having different
indentations.

    proc printList {theList} {
        if {[llength $theList]} {
            puts "> [lindex $theList 0]"
            tailcall printList2 [lrange $theList 1 end]
        }
    }
    proc printList2 {theList} {
        if {[llength $theList]} {
            puts "< [lindex $theList 0]"
            tailcall printList [lrange $theList 1 end]
        }
    }

# SEE ALSO

apply(n), proc(n), uplevel(n)

# KEYWORDS

call, recursion, tail recursion
