# NAME

Tk_Main - main program for Tk-based applications

# SYNOPSIS

**#include \<tk.h\>**

**Tk_Main**(*argc, argv, appInitProc*)

# ARGUMENTS

Number of elements in *argv*.

Array of strings containing command-line arguments. On Windows, when
using -DUNICODE, the parameter type changes to wchar_t \*.

Address of an application-specific initialization procedure. The value
for this argument is usually **Tcl_AppInit**.

# DESCRIPTION

**Tk_Main** acts as the main program for most Tk-based applications.
Starting with Tk 4.0 it is not called **main** anymore because it is
part of the Tk library and having a function **main** in a library
(particularly a shared library) causes problems on many systems. Having
**main** in the Tk library would also make it hard to use Tk in C++
programs, since C++ programs must have special C++ **main** functions.

Normally each application contains a small **main** function that does
nothing but invoke **Tk_Main**. **Tk_Main** then does all the work of
creating and running a **wish**-like application.

When it is has finished its own initialization, but before it processes
commands, **Tk_Main** calls the procedure given by the *appInitProc*
argument. This procedure provides a for the application to perform its
own initialization, such as defining application-specific commands. The
procedure must have an interface that matches the type
**Tcl_AppInitProc**:

    typedef int Tcl_AppInitProc(
            Tcl_Interp *interp);

*AppInitProc* is almost always a pointer to **Tcl_AppInit**; for more
details on this procedure, see the documentation for **Tcl_AppInit**.

**Tk_Main** functions much the same as **Tcl_Main**. In particular,
**Tk_Main** supports both an interactive mode and a startup script mode,
with the file name and encoding of a startup script under the control of
the **Tcl_SetStartupScript** and **Tcl_GetStartupScript** routines.
However it calls **Tk_MainLoop** after processing any supplied script,
and in interactive uses events registered with **Tcl_CreateFileHandler**
to process user input.

# SEE ALSO

Tcl_DoOneEvent(3)

# KEYWORDS

application-specific initialization, command-line arguments, main
program
