# NAME

Tcl_SignalId, Tcl_SignalMsg - Convert signal codes

# SYNOPSIS

**#include \<tcl.h\>**

const char \* **Tcl_SignalId**(*sig*)

const char \* **Tcl_SignalMsg**(*sig*)

# ARGUMENTS

A POSIX signal number such as **SIGPIPE**.

# DESCRIPTION

**Tcl_SignalId** and **Tcl_SignalMsg** return a string representation of
the provided signal number (*sig*). **Tcl_SignalId** returns a
machine-readable textual identifier such as **Tcl_SignalMsg** returns a
human-readable string such as The strings returned by these functions
are statically allocated and the caller must not free or modify them.

# KEYWORDS

signals, signal numbers
