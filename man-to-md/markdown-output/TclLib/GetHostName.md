# NAME

Tcl_GetHostName - get the name of the local host

# SYNOPSIS

**#include \<tcl.h\>**

const char \* **Tcl_GetHostName**()

# DESCRIPTION

**Tcl_GetHostName** is a utility procedure used by some of the Tcl
commands. It returns a pointer to a string containing the name for the
current machine, or an empty string if the name cannot be determined.
The string is statically allocated, and the caller must not modify of
free it.

# KEYWORDS

hostname

<!---
Copyright (c) 1998-2000 Scriptics Corporation
-->

