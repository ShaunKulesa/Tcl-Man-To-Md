# NAME

Tk_HWNDToWindow - Find Tk\'s window information for a Windows window

# SYNOPSIS

**#include \<tkPlatDecls.h\>**

Tk_Window **Tk_HWNDToWindow**(*hwnd*)

# ARGUMENTS

Windows handle for the window.

# DESCRIPTION

Given a Windows HWND window identifier, this procedure returns the
corresponding Tk_Window handle. If there is no Tk_Window corresponding
to *hwnd* then NULL is returned.

# KEYWORDS

Windows window id

<!---
Copyright (c) 1998-2000 by Scriptics Corporation
-->

