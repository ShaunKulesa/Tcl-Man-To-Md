# NAME

Tk_Init, Tk_SafeInit - add Tk to an interpreter and make a new Tk
application.

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_Init**(*interp*)

int **Tk_SafeInit**(*interp*)

# ARGUMENTS

Interpreter in which to load Tk. Tk should not already be loaded in this
interpreter.

# DESCRIPTION

**Tk_Init** is the package initialization procedure for Tk. It is
normally invoked by the **Tcl_AppInit** procedure for an application or
by the **load** command. **Tk_Init** adds all of Tk\'s commands to
*interp* and creates a new Tk application, including its main window. If
the initialization is successful **Tk_Init** returns **TCL_OK**; if
there is an error it returns **TCL_ERROR**. **Tk_Init** also leaves a
result or error message in interpreter *interp*\'s result.

If there is a variable **argv** in *interp*, **Tk_Init** treats the
contents of this variable as a list of options for the new Tk
application. The options may have any of the forms documented for the
**wish** application (in fact, **wish** uses Tk_Init to process its
command-line arguments).

**Tk_SafeInit** is identical to **Tk_Init** except that it removes all
Tk commands that are considered unsafe. Those commands and the reasons
for their exclusion are:

**bell**

:   Continuous ringing of the bell is a nuisance.

**clipboard**

:   A malicious script could replace the contents of the clipboard with
    the string and lead to surprises when the contents of the clipboard
    are pasted.

**grab**

:   Grab can be used to block the user from using any other
    applications.

**menu**

:   Menus can be used to cover the entire screen and to steal input from
    the user.

**selection**

:   See clipboard.

**send**

:   Send can be used to cause unsafe interpreters to execute commands.

**tk**

:   The tk command recreates the send command, which is unsafe.

**tkwait**

:   Tkwait can block the containing process forever

**toplevel**

:   Toplevels can be used to cover the entire screen and to steal input
    from the user.

**wm**

:   If toplevels are ever allowed, wm can be used to remove decorations,
    move windows around, etc.

# KEYWORDS

safe, application, initialization, load, main window

<!---
Copyright (c) 1995-1996 Sun Microsystems, Inc
-->

