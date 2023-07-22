# NAME

Tk_CreateSelHandler, Tk_DeleteSelHandler - arrange to handle requests
for a selection

# SYNOPSIS

**#include \<tk.h\>**

**Tk_CreateSelHandler**(*tkwin, selection, target, proc, clientData,
format*)

**Tk_DeleteSelHandler**(*tkwin, selection, target*)

# ARGUMENTS

Window for which *proc* will provide selection information.

The name of the selection for which *proc* will provide selection
information.

Form in which *proc* can provide the selection (e.g. STRING or
FILE_NAME). Corresponds to *type* arguments in **selection** commands.

Procedure to invoke whenever the selection is owned by *tkwin* and the
selection contents are requested in the format given by *target*.

Arbitrary one-word value to pass to *proc*.

If the selection requestor is not in this process, *format* determines
the representation used to transmit the selection to its requestor.

# DESCRIPTION

**Tk_CreateSelHandler** arranges for a particular procedure (*proc*) to
be called whenever *selection* is owned by *tkwin* and the selection
contents are requested in the form given by *target*. *Target* should be
one of the entries defined in the left column of Table 2 of the X
Inter-Client Communication Conventions Manual (ICCCM) or any other form
in which an application is willing to present the selection. The most
common form is STRING.

*Proc* should have arguments and result that match the type
**Tk_SelectionProc**:

    typedef int Tk_SelectionProc(
            ClientData clientData,
            int offset,
            char *buffer,
            int maxBytes);

The *clientData* parameter to *proc* is a copy of the *clientData*
argument given to **Tk_CreateSelHandler**. Typically, *clientData*
points to a data structure containing application-specific information
that is needed to retrieve the selection. *Offset* specifies an offset
position into the selection, *buffer* specifies a location at which to
copy information about the selection, and *maxBytes* specifies the
amount of space available at *buffer*. *Proc* should place a
NULL-terminated string at *buffer* containing *maxBytes* or fewer
characters (not including the terminating NULL), and it should return a
count of the number of non-NULL characters stored at *buffer*. If the
selection no longer exists (e.g. it once existed but the user deleted
the range of characters containing it), then *proc* should return -1.

When transferring large selections, Tk will break them up into smaller
pieces (typically a few thousand bytes each) for more efficient
transmission. It will do this by calling *proc* one or more times, using
successively higher values of *offset* to retrieve successive portions
of the selection. If *proc* returns a count less than *maxBytes* it
means that the entire remainder of the selection has been returned. If
*proc*\'s return value is *maxBytes* it means there may be additional
information in the selection, so Tk must make another call to *proc* to
retrieve the next portion.

*Proc* always returns selection information in the form of a character
string. However, the ICCCM allows for information to be transmitted from
the selection owner to the selection requestor in any of several
formats, such as a string, an array of atoms, an array of integers, etc.
The *format* argument to **Tk_CreateSelHandler** indicates what format
should be used to transmit the selection to its requestor (see the
middle column of Table 2 of the ICCCM for examples). If *format* is not
STRING, then Tk will take the value returned by *proc* and divided it
into fields separated by white space. If *format* is ATOM, then Tk will
return the selection as an array of atoms, with each field in *proc*\'s
result treated as the name of one atom. For any other value of *format*,
Tk will return the selection as an array of 32-bit values where each
field of *proc*\'s result is treated as a number and translated to a
32-bit value. In any event, the *format* atom is returned to the
selection requestor along with the contents of the selection.

If **Tk_CreateSelHandler** is called when there already exists a handler
for *selection* and *target* on *tkwin*, then the existing handler is
replaced with a new one.

**Tk_DeleteSelHandler** removes the handler given by *tkwin*,
*selection*, and *target*, if such a handler exists. If there is no such
handler then it has no effect.

# KEYWORDS

format, handler, selection, target
