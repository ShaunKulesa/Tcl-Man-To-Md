# NAME

Tcl_Alloc, Tcl_Free, Tcl_Realloc, Tcl_AttemptAlloc, Tcl_AttemptRealloc,
Tcl_GetMemoryInfo, ckalloc, ckfree, ckrealloc, attemptckalloc,
attemptckrealloc - allocate or free heap memory

# SYNOPSIS

**#include \<tcl.h\>**

char \* **Tcl_Alloc**(*size*)

void **Tcl_Free**(*ptr*)

char \* **Tcl_Realloc**(*ptr, size*)

char \* **Tcl_AttemptAlloc**(*size*)

char \* **Tcl_AttemptRealloc**(*ptr, size*)

void **Tcl_GetMemoryInfo**(*dsPtr*)

char \* **ckalloc**(*size*)

void **ckfree**(*ptr*)

char \* **ckrealloc**(*ptr, size*)

char \* **attemptckalloc**(*size*)

char \* **attemptckrealloc**(*ptr, size*)

# ARGUMENTS

Size in bytes of the memory block to allocate.

Pointer to memory block to free or realloc.

Initialized DString pointer.

# DESCRIPTION

These procedures provide a platform and compiler independent interface
for memory allocation. Programs that need to transfer ownership of
memory blocks between Tcl and other modules should use these routines
rather than the native **malloc()** and **free()** routines provided by
the C run-time library.

**Tcl_Alloc** returns a pointer to a block of at least *size* bytes
suitably aligned for any use.

**Tcl_Free** makes the space referred to by *ptr* available for further
allocation.

**Tcl_Realloc** changes the size of the block pointed to by *ptr* to
*size* bytes and returns a pointer to the new block. The contents will
be unchanged up to the lesser of the new and old sizes. The returned
location may be different from *ptr*. If *ptr* is NULL, this is
equivalent to calling **Tcl_Alloc** with just the *size* argument.

**Tcl_AttemptAlloc** and **Tcl_AttemptRealloc** are identical in
function to **Tcl_Alloc** and **Tcl_Realloc**, except that
**Tcl_AttemptAlloc** and **Tcl_AttemptRealloc** will not cause the Tcl
interpreter to **panic** if the memory allocation fails. If the
allocation fails, these functions will return NULL. Note that on some
platforms, but not all, attempting to allocate a zero-sized block of
memory will also cause these functions to return NULL.

The procedures **ckalloc**, **ckfree**, **ckrealloc**,
**attemptckalloc**, and **attemptckrealloc** are implemented as macros.
Normally, they are synonyms for the corresponding procedures documented
on this page. When Tcl and all modules calling Tcl are compiled with
**TCL_MEM_DEBUG** defined, however, these macros are redefined to be
special debugging versions of these procedures. To support Tcl\'s memory
debugging within a module, use the macros rather than direct calls to
**Tcl_Alloc**, etc.

**Tcl_GetMemoryInfo** appends a list-of-lists of memory stats to the
provided DString. This function cannot be used in stub-enabled
extensions, and it is only available if Tcl is compiled with the
threaded memory allocator.

# KEYWORDS

alloc, allocation, free, malloc, memory, realloc, TCL_MEM_DEBUG

<!---
Copyright (c) 1995-1996 Sun Microsystems, Inc
-->

