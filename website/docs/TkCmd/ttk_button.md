# NAME

ttk::button - Widget that issues a command when pressed

# SYNOPSIS

**ttk::button** *pathName *?*options*?

# DESCRIPTION

A **ttk::button** widget displays a textual label and/or image, and
evaluates a command when pressed.

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

> A script to evaluate when the widget is invoked.

    Command-Line Name:	-default
    Database Name:	default
    Database Class:	Default

> May be set to one of **normal**, **active**, or **disabled**. In a
> dialog box, one button may be designated the button (meaning, roughly,
> **active** indicates that this is currently the default button;
> **normal** means that it may become the default button, and
> **disabled** means that it is not defaultable. The default is
> **normal**.

> Depending on the theme, the default button may be displayed with an
> extra highlight ring, or with a different border color.

# WIDGET COMMAND

In addition to the standard **cget**, **configure**, **identify**,
**instate**, and **state** commands, buttons support the following
additional widget commands:

*pathName ***invoke**

:   Invokes the command associated with the button.

# STANDARD STYLES

**Ttk::button** widgets support the **Toolbutton** style in all standard
themes, which is useful for creating widgets for toolbars.

# STYLING OPTIONS

The class name for a **ttk::button** is **TButton**.

Dynamic states: **active**, **disabled**, **pressed**, **readonly**.

**TButton** styling options configurable with **ttk::style** are:

**-anchor** *anchor*\
**-background** *color*\
**-bordercolor** *color*\
**-compound** *compound*\
**-darkcolor** *color*\
**-foreground** *color*\
**-font** *font*\
**-highlightcolor** *color*\
**-highlightthickness** *amount*\
**-lightcolor** *color*\
**-padding** *padding*\
**-relief** *relief*\
**-shiftrelief** *amount*

> **-shiftrelief** specifies how far the button contents are shifted
> down and right in the *pressed* state. This action provides additional
> skeumorphic feedback.

**-width** *amount*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), button(n)

# KEYWORDS

widget, button, default, command
