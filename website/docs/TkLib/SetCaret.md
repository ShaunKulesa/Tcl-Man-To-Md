# NAME

Tk_SetCaretPos - set the display caret location

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_SetCaretPos**(*tkwin, x, y, height*)

# ARGUMENTS

Token for window.

Window-relative x coordinate.

Window-relative y coordinate.

Height of the caret in the window.

# DESCRIPTION

**Tk_SetCaretPos** sets the caret location for the display of the
specified Tk_Window *tkwin*. The caret is the per-display cursor
location used for indicating global focus (e.g. to comply with Microsoft
Accessibility guidelines), as well as for location of the over-the-spot
XIM (X Input Methods) or Windows IME windows.

# KEYWORDS

caret, cursor
