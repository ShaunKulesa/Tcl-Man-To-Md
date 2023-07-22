# NAME

Tcl_LinkVar, Tcl_UnlinkVar, Tcl_UpdateLinkedVar - link Tcl variable to C
variable

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_LinkVar**(*interp, varName, addr, type*)

**Tcl_UnlinkVar**(*interp, varName*)

**Tcl_UpdateLinkedVar**(*interp, varName*)

# ARGUMENTS

Interpreter that contains *varName*. Also used by **Tcl_LinkVar** to
return error messages.

Name of global variable.

Address of C variable that is to be linked to *varName*.

Type of C variable. Must be one of **TCL_LINK_INT**, **TCL_LINK_UINT**,
**TCL_LINK_CHAR**, **TCL_LINK_UCHAR**, **TCL_LINK_SHORT**,
**TCL_LINK_USHORT**, **TCL_LINK_LONG**, **TCL_LINK_ULONG**,
**TCL_LINK_WIDE_INT**, **TCL_LINK_WIDE_UINT**, **TCL_LINK_FLOAT**,
**TCL_LINK_DOUBLE**, **TCL_LINK_BOOLEAN**, or **TCL_LINK_STRING**,
optionally OR\'ed with **TCL_LINK_READ_ONLY** to make Tcl variable
read-only.

# DESCRIPTION

**Tcl_LinkVar** uses variable traces to keep the Tcl variable named by
*varName* in sync with the C variable at the address given by *addr*.
Whenever the Tcl variable is read the value of the C variable will be
returned, and whenever the Tcl variable is written the C variable will
be updated to have the same value. **Tcl_LinkVar** normally returns
**TCL_OK**; if an error occurs while setting up the link (e.g. because
*varName* is the name of array) then **TCL_ERROR** is returned and the
interpreter\'s result contains an error message.

The *type* argument specifies the type of the C variable, and must have
one of the following values, optionally OR\'ed with
**TCL_LINK_READ_ONLY**:

**TCL_LINK_INT**

:   The C variable is of type **int**. Any value written into the Tcl
    variable must have a proper integer form acceptable to
    **Tcl_GetIntFromObj**; attempts to write non-integer values into
    *varName* will be rejected with Tcl errors. Incomplete integer
    representations (like the empty string, \'+\', \'-\' or the
    hex/octal/binary prefix) are accepted as if they are valid too.

**TCL_LINK_UINT**

:   The C variable is of type **unsigned int**. Any value written into
    the Tcl variable must have a proper unsigned integer form acceptable
    to **Tcl_GetWideIntFromObj** and in the platform\'s defined range
    for the **unsigned int** type; attempts to write non-integer values
    (or values outside the range) into *varName* will be rejected with
    Tcl errors. Incomplete integer representations (like the empty
    string, \'+\', \'-\' or the hex/octal/binary prefix) are accepted as
    if they are valid too.

**TCL_LINK_CHAR**

:   The C variable is of type **char**. Any value written into the Tcl
    variable must have a proper integer form acceptable to
    **Tcl_GetIntFromObj** and be in the range of the **char** datatype;
    attempts to write non-integer or out-of-range values into *varName*
    will be rejected with Tcl errors. Incomplete integer representations
    (like the empty string, \'+\', \'-\' or the hex/octal/binary prefix)
    are accepted as if they are valid too.

**TCL_LINK_UCHAR**

:   The C variable is of type **unsigned char**. Any value written into
    the Tcl variable must have a proper unsigned integer form acceptable
    to **Tcl_GetIntFromObj** and in the platform\'s defined range for
    the **unsigned char** type; attempts to write non-integer values (or
    values outside the range) into *varName* will be rejected with Tcl
    errors. Incomplete integer representations (like the empty string,
    \'+\', \'-\' or the hex/octal/binary prefix) are accepted as if they
    are valid too.

**TCL_LINK_SHORT**

:   The C variable is of type **short**. Any value written into the Tcl
    variable must have a proper integer form acceptable to
    **Tcl_GetIntFromObj** and be in the range of the **short** datatype;
    attempts to write non-integer or out-of-range values into *varName*
    will be rejected with Tcl errors. Incomplete integer representations
    (like the empty string, \'+\', \'-\' or the hex/octal/binary prefix)
    are accepted as if they are valid too.

**TCL_LINK_USHORT**

:   The C variable is of type **unsigned short**. Any value written into
    the Tcl variable must have a proper unsigned integer form acceptable
    to **Tcl_GetIntFromObj** and in the platform\'s defined range for
    the **unsigned short** type; attempts to write non-integer values
    (or values outside the range) into *varName* will be rejected with
    Tcl errors. Incomplete integer representations (like the empty
    string, \'+\', \'-\' or the hex/octal/binary prefix) are accepted as
    if they are valid too.

**TCL_LINK_LONG**

:   The C variable is of type **long**. Any value written into the Tcl
    variable must have a proper integer form acceptable to
    **Tcl_GetLongFromObj**; attempts to write non-integer or
    out-of-range values into *varName* will be rejected with Tcl errors.
    Incomplete integer representations (like the empty string, \'+\',
    \'-\' or the hex/octal/binary prefix) are accepted as if they are
    valid too.

**TCL_LINK_ULONG**

:   The C variable is of type **unsigned long**. Any value written into
    the Tcl variable must have a proper unsigned integer form acceptable
    to **Tcl_GetWideIntFromObj** and in the platform\'s defined range
    for the **unsigned long** type; attempts to write non-integer values
    (or values outside the range) into *varName* will be rejected with
    Tcl errors. Incomplete integer representations (like the empty
    string, \'+\', \'-\' or the hex/octal/binary prefix) are accepted as
    if they are valid too.

**TCL_LINK_DOUBLE**

:   The C variable is of type **double**. Any value written into the Tcl
    variable must have a proper real form acceptable to
    **Tcl_GetDoubleFromObj**; attempts to write non-real values into
    *varName* will be rejected with Tcl errors. Incomplete integer or
    real representations (like the empty string, \'.\', \'+\', \'-\' or
    the hex/octal/binary prefix) are accepted as if they are valid too.

**TCL_LINK_FLOAT**

:   The C variable is of type **float**. Any value written into the Tcl
    variable must have a proper real form acceptable to
    **Tcl_GetDoubleFromObj** and must be within the range acceptable for
    a **float**; attempts to write non-real values (or values outside
    the range) into *varName* will be rejected with Tcl errors.
    Incomplete integer or real representations (like the empty string,
    \'.\', \'+\', \'-\' or the hex/octal/binary prefix) are accepted as
    if they are valid too.

**TCL_LINK_WIDE_INT**

:   The C variable is of type **Tcl_WideInt** (which is an integer type
    at least 64-bits wide on all platforms that can support it.) Any
    value written into the Tcl variable must have a proper integer form
    acceptable to **Tcl_GetWideIntFromObj**; attempts to write
    non-integer values into *varName* will be rejected with Tcl errors.
    Incomplete integer representations (like the empty string, \'+\',
    \'-\' or the hex/octal/binary prefix) are accepted as if they are
    valid too.

**TCL_LINK_WIDE_UINT**

:   The C variable is of type **Tcl_WideUInt** (which is an unsigned
    integer type at least 64-bits wide on all platforms that can support
    it.) Any value written into the Tcl variable must have a proper
    unsigned integer form acceptable to **Tcl_GetWideIntFromObj** (it
    will be cast to unsigned); attempts to write non-integer values into
    *varName* will be rejected with Tcl errors. Incomplete integer
    representations (like the empty string, \'+\', \'-\' or the
    hex/octal/binary prefix) are accepted as if they are valid too.

**TCL_LINK_BOOLEAN**

:   The C variable is of type **int**. If its value is zero then it will
    read from Tcl as otherwise it will read from Tcl as Whenever
    *varName* is modified, the C variable will be set to a 0 or 1 value.
    Any value written into the Tcl variable must have a proper boolean
    form acceptable to **Tcl_GetBooleanFromObj**; attempts to write
    non-boolean values into *varName* will be rejected with Tcl errors.

**TCL_LINK_STRING**

:   The C variable is of type **char \***. If its value is not NULL then
    it must be a pointer to a string allocated with **Tcl_Alloc** or
    **ckalloc**. Whenever the Tcl variable is modified the current C
    string will be freed and new memory will be allocated to hold a copy
    of the variable\'s new value. If the C variable contains a NULL
    pointer then the Tcl variable will read as

If the **TCL_LINK_READ_ONLY** flag is present in *type* then the
variable will be read-only from Tcl, so that its value can only be
changed by modifying the C variable. Attempts to write the variable from
Tcl will be rejected with errors.

**Tcl_UnlinkVar** removes the link previously set up for the variable
given by *varName*. If there does not exist a link for *varName* then
the procedure has no effect.

**Tcl_UpdateLinkedVar** may be invoked after the C variable has changed
to force the Tcl variable to be updated immediately. In many cases this
procedure is not needed, since any attempt to read the Tcl variable will
return the latest value of the C variable. However, if a trace has been
set on the Tcl variable (such as a Tk widget that wishes to display the
value of the variable), the trace will not trigger when the C variable
has changed. **Tcl_UpdateLinkedVar** ensures that any traces on the Tcl
variable are invoked.

Note that, as with any call to a Tcl interpreter,
**Tcl_UpdateLinkedVar** must be called from the same thread that created
the interpreter. The safest mechanism is to ensure that the C variable
is only ever updated from the same thread that created the interpreter
(possibly in response to an event posted with **Tcl_ThreadQueueEvent**),
but when it is necessary to update the variable in a separate thread, it
is advised that **Tcl_AsyncMark** be used to indicate to the thread
hosting the interpreter that it is ready to run **Tcl_UpdateLinkedVar**.

# SEE ALSO

Tcl_TraceVar(3)

# KEYWORDS

boolean, integer, link, read-only, real, string, trace, variable

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

