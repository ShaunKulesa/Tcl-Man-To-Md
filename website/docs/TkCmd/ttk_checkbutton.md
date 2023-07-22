# NAME

ttk::checkbutton - On/off widget

# SYNOPSIS

**ttk::checkbutton** *pathName *?*options*?

# DESCRIPTION

A **ttk::checkbutton** widget is used to show or change a setting. It
has two states, selected and deselected. The state of the checkbutton
may be linked to a Tcl variable.

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

> A Tcl script to execute whenever the widget is invoked.

    Command-Line Name:	-offvalue
    Database Name:	offValue
    Database Class:	OffValue

> The value to store in the associated **-variable** when the widget is
> deselected. Defaults to **0**.

    Command-Line Name:	-onvalue
    Database Name:	onValue
    Database Class:	OnValue

> The value to store in the associated **-variable** when the widget is
> selected. Defaults to **1**.

    Command-Line Name:	-variable
    Database Name:	variable
    Database Class:	Variable

> The name of a global variable whose value is linked to the widget.
> Defaults to the widget pathname if not specified.

# WIDGET COMMAND

In addition to the standard **cget**, **configure**, **identify**,
**instate**, and **state** commands, checkbuttons support the following
additional widget commands:

*pathname*** invoke**

:   Toggles between the selected and deselected states and evaluates the
    associated **-command**. If the widget is currently selected, sets
    the **-variable** to the **-offvalue** and deselects the widget;
    otherwise, sets the **-variable** to the **-onvalue** Returns the
    result of the **-command**.

# WIDGET STATES

The widget does not respond to user input if the **disabled** state is
set. The widget sets the **selected** state whenever the linked
**-variable** is set to the widget\'s **-onvalue**, and clears it
otherwise. The widget sets the **alternate** state whenever the linked
**-variable** is unset. (The **alternate** state may be used to indicate
a or selection.)

# STANDARD STYLES

**Ttk::checkbutton** widgets support the **Toolbutton** style in all
standard themes, which is useful for creating widgets for toolbars.

# STYLING OPTIONS

The class name for a **ttk::checkbutton** is **TCheckbutton**.

Dynamic states: **active**, **alternate**, **disabled**, **pressed**,
**selected**, **readonly**.

**TCheckbutton** styling options configurable with **ttk::style** are:

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

ttk::widget(n), ttk::radiobutton(n), checkbutton(n)

# KEYWORDS

widget, button, toggle, check, option
