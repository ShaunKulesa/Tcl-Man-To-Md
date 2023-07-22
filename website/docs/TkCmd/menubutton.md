# NAME

menubutton - Create and manipulate \'menubutton\' pop-up menu indicator
widgets

# SYNOPSIS

**menubutton** *pathName *?*options*?

# STANDARD OPTIONS

    -activebackground	-disabledforeground	-padx
    -activeforeground	-font	-pady
    -anchor	-foreground	-relief
    -background	-highlightbackground	-takefocus
    -bitmap	-highlightcolor	-text
    -borderwidth	-highlightthickness	-textvariable
    -cursor	-image	-underline
    -compound	-justify	-wraplength

See the manual entry for details on the standard options.

# WIDGET-SPECIFIC OPTIONS

    Command-Line Name:	-direction
    Database Name:	direction
    Database Class:	Direction

> Specifies where the menu is going to be popup up. **above** tries to
> pop the menu above the menubutton. **below** tries to pop the menu
> below the menubutton. **left** tries to pop the menu to the left of
> the menubutton. **right** tries to pop the menu to the right of the
> menu button. **flush** pops the menu directly over the menubutton. In
> the case of **above** or **below**, the direction will be reversed if
> the menu would show offscreen.

    Command-Line Name:	-height
    Database Name:	height
    Database Class:	Height

> Specifies a desired height for the menubutton. If an image or bitmap
> is being displayed in the menubutton then the value is in screen units
> (i.e. any of the forms acceptable to **Tk_GetPixels**); for text it is
> in lines of text. If this option is not specified, the menubutton\'s
> desired height is computed from the size of the image or bitmap or
> text being displayed in it.

    Command-Line Name:	-indicatoron
    Database Name:	indicatorOn
    Database Class:	IndicatorOn

> The value must be a proper boolean value. If it is true then a small
> indicator rectangle will be displayed on the right side of the
> menubutton and the default menu bindings will treat this as an option
> menubutton. If false then no indicator will be displayed.

    Command-Line Name:	-menu
    Database Name:	menu
    Database Class:	MenuName

> Specifies the path name of the menu associated with this menubutton.
> The menu must be a child of the menubutton.

    Command-Line Name:	-state
    Database Name:	state
    Database Class:	State

> Specifies one of three states for the menubutton: **normal**,
> **active**, or **disabled**. In normal state the menubutton is
> displayed using the **foreground** and **background** options. The
> active state is typically used when the pointer is over the
> menubutton. In active state the menubutton is displayed using the
> **-activeforeground** and **-activebackground** options. Disabled
> state means that the menubutton should be insensitive: the default
> bindings will refuse to activate the widget and will ignore mouse
> button presses. In this state the **-disabledforeground** and
> **-background** options determine how the button is displayed.

    Command-Line Name:	-width
    Database Name:	width
    Database Class:	Width

> Specifies a desired width for the menubutton. If an image or bitmap is
> being displayed in the menubutton then the value is in screen units
> (i.e. any of the forms acceptable to **Tk_GetPixels**); for text it is
> in characters. If this option is not specified, the menubutton\'s
> desired width is computed from the size of the image or bitmap or text
> being displayed in it.

# INTRODUCTION

The **menubutton** command creates a new window (given by the *pathName*
argument) and makes it into a menubutton widget. Additional options,
described above, may be specified on the command line or in the option
database to configure aspects of the menubutton such as its colors,
font, text, and initial relief. The **menubutton** command returns its
*pathName* argument. At the time this command is invoked, there must not
exist a window named *pathName*, but *pathName*\'s parent must exist.

A menubutton is a widget that displays a textual string, bitmap, or
image and is associated with a menu widget. If text is displayed, it
must all be in a single font, but it can occupy multiple lines on the
screen (if it contains newlines or if wrapping occurs because of the
**-wraplength** option) and one of the characters may optionally be
underlined using the **-underline** option. In normal usage, pressing
mouse button 1 over the menubutton causes the associated menu to be
posted just underneath the menubutton. If the mouse is moved over the
menu before releasing the mouse button, the button release causes the
underlying menu entry to be invoked. When the button is released, the
menu is unposted.

Menubuttons are used to construct a **tk_optionMenu**, which is the
preferred mechanism for allowing a user to select one item from a list
on Mac OS X.

Menubuttons were also typically organized into groups called menu bars
that allow scanning: if the mouse button is pressed over one menubutton
(causing it to post its menu) and the mouse is moved over another
menubutton in the same menu bar without releasing the mouse button, then
the menu of the first menubutton is unposted and the menu of the new
menubutton is posted instead. *This use is deprecated* in favor of
setting a **menu** directly as a menubar; see the **toplevel**\'s
**-menu** option for how to do that.

There are several interactions between menubuttons and menus; see the
**menu** manual entry for information on various menu configurations,
such as pulldown menus and option menus.

# WIDGET COMMAND

The **menubutton** command creates a new Tcl command whose name is
*pathName*. This command may be used to invoke various operations on the
widget. It has the following general form:

    pathName option ?arg arg ...?

*Option* and the *arg*s determine the exact behavior of the command. The
following commands are possible for menubutton widgets:

*pathName ***cget ***option*

:   Returns the current value of the configuration option given by
    *option*. *Option* may have any of the values accepted by the
    **menubutton** command.

*pathName ***configure** ?*option*? ?*value option value \...*?

:   Query or modify the configuration options of the widget. If no
    *option* is specified, returns a list describing all of the
    available options for *pathName* (see **Tk_ConfigureInfo** for
    information on the format of this list). If *option* is specified
    with no *value*, then the command returns a list describing the one
    named option (this list will be identical to the corresponding
    sublist of the value returned if no *option* is specified). If one
    or more *option-value* pairs are specified, then the command
    modifies the given widget option(s) to have the given value(s); in
    this case the command returns an empty string. *Option* may have any
    of the values accepted by the **menubutton** command.

# DEFAULT BINDINGS

Tk automatically creates class bindings for menubuttons that give them
the following default behavior:

\[1\]

:   A menubutton activates whenever the mouse passes over it and
    deactivates whenever the mouse leaves it.

\[2\]

:   Pressing mouse button 1 over a menubutton posts the menubutton: its
    relief changes to raised and its associated menu is posted under the
    menubutton. If the mouse is dragged down into the menu with the
    button still down, and if the mouse button is then released over an
    entry in the menu, the menubutton is unposted and the menu entry is
    invoked.

\[3\]

:   If button 1 is pressed over a menubutton and then released over that
    menubutton, the menubutton stays posted: you can still move the
    mouse over the menu and click button 1 on an entry to invoke it.
    Once a menu entry has been invoked, the menubutton unposts itself.

\[4\]

:   If button 1 is pressed over a menubutton and then dragged over some
    other menubutton, the original menubutton unposts itself and the new
    menubutton posts.

\[5\]

:   If button 1 is pressed over a menubutton and released outside any
    menubutton or menu, the menubutton unposts without invoking any menu
    entry.

\[6\]

:   When a menubutton is posted, its associated menu claims the input
    focus to allow keyboard traversal of the menu and its submenus. See
    the **menu** manual entry for details on these bindings.

\[7\]

:   If the **-underline** option has been specified for a menubutton
    then keyboard traversal may be used to post the menubutton: Alt+*x*,
    where *x* is the underlined character (or its lower-case or
    upper-case equivalent), may be typed in any window under the
    menubutton\'s toplevel to post the menubutton.

\[8\]

:   The F10 key may be typed in any window to post the first menubutton
    under its toplevel window that is not disabled.

\[9\]

:   If a menubutton has the input focus, the space and return keys post
    the menubutton.

If the menubutton\'s state is **disabled** then none of the above
actions occur: the menubutton is completely non-responsive.

The behavior of menubuttons can be changed by defining new bindings for
individual widgets or by redefining the class bindings.

# SEE ALSO

ttk::menubutton(n), menu(n)

# KEYWORDS

menubutton, widget
