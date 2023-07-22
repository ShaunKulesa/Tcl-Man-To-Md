# NAME

Tk_GetUid, Tk_Uid - convert from string to unique identifier

# SYNOPSIS

**#include \<tk.h\>**

Tk_Uid **Tk_GetUid**(*string*)

# ARGUMENTS

String for which the corresponding unique identifier is desired.

# DESCRIPTION

**Tk_GetUid** returns the unique identifier corresponding to *string*.
Unique identifiers are similar to atoms in Lisp, and are used in Tk to
speed up comparisons and searches. A unique identifier (type Tk_Uid) is
a string pointer and may be used anywhere that a variable of type could
be used. However, there is guaranteed to be exactly one unique
identifier for any given string value. If **Tk_GetUid** is called twice,
once with string *a* and once with string *b*, and if *a* and *b* have
the same string value (strcmp(a, b) == 0), then **Tk_GetUid** will
return exactly the same Tk_Uid value for each call (Tk_GetUid(a) ==
Tk_GetUid(b)). This means that variables of type Tk_Uid may be compared
directly (x == y) without having to call **strcmp**. In addition, the
return value from **Tk_GetUid** will have the same string value as its
argument (strcmp(Tk_GetUid(a), a) == 0).

# KEYWORDS

atom, unique identifier

<!---
Copyright (c) 1990 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

