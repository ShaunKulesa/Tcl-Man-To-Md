# NAME

Tk_SetClass, Tk_Class - set or retrieve a window\'s class

# SYNOPSIS

**#include \<tk.h\>**

**Tk_SetClass**(*tkwin, class*)

Tk_Uid **Tk_Class**(*tkwin*)

# ARGUMENTS

Token for window.

New class name for window.

# DESCRIPTION

**Tk_SetClass** is called to associate a class with a particular window.
The *class* string identifies the type of the window; all windows with
the same general class of behavior (button, menu, etc.) should have the
same class. By convention all class names start with a capital letter,
and there exists a Tcl command with the same name as each class (except
all in lower-case) which can be used to create and manipulate windows of
that class. A window\'s class string is initialized to NULL when the
window is created.

For main windows, Tk automatically propagates the name and class to the
WM_CLASS property used by window managers. This happens either when a
main window is actually created (e.g. in **Tk_MakeWindowExist**), or
when **Tk_SetClass** is called, whichever occurs later. If a main window
has not been assigned a class then Tk will not set the WM_CLASS property
for the window.

**Tk_Class** is a macro that returns the current value of *tkwin*\'s
class. The value is returned as a Tk_Uid, which may be used just like a
string pointer but also has the properties of a unique identifier (see
the manual entry for **Tk_GetUid** for details). If *tkwin* has not yet
been given a class, then **Tk_Class** will return NULL.

# KEYWORDS

class, unique identifier, window, window manager

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

