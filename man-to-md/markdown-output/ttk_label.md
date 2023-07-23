# NAME

ttk::label - Display a text string and/or image

# SYNOPSIS

**ttk::label** *pathName *?*options*?

# DESCRIPTION

A **ttk::label** widget displays a textual label and/or image. The label
may be linked to a Tcl variable to automatically change the displayed
text.

# STANDARD OPTIONS

    -class	-compound	-cursor
    -image	-padding	-state	-style	-takefocus
    -text	-textvariable	-underline
    -width

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-anchor
    Database Name:	anchor
    Database Class:	Anchor

> Specifies how the information in the widget is positioned relative to
> the inner margins. Legal values are **n**, **ne**, **e**, **se**,
> **s**, **sw**, **w**, **nw**, and **center**. See also **-justify**.

    Command-Line Name:	-background
    Database Name:	frameColor
    Database Class:	FrameColor

> The widget\'s background color. If unspecified, the theme default is
> used.

    Command-Line Name:	-font
    Database Name:	font
    Database Class:	Font

> Font to use for label text.

    Command-Line Name:	-foreground
    Database Name:	textColor
    Database Class:	TextColor

> The widget\'s foreground color. If unspecified, the theme default is
> used.

    Command-Line Name:	-justify
    Database Name:	justify
    Database Class:	Justify

> If there are multiple lines of text, specifies how the lines are laid
> out relative to one another. One of **left**, **center**, or
> **right**. See also **-anchor**.

    Command-Line Name:	-relief
    Database Name:	relief
    Database Class:	Relief

> Specifies the 3-D effect desired for the widget border. Valid values
> are **flat**, **groove**, **raised**, **ridge**, **solid**, and
> **sunken**.

    Command-Line Name:	-wraplength
    Database Name:	wrapLength
    Database Class:	WrapLength

> Specifies the maximum line length (in pixels). If this option is less
> than or equal to zero, then automatic wrapping is not performed;
> otherwise the text is split into lines such that no line is longer
> than the specified value.

# WIDGET COMMAND

Supports the standard widget commands **configure**, **cget**,
**identify**, **instate**, and **state**; see *ttk::widget(n)*.

# STYLING OPTIONS

The class name for a **ttk::label** is **TLabel**.

Dynamic states: **disabled**, **readonly**.

**TLabel** styling options configurable with **ttk::style** are:

**-background** *color*\
**-compound** *compound*\
**-foreground** *color*\
**-font** *font*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), label(n)

<!---
Copyright (c) 2004 Joe Englis
-->

