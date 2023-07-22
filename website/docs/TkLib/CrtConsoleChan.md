# NAME

Tk_InitConsoleChannels - Install the console channels as standard
channels

# SYNOPSIS

**#include \<tk.h\>**

**Tk_InitConsoleChannels**(*interp*)

# ARGUMENTS

Interpreter in which the console channels are created.

# DESCRIPTION

**Tk_InitConsoleChannels** is invoked to create a set of console
channels and install them as the standard channels. All I/O on these
channels will be discarded until **Tk_CreateConsoleWindow** is called to
attach the console to a text widget.

This function is for use by shell applications based on Tk, like
**wish**, on platforms which have no standard channels in graphical
mode, like Win32.

The *interp* argument is the interpreter in which to create and install
the console channels.

**NOTE:** If this function is used it has to be called before the first
call to **Tcl_RegisterChannel**, directly, or indirectly through other
channel functions. Because otherwise the standard channels will be
already initialized to the system defaults, which will be nonsensical
for the case **Tk_InitConsoleChannels** is for.

# SEE ALSO

console(n)

# KEYWORDS

standard channels, console
