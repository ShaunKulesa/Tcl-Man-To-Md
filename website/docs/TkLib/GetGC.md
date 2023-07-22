# NAME

Tk_GetGC, Tk_FreeGC - maintain database of read-only graphics contexts

# SYNOPSIS

**#include \<tk.h\>**

GC **Tk_GetGC**(*tkwin, valueMask, valuePtr*)

**Tk_FreeGC(***display, gc*)

# ARGUMENTS

Token for window in which the graphics context will be used.

Mask of bits (such as **GCForeground** or **GCStipple**) indicating
which fields of *\*valuePtr* are valid.

Pointer to structure describing the desired values for the graphics
context.

Display for which *gc* was allocated.

X identifier for graphics context that is no longer needed. Must have
been allocated by **Tk_GetGC**.

# DESCRIPTION

**Tk_GetGC** and **Tk_FreeGC** manage a collection of graphics contexts
being used by an application. The procedures allow graphics contexts to
be shared, thereby avoiding the server overhead that would be incurred
if a separate GC were created for each use. **Tk_GetGC** takes arguments
describing the desired graphics context and returns an X identifier for
a GC that fits the description. The graphics context that is returned
will have default values in all of the fields not specified explicitly
by *valueMask* and *valuePtr*.

**Tk_GetGC** maintains a database of all the graphics contexts it has
created. Whenever possible, a call to **Tk_GetGC** will return an
existing graphics context rather than creating a new one. This approach
can substantially reduce server overhead, so **Tk_GetGC** should
generally be used in preference to the Xlib procedure **XCreateGC**,
which creates a new graphics context on each call.

Since the return values of **Tk_GetGC** are shared, callers should never
modify the graphics contexts returned by **Tk_GetGC**. If a graphics
context must be modified dynamically, then it should be created by
calling **XCreateGC** instead of **Tk_GetGC**.

When a graphics context is no longer needed, **Tk_FreeGC** should be
called to release it. There should be exactly one call to **Tk_FreeGC**
for each call to **Tk_GetGC**. When a graphics context is no longer in
use anywhere (i.e. it has been freed as many times as it has been
gotten) **Tk_FreeGC** will release it to the X server and delete it from
the database.

# KEYWORDS

graphics context
