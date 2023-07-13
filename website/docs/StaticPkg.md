\

# NAME

Tcl_StaticPackage - make a statically linked package available via the
\'load\' command

# SYNOPSIS

    #include <tcl.h>

    Tcl_StaticPackage(interp, prefix, initProc, safeInitProc)

# ARGUMENTS

If not NULL, points to an interpreter into which the package has already
been loaded (i.e., the caller has already invoked the appropriate
initialization procedure). NULL means the package has not yet been
incorporated into any interpreter.

Prefix for library initialization function; should be properly
capitalized (first letter upper-case, all others lower-case).

Procedure to invoke to incorporate this package into a trusted
interpreter.

Procedure to call to incorporate this package into a safe interpreter
(one that will execute untrusted scripts). NULL means the package cannot
be used in safe interpreters.

\

# DESCRIPTION

This procedure may be invoked to announce that a package has been linked
statically with a Tcl application and, optionally, that it has already
been loaded into an interpreter. Once **Tcl_StaticPackage** has been
invoked for a package, it may be loaded into interpreters using the
**load** command. **Tcl_StaticPackage** is normally invoked only by the
**Tcl_AppInit** procedure for the application, not by packages for
themselves (**Tcl_StaticPackage** should only be invoked for statically
loaded packages, and code in the package itself should not need to know
whether the package is dynamically or statically loaded).

When the **load** command is used later to load the package into an
interpreter, one of *initProc* and *safeInitProc* will be invoked,
depending on whether the target interpreter is safe or not. *initProc*
and *safeInitProc* must both match the following prototype:

    typedef int Tcl_PackageInitProc(
            Tcl_Interp *interp);

The *interp* argument identifies the interpreter in which the package is
to be loaded. The initialization procedure must return **TCL_OK** or
**TCL_ERROR** to indicate whether or not it completed successfully; in
the event of an error it should set the interpreter\'s result to point
to an error message. The result or error from the initialization
procedure will be returned as the result of the **load** command that
caused the initialization procedure to be invoked.

# KEYWORDS

initialization procedure, package, static linking

# SEE ALSO

load(n), package(n), Tcl_PkgRequire(3)
