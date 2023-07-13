\

# NAME

Tcl_UniCharIsAlnum, Tcl_UniCharIsAlpha, Tcl_UniCharIsControl,
Tcl_UniCharIsDigit, Tcl_UniCharIsGraph, Tcl_UniCharIsLower,
Tcl_UniCharIsPrint, Tcl_UniCharIsPunct, Tcl_UniCharIsSpace,
Tcl_UniCharIsUpper, Tcl_UniCharIsWordChar - routines for classification
of Tcl_UniChar characters

# SYNOPSIS

    #include <tcl.h>

    int
    Tcl_UniCharIsAlnum(ch)

    int
    Tcl_UniCharIsAlpha(ch)

    int
    Tcl_UniCharIsControl(ch)

    int
    Tcl_UniCharIsDigit(ch)

    int
    Tcl_UniCharIsGraph(ch)

    int
    Tcl_UniCharIsLower(ch)

    int
    Tcl_UniCharIsPrint(ch)

    int
    Tcl_UniCharIsPunct(ch)

    int
    Tcl_UniCharIsSpace(ch)

    int
    Tcl_UniCharIsUpper(ch)

    int
    Tcl_UniCharIsWordChar(ch)

# ARGUMENTS

The Tcl_UniChar to be examined.

\

# DESCRIPTION

All of the routines described examine Unicode characters and return a
boolean value. A non-zero return value means that the character does
belong to the character class associated with the called routine. The
rest of this document just describes the character classes associated
with the various routines.

# CHARACTER CLASSES

**Tcl_UniCharIsAlnum** tests if the character is an alphanumeric Unicode
character.

**Tcl_UniCharIsAlpha** tests if the character is an alphabetic Unicode
character.

**Tcl_UniCharIsControl** tests if the character is a Unicode control
character.

**Tcl_UniCharIsDigit** tests if the character is a numeric Unicode
character.

**Tcl_UniCharIsGraph** tests if the character is any Unicode print
character except space.

**Tcl_UniCharIsLower** tests if the character is a lowercase Unicode
character.

**Tcl_UniCharIsPrint** tests if the character is a Unicode print
character.

**Tcl_UniCharIsPunct** tests if the character is a Unicode punctuation
character.

**Tcl_UniCharIsSpace** tests if the character is a whitespace Unicode
character.

**Tcl_UniCharIsUpper** tests if the character is an uppercase Unicode
character.

**Tcl_UniCharIsWordChar** tests if the character is alphanumeric or a
connector punctuation mark.

# KEYWORDS

unicode, classification
