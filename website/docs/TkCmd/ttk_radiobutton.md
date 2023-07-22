# NAME

ttk::radiobutton - Mutually exclusive option widget

# SYNOPSIS

**ttk::radiobutton** *pathName *?*options*?

# DESCRIPTION

**ttk::radiobutton** widgets are used in groups to show or change a set
of mutually-exclusive options. Radiobuttons are linked to a Tcl
variable, and have an associated value; when a radiobutton is clicked,
it sets the variable to its associated value.

# STANDARD OPTIONS

    -class	-compound	-cursor
    -image	-state	-style
    -takefocus	-text	-textvariable
    -underline	-width

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-command
    Database Name:	command
    Database Class:	Command

> A Tcl script to evaluate whenever the widget is invoked.

    Command-Line Name:	-value
    Database Name:	Value
    Database Class:	Value

> The value to store in the associated **-variable** when the widget is
> selected.

    Command-Line Name:	-variable
    Database Name:	variable
    Database Class:	Variable

> The name of a global variable whose value is linked to the widget.
> Default value is **::selectedButton**.

# WIDGET COMMAND

In addition to the standard **cget**, **configure**, **identify**,
**instate**, and **state** commands, radiobuttons support the following
additional widget commands:

*pathname*** invoke**

:   Sets the **-variable** to the **-value**, selects the widget, and
    evaluates the associated **-command**. Returns the result of the
    **-command**, or the empty string if no **-command** is specified.

# WIDGET STATES

The widget does not respond to user input if the **disabled** state is
set. The widget sets the **selected** state whenever the linked
**-variable** is set to the widget\'s **-value**, and clears it
otherwise. The widget sets the **alternate** state whenever the linked
**-variable** is unset. (The **alternate** state may be used to indicate
a or selection.)

# STANDARD STYLES

**Ttk::radiobutton** widgets support the **Toolbutton** style in all
standard themes, which is useful for creating widgets for toolbars.

# STYLING OPTIONS

The class name for a **ttk::radiobutton** is **TRadiobutton**.

Dynamic states: **active**, **alternate**, **disabled**, **pressed**,
**readonly**, **selected**.

**TRadiobutton** styling options configurable with **ttk::style** are:

**-background** *color*\
**-compound** *compound*\
**-foreground** *color*\
**-indicatorbackground** *color*\
**-indicatorcolor** *color*\
**-indicatormargin** *padding*\
**-indicatorrelief** *relief*\
**-padding** *padding*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), ttk::checkbutton(n), radiobutton(n)

# KEYWORDS

widget, button, option
