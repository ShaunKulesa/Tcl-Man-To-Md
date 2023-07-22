# NAME

ttk::frame - Simple container widget

# SYNOPSIS

**ttk::frame** *pathName *?*options*?

# DESCRIPTION

A **ttk::frame** widget is a container, used to group other widgets
together.

# STANDARD OPTIONS

    -class	-cursor	-padding	-style
    -takefocus

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-borderwidth
    Database Name:	borderWidth
    Database Class:	BorderWidth

> The desired width of the widget border. Defaults to 0. May be ignored
> depending on the theme used.

    Command-Line Name:	-relief
    Database Name:	relief
    Database Class:	Relief

> One of the standard Tk border styles: **flat**, **groove**,
> **raised**, **ridge**, **solid**, or **sunken**. Defaults to **flat**.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> If specified, the widget\'s requested width in pixels.

    Command-Line Name:	-height
    Database Name:	height
    Database Class:	Height

> If specified, the widget\'s requested height in pixels.

# WIDGET COMMAND

Supports the standard widget commands **configure**, **cget**,
**identify**, **instate**, and **state**; see *ttk::widget(n)*.

# NOTES

Note that if the **pack**, **grid**, or other geometry managers are used
to manage the children of the **frame**, by the GM\'s requested size
will normally take precedence over the **frame** widget\'s **-width**
and **-height** options. **pack propagate** and **grid propagate** can
be used to change this.

# STYLING OPTIONS

The class name for a **ttk::frame** is **TFrame**.

**TFrame** styling options configurable with **ttk::style** are:

**-background** *color*\
**-relief** *relief*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# BINDINGS

When a new **ttk::frame** is created, it has no default event bindings;
**ttk::frame**s are not intended to be interactive.

# SEE ALSO

ttk::widget(n), ttk::labelframe(n), frame(n)

# KEYWORDS

widget, frame, container
