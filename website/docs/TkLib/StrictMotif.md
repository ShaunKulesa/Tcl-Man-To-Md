# NAME

Tk_StrictMotif - Return value of tk_strictMotif variable

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_StrictMotif**(*tkwin*)

# ARGUMENTS

Token for window.

# DESCRIPTION

This procedure returns the current value of the **tk_strictMotif**
variable in the interpreter associated with *tkwin*\'s application. The
value is returned as an integer that is either 0 or 1. 1 means that
strict Motif compliance has been requested, so anything that is not part
of the Motif specification should be avoided. 0 means that is good
enough, and extra features are welcome.

This procedure uses a link to the Tcl variable to provide much faster
access to the variable\'s value than could be had by calling
**Tcl_GetVar**.

# KEYWORDS

Motif compliance, tk_strictMotif variable
