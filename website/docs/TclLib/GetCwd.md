# NAME

Tcl_GetCwd, Tcl_Chdir - manipulate the current working directory

# SYNOPSIS

**#include \<tcl.h\>**

char \* **Tcl_GetCwd**(*interp*, *bufferPtr*)

int **Tcl_Chdir**(*dirName*)

# ARGUMENTS

Interpreter in which to report an error, if any.

This dynamic string is used to store the current working directory. At
the time of the call it should be uninitialized or free. The caller must
eventually call **Tcl_DStringFree** to free up anything stored here.

File path in UTF-8 format.

# DESCRIPTION

These procedures may be used to manipulate the current working directory
for the application. They provide C-level access to the same
functionality as the Tcl **pwd** command.

**Tcl_GetCwd** returns a pointer to a string specifying the current
directory, or NULL if the current directory could not be determined. If
NULL is returned, an error message is left in the *interp*\'s result.
Storage for the result string is allocated in bufferPtr; the caller must
call **Tcl_DStringFree()** when the result is no longer needed. The
format of the path is UTF-8.

**Tcl_Chdir** changes the applications current working directory to the
value specified in *dirName*. The format of the passed in string must be
UTF-8. The function returns -1 on error or 0 on success.

# KEYWORDS

pwd
