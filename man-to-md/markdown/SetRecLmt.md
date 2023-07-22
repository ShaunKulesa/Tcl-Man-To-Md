# NAME

Tcl_SetRecursionLimit - set maximum allowable nesting depth in
interpreter

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_SetRecursionLimit**(*interp, depth*)

# ARGUMENTS

Interpreter whose recursion limit is to be set. Must be greater than
zero.

New limit for nested calls to **Tcl_Eval** for *interp*.

# DESCRIPTION

At any given time Tcl enforces a limit on the number of recursive calls
that may be active for **Tcl_Eval** and related procedures such as
**Tcl_GlobalEval**. Any call to **Tcl_Eval** that exceeds this depth is
aborted with an error. By default the recursion limit is 1000.

**Tcl_SetRecursionLimit** may be used to change the maximum allowable
nesting depth for an interpreter. The *depth* argument specifies a new
limit for *interp*, and **Tcl_SetRecursionLimit** returns the old limit.
To read out the old limit without modifying it, invoke
**Tcl_SetRecursionLimit** with *depth* equal to 0.

The **Tcl_SetRecursionLimit** only sets the size of the Tcl call stack:
it cannot by itself prevent stack overflows on the C stack being used by
the application. If your machine has a limit on the size of the C stack,
you may get stack overflows before reaching the limit set by
**Tcl_SetRecursionLimit**. If this happens, see if there is a mechanism
in your system for increasing the maximum size of the C stack.

# KEYWORDS

nesting depth, recursion

<!---
Copyright (c) 1989-1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

