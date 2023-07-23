# NAME

Tk_GetHWND, Tk_AttachHWND - manage interactions between the Windows
handle and an X window

# SYNOPSIS

**#include \<tkPlatDecls.h\>**

HWND **Tk_GetHWND**(*window*)

Window **Tk_AttachHWND**(*tkwin, hwnd*)

# ARGUMENTS

X token for window.

Tk window for window.

Windows HWND for window.

# DESCRIPTION

**Tk_GetHWND** returns the Windows HWND identifier for X Windows window
given by *window*.

**Tk_AttachHWND** binds the Windows HWND identifier to the specified
Tk_Window given by *tkwin*. It returns an X Windows window that
encapsulates the HWND.

# KEYWORDS

identifier, window

<!---
Copyright (c) 1998-2000 by Scriptics Corporation
-->

