# NAME

time - Time the execution of a script

# SYNOPSIS

**time ***script* ?*count*?

# DESCRIPTION

This command will call the Tcl interpreter *count* times to evaluate
*script* (or once if *count* is not specified). It will then return a
string of the form

    503.2 microseconds per iteration

which indicates the average amount of time required per iteration, in
microseconds. Time is measured in elapsed time, not CPU time.

# EXAMPLE

Estimate how long it takes for a simple Tcl **for** loop to count to a
thousand:

    time {
        for {set i 0} {$i<1000} {incr i} {
            # empty body
        }
    }

# SEE ALSO

clock(n)

# KEYWORDS

script, time

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

