# NAME

Tk_GetSelection - retrieve the contents of a selection

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetSelection**(*interp, tkwin, selection, target, proc,
clientData*)

# ARGUMENTS

Interpreter to use for reporting errors.

Window on whose behalf to retrieve the selection (determines display
from which to retrieve).

The name of the selection to be retrieved.

Form in which to retrieve selection.

Procedure to invoke to process pieces of the selection as they are
retrieved.

Arbitrary one-word value to pass to *proc*.

# DESCRIPTION

**Tk_GetSelection** retrieves the selection specified by the atom
*selection* in the format specified by *target*. The selection may
actually be retrieved in several pieces; as each piece is retrieved,
*proc* is called to process the piece. *Proc* should have arguments and
result that match the type **Tk_GetSelProc**:

    typedef int Tk_GetSelProc(
            ClientData clientData,
            Tcl_Interp *interp,
            char *portion);

The *clientData* and *interp* parameters to *proc* will be copies of the
corresponding arguments to **Tk_GetSelection**. *Portion* will be a
pointer to a string containing part or all of the selection. For large
selections, *proc* will be called several times with successive portions
of the selection. The X Inter-Client Communication Conventions Manual
allows a selection to be returned in formats other than strings, e.g. as
an array of atoms or integers. If this happens, Tk converts the
selection back into a string before calling *proc*. If a selection is
returned as an array of atoms, Tk converts it to a string containing the
atom names separated by white space. For any other format besides
string, Tk converts a selection to a string containing hexadecimal
values separated by white space.

**Tk_GetSelection** returns to its caller when the selection has been
completely retrieved and processed by *proc*, or when a fatal error has
occurred (e.g. the selection owner did not respond promptly).
**Tk_GetSelection** normally returns **TCL_OK**; if an error occurs, it
returns **TCL_ERROR** and leaves an error message in interpreter
*interp*\'s result. *Proc* should also return either **TCL_OK** or
**TCL_ERROR**. If *proc* encounters an error in dealing with the
selection, it should leave an error message in the interpreter result
and return **TCL_ERROR**; this will abort the selection retrieval.

# KEYWORDS

format, get, selection retrieval
