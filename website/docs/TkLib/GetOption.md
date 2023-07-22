# NAME

Tk_GetOption - retrieve an option from the option database

# SYNOPSIS

**#include \<tk.h\>**

Tk_Uid **Tk_GetOption**(*tkwin, name, class*)

# ARGUMENTS

Token for window.

Name of desired option.

Class of desired option. Null means there is no class for this option;
do lookup based on name only.

# DESCRIPTION

This procedure is invoked to retrieve an option from the database
associated with *tkwin*\'s main window. If there is an option for
*tkwin* that matches the given *name* or *class*, then it is returned in
the form of a Tk_Uid. If multiple options match *name* and *class*, then
the highest-priority one is returned. If no option matches, then NULL is
returned.

**Tk_GetOption** caches options related to *tkwin* so that successive
calls for the same *tkwin* will execute much more quickly than
successive calls for different windows.

# KEYWORDS

class, name, option, retrieve
