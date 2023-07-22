# NAME

Tcl_Sleep - delay execution for a given number of milliseconds

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_Sleep**(*ms*)

# ARGUMENTS

Number of milliseconds to sleep.

# DESCRIPTION

This procedure delays the calling process by the number of milliseconds
given by the *ms* parameter and returns after that time has elapsed. It
is typically used for things like flashing a button, where the delay is
short and the application need not do anything while it waits. For
longer delays where the application needs to respond to other events
during the delay, the procedure **Tcl_CreateTimerHandler** should be
used instead of **Tcl_Sleep**.

# KEYWORDS

sleep, time, wait
