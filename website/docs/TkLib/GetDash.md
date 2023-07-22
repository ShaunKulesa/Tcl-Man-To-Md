# NAME

Tk_GetDash - convert from string to valid dash structure.

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_GetDash**(*interp, string, dashPtr*)

# ARGUMENTS

Interpreter to use for error reporting.

Textual value to be converted.

Points to place to store the dash pattern value converted from *string*.
Must not be NULL.

# DESCRIPTION

These procedure parses the string and fills in the result in the Tk_Dash
structure. The string can be a list of integers or a character string
containing only and spaces. If all goes well, **TCL_OK** is returned and
a dash descriptor is stored in the variable pointed to by *dashPtr*. If
*string* does not have the proper syntax then **TCL_ERROR** is returned,
an error message is left in the interpreter\'s result, and nothing is
stored at \**dashPtr*.

The first possible syntax is a list of integers. Each element represents
the number of pixels of a line segment. Only the odd segments are drawn
using the color. The other segments are drawn transparent.

The second possible syntax is a character list containing only 5
possible characters The space can be used to enlarge the space between
other line elements, and can not occur in the first position of the
string. Some examples:

        -dash .     = -dash {2 4}
        -dash -     = -dash {6 4}
        -dash -.    = -dash {6 4 2 4}
        -dash -..   = -dash {6 4 2 4 2 4}
        -dash {. }  = -dash {2 8}
        -dash ,     = -dash {4 4}

The main difference between this syntax and the numeric is that it is
shape-conserving. This means that all values in the dash list will be
multiplied by the line width before display. This ensures that will
always be displayed as a dot and always as a dash regardless of the line
width.

On systems where only a limited set of dash patterns, the dash pattern
will be displayed as the most close dash pattern that is available. For
example, on Windows only the first 4 of the above examples are
available; the last 2 examples will be displayed identically to the
first one.

# SEE ALSO

canvas(n), Tk_CreateItemType(3)

# KEYWORDS

dash, conversion
