# NAME

Tk_ClearSelection - Deselect a selection

# SYNOPSIS

**#include \<tk.h\>**

**Tk_ClearSelection**(*tkwin, selection*)

# ARGUMENTS

The selection will be cleared from the display containing this window.

The name of selection to be cleared.

# DESCRIPTION

**Tk_ClearSelection** cancels the selection specified by the atom
*selection* for the display containing *tkwin*. The selection need not
be in *tkwin* itself or even in *tkwin*\'s application. If there is a
window anywhere on *tkwin*\'s display that owns *selection*, the window
will be notified and the selection will be cleared. If there is no owner
for *selection* on the display, then the procedure has no effect.

# KEYWORDS

clear, selection
