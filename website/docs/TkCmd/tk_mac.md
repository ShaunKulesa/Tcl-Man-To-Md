# NAME

tk::mac - Access Mac-Specific Functionality on OS X from Tk

# SYNOPSIS

**::tk::mac::DoScriptFile** **::tk::mac::DoScriptText**
**::tk::mac::ShowPreferences** **::tk::mac::OpenApplication**
**::tk::mac::ReopenApplication** **::tk::mac::OpenDocument ***file\...*
**::tk::mac::PrintDocument ***file\...* **::tk::mac::Quit**
**::tk::mac::OnHide** **::tk::mac::OnShow** **::tk::mac::ShowHelp**
**::tk::mac::PerformService** **::tk::mac::LaunchURL ***URL\...*
**::tk::mac::GetAppPath**

**::tk::mac::standardAboutPanel**

**::tk::mac::useCompatibilityMetrics ***boolean*
**::tk::mac::CGAntialiasLimit ***limit* **::tk::mac::antialiasedtext
***number* **::tk::mac::useThemedToplevel ***boolean*

**::tk::mac::iconBitmap ***name width height -kind value*

# EVENT HANDLER CALLBACKS

The Aqua/Mac OS X application environment defines a number of additional
events that applications should respond to. These events are mapped by
Tk to calls to commands in the **::tk::mac** namespace; unless otherwise
noted, if the command is absent, no action will be taken.

**::tk::mac::DoScriptFile**

:   The default Apple Event handler for AEDoScriptHandler. This command
    executes a Tcl file when an AppleScript sends a command to Wish with
    a file path as a parameter.

**::tk::mac::DoScriptText**

:   The default Apple Event handler for AEDoScriptHandler. This command
    executes Tcl code when an AppleScript sends a command to Wish with
    Tcl code or a Tcl procedure as a parameter.

**::tk::mac::ShowPreferences**

:   The default Apple Event handler for kAEShowPreferences, The
    application menu menu item is only enabled when this proc is
    defined. Typically this command is used to wrap a specific own
    preferences command, which pops up a preferences window. Something
    like:

        proc ::tk::mac::ShowPreferences {} {
            setPref
        }

**::tk::mac::OpenApplication**

:   If a proc of this name is defined, this proc fill fire when your
    application is initially opened. It is the default Apple Event
    handler for kAEOpenApplication,

**::tk::mac::ReopenApplication**

:   If a proc of this name is defined it is the default Apple Event
    handler for kAEReopenApplication, the Apple Event sent when your
    application is opened when it is already running (e.g. by clicking
    its icon in the Dock). Here is a sample that raises a minimized
    window when the Dock icon is clicked:

        proc ::tk::mac::ReopenApplication {} {
            if {[wm state .] eq "withdrawn"} {
                wm state . normal
            } else {
                wm deiconify .
            }
            raise .
        }

**::tk::mac::OpenDocument ***file\...*

:   If a proc of this name is defined it is the default Apple Event
    handler for kAEOpenDocuments, the Apple Event sent when your
    application is asked to open one or more documents (e.g., by drag &
    drop onto the app or by opening a document of a type associated to
    the app). The proc should take as arguments paths to the files to be
    opened, like so:

        proc ::tk::mac::OpenDocument {args} {
            foreach f $args {my_open_document $f}
        }

**::tk::mac::PrintDocument ***file\...*

:   If a proc of this name is defined it is the default Apple Event
    handler for kAEPrintDocuments, the Apple Event sent when your
    application is asked to print a document. It takes a single absolute
    file path as an argument.

**::tk::mac::Quit**

:   If a proc of this name is defined it is the default Apple Event
    handler for kAEQuitApplication, the Apple Event sent when your
    application is asked to be quit, e.g. via the quit menu item in the
    application menu, the quit menu item in the Dock menu, or during a
    logout/restart/shutdown etc. If this is not defined, **exit** is
    called instead.

**::tk::mac::OnHide**

:   If defined, this is called when your application receives a
    kEventAppHidden event, e.g. via the hide menu item in the
    application or Dock menus.

**::tk::mac::OnShow**

:   If defined, this is called when your application receives a
    kEventAppShown event, e.g. via the show all menu item in the
    application menu, or by clicking the Dock icon of a hidden
    application.

**::tk::mac::ShowHelp**

:   Customizes behavior of Apple Help menu; if this procedure is not
    defined, the platform-specific standard Help menu item performs the
    default Cocoa action of showing the Help Book configured in the
    application\'s Info.plist (or displaying an alert if no Help Book is
    set).

**::tk::mac::PerformService**

:   Executes a Tcl procedure called from the macOS menu in the
    Application menu item. The menu item allows for inter-application
    communication; data from one application, such as selected text, can
    be sent to another application for processing, for example to Safari
    as a search item for Google, or to TextEdit to be appended to a
    file. An example of the proc is below, and should be rewritten in an
    application script for customization:

        proc ::tk::mac::PerformService {} {
            set data [clipboard get]
            $w insert end $data
        }

Note that the mechanism for retrieving the data is from the clipboard;
there is no other supported way to obtain the data. If the Services
process is not desired, the NSServices keys can be deleted from the
application\'s Info.plist file. The underlying code supporting this
command also allows the text, entry and ttk::entry widgets to access
services from other applications via the Services menu. The NSPortName
key in Wish\'s Info.plist file is currently set as ; if a developer
changes the name of the Wish executable to something else, this key
should be modified with the same name.

**::tk::mac::LaunchURL ***URL\...*

:   If defined, launches a URL within Tk. This would be used if a Tk
    application wants to handle a URL itself, such as displaying data
    from an RSS feed, rather than launching a default application to
    handle the URL, although it can defined as such. Wish includes a
    stub URL scheme of in the CFBundleURLSchemes key of its Info.plist
    file; this should be customized for the specific URL scheme the
    developer wants to support.

**::tk::mac::GetAppPath**

:   Returns the current applications\'s file path.

# ADDITIONAL DIALOGS

The Aqua/Mac OS X defines additional dialogs that applications should
support.

**::tk::mac::standardAboutPanel**

:   Brings the standard Cocoa about panel to the front with information
    filled in from the application bundle files. The panel displays the
    application icon and the values associated to the info.plist keys
    named CFBundleName, CFBundleShortVersionString,
    NSAboutPanelOptionVersion and NSHumanReadableCopyright. If a file
    named *Credits.html* or *Credits.rtf* exists in the bundle\'s
    Resources directory then its contents will be displayed in a
    scrolling text box at the bottom of the dialog. See the
    documentation for -\[NSApplication
    orderFrontStandardAboutPanelWithOptions:\] for more details. A hook
    is also provided for a custom About dialog. If a Tcl proc named
    tkAboutDialog is defined in the main interpreter then that procedure
    will be called instead of opening the standardAboutPanel.

# SYSTEM CONFIGURATION

There are a number of additional global configuration options that
control the details of how Tk renders by default.

**::tk::mac::useCompatibilityMetrics ***boolean*

:   Preserves compatibility with older Tk/Aqua metrics; set to **false**
    for more native spacing.

**::tk::mac::CGAntialiasLimit ***limit*

:   Sets the antialiasing limit; lines thinner that *limit* pixels will
    not be antialiased. Integer, set to 0 by default, making all lines
    be antialiased.

**::tk::mac::antialiasedtext ***number*

:   Sets anti-aliased text. Controls text antialiasing, possible values
    for *number* are -1 (default, use system default for text AA), 0 (no
    text AA), 1 (use text AA).

**::tk::mac::useThemedToplevel ***boolean*

:   Sets toplevel windows to draw with the modern grayish/ pinstripe Mac
    background. Equivalent to configuring the toplevel with or to using
    a **ttk::frame**.

# SUPPORT COMMANDS

**::tk::mac::iconBitmap ***name width height -kind value*

:   Renders native icons and bitmaps in Tk applications (including any
    image file readable by NSImage). A native bitmap name is interpreted
    as follows (in order):

    -   predefined builtin 32x32 icon name (**stop**, **caution**,
        **document**, etc.)

    -   *name*, as defined by **tk::mac::iconBitmap**

    -   NSImage named image name

    -   NSImage url string

    -   4-char OSType of IconServices icon

    The *width* and *height* arguments to **tk::mac::iconBitmap** define
    the dimensions of the image to create, and *-kind* must be one of:

    **-file**

    :   icon of file at given path

    **-fileType**

    :   icon of given file type

    **-osType**

    :   icon of given 4-char OSType file type

    **-systemType**

    :   icon for given IconServices 4-char OSType

    **-namedImage**

    :   named NSImage for given name

    **-imageFile**

    :   image at given path

# SEE ALSO

bind(n), wm(n)

# KEYWORDS

about dialog, antialiasing, Apple event, icon, NSImage
