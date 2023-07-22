# NAME

Tk_AddOption - Add an option to the option database

# SYNOPSIS

**#include \<tk.h\>**

void **Tk_AddOption**(*tkwin, name, value, priority*)

# ARGUMENTS

Token for window.

Multi-element name of option.

Value of option.

Overall priority level to use for option.

# DESCRIPTION

This procedure is invoked to add an option to the database associated
with *tkwin*\'s main window. *Name* contains the option being specified
and consists of names and/or classes separated by asterisks or dots, in
the usual X format. *Value* contains the text string to associate with
*name*; this value will be returned in calls to **Tk_GetOption**.
*Priority* specifies the priority of the value; when options are queried
using **Tk_GetOption**, the value with the highest priority is returned.
*Priority* must be between 0 and **TK_MAX_PRIO**. Some common priority
values are:

20. Used for default values hard-coded into widgets.

21. Used for options specified in application-specific startup files.

22. Used for options specified in user-specific defaults files, such as
    **.Xdefaults**, resource databases loaded into the X server, or
    user-specific startup files.

23. Used for options specified interactively after the application
    starts running.

# KEYWORDS

class, name, option, add
