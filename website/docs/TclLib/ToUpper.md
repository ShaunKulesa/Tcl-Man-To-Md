# NAME

Tcl_UniCharToUpper, Tcl_UniCharToLower, Tcl_UniCharToTitle,
Tcl_UtfToUpper, Tcl_UtfToLower, Tcl_UtfToTitle - routines for
manipulating the case of Unicode characters and UTF-8 strings

# SYNOPSIS

**#include \<tcl.h\>**

Tcl_UniChar **Tcl_UniCharToUpper**(*ch*)

Tcl_UniChar **Tcl_UniCharToLower**(*ch*)

Tcl_UniChar **Tcl_UniCharToTitle**(*ch*)

int **Tcl_UtfToUpper**(*str*)

int **Tcl_UtfToLower**(*str*)

int **Tcl_UtfToTitle**(*str*)

# ARGUMENTS

The Unicode character to be converted.

Pointer to UTF-8 string to be converted in place.

# DESCRIPTION

The first three routines convert the case of individual Unicode
characters:

If *ch* represents a lower-case character, **Tcl_UniCharToUpper**
returns the corresponding upper-case character. If no upper-case
character is defined, it returns the character unchanged.

If *ch* represents an upper-case character, **Tcl_UniCharToLower**
returns the corresponding lower-case character. If no lower-case
character is defined, it returns the character unchanged.

If *ch* represents a lower-case character, **Tcl_UniCharToTitle**
returns the corresponding title-case character. If no title-case
character is defined, it returns the corresponding upper-case character.
If no upper-case character is defined, it returns the character
unchanged. Title-case is defined for a small number of characters that
have a different appearance when they are at the beginning of a
capitalized word.

The next three routines convert the case of UTF-8 strings in place in
memory:

**Tcl_UtfToUpper** changes every UTF-8 character in *str* to upper-case.
Because changing the case of a character may change its size, the byte
offset of each character in the resulting string may differ from its
original location. **Tcl_UtfToUpper** writes a null byte at the end of
the converted string. **Tcl_UtfToUpper** returns the new length of the
string in bytes. This new length is guaranteed to be no longer than the
original string length.

**Tcl_UtfToLower** is the same as **Tcl_UtfToUpper** except it turns
each character in the string into its lower-case equivalent.

**Tcl_UtfToTitle** is the same as **Tcl_UtfToUpper** except it turns the
first character in the string into its title-case equivalent and all
following characters into their lower-case equivalents.

# BUGS

At this time, the case conversions are only defined for the Unicode
plane 0 characters. The result for Unicode characters above 0xFFFF is
undefined, but - actually - only the lower 16 bits of the character
value is handled.

# KEYWORDS

utf, unicode, toupper, tolower, totitle, case
