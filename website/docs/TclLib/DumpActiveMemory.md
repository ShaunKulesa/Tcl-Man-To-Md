# NAME

Tcl_DumpActiveMemory, Tcl_InitMemory, Tcl_ValidateAllMemory - Validated
memory allocation interface

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_DumpActiveMemory**(*fileName*)

void **Tcl_InitMemory**(*interp*)

void **Tcl_ValidateAllMemory**(*fileName, line*)

# ARGUMENTS

Tcl interpreter in which to add commands.

For **Tcl_DumpActiveMemory**, name of the file to which memory
information will be written. For **Tcl_ValidateAllMemory**, name of the
file from which the call is being made (normally **\_\_FILE\_\_**).

Line number at which the call to **Tcl_ValidateAllMemory** is made
(normally **\_\_LINE\_\_**).

# DESCRIPTION

These functions provide access to Tcl memory debugging information. They
are only functional when Tcl has been compiled with **TCL_MEM_DEBUG**
defined at compile-time. When **TCL_MEM_DEBUG** is not defined, these
functions are all no-ops.

**Tcl_DumpActiveMemory** will output a list of all currently allocated
memory to the specified file. The information output for each allocated
block of memory is: starting and ending addresses (excluding guard
zone), size, source file where **ckalloc** was called to allocate the
block and line number in that file. It is especially useful to call
**Tcl_DumpActiveMemory** after the Tcl interpreter has been deleted.

**Tcl_InitMemory** adds the Tcl **memory** command to the interpreter
given by *interp*. **Tcl_InitMemory** is called by **Tcl_Main**.

**Tcl_ValidateAllMemory** forces a validation of the guard zones of all
currently allocated blocks of memory. Normally validation of a block
occurs when its freed, unless full validation is enabled, in which case
validation of all blocks occurs when **ckalloc** and **ckfree** are
called. This function forces the validation to occur at any point.

# SEE ALSO

TCL_MEM_DEBUG, memory

# KEYWORDS

memory, debug
