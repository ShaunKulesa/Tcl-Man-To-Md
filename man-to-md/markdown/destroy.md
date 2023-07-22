# NAME

destroy - Destroy one or more windows

# SYNOPSIS

**destroy **?*window window \...*?

# DESCRIPTION

This command deletes the windows given by the *window* arguments, plus
all of their descendants. If a *window* is deleted then all windows will
be destroyed and the application will (normally) exit. The *window*s are
destroyed in order, and if an error occurs in destroying a window the
command aborts without destroying the remaining windows. No error is
returned if *window* does not exist.

# EXAMPLE

Destroy all checkbuttons that are direct children of the given widget:

    proc killCheckbuttonChildren {parent} {
       foreach w [winfo children $parent] {
          if {[winfo class $w] eq "Checkbutton"} {
             destroy $w
          }
       }
    }

# KEYWORDS

application, destroy, window

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

