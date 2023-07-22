# NAME

Tk_CreateWindow, Tk_CreateWindowFromPath, Tk_DestroyWindow,
Tk_MakeWindowExist - create or delete window

# SYNOPSIS

**#include \<tk.h\>**

Tk_Window **Tk_CreateWindow**(*interp, parent, name, topLevScreen*)

Tk_Window **Tk_CreateAnonymousWindow**(*interp, parent, topLevScreen*)

Tk_Window **Tk_CreateWindowFromPath**(*interp, tkwin, pathName,
topLevScreen*)

**Tk_DestroyWindow**(*tkwin*)

**Tk_MakeWindowExist**(*tkwin*)

# ARGUMENTS

Tcl interpreter to use for error reporting. If no error occurs, then
*\*interp* is not modified.

Token for the window that is to serve as the logical parent of the new
window.

Name to use for this window. Must be unique among all children of the
same *parent*.

Has same format as *screenName*. If NULL, then new window is created as
an internal window. If non-NULL, new window is created as a top-level
window on screen *topLevScreen*. If *topLevScreen* is an empty string
then new window is created as top-level window of *parent*\'s screen.

Token for window.

Name of new window, specified as path name within application (e.g.
**.a.b.c**).

# DESCRIPTION

The procedures **Tk_CreateWindow**, **Tk_CreateAnonymousWindow**, and
**Tk_CreateWindowFromPath** are used to create new windows for use in
Tk-based applications. Each of the procedures returns a token that can
be used to manipulate the window in other calls to the Tk library. If
the window could not be created successfully, then NULL is returned and
the result of interpreter *interp* is modified to hold an error message.

Tk supports two different kinds of windows: internal windows and
top-level windows. An internal window is an interior window of a Tk
application, such as a scrollbar or menu bar or button. A top-level
window is one that is created as a child of a screen\'s root window,
rather than as an interior window, but which is logically part of some
existing main window. Examples of top-level windows are pop-up menus and
dialog boxes.

New windows may be created by calling **Tk_CreateWindow**. If the
*topLevScreen* argument is NULL, then the new window will be an internal
window. If *topLevScreen* is non-NULL, then the new window will be a
top-level window: *topLevScreen* indicates the name of a screen and the
new window will be created as a child of the root window of
*topLevScreen*. In either case Tk will consider the new window to be the
logical child of *parent*: the new window\'s path name will reflect this
fact, options may be specified for the new window under this assumption,
and so on. The only difference is that new X window for a top-level
window will not be a child of *parent*\'s X window. For example, a
pull-down menu\'s *parent* would be the button-like window used to
invoke it, which would in turn be a child of the menu bar window. A
dialog box might have the application\'s main window as its parent.

**Tk_CreateAnonymousWindow** differs from **Tk_CreateWindow** in that it
creates an unnamed window. This window will be manipulatable only using
C interfaces, and will not be visible to Tcl scripts. Both interior
windows and top-level windows may be created with
**Tk_CreateAnonymousWindow**.

**Tk_CreateWindowFromPath** offers an alternate way of specifying new
windows. In **Tk_CreateWindowFromPath** the new window is specified with
a token for any window in the target application (*tkwin*), plus a path
name for the new window. It produces the same effect as
**Tk_CreateWindow** and allows both top-level and internal windows to be
created, depending on the value of *topLevScreen*. In calls to
**Tk_CreateWindowFromPath**, as in calls to **Tk_CreateWindow**, the
parent of the new window must exist at the time of the call, but the new
window must not already exist.

The window creation procedures do not actually issue the command to X to
create a window. Instead, they create a local data structure associated
with the window and defer the creation of the X window. The window will
actually be created by the first call to **Tk_MapWindow**. Deferred
window creation allows various aspects of the window (such as its size,
background color, etc.) to be modified after its creation without
incurring any overhead in the X server. When the window is finally
mapped all of the window attributes can be set while creating the
window.

The value returned by a window-creation procedure is not the X token for
the window (it cannot be, since X has not been asked to create the
window yet). Instead, it is a token for Tk\'s local data structure for
the window. Most of the Tk library procedures take Tk_Window tokens,
rather than X identifiers. The actual X window identifier can be
retrieved from the local data structure using the **Tk_WindowId** macro;
see the manual entry for **Tk_WindowId** for details.

**Tk_DestroyWindow** deletes a window and all the data structures
associated with it, including any event handlers created with
**Tk_CreateEventHandler**. In addition, **Tk_DestroyWindow** will delete
any children of *tkwin* recursively (where children are defined in the
Tk sense, consisting of all windows that were created with the given
window as *parent*). If *tkwin* is an internal window, then event
handlers interested in destroy events are invoked immediately. If
*tkwin* is a top-level or main window, then the event handlers will be
invoked later, after X has seen the request and returned an event for
it.

If a window has been created but has not been mapped, so no X window
exists, it is possible to force the creation of the X window by calling
**Tk_MakeWindowExist**. This procedure issues the X commands to
instantiate the window given by *tkwin*.

# KEYWORDS

create, deferred creation, destroy, display, internal window, screen,
top-level window, window
