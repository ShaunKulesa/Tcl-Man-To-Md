# NAME

Tk_GetUserInactiveTime, Tk_ResetUserInactiveTime - discover user
inactivity time

# SYNOPSIS

**#include \<tk.h\>**

long **Tk_GetUserInactiveTime(***display***)**

**Tk_ResetUserInactiveTime(***display***)**

# ARGUMENTS

The display on which the user inactivity timer is to be queried or
reset.

# DESCRIPTION

**Tk_GetUserInactiveTime** returns the number of milliseconds that have
passed since the last user interaction (usually via keyboard or mouse)
with the respective display. On systems and displays that do not support
querying the user inactivity time, **-1** is returned.
**Tk_ResetUserInactiveTime** resets the user inactivity timer of the
given display to zero. On windowing systems that do not support multiple
displays *display* can be passed as **NULL**.

# KEYWORDS

idle, inactive

<!---
Copyright (c) 1998-2000 by Scriptics Corporation
-->

