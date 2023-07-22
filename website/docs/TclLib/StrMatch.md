# NAME

Tcl_StringMatch, Tcl_StringCaseMatch - test whether a string matches a
pattern

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_StringMatch**(*str*, *pattern*)

int **Tcl_StringCaseMatch**(*str*, *pattern*, *flags*)

# ARGUMENTS

String to test.

Pattern to match against string. May contain special characters from the
set \*?\\\[\].

OR-ed combination of match flags, currently only **TCL_MATCH_NOCASE**. 0
specifies a case-sensitive search.

# DESCRIPTION

This utility procedure determines whether a string matches a given
pattern. If it does, then **Tcl_StringMatch** returns 1. Otherwise
**Tcl_StringMatch** returns 0. The algorithm used for matching is the
same algorithm used in the **string match** Tcl command and is similar
to the algorithm used by the C-shell for file name matching; see the Tcl
manual entry for details.

In **Tcl_StringCaseMatch**, the algorithm is the same, but you have the
option to make the matching case-insensitive. If you choose this (by
passing **TCL_MATCH_NOCASE**), then the string and pattern are
essentially matched in the lower case.

# KEYWORDS

match, pattern, string
