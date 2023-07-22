# NAME

ttk::panedwindow - Multi-pane container window

# SYNOPSIS

**ttk::panedwindow** *pathname *?*options*?\
*pathname ***add** *window* ?*options\...*? *pathname ***insert**
*index* *window* ?*options\...*?

# DESCRIPTION

A **ttk::panedwindow** widget displays a number of subwindows, stacked
either vertically or horizontally. The user may adjust the relative
sizes of the subwindows by dragging the sash between panes.

# STANDARD OPTIONS

    -class	-cursor	-takefocus
    -style

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-orient
    Database Name:	orient
    Database Class:	Orient

> Specifies the orientation of the window. If **vertical**, subpanes are
> stacked top-to-bottom; if **horizontal**, subpanes are stacked
> left-to-right.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> If present and greater than zero, specifies the desired width of the
> widget in pixels. Otherwise, the requested width is determined by the
> width of the managed windows.

    Command-Line Name:	-height
    Database Name:	height
    Database Class:	Height

> If present and greater than zero, specifies the desired height of the
> widget in pixels. Otherwise, the requested height is determined by the
> height of the managed windows.

# PANE OPTIONS

The following options may be specified for each pane:

    Command-Line Name:	-weight
    Database Name:	weight
    Database Class:	Weight

> An integer specifying the relative stretchability of the pane. When
> the paned window is resized, the extra space is added or subtracted to
> each pane proportionally to its **-weight**.

# WIDGET COMMAND

Supports the standard **configure**, **cget**, **state**, and
**instate** commands; see *ttk::widget(n)* for details. Additional
commands:

*pathname ***add ***subwindow options\...*

:   Adds a new pane to the window. See **PANE OPTIONS** for the list of
    available options.

*pathname ***forget ***pane*

:   Removes the specified subpane from the widget. *pane* is either an
    integer index or the name of a managed subwindow.

*pathname ***identify ***component x y*

:   Returns the name of the element under the point given by *x* and
    *y*, or the empty string if no component is present at that
    location. If *component* is omitted, it defaults to **sash**. The
    following subcommands are supported:

    *pathname ***identify element ***x y*

    :   Returns the name of the element at the specified location.

    *pathname ***identify sash ***x y*

    :   Returns the index of the sash at the specified location.

*pathname ***insert ***pos subwindow options\...*

:   Inserts a pane at the specified position. *pos* is either the string
    **end**, an integer index, or the name of a managed subwindow. If
    *subwindow* is already managed by the paned window, moves it to the
    specified position. See **PANE OPTIONS** for the list of available
    options.

*pathname ***pane ***pane -option *?*value *?*-option value\...*

:   Query or modify the options of the specified *pane*, where *pane* is
    either an integer index or the name of a managed subwindow. If no
    *-option* is specified, returns a dictionary of the pane option
    values. If one *-option* is specified, returns the value of that
    *option*. Otherwise, sets the *-option*s to the corresponding
    *value*s.

*pathname ***panes**

:   Returns the list of all windows managed by the widget, in the index
    order of their associated panes.

*pathname ***sashpos ***index* ?*newpos*?

:   If *newpos* is specified, sets the position of sash number *index*.
    May adjust the positions of adjacent sashes to ensure that positions
    are monotonically increasing. Sash positions are further constrained
    to be between 0 and the total size of the widget. Returns the new
    position of sash number *index*.

The panedwindow widget also supports the following generic
**ttk::widget** widget subcommands (see *ttk::widget(n)* for details):

>
>     cget	configure
>     instate	state

# VIRTUAL EVENTS

The panedwindow widget generates an **\<\<EnteredChild\>\>** virtual
event on LeaveNotify/NotifyInferior events, because Tk does not execute
binding scripts for \<Leave\> events when the pointer crosses from a
parent to a child. The panedwindow widget needs to know when that
happens.

# STYLING OPTIONS

The class name for a **ttk::panedwindow** is **TPanedwindow**. The sash
has a class name of **Sash**.

**TPanedwindow** styling options configurable with **ttk::style** are:

**-background** *color*

**Sash** styling options configurable with **ttk::style** are:

**-background** *color*\
**-bordercolor** *color*\
**-gripcount** *count*\
**-handlepad** *amount*\
**-handlesize** *amount*\
**-lightcolor** *color*\
**-sashpad** *amount*\
**-sashrelief** *relief*\
**-sashthickness** *amount*

Some options are only available for specific themes.

See the **ttk::style** manual page for information on how to configure
ttk styles.

# SEE ALSO

ttk::widget(n), ttk::notebook(n), panedwindow(n)
