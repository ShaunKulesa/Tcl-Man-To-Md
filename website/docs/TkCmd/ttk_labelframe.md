# NAME

ttk::labelframe - Container widget with optional label

# SYNOPSIS

**ttk::labelframe** *pathName *?*options*?

# DESCRIPTION

A **ttk::labelframe** widget is a container used to group other widgets
together. It has an optional label, which may be a plain text string or
another widget.

# STANDARD OPTIONS

    -class	-cursor	-padding	-style
    -takefocus

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-height
    Database Name:	height
    Database Class:	Height

> If specified, the widget\'s requested height in pixels. (See
> *ttk::frame(n)* for further notes on **-width** and **-height**).

    Command-Line Name:	-labelanchor
    Database Name:	labelAnchor
    Database Class:	LabelAnchor

> Specifies where to place the label. Allowed values are (clockwise from
> the top upper left corner): **nw**, **n**, **ne**, **en**, **e**,
> **es**, **se**, **s**,**sw**, **ws**, **w** and **wn**. The default
> value is theme-dependent.

    Command-Line Name:	-labelwidget
    Database Name:	labelWidget
    Database Class:	LabelWidget

> The name of a widget to use for the label. If set, overrides the
> **-text** option. The **-labelwidget** must be a child of the
> **labelframe** widget or one of the **labelframe**\'s ancestors, and
> must belong to the same top-level widget as the **labelframe**.

    Command-Line Name:	-text
    Database Name:	text
    Database Class:	Text

> Specifies the text of the label.

    Command-Line Name:	-underline
    Database Name:	underline
    Database Class:	Underline

> If set, specifies the integer index (0-based) of a character to
> underline in the text string. The underlined character is used for
> mnemonic activation. Mnemonic activation for a **ttk::labelframe**
> sets the keyboard focus to the first child of the **ttk::labelframe**
> widget.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> If specified, the widget\'s requested width in pixels.

# WIDGET COMMAND

Supports the standard widget commands **configure**, **cget**,
**identify**, **instate**, and **state**; see *ttk::widget(n)*.

# STYLING OPTIONS

The class name for a **ttk::labelframe** is **TLabelframe**. The text
label has a class of **TLabelframe.Label**.

Dynamic states: **disabled**, **readonly**.

**TLabelframe** styling options configurable with **ttk::style** are:

**-background** *color*\
**-bordercolor** *color*\
**-borderwidth** *amount*\
**-darkcolor** *color*\
**-labelmargins** *amount*\
**-labeloutside** *boolean*\
**-lightcolor** *color*\
**-relief** *relief*

**TLabelframe.Label** styling options configurable with **ttk::style**
are:

**-background** *color*\
**-font** *font*\
**-foreground** *color*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), ttk::frame(n), labelframe(n)

# KEYWORDS

widget, frame, container, label, groupbox
