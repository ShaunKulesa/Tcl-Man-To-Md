# NAME

ttk::spinbox - Selecting text field widget

# SYNOPSIS

**ttk::spinbox** *pathName *?*options*?

# DESCRIPTION

A **ttk::spinbox** widget is a **ttk::entry** widget with built-in up
and down buttons that are used to either modify a numeric value or to
select among a set of values. The widget implements all the features of
the **ttk::entry** widget including support of the **-textvariable**
option to link the value displayed by the widget to a Tcl variable.

# STANDARD OPTIONS

    -class	-cursor	-state	-style
    -takefocus	-xscrollcommand

See the manual entry for details on the standard options.

# STANDARD OPTIONS

    -validate	-validatecommand

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-command
    Database Name:	command
    Database Class:	Command

> Specifies a Tcl command to be invoked whenever a spinbutton is
> invoked.

    Command-Line Name:	-format
    Database Name:	format
    Database Class:	Format

> Specifies an alternate format to use when setting the string value
> when using the **-from** and **-to** range. This must be a format
> specifier of the form **%\<pad\>.\<pad\>f**, as it will format a
> floating-point number.

    Command-Line Name:	-from
    Database Name:	from
    Database Class:	From

> A floating-point value specifying the lowest value for the spinbox.
> This is used in conjunction with **-to** and **-increment** to set a
> numerical range.

    Command-Line Name:	-increment
    Database Name:	increment
    Database Class:	Increment

> A floating-point value specifying the change in value to be applied
> each time one of the widget spin buttons is pressed. The up button
> applies a positive increment, the down button applies a negative
> increment.

    Command-Line Name:	-to
    Database Name:	to
    Database Class:	To

> A floating-point value specifying the highest permissible value for
> the widget. See also **-from** and **-increment**. range.

    Command-Line Name:	-values
    Database Name:	values
    Database Class:	Values

> This must be a Tcl list of values. If this option is set then this
> will override any range set using the **-from**, **-to** and
> **-increment** options. The widget will instead use the values
> specified beginning with the first value.

    Command-Line Name:	-wrap
    Database Name:	wrap
    Database Class:	Wrap

> Must be a proper boolean value. If on, the spinbox will wrap around
> the values of data in the widget.

# INDICES

See the **ttk::entry** manual for information about indexing characters.

# VALIDATION

See the **ttk::entry** manual for information about using the
**-validate** and **-validatecommand** options.

# WIDGET COMMAND

The following subcommands are possible for spinbox widgets in addition
to the commands described for the **ttk::entry** widget:

*pathName ***get**

:   Returns the spinbox\'s current value.

*pathName ***set ***value*

:   Set the spinbox string to *value*. If a **-format** option has been
    configured then this format will be applied. If formatting fails or
    is not set or the **-values** option has been used then the value is
    set directly.

# VIRTUAL EVENTS

The spinbox widget generates a **\<\<Increment\>\>** virtual event when
the user presses \<Up\>, and a **\<\<Decrement\>\>** virtual event when
the user presses \<Down\>.

# STYLING OPTIONS

The class name for a **ttk::spinbox** is **TSpinbox**.

Dynamic states: **active**, **disabled**, **focus**, **readonly**.

**TSpinbox** styling options configurable with **ttk::style** are:

**-arrowcolor** *color*\
**-arrowsize** *amount*\
**-background** *color*

> For backwards compatibility, when using the aqua theme (for macOS),
> this option behaves as an alias for the **-fieldbackground** provided
> that no value is specified for **-fieldbackground**. Otherwise it is
> ignored.

**-bordercolor** *color*\
**-darkcolor** *color*\
**-fieldbackground** *color*\
**-foreground** *color*\
**-insertcolor** *color*\
**-insertwidth** *amount*\
**-lightcolor** *color*\
**-padding** *padding*\
**-selectbackground** *color*\
**-selectforeground** *color*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), ttk::entry(n), spinbox(n)

# KEYWORDS

entry, spinbox, widget, text field

<!---
Copyright (c) 2008 Pat Thoyt
-->

