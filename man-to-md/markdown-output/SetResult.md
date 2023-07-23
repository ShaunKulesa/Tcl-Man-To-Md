# NAME

Tcl_SetObjResult, Tcl_GetObjResult, Tcl_SetResult, Tcl_GetStringResult,
Tcl_AppendResult, Tcl_AppendResultVA, Tcl_AppendElement,
Tcl_ResetResult, Tcl_TransferResult, Tcl_FreeResult - manipulate Tcl
result

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_SetObjResult**(*interp, objPtr*)

Tcl_Obj \* **Tcl_GetObjResult**(*interp*)

**Tcl_SetResult**(*interp, result, freeProc*)

const char \* **Tcl_GetStringResult**(*interp*)

**Tcl_AppendResult**(*interp, result, result, \... , ***(char \*)
NULL**)

**Tcl_AppendResultVA**(*interp, argList*)

**Tcl_ResetResult**(*interp*)

**Tcl_TransferResult**(*sourceInterp, code, targetInterp*)

**Tcl_AppendElement**(*interp, element*)

**Tcl_FreeResult**(*interp*)

# ARGUMENTS

Interpreter whose result is to be modified or read.

Tcl value to become result for *interp*.

String value to become result for *interp* or to be appended to the
existing result.

String value to append as a list element to the existing result of
*interp*.

Address of procedure to call to release storage at *result*, or
**TCL_STATIC**, **TCL_DYNAMIC**, or **TCL_VOLATILE**.

An argument list which must have been initialized using **va_start**,
and cleared using **va_end**.

Interpreter that the result and return options should be transferred
from.

Interpreter that the result and return options should be transferred to.

Return code value that controls transfer of return options.

# DESCRIPTION

The procedures described here are utilities for manipulating the result
value in a Tcl interpreter. The interpreter result may be either a Tcl
value or a string. For example, **Tcl_SetObjResult** and
**Tcl_SetResult** set the interpreter result to, respectively, a value
and a string. Similarly, **Tcl_GetObjResult** and
**Tcl_GetStringResult** return the interpreter result as a value and as
a string. The procedures always keep the string and value forms of the
interpreter result consistent. For example, if **Tcl_SetObjResult** is
called to set the result to a value, then **Tcl_GetStringResult** is
called, it will return the value\'s string representation.

**Tcl_SetObjResult** arranges for *objPtr* to be the result for
*interp*, replacing any existing result. The result is left pointing to
the value referenced by *objPtr*. *objPtr*\'s reference count is
incremented since there is now a new reference to it from *interp*. The
reference count for any old result value is decremented and the old
result value is freed if no references to it remain.

**Tcl_GetObjResult** returns the result for *interp* as a value. The
value\'s reference count is not incremented; if the caller needs to
retain a long-term pointer to the value they should use
**Tcl_IncrRefCount** to increment its reference count in order to keep
it from being freed too early or accidentally changed.

**Tcl_SetResult** arranges for *result* to be the result for the current
Tcl command in *interp*, replacing any existing result. The *freeProc*
argument specifies how to manage the storage for the *result* argument;
it is discussed in the section **THE TCL_FREEPROC ARGUMENT TO
TCL_SETRESULT** below. If *result* is **NULL**, then *freeProc* is
ignored and **Tcl_SetResult** re-initializes *interp*\'s result to point
to an empty string.

**Tcl_GetStringResult** returns the result for *interp* as a string. If
the result was set to a value by a **Tcl_SetObjResult** call, the value
form will be converted to a string and returned. If the value\'s string
representation contains null bytes, this conversion will lose
information. For this reason, programmers are encouraged to write their
code to use the new value API procedures and to call
**Tcl_GetObjResult** instead.

**Tcl_ResetResult** clears the result for *interp* and leaves the result
in its normal empty initialized state. If the result is a value, its
reference count is decremented and the result is left pointing to an
unshared value representing an empty string. If the result is a
dynamically allocated string, its memory is free\*d and the result is
left as a empty string. **Tcl_ResetResult** also clears the error state
managed by **Tcl_AddErrorInfo**, **Tcl_AddObjErrorInfo**, and
**Tcl_SetErrorCode**.

**Tcl_AppendResult** makes it easy to build up Tcl results in pieces. It
takes each of its *result* arguments and appends them in order to the
current result associated with *interp*. If the result is in its
initialized empty state (e.g. a command procedure was just invoked or
**Tcl_ResetResult** was just called), then **Tcl_AppendResult** sets the
result to the concatenation of its *result* arguments.
**Tcl_AppendResult** may be called repeatedly as additional pieces of
the result are produced. **Tcl_AppendResult** takes care of all the
storage management issues associated with managing *interp*\'s result,
such as allocating a larger result area if necessary. It also manages
conversion to and from the *result* field of the *interp* so as to
handle backward-compatibility with old-style extensions. Any number of
*result* arguments may be passed in a single call; the last argument in
the list must be a NULL pointer.

**Tcl_AppendResultVA** is the same as **Tcl_AppendResult** except that
instead of taking a variable number of arguments it takes an argument
list.

**Tcl_TransferResult** transfers interpreter state from *sourceInterp*
to *targetInterp*. The two interpreters must have been created in the
same thread. If *sourceInterp* and *targetInterp* are the same, nothing
is done. Otherwise, **Tcl_TransferResult** moves the result from
*sourceInterp* to *targetInterp*, and resets the result in
*sourceInterp*. It also moves the return options dictionary as
controlled by the return code value *code* in the same manner as
**Tcl_GetReturnOptions**.

# DEPRECATED INTERFACES

## OLD STRING PROCEDURES

Use of the following procedures is deprecated since they manipulate the
Tcl result as a string. Procedures such as **Tcl_SetObjResult** that
manipulate the result as a value can be significantly more efficient.

**Tcl_AppendElement** is similar to **Tcl_AppendResult** in that it
allows results to be built up in pieces. However, **Tcl_AppendElement**
takes only a single *element* argument and it appends that argument to
the current result as a proper Tcl list element. **Tcl_AppendElement**
adds backslashes or braces if necessary to ensure that *interp*\'s
result can be parsed as a list and that *element* will be extracted as a
single element. Under normal conditions, **Tcl_AppendElement** will add
a space character to *interp*\'s result just before adding the new list
element, so that the list elements in the result are properly separated.
However if the new list element is the first in a list or sub-list (i.e.
*interp*\'s current result is empty, or consists of the single character
or ends in the characters then no space is added.

**Tcl_FreeResult** performs part of the work of **Tcl_ResetResult**. It
frees up the memory associated with *interp*\'s result. It also sets
*interp-\>freeProc* to zero, but does not change *interp-\>result* or
clear error state. **Tcl_FreeResult** is most commonly used when a
procedure is about to replace one result value with another.

## DIRECT ACCESS TO INTERP-\>RESULT

It used to be legal for programs to directly read and write
*interp-\>result* to manipulate the interpreter result. The Tcl headers
no longer permit this access by default, and C code still doing this
must be updated to use supported routines **Tcl_GetObjResult**,
**Tcl_GetStringResult**, **Tcl_SetObjResult**, and **Tcl_SetResult**. As
a migration aid, access can be restored with the compiler directive

    #define USE_INTERP_RESULT

but this is meant only to offer life support to otherwise dead code.

# THE TCL_FREEPROC ARGUMENT TO TCL_SETRESULT

**Tcl_SetResult**\'s *freeProc* argument specifies how the Tcl system is
to manage the storage for the *result* argument. If **Tcl_SetResult** or
**Tcl_SetObjResult** are called at a time when *interp* holds a string
result, they do whatever is necessary to dispose of the old string
result (see the **Tcl_Interp** manual entry for details on this).

If *freeProc* is **TCL_STATIC** it means that *result* refers to an area
of static storage that is guaranteed not to be modified until at least
the next call to **Tcl_Eval**. If *freeProc* is **TCL_DYNAMIC** it means
that *result* was allocated with a call to **Tcl_Alloc** and is now the
property of the Tcl system. **Tcl_SetResult** will arrange for the
string\'s storage to be released by calling **Tcl_Free** when it is no
longer needed. If *freeProc* is **TCL_VOLATILE** it means that *result*
points to an area of memory that is likely to be overwritten when
**Tcl_SetResult** returns (e.g. it points to something in a stack
frame). In this case **Tcl_SetResult** will make a copy of the string in
dynamically allocated storage and arrange for the copy to be the result
for the current Tcl command.

If *freeProc* is not one of the values **TCL_STATIC**, **TCL_DYNAMIC**,
and **TCL_VOLATILE**, then it is the address of a procedure that Tcl
should call to free the string. This allows applications to use
non-standard storage allocators. When Tcl no longer needs the storage
for the string, it will call *freeProc*. *FreeProc* should have
arguments and result that match the type **Tcl_FreeProc**:

    typedef void Tcl_FreeProc(
            char *blockPtr);

When *freeProc* is called, its *blockPtr* will be set to the value of
*result* passed to **Tcl_SetResult**.

# SEE ALSO

Tcl_AddErrorInfo, Tcl_CreateObjCommand, Tcl_SetErrorCode, Tcl_Interp,
Tcl_GetReturnOptions

# KEYWORDS

append, command, element, list, value, result, return value, interpreter

<!---
Copyright (c) 1989-1993 The Regents of the University of California
Copyright (c) 1994-1997 Sun Microsystems, Inc
-->

