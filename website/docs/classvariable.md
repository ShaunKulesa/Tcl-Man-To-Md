\

# NAME

classvariable - create link from local variable to variable in class

# SYNOPSIS

    package require tcl::oo

    classvariable variableName ?...?

\

# DESCRIPTION

The **classvariable** command is available within methods. It takes a
series of one or more variable names and makes them available in the
method\'s scope; those variable names must not be qualified and must not
refer to array elements. The originating scope for the variables is the
namespace of the class that the method was defined by. In other words,
the referenced variables are shared between all instances of that class.

Note: This command is equivalent to the command **typevariable**
provided by the snit package in tcllib for approximately the same
purpose. If used in a method defined directly on a class instance (e.g.,
through the **oo::objdefine** **method** definition) this is very much
like just using:

    namespace upvar [namespace current] $var $var

for each variable listed to **classvariable**.

# EXAMPLE

This class counts how many instances of it have been made.

    oo::class create Counted {
        initialise {
            variable count 0
        }

        variable number
        constructor {} {
            classvariable count
            set number [incr count]
        }

        method report {} {
            classvariable count
            puts "This is instance $number of $count"
        }
    }

    set a [Counted new]
    set b [Counted new]
    $a report
            → This is instance 1 of 2
    set c [Counted new]
    $b report
            → This is instance 2 of 3
    $c report
            → This is instance 3 of 3

# SEE ALSO

global(n), namespace(n), oo::class(n), oo::define(n), upvar(n),
variable(n)

# KEYWORDS

class, class variable, variable
