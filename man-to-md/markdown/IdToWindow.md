# NAME

Tk_IdToWindow - Find Tk\'s window information for an X window

# SYNOPSIS

**#include \<tk.h\>**

Tk_Window **Tk_IdToWindow**(*display, window*)

# ARGUMENTS

X display containing the window.

X id for window.

# DESCRIPTION

Given an X window identifier and the X display it corresponds to, this
procedure returns the corresponding Tk_Window handle. If there is no
Tk_Window corresponding to *window* then NULL is returned.

# KEYWORDS

X window id

<!---
Copyright (c) 1995-1996 Sun Microsystems, Inc
-->

