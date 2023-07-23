# NAME

ttk::notebook - Multi-paned container widget

# SYNOPSIS

**ttk::notebook** *pathname *?*options\...*?\
*pathname ***add** *window* ?*options\...*? *pathname ***insert**
*index* *window* ?*options\...*?

# DESCRIPTION

A **ttk::notebook** widget manages a collection of windows and displays
a single one at a time. Each content window is associated with a *tab*,
which the user may select to change the currently-displayed window.

# STANDARD OPTIONS

    -class	-cursor	-takefocus
    -style

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-height
    Database Name:	height
    Database Class:	Height

> If present and greater than zero, specifies the desired height of the
> pane area (not including internal padding or tabs). Otherwise, the
> maximum height of all panes is used.

    Command-Line Name:	-padding
    Database Name:	padding
    Database Class:	Padding

> Specifies the amount of extra space to add around the outside of the
> notebook. The padding is a list of up to four length specifications
> *left top right bottom*. If fewer than four elements are specified,
> *bottom* defaults to *top*, *right* defaults to *left*, and *top*
> defaults to *left*. In other words, a list of three numbers specify
> the left, vertical, and right padding; a list of two numbers specify
> the horizontal and the vertical padding; a single number specifies the
> same padding all the way around the widget.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> If present and greater than zero, specifies the desired width of the
> pane area (not including internal padding). Otherwise, the maximum
> width of all panes is used.

# TAB OPTIONS

The following options may be specified for individual notebook panes:

    Command-Line Name:	-state
    Database Name:	state
    Database Class:	State

> Either **normal**, **disabled** or **hidden**. If **disabled**, then
> the tab is not selectable. If **hidden**, then the tab is not shown.

    Command-Line Name:	-sticky
    Database Name:	sticky
    Database Class:	Sticky

> Specifies how the content window is positioned within the pane area.
> Value is a string containing zero or more of the characters **n, s,
> e,** or **w**. Each letter refers to a side (north, south, east, or
> west) that the content window will to, as per the **grid** geometry
> manager.

    Command-Line Name:	-padding
    Database Name:	padding
    Database Class:	Padding

> Specifies the amount of extra space to add between the notebook and
> this pane. Syntax is the same as for the widget **-padding** option.

    Command-Line Name:	-text
    Database Name:	text
    Database Class:	Text

> Specifies a string to be displayed in the tab.

    Command-Line Name:	-image
    Database Name:	image
    Database Class:	Image

> Specifies an image to display in the tab. See *ttk_widget(n)* for
> details.

    Command-Line Name:	-compound
    Database Name:	compound
    Database Class:	Compound

> Specifies how to display the image relative to the text, in the case
> both **-text** and **-image** are present. See *label(n)* for legal
> values.

    Command-Line Name:	-underline
    Database Name:	underline
    Database Class:	Underline

> Specifies the integer index (0-based) of a character to underline in
> the text string. The underlined character is used for mnemonic
> activation if **ttk::notebook::enableTraversal** is called.

# TAB IDENTIFIERS

The *tabid* argument to the following commands may take any of the
following forms:

-   An integer between zero and the number of tabs;

-   The name of a content window;

-   A positional specification of the form which identifies the tab

-   The literal string which identifies the currently-selected tab; or:

-   The literal string which returns the number of tabs (only valid for

# WIDGET COMMAND

*pathname ***add ***window* ?*options\...*?

:   Adds a new tab to the notebook. See **TAB OPTIONS** for the list of
    available *options*. If *window* is currently managed by the
    notebook but hidden, it is restored to its previous position.

*pathname ***configure** ?*options*?

:   See *ttk::widget(n)*.

*pathname ***cget ***option*

:   See *ttk::widget(n)*.

*pathname ***forget ***tabid*

:   Removes the tab specified by *tabid*, unmaps and unmanages the
    associated window.

*pathname ***hide ***tabid*

:   Hides the tab specified by *tabid*. The tab will not be displayed,
    but the associated window remains managed by the notebook and its
    configuration remembered. Hidden tabs may be restored with the
    **add** command.

*pathname ***identify*** component x y*

:   Returns the name of the element under the point given by *x* and
    *y*, or the empty string if no component is present at that
    location. The following subcommands are supported:

    *pathname ***identify element** *x y*

    :   Returns the name of the element at the specified location.

    *pathname ***identify tab** *x y*

    :   Returns the index of the tab at the specified location.

*pathname ***index ***tabid*

:   Returns the numeric index of the tab specified by *tabid*, or the
    total number of tabs if *tabid* is the string

*pathname ***insert ***pos subwindow options\...*

:   Inserts a pane at the specified position. *pos* is either the string
    **end**, an integer index, or the name of a managed subwindow. If
    *subwindow* is already managed by the notebook, moves it to the
    specified position. See **TAB OPTIONS** for the list of available
    options.

*pathname ***instate ***statespec *?*script\...*?

:   See *ttk::widget(n)*.

*pathname ***select** ?*tabid*?

:   Selects the specified tab. The associated content window will be
    displayed, and the previously-selected window (if different) is
    unmapped. If *tabid* is omitted, returns the widget name of the
    currently selected pane.

*pathname ***state** ?*statespec*?

:   See *ttk::widget(n)*.

*pathname ***tab ***tabid* ?*-option *?*value \...*

:   Query or modify the options of the specific tab. If no *-option* is
    specified, returns a dictionary of the tab option values. If one
    *-option* is specified, returns the value of that *option*.
    Otherwise, sets the *-option*s to the corresponding *value*s. See
    **TAB OPTIONS** for the available options.

*pathname ***tabs**

:   Returns the list of windows managed by the notebook, in the index
    order of their associated tabs.

# KEYBOARD TRAVERSAL

To enable keyboard traversal for a toplevel window containing a notebook
widget *\$nb*, call:

    ttk::notebook::enableTraversal $nb

This will extend the bindings for the toplevel window containing the
notebook as follows:

-   **Control-Tab** selects the tab following the currently selected
    one.

-   **Control-Shift-Tab** selects the tab preceding the currently
    selected one.

-   **Alt-***K*, where *K* is the mnemonic (underlined) character of any
    tab, will select that tab.

Multiple notebooks in a single toplevel may be enabled for traversal,
including nested notebooks. However, notebook traversal only works
properly if all panes are direct children of the notebook.

# VIRTUAL EVENTS

The notebook widget generates a **\<\<NotebookTabChanged\>\>** virtual
event after a new tab is selected.

# EXAMPLE

    pack [ttk::notebook .nb]
    .nb add [frame .nb.f1] -text "First tab"
    .nb add [frame .nb.f2] -text "Second tab"
    .nb select .nb.f2
    ttk::notebook::enableTraversal .nb

# STYLING OPTIONS

The class name for a **ttk::notebook** is **TNotebook**. The tab has a
class name of **TNotebook.Tab**

Dynamic states: **active**, **disabled**, **selected**.

**TNotebook** styling options configurable with **ttk::style** are:

**-background** *color*\
**-bordercolor** *color*\
**-darkcolor** *color*\
**-foreground** *color*\
**-lightcolor** *color*\
**-padding** *padding*\
**-tabmargins** *padding*\
**-tabposition** *side*\

**TNotebook.Tab** styling options configurable with **ttk::style** are:

**-background** *color*\
**-bordercolor** *color*\
**-compound** *compound*\
**-expand** *padding*

> Defines how much the tab grows in size. Usually used with the
> **selected** dynamic state. **-tabmargins** should be set
> appropriately so that there is room for the tab growth.

**-font** *font*\
**-foreground** *color*\
**-padding** *padding*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), grid(n)

# KEYWORDS

pane, tab

<!---
Copyright (c) 2004 Joe Englis
-->

