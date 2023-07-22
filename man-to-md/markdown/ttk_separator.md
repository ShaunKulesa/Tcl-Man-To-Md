# NAME

ttk::separator - Separator bar

# SYNOPSIS

**ttk::separator** *pathName *?*options*?

# DESCRIPTION

A **ttk::separator** widget displays a horizontal or vertical separator
bar.

# STANDARD OPTIONS

    -class	-cursor
    -style	-takefocus

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-orient
    Database Name:	orient
    Database Class:	Orient

> One of **horizontal** or **vertical**. Specifies the orientation of
> the separator.

# WIDGET COMMAND

Separator widgets support the standard **cget**, **configure**,
**identify**, **instate**, and **state** methods. No other widget
methods are used.

# STYLING OPTIONS

The class name for a **ttk::separator** is **TSeparator**.

**TSeparator** styling options configurable with **ttk::style** are:

**-background** *color*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n)

# KEYWORDS

widget, separator

<!---
Copyright (c) 2004 Joe Englis
-->

