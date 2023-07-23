# NAME

ttk::widget - Standard options and commands supported by Tk themed
widgets

# DESCRIPTION

This manual describes common widget options and commands.

# STANDARD OPTIONS

The following options are supported by all Tk themed widgets:

    Command-Line Name:	-class
    Database Name:	undefined
    Database Class:	undefined

> Specifies the window class. The class is used when querying the option
> database for the window\'s other options, to determine the default
> bindtags for the window, and to select the widget\'s default layout
> and style. This is a read-only option: it may only be specified when
> the window is created, and may not be changed with the **configure**
> widget command.

    Command-Line Name:	-cursor
    Database Name:	cursor
    Database Class:	Cursor

> Specifies the mouse cursor to be used for the widget. See
> **Tk_GetCursor** and *cursors(n)* in the Tk reference manual for the
> legal values. If set to the empty string (the default), the cursor is
> inherited from the parent widget.

    Command-Line Name:	-takefocus
    Database Name:	takeFocus
    Database Class:	TakeFocus

> Determines whether the window accepts the focus during keyboard
> traversal. Either **0**, **1**, a command prefix (to which the widget
> path is appended, and which should return **0** or **1**), or the
> empty string. See *options(n)* in the Tk reference manual for the full
> description.

    Command-Line Name:	-style
    Database Name:	style
    Database Class:	Style

> May be used to specify a custom widget style.

# SCROLLABLE WIDGET OPTIONS

The following options are supported by widgets that are controllable by
a scrollbar. See *scrollbar(n)* for more information

    Command-Line Name:	-xscrollcommand
    Database Name:	xScrollCommand
    Database Class:	ScrollCommand

> A command prefix, used to communicate with horizontal scrollbars.

> When the view in the widget\'s window changes, the widget will
> generate a Tcl command by concatenating the scroll command and two
> numbers. Each of the numbers is a fraction between 0 and 1 indicating
> a position in the document; 0 indicates the beginning, and 1 indicates
> the end. The first fraction indicates the first information in the
> widget that is visible in the window, and the second fraction
> indicates the information just after the last portion that is visible.
>
> Typically the **-xscrollcommand** option consists of the path name of
> a **scrollbar** widget followed by e.g. This will cause the scrollbar
> to be updated whenever the view in the window changes.
>
> If this option is set to the empty string (the default), then no
> command will be executed.

    Command-Line Name:	-yscrollcommand
    Database Name:	yScrollCommand
    Database Class:	ScrollCommand

> A command prefix, used to communicate with vertical scrollbars. See
> the description of **-xscrollcommand** above for details.

# LABEL OPTIONS

The following options are supported by labels, buttons, and other
button-like widgets:

    Command-Line Name:	-compound
    Database Name:	compound
    Database Class:	Compound

> Specifies how to display the image relative to the text, in the case
> both **-text** and **-image** are present. If set to the empty string
> (the default), the rules described in the \"Elements\" section of
> *ttk::intro(n)* explain which value is actually used. The other valid
> values are:

> text
>
> :   Display text only.
>
> image
>
> :   Display image only.
>
> center
>
> :   Display text centered on top of image.
>
> top
>
> :   
>
> bottom
>
> :   
>
> left
>
> :   
>
> right
>
> :   Display image above, below, left of, or right of the text,
>     respectively.
>
> none
>
> :   Display the image if present, otherwise the text.

    Command-Line Name:	-font
    Database Name:	font
    Database Class:	Font

> Font to use for the text displayed by the widget.

    Command-Line Name:	-foreground
    Database Name:	textColor
    Database Class:	TextColor

> The widget\'s foreground color. If unspecified, the theme default is
> used.

    Command-Line Name:	-image
    Database Name:	image
    Database Class:	Image

> Specifies an image to display. This is a list of 1 or more elements.
> The first element is the default image name. The rest of the list is a
> sequence of *statespec / value* pairs as per **style map**, specifying
> different images to use when the widget is in a particular state or
> combination of states. All images in the list should have the same
> size.

    Command-Line Name:	-padding
    Database Name:	padding
    Database Class:	Padding

> Specifies the internal padding for the widget. The padding is a list
> of up to four length specifications *left top right bottom*. If fewer
> than four elements are specified, *bottom* defaults to *top*, *right*
> defaults to *left*, and *top* defaults to *left*. In other words, a
> list of three numbers specify the left, vertical, and right padding; a
> list of two numbers specify the horizontal and the vertical padding; a
> single number specifies the same padding all the way around the
> widget.

    Command-Line Name:	-text
    Database Name:	text
    Database Class:	Text

> Specifies a text string to be displayed inside the widget (unless
> overridden by **-textvariable**).

    Command-Line Name:	-textvariable
    Database Name:	textVariable
    Database Class:	Variable

> Specifies the name of a global variable whose value will be used in
> place of the **-text** resource.

    Command-Line Name:	-underline
    Database Name:	underline
    Database Class:	Underline

> If set, specifies the integer index (0-based) of a character to
> underline in the text string. The underlined character is used for
> mnemonic activation.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> If greater than zero, specifies how much space, in character widths,
> to allocate for the text label. If less than zero, specifies a minimum
> width. If zero or unspecified, the natural width of the text label is
> used.

# COMPATIBILITY OPTIONS

This option is only available for themed widgets that have traditional
Tk widgets.

    Command-Line Name:	-state
    Database Name:	state
    Database Class:	State

> May be set to **normal** or **disabled** to control the **disabled**
> state bit. This is a write-only option: setting it changes the widget
> state, but the **state** widget command does not affect the **-state**
> option.

# COMMANDS

*pathName ***cget ***option*

:   Returns the current value of the configuration option given by
    *option*.

*pathName ***configure** ?*option*? ?*value option value \...*?

:   Query or modify the configuration options of the widget. If one or
    more *option-value* pairs are specified, then the command modifies
    the given widget option(s) to have the given value(s); in this case
    the command returns an empty string. If *option* is specified with
    no *value*, then the command returns a list describing the named
    option: the elements of the list are the option name, database name,
    database class, default value, and current value. If no *option* is
    specified, returns a list describing all of the available options
    for *pathName*.

*pathName ***identify element ***x y*

:   Returns the name of the element under the point given by *x* and
    *y*, or an empty string if the point does not lie within any
    element. *x* and *y* are pixel coordinates relative to the widget.
    Some widgets accept other **identify** subcommands.

*pathName ***instate ***statespec* ?*script*?

:   Test the widget\'s state. If *script* is not specified, returns 1 if
    the widget state matches *statespec* and 0 otherwise. If *script* is
    specified, equivalent to

```{=html}
<!-- -->
```
    if {[pathName instate stateSpec]} script

*pathName ***state** ?*stateSpec*?

:   Modify or inquire widget state. If *stateSpec* is present, sets the
    widget state: for each flag in *stateSpec*, sets the corresponding
    flag or clears it if prefixed by an exclamation point.

    Returns a new state spec indicating which flags were changed:

        set changes [pathName state spec]
        pathName state $changes

    will restore *pathName* to the original state. If *stateSpec* is not
    specified, returns a list of the currently-enabled state flags.

*pathName ***xview ***args*

:   This command is used to query and change the horizontal position of
    the content in the widget\'s window. It can take any of the
    following forms:

    *pathName ***xview**

    :   Returns a list containing two elements. Each element is a real
        fraction between 0 and 1; together they describe the horizontal
        span that is visible in the window. For example, if the first
        element is .2 and the second element is .6, 20% of the widget\'s
        content is off-screen to the left, the middle 40% is visible in
        the window, and 40% of the content is off-screen to the right.
        These are the same values passed to scrollbars via the
        **-xscrollcommand** option.

    *pathName ***xview** *index*

    :   Adjusts the view in the window so that the content given by
        *index* is displayed at the left edge of the window.

    *pathName ***xview moveto*** fraction*

    :   Adjusts the view in the window so that the character *fraction*
        of the way through the content appears at the left edge of the
        window. *Fraction* must be a fraction between 0 and 1.

    *pathName ***xview scroll ***number what*

    :   This command shifts the view in the window left or right
        according to *number* and *what*. *Number* must be an integer.
        *What* must be either **units** or **pages**. If *what* is
        **units**, the view adjusts left or right by *number*
        average-width characters on the display; if it is **pages** then
        the view adjusts by *number* screenfuls. If *number* is negative
        then characters farther to the left become visible; if it is
        positive then characters farther to the right become visible.

*pathName ***yview ***args*

:   This command is used to query and change the vertical position of
    the content in the widget\'s window. It can take any of the
    following forms:

    *pathName ***yview**

    :   Returns a list containing two elements. Each element is a real
        fraction between 0 and 1; together they describe the vertical
        span that is visible in the window. For example, if the first
        element is .2 and the second element is .6, 20% of the widget\'s
        content is off-screen to the top, the middle 40% is visible in
        the window, and 40% of the content is off-screen to the bottom.
        These are the same values passed to scrollbars via the
        **-yscrollcommand** option.

    *pathName ***yview** *index*

    :   Adjusts the view in the window so that the content given by
        *index* is displayed at the top edge of the window.

    *pathName ***yview moveto*** fraction*

    :   Adjusts the view in the window so that the item *fraction* of
        the way through the content appears at the top edge of the
        window. *Fraction* must be a fraction between 0 and 1.

    *pathName ***yview scroll ***number what*

    :   This command shifts the view in the window up or down according
        to *number* and *what*. *Number* must be an integer. *What* must
        be either **units** or **pages**. If *what* is **units**, the
        view adjusts up or down by *number* average-width characters on
        the display; if it is **pages** then the view adjusts by
        *number* screenfuls. If *number* is negative then items farther
        to the top become visible; if it is positive then items farther
        to the bottom become visible.

# WIDGET STATES

The widget state is a bitmap of independent state flags. Widget state
flags include:

**active**

:   The mouse cursor is over the widget and pressing a mouse button will
    cause some action to occur. (aka (Gnome), (Windows),

**disabled**

:   Widget is disabled under program control (aka

**focus**

:   Widget has keyboard focus.

**pressed**

:   Widget is being pressed (aka in Motif).

**selected**

:   or for things like checkbuttons and radiobuttons.

**background**

:   Windows and the Mac have a notion of an or foreground window. The
    **background** state is set for widgets in a background window, and
    cleared for those in the foreground window.

**readonly**

:   Widget should not allow user modification.

**alternate**

:   A widget-specific alternate display format. For example, used for
    checkbuttons and radiobuttons in the or state, and for buttons with
    **-default active**.

**invalid**

:   The widget\'s value is invalid. (Potential uses: scale widget value
    out of bounds, entry widget value failed validation.)

**hover**

:   The mouse cursor is within the widget. This is similar to the
    **active** state; it is used in some themes for widgets that provide
    distinct visual feedback for the active widget in addition to the
    active element within the widget.

A *state specification* or *stateSpec* is a list of state names,
optionally prefixed with an exclamation point (!) indicating that the
bit is off.

# EXAMPLES

    set b [ttk::button .b]

    # Disable the widget:
    $b state disabled

    # Invoke the widget only if it is currently pressed and enabled:
    $b instate {pressed !disabled} { .b invoke }

    # Reenable widget:
    $b state !disabled

# SEE ALSO

ttk::intro(n), ttk::style(n)

# KEYWORDS

state, configure, option

<!---
Copyright (c) 2004 Joe Englis
-->

