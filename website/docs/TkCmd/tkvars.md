# NAME

geometry, tk_library, tk_patchLevel, tk_strictMotif, tk_version -
Variables used or set by Tk

# DESCRIPTION

The following Tcl variables are either set or used by Tk at various
times in its execution:

**tk_library**

:   This variable holds the file name for a directory containing a
    library of Tcl scripts related to Tk. These scripts include an
    initialization file that is normally processed whenever a Tk
    application starts up, plus other files containing procedures that
    implement default behaviors for widgets.

    The initial value of **tk_library** is set when Tk is added to an
    interpreter; this is done by searching several different directories
    until one is found that contains an appropriate Tk startup script.
    If the **TK_LIBRARY** environment variable exists, then the
    directory it names is checked first. If **TK_LIBRARY** is not set or
    does not refer to an appropriate directory, then Tk checks several
    other directories based on a compiled-in default location, the
    location of the Tcl library directory, the location of the binary
    containing the application, and the current working directory.

    The variable can be modified by an application to switch to a
    different library.

**tk_patchLevel**

:   Contains a dot-separated sequence of decimal integers giving the
    current patch level for Tk. The patch level is incremented for each
    new release or patch, and it uniquely identifies an official version
    of Tk.

    This value is normally the same as the result of

**tk_strictMotif**

:   This variable is set to zero by default. If an application sets it
    to one, then Tk attempts to adhere as closely as possible to Motif
    look-and-feel standards. For example, active elements such as
    buttons and scrollbar sliders will not change color when the pointer
    passes over them. Modern applications should not normally set this
    variable.

**tk_version**

:   Tk sets this variable in the interpreter for each application. The
    variable holds the current version number of the Tk library in the
    form *major*.*minor*. *Major* and *minor* are integers. The major
    version number increases in any Tk release that includes changes
    that are not backward compatible (i.e. whenever existing Tk
    applications and scripts may have to change to work with the new
    release). The minor version number increases with each new release
    of Tk, except that it resets to zero whenever the major version
    number changes.

## INTERNAL AND DEBUGGING VARIABLES

These variables should not normally be set by user code.

**tk::Priv**

:   This variable is an array containing several pieces of information
    that are private to Tk. The elements of **tk::Priv** are used by Tk
    library procedures and default bindings. They should not be accessed
    by any code outside Tk.

**tk_textRedraw**

:   

**tk_textRelayout**

:   These variables are set by text widgets when they have debugging
    turned on. The values written to these variables can be used to test
    or debug text widget operations. These variables are mostly used by
    Tk\'s test suite.

# OTHER GLOBAL VARIABLES

The following variables are only guaranteed to exist in **wish**
executables; the Tk library does not define them itself but many Tk
environments do.

**geometry**

:   If set, contains the user-supplied geometry specification to use for
    the main Tk window.

# SEE ALSO

package(n), tclvars(n), wish(1)

# KEYWORDS

environment, text, variables, version
