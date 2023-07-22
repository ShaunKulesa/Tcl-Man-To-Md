# NAME

Tcl_AllowExceptions - allow all exceptions in next script evaluation

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_AllowExceptions**(*interp*)

# ARGUMENTS

Interpreter in which script will be evaluated.

# DESCRIPTION

If a script is evaluated at top-level (i.e. no other scripts are pending
evaluation when the script is invoked), and if the script terminates
with a completion code other than **TCL_OK**, **TCL_ERROR** or
**TCL_RETURN**, then Tcl normally converts this into a **TCL_ERROR**
return with an appropriate message. The particular script evaluation
procedures of Tcl that act in the manner are **Tcl_EvalObjEx**,
**Tcl_EvalObjv**, **Tcl_Eval**, **Tcl_EvalEx**, **Tcl_GlobalEval**,
**Tcl_GlobalEvalObj**, **Tcl_VarEval** and **Tcl_VarEvalVA**.

However, if **Tcl_AllowExceptions** is invoked immediately before
calling one of those a procedures, then arbitrary completion codes are
permitted from the script, and they are returned without modification.
This is useful in cases where the caller can deal with exceptions such
as **TCL_BREAK** or **TCL_CONTINUE** in a meaningful way.

# KEYWORDS

continue, break, exception, interpreter
