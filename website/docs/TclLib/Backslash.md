# NAME

Tcl_Backslash - parse a backslash sequence

# SYNOPSIS

**#include \<tcl.h\>**

char **Tcl_Backslash**(*src, countPtr*)

# ARGUMENTS

Pointer to a string starting with a backslash.

If *countPtr* is not NULL, *\*countPtr* gets filled in with number of
characters in the backslash sequence, including the backslash character.

# DESCRIPTION

The use of **Tcl_Backslash** is deprecated in favor of
**Tcl_UtfBackslash**.

This is a utility procedure provided for backwards compatibility with
non-internationalized Tcl extensions. It parses a backslash sequence and
returns the low byte of the Unicode character corresponding to the
sequence. **Tcl_Backslash** modifies *\*countPtr* to contain the number
of characters in the backslash sequence.

See the Tcl manual entry for information on the valid backslash
sequences. All of the sequences described in the Tcl manual entry are
supported by **Tcl_Backslash**.

# SEE ALSO

Tcl(n), Tcl_UtfBackslash(3)

# KEYWORDS

backslash, parse
