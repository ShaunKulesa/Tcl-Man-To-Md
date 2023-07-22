# NAME

Tcl_FindExecutable, Tcl_GetNameOfExecutable - identify or return the
name of the binary file containing the application

# SYNOPSIS

**#include \<tcl.h\>**

void **Tcl_FindExecutable**(*argv0*)

const char \* **Tcl_GetNameOfExecutable**()

# ARGUMENTS

The first command-line argument to the program, which gives the
application\'s name.

# DESCRIPTION

The **Tcl_FindExecutable** procedure computes the full path name of the
executable file from which the application was invoked and saves it for
Tcl\'s internal use. The executable\'s path name is needed for several
purposes in Tcl. For example, it is needed on some platforms in the
implementation of the **load** command. It is also returned by the
**info nameofexecutable** command.

On UNIX platforms this procedure is typically invoked as the very first
thing in the application\'s main program; it must be passed *argv\[0\]*
as its argument. It is important not to change the working directory
before the invocation. **Tcl_FindExecutable** uses *argv0* along with
the **PATH** environment variable to find the application\'s executable,
if possible. If it fails to find the binary, then future calls to **info
nameofexecutable** will return an empty string.

On Windows platforms this procedure is typically invoked as the very
first thing in the application\'s main program as well; Its *argv\[0\]*
argument is only used to indicate whether the executable has a stderr
channel (any non-null value) or not (the value null). If
**Tcl_SetPanicProc** is never called and no debugger is running, this
determines whether the panic message is sent to stderr or to a standard
system dialog.

**Tcl_GetNameOfExecutable** simply returns a pointer to the internal
full path name of the executable file as computed by
**Tcl_FindExecutable**. This procedure call is the C API equivalent to
the **info nameofexecutable** command. NULL is returned if the internal
full path name has not been computed or unknown.

# KEYWORDS

binary, executable file
