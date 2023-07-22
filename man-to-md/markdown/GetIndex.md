# NAME

Tcl_GetIndexFromObj, Tcl_GetIndexFromObjStruct - lookup string in table
of keywords

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_GetIndexFromObj**(*interp, objPtr, tablePtr, msg, flags,*
indexPtr)

int **Tcl_GetIndexFromObjStruct**(*interp, objPtr, structTablePtr,
offset,* msg, flags, indexPtr)

# ARGUMENTS

Interpreter to use for error reporting; if NULL, then no message is
provided on errors.

The string value of this value is used to search through *tablePtr*. The
internal representation is modified to hold the index of the matching
table entry.

An array of null-terminated strings. The end of the array is marked by a
NULL string pointer. Note that references to the *tablePtr* may be
retained in the internal representation of *objPtr*, so this should
represent the address of a statically-allocated array.

An array of arbitrary type, typically some **struct** type. The first
member of the structure must be a null-terminated string. The size of
the structure is given by *offset*. Note that references to the
*structTablePtr* may be retained in the internal representation of
*objPtr*, so this should represent the address of a statically-allocated
array of structures.

The offset to add to structTablePtr to get to the next entry. The end of
the array is marked by a NULL string pointer.

Null-terminated string describing what is being looked up, such as
**option**. This string is included in error messages.

OR-ed combination of bits providing additional information for
operation. The only bit that is currently defined is **TCL_EXACT**.

The index of the string in *tablePtr* that matches the value of *objPtr*
is returned here.

# DESCRIPTION

These procedures provide an efficient way for looking up keywords,
switch names, option names, and similar things where the literal value
of a Tcl value must be chosen from a predefined set.
**Tcl_GetIndexFromObj** compares *objPtr* against each of the strings in
*tablePtr* to find a match. A match occurs if *objPtr*\'s string value
is identical to one of the strings in *tablePtr*, or if it is a
non-empty unique abbreviation for exactly one of the strings in
*tablePtr* and the **TCL_EXACT** flag was not specified; in either case
the index of the matching entry is stored at *\*indexPtr* and **TCL_OK**
is returned.

If there is no matching entry, **TCL_ERROR** is returned and an error
message is left in *interp*\'s result if *interp* is not NULL. *Msg* is
included in the error message to indicate what was being looked up. For
example, if *msg* is **option** the error message will have a form like

If **Tcl_GetIndexFromObj** completes successfully it modifies the
internal representation of *objPtr* to hold the address of the table and
the index of the matching entry. If **Tcl_GetIndexFromObj** is invoked
again with the same *objPtr* and *tablePtr* arguments (e.g. during a
reinvocation of a Tcl command), it returns the matching index
immediately without having to redo the lookup operation. Note:
**Tcl_GetIndexFromObj** assumes that the entries in *tablePtr* are
static: they must not change between invocations. If the value of
*objPtr* is the empty string, **Tcl_GetIndexFromObj** will treat it as a
non-matching value and return **TCL_ERROR**.

**Tcl_GetIndexFromObjStruct** works just like **Tcl_GetIndexFromObj**,
except that instead of treating *tablePtr* as an array of string
pointers, it treats it as a pointer to the first string in a series of
strings that have *offset* bytes between them (i.e. that there is a
pointer to the first array of characters at *tablePtr*, a pointer to the
second array of characters at *tablePtr*+*offset* bytes, etc.) This is
particularly useful when processing things like
**Tk_ConfigurationSpec**, whose string keys are in the same place in
each of several array elements.

# SEE ALSO

prefix(n), Tcl_WrongNumArgs(3)

# KEYWORDS

index, option, value, table lookup

<!---
Copyright (c) 1997 Sun Microsystems, Inc
-->

