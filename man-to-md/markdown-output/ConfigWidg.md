# NAME

Tk_ConfigureWidget, Tk_ConfigureInfo, Tk_ConfigureValue,
Tk_FreeOptions - process configuration options for widgets

# SYNOPSIS

**#include \<tk.h\>**

int **Tk_ConfigureWidget(***interp, tkwin, specs, argc, argv, widgRec,
flags***)**

int **Tk_ConfigureInfo(***interp, tkwin, specs, widgRec, argvName,
flags***)**

int **Tk_ConfigureValue(***interp, tkwin, specs, widgRec, argvName,
flags***)**

**Tk_FreeOptions(***specs, widgRec, display, flags***)**

# ARGUMENTS

Interpreter to use for returning error messages.

Window used to represent widget (needed to set up X resources).

Pointer to table specifying legal configuration options for this widget.

Number of arguments in *argv*.

Command-line options for configuring widget.

Points to widget record structure. Fields in this structure get modified
by **Tk_ConfigureWidget** to hold configuration information.

If non-zero, then it specifies an OR-ed combination of flags that
control the processing of configuration information.
**TK_CONFIG_ARGV_ONLY** causes the option database and defaults to be
ignored, and flag bits **TK_CONFIG_USER_BIT** and higher are used to
selectively disable entries in *specs*.

The name of the type of a widget record.

The name of a field in records of type *type*.

The name used on Tcl command lines to refer to a particular option (e.g.
when creating a widget or invoking the **configure** widget command). If
non-NULL, then information is returned only for this option. If NULL,
then information is returned for all available options.

Display containing widget whose record is being freed; needed in order
to free up resources.

# DESCRIPTION

Note: **Tk_ConfigureWidget** should be replaced with the new **Tcl_Obj**
based API **Tk_SetOptions**. The old interface is retained for backward
compatibility.

**Tk_ConfigureWidget** is called to configure various aspects of a
widget, such as colors, fonts, border width, etc. It is intended as a
convenience procedure to reduce the amount of code that must be written
in individual widget managers to handle configuration information. It is
typically invoked when widgets are created, and again when the
**configure** command is invoked for a widget. Although intended
primarily for widgets, **Tk_ConfigureWidget** can be used in other
situations where *argc-argv* information is to be used to fill in a
record structure, such as configuring graphical elements for a canvas
widget or entries of a menu.

**Tk_ConfigureWidget** processes a table specifying the configuration
options that are supported (*specs*) and a collection of command-line
arguments (*argc* and *argv*) to fill in fields of a record (*widgRec*).
It uses the option database and defaults specified in *specs* to fill in
fields of *widgRec* that are not specified in *argv*.
**Tk_ConfigureWidget** normally returns the value **TCL_OK**; in this
case it does not modify *interp*. If an error occurs then **TCL_ERROR**
is returned and **Tk_ConfigureWidget** will leave an error message in
interpreter *interp*\'s result in the standard Tcl fashion. In the event
of an error return, some of the fields of *widgRec* could already have
been set, if configuration information for them was successfully
processed before the error occurred. The other fields will be set to
reasonable initial values so that **Tk_FreeOptions** can be called for
cleanup.

The *specs* array specifies the kinds of configuration options expected
by the widget. Each of its entries specifies one configuration option
and has the following structure:

    typedef struct {
        int type;
        const char *argvName;
        const char *dbName;
        const char *dbClass;
        const char *defValue;
        int offset;
        int specFlags;
        const Tk_CustomOption *customPtr;
    } Tk_ConfigSpec;

The *type* field indicates what type of configuration option this is
(e.g. **TK_CONFIG_COLOR** for a color value, or **TK_CONFIG_INT** for an
integer value). The *type* field indicates how to use the value of the
option (more on this below). The *argvName* field is a string such as or
which is compared with the values in *argv* (if *argvName* is NULL it
means this is a grouped entry; see **GROUPED ENTRIES** below). The
*dbName* and *dbClass* fields are used to look up a value for this
option in the option database. The *defValue* field specifies a default
value for this configuration option if no value is specified in either
*argv* or the option database. *Offset* indicates where in *widgRec* to
store information about this option, and *specFlags* contains additional
information to control the processing of this configuration option (see
FLAGS below). The last field, *customPtr*, is only used if *type* is
**TK_CONFIG_CUSTOM**; see CUSTOM OPTION TYPES below.

**Tk_ConfigureWidget** first processes *argv* to see which (if any)
configuration options are specified there. *Argv* must contain an even
number of fields; the first of each pair of fields must match the
*argvName* of some entry in *specs* (unique abbreviations are
acceptable), and the second field of the pair contains the value for
that configuration option. If there are entries in *spec* for which
there were no matching entries in *argv*, **Tk_ConfigureWidget** uses
the *dbName* and *dbClass* fields of the *specs* entry to probe the
option database; if a value is found, then it is used as the value for
the option. Finally, if no entry is found in the option database, the
*defValue* field of the *specs* entry is used as the value for the
configuration option. If the *defValue* is NULL, or if the
**TK_CONFIG_DONT_SET_DEFAULT** bit is set in *flags*, then there is no
default value and this *specs* entry will be ignored if no value is
specified in *argv* or the option database.

Once a string value has been determined for a configuration option,
**Tk_ConfigureWidget** translates the string value into a more useful
form, such as a color if *type* is **TK_CONFIG_COLOR** or an integer if
*type* is **TK_CONFIG_INT**. This value is then stored in the record
pointed to by *widgRec*. This record is assumed to contain information
relevant to the manager of the widget; its exact type is unknown to
**Tk_ConfigureWidget**. The *offset* field of each *specs* entry
indicates where in *widgRec* to store the information about this
configuration option. You should use the **Tk_Offset** macro to generate
*offset* values (see below for a description of **Tk_Offset**). The
location indicated by *widgRec* and *offset* will be referred to as the
in the descriptions below.

The *type* field of each entry in *specs* determines what to do with the
string value of that configuration option. The legal values for *type*,
and the corresponding actions, are:

**TK_CONFIG_ACTIVE_CURSOR**

:   The value must be an ASCII string identifying a cursor in a form
    suitable for passing to **Tk_GetCursor**. The value is converted to
    a **Tk_Cursor** by calling **Tk_GetCursor** and the result is stored
    in the target. In addition, the resulting cursor is made the active
    cursor for *tkwin* by calling **XDefineCursor**. If
    **TK_CONFIG_NULL_OK** is specified in *specFlags* then the value may
    be an empty string, in which case the target and *tkwin*\'s active
    cursor will be set to **None**. If the previous value of the target
    was not **None**, then it is freed by passing it to
    **Tk_FreeCursor**.

**TK_CONFIG_ANCHOR**

:   The value must be an ASCII string identifying an anchor point in one
    of the ways accepted by **Tk_GetAnchor**. The string is converted to
    a **Tk_Anchor** by calling **Tk_GetAnchor** and the result is stored
    in the target.

**TK_CONFIG_BITMAP**

:   The value must be an ASCII string identifying a bitmap in a form
    suitable for passing to **Tk_GetBitmap**. The value is converted to
    a **Pixmap** by calling **Tk_GetBitmap** and the result is stored in
    the target. If **TK_CONFIG_NULL_OK** is specified in *specFlags*
    then the value may be an empty string, in which case the target is
    set to **None**. If the previous value of the target was not
    **None**, then it is freed by passing it to **Tk_FreeBitmap**.

**TK_CONFIG_BOOLEAN**

:   The value must be an ASCII string specifying a boolean value. Any of
    the values or or an abbreviation of one of these values, means true;
    any of the values or or an abbreviation of one of these values,
    means false. The target is expected to be an integer; for true
    values it will be set to 1 and for false values it will be set to 0.

**TK_CONFIG_BORDER**

:   The value must be an ASCII string identifying a border color in a
    form suitable for passing to **Tk_Get3DBorder**. The value is
    converted to a (**Tk_3DBorder \***) by calling **Tk_Get3DBorder**
    and the result is stored in the target. If **TK_CONFIG_NULL_OK** is
    specified in *specFlags* then the value may be an empty string, in
    which case the target will be set to NULL. If the previous value of
    the target was not NULL, then it is freed by passing it to
    **Tk_Free3DBorder**.

**TK_CONFIG_CAP_STYLE**

:   The value must be an ASCII string identifying a cap style in one of
    the ways accepted by **Tk_GetCapStyle**. The string is converted to
    an integer value corresponding to the cap style by calling
    **Tk_GetCapStyle** and the result is stored in the target.

**TK_CONFIG_COLOR**

:   The value must be an ASCII string identifying a color in a form
    suitable for passing to **Tk_GetColor**. The value is converted to
    an (**XColor \***) by calling **Tk_GetColor** and the result is
    stored in the target. If **TK_CONFIG_NULL_OK** is specified in
    *specFlags* then the value may be an empty string, in which case the
    target will be set to **None**. If the previous value of the target
    was not NULL, then it is freed by passing it to **Tk_FreeColor**.

**TK_CONFIG_CURSOR**

:   This option is identical to **TK_CONFIG_ACTIVE_CURSOR** except that
    the new cursor is not made the active one for *tkwin*.

**TK_CONFIG_CUSTOM**

:   This option allows applications to define new option types. The
    *customPtr* field of the entry points to a structure defining the
    new option type. See the section **CUSTOM OPTION TYPES** below for
    details.

**TK_CONFIG_DOUBLE**

:   The value must be an ASCII floating-point number in the format
    accepted by **strtol**. The string is converted to a **double**
    value, and the value is stored in the target.

**TK_CONFIG_END**

:   Marks the end of the table. The last entry in *specs* must have this
    type; all of its other fields are ignored and it will never match
    any arguments.

**TK_CONFIG_FONT**

:   The value must be an ASCII string identifying a font in a form
    suitable for passing to **Tk_GetFont**. The value is converted to a
    **Tk_Font** by calling **Tk_GetFont** and the result is stored in
    the target. If **TK_CONFIG_NULL_OK** is specified in *specFlags*
    then the value may be an empty string, in which case the target will
    be set to NULL. If the previous value of the target was not NULL,
    then it is freed by passing it to **Tk_FreeFont**.

**TK_CONFIG_INT**

:   The value must be an ASCII integer string in the format accepted by
    **strtol** (e.g. and prefixes may be used to specify octal or
    hexadecimal numbers, respectively). The string is converted to an
    integer value and the integer is stored in the target.

**TK_CONFIG_JOIN_STYLE**

:   The value must be an ASCII string identifying a join style in one of
    the ways accepted by **Tk_GetJoinStyle**. The string is converted to
    an integer value corresponding to the join style by calling
    **Tk_GetJoinStyle** and the result is stored in the target.

**TK_CONFIG_JUSTIFY**

:   The value must be an ASCII string identifying a justification method
    in one of the ways accepted by **Tk_GetJustify**. The string is
    converted to a **Tk_Justify** by calling **Tk_GetJustify** and the
    result is stored in the target.

**TK_CONFIG_MM**

:   The value must specify a screen distance in one of the forms
    acceptable to **Tk_GetScreenMM**. The string is converted to
    double-precision floating-point distance in millimeters and the
    value is stored in the target.

**TK_CONFIG_PIXELS**

:   The value must specify screen units in one of the forms acceptable
    to **Tk_GetPixels**. The string is converted to an integer distance
    in pixels and the value is stored in the target.

**TK_CONFIG_RELIEF**

:   The value must be an ASCII string identifying a relief in a form
    suitable for passing to **Tk_GetRelief**. The value is converted to
    an integer relief value by calling **Tk_GetRelief** and the result
    is stored in the target.

**TK_CONFIG_STRING**

:   A copy of the value is made by allocating memory space with
    **Tcl_Alloc** and copying the value into the dynamically-allocated
    space. A pointer to the new string is stored in the target. If
    **TK_CONFIG_NULL_OK** is specified in *specFlags* then the value may
    be an empty string, in which case the target will be set to NULL. If
    the previous value of the target was not NULL, then it is freed by
    passing it to **Tcl_Free**.

**TK_CONFIG_SYNONYM**

:   This *type* value identifies special entries in *specs* that are
    synonyms for other entries. If an *argv* value matches the
    *argvName* of a **TK_CONFIG_SYNONYM** entry, the entry is not used
    directly. Instead, **Tk_ConfigureWidget** searches *specs* for
    another entry whose *argvName* is the same as the *dbName* field in
    the **TK_CONFIG_SYNONYM** entry; this new entry is used just as if
    its *argvName* had matched the *argv* value. The synonym mechanism
    allows multiple *argv* values to be used for a single configuration
    option, such as and

**TK_CONFIG_UID**

:   The value is translated to a **Tk_Uid** (by passing it to
    **Tk_GetUid**). The resulting value is stored in the target. If
    **TK_CONFIG_NULL_OK** is specified in *specFlags* and the value is
    an empty string then the target will be set to NULL.

**TK_CONFIG_WINDOW**

:   The value must be a window path name. It is translated to a
    **Tk_Window** token and the token is stored in the target.

# GROUPED ENTRIES

In some cases it is useful to generate multiple resources from a single
configuration value. For example, a color name might be used both to
generate the background color for a widget (using **TK_CONFIG_COLOR**)
and to generate a 3-D border to draw around the widget (using
**TK_CONFIG_BORDER**). In cases like this it is possible to specify that
several consecutive entries in *specs* are to be treated as a group. The
first entry is used to determine a value (using its *argvName*,
*dbName*, *dbClass*, and *defValue* fields). The value will be processed
several times (one for each entry in the group), generating multiple
different resources and modifying multiple targets within *widgRec*.
Each of the entries after the first must have a NULL value in its
*argvName* field; this indicates that the entry is to be grouped with
the entry that precedes it. Only the *type* and *offset* fields are used
from these follow-on entries.

# FLAGS

The *flags* argument passed to **Tk_ConfigureWidget** is used in
conjunction with the *specFlags* fields in the entries of *specs* to
provide additional control over the processing of configuration options.
These values are used in three different ways as described below.

First, if the *flags* argument to **Tk_ConfigureWidget** has the
**TK_CONFIG_ARGV_ONLY** bit set (i.e., *flags* \|
**TK_CONFIG_ARGV_ONLY** != 0), then the option database and *defValue*
fields are not used. In this case, if an entry in *specs* does not match
a field in *argv* then nothing happens: the corresponding target is not
modified. This feature is useful when the goal is to modify certain
configuration options while leaving others in their current state, such
as when a **configure** widget command is being processed.

Second, the *specFlags* field of an entry in *specs* may be used to
control the processing of that entry. Each *specFlags* field may
consists of an OR-ed combination of the following values:

**TK_CONFIG_COLOR_ONLY**

:   If this bit is set then the entry will only be considered if the
    display for *tkwin* has more than one bit plane. If the display is
    monochromatic then this *specs* entry will be ignored.

**TK_CONFIG_MONO_ONLY**

:   If this bit is set then the entry will only be considered if the
    display for *tkwin* has exactly one bit plane. If the display is not
    monochromatic then this *specs* entry will be ignored.

**TK_CONFIG_NULL_OK**

:   This bit is only relevant for some types of entries (see the
    descriptions of the various entry types above). If this bit is set,
    it indicates that an empty string value for the field is acceptable
    and if it occurs then the target should be set to NULL or **None**,
    depending on the type of the target. This flag is typically used to
    allow a feature to be turned off entirely, e.g. set a cursor value
    to **None** so that a window simply inherits its parent\'s cursor.
    If this bit is not set then empty strings are processed as strings,
    which generally results in an error.

**TK_CONFIG_DONT_SET_DEFAULT**

:   If this bit is one, it means that the *defValue* field of the entry
    should only be used for returning the default value in
    **Tk_ConfigureInfo**. In calls to **Tk_ConfigureWidget** no default
    will be supplied for entries with this flag set; it is assumed that
    the caller has already supplied a default value in the target
    location. This flag provides a performance optimization where it is
    expensive to process the default string: the client can compute the
    default once, save the value, and provide it before calling
    **Tk_ConfigureWidget**.

**TK_CONFIG_OPTION_SPECIFIED**

:   This bit is deprecated. It used to be set and cleared by
    **Tk_ConfigureWidget** so that callers could detect what entries
    were specified in *argv*, but it was removed because it was
    inherently thread-unsafe. Code that wishes to detect what options
    were specified should use **Tk_SetOptions** instead.

The **TK_CONFIG_MONO_ONLY** and **TK_CONFIG_COLOR_ONLY** flags are
typically used to specify different default values for monochrome and
color displays. This is done by creating two entries in *specs* that are
identical except for their *defValue* and *specFlags* fields. One entry
should have the value **TK_CONFIG_MONO_ONLY** in its *specFlags* and the
default value for monochrome displays in its *defValue*; the other entry
should have the value **TK_CONFIG_COLOR_ONLY** in its *specFlags* and
the appropriate *defValue* for color displays.

Third, it is possible to use *flags* and *specFlags* together to
selectively disable some entries. This feature is not needed very often.
It is useful in cases where several similar kinds of widgets are
implemented in one place. It allows a single *specs* table to be created
with all the configuration options for all the widget types. When
processing a particular widget type, only entries relevant to that type
will be used. This effect is achieved by setting the high-order bits
(those in positions equal to or greater than **TK_CONFIG_USER_BIT**) in
*specFlags* values or in *flags*. In order for a particular entry in
*specs* to be used, its high-order bits must match exactly the
high-order bits of the *flags* value passed to **Tk_ConfigureWidget**.
If a *specs* table is being used for N different widget types, then N of
the high-order bits will be used. Each *specs* entry will have one of
more of those bits set in its *specFlags* field to indicate the widget
types for which this entry is valid. When calling
**Tk_ConfigureWidget**, *flags* will have a single one of these bits set
to select the entries for the desired widget type. For a working example
of this feature, see the code in tkButton.c.

# TK_OFFSET

The **Tk_Offset** macro is provided as a safe way of generating the
*offset* values for entries in Tk_ConfigSpec structures. It takes two
arguments: the name of a type of record, and the name of a field in that
record. It returns the byte offset of the named field in records of the
given type.

# TK_CONFIGUREINFO

The **Tk_ConfigureInfo** procedure may be used to obtain information
about one or all of the options for a given widget. Given a token for a
window (*tkwin*), a table describing the configuration options for a
class of widgets (*specs*), a pointer to a widget record containing the
current information for a widget (*widgRec*), and a NULL *argvName*
argument, **Tk_ConfigureInfo** generates a string describing all of the
configuration options for the window. The string is placed in
interpreter *interp*\'s result. Under normal circumstances it returns
**TCL_OK**; if an error occurs then it returns **TCL_ERROR** and the
interpreter\'s result will contain an error message.

If *argvName* is NULL, then the value left in the interpreter\'s result
by **Tk_ConfigureInfo** consists of a list of one or more entries, each
of which describes one configuration option (i.e. one entry in *specs*).
Each entry in the list will contain either two or five values. If the
corresponding entry in *specs* has type **TK_CONFIG_SYNONYM**, then the
list will contain two values: the *argvName* for the entry and the
*dbName* (synonym name). Otherwise the list will contain five values:
*argvName*, *dbName*, *dbClass*, *defValue*, and current value. The
current value is computed from the appropriate field of *widgRec* by
calling procedures like **Tk_NameOfColor**.

If the *argvName* argument to **Tk_ConfigureInfo** is non-NULL, then it
indicates a single option, and information is returned only for that
option. The string placed in the interpreter\'s result will be a list
containing two or five values as described above; this will be identical
to the corresponding sublist that would have been returned if *argvName*
had been NULL.

The *flags* argument to **Tk_ConfigureInfo** is used to restrict the
*specs* entries to consider, just as for **Tk_ConfigureWidget**.

# TK_CONFIGUREVALUE

**Tk_ConfigureValue** takes arguments similar to **Tk_ConfigureInfo**;
instead of returning a list of values, it just returns the current value
of the option given by *argvName* (*argvName* must not be NULL). The
value is returned in interpreter *interp*\'s result and **TCL_OK** is
normally returned as the procedure\'s result. If an error occurs in
**Tk_ConfigureValue** (e.g., *argvName* is not a valid option name),
**TCL_ERROR** is returned and an error message is left in the
interpreter\'s result. This procedure is typically called to implement
**cget** widget commands.

# TK_FREEOPTIONS

The **Tk_FreeOptions** procedure may be invoked during widget cleanup to
release all of the resources associated with configuration options. It
scans through *specs* and for each entry corresponding to a resource
that must be explicitly freed (e.g. those with type
**TK_CONFIG_COLOR**), it frees the resource in the widget record. If the
field in the widget record does not refer to a resource (e.g. it
contains a null pointer) then no resource is freed for that entry. After
freeing a resource, **Tk_FreeOptions** sets the corresponding field of
the widget record to null.

# CUSTOM OPTION TYPES

Applications can extend the built-in configuration types with additional
configuration types by writing procedures to parse and print options of
the a type and creating a structure pointing to those procedures:

    typedef struct Tk_CustomOption {
        Tk_OptionParseProc *parseProc;
        Tk_OptionPrintProc *printProc;
        ClientData clientData;
    } Tk_CustomOption;

    typedef int Tk_OptionParseProc(
            ClientData clientData,
            Tcl_Interp *interp,
            Tk_Window tkwin,
            char *value,
            char *widgRec,
            int offset);

    typedef const char *Tk_OptionPrintProc(
            ClientData clientData,
            Tk_Window tkwin,
            char *widgRec,
            int offset,
            Tcl_FreeProc **freeProcPtr);

The Tk_CustomOption structure contains three fields, which are pointers
to the two procedures and a *clientData* value to be passed to those
procedures when they are invoked. The *clientData* value typically
points to a structure containing information that is needed by the
procedures when they are parsing and printing options.

The *parseProc* procedure is invoked by **Tk_ConfigureWidget** to parse
a string and store the resulting value in the widget record. The
*clientData* argument is a copy of the *clientData* field in the
Tk_CustomOption structure. The *interp* argument points to a Tcl
interpreter used for error reporting. *Tkwin* is a copy of the *tkwin*
argument to **Tk_ConfigureWidget**. The *value* argument is a string
describing the value for the option; it could have been specified
explicitly in the call to **Tk_ConfigureWidget** or it could come from
the option database or a default. *Value* will never be a null pointer
but it may point to an empty string. *RecordPtr* is the same as the
*widgRec* argument to **Tk_ConfigureWidget**; it points to the start of
the widget record to modify. The last argument, *offset*, gives the
offset in bytes from the start of the widget record to the location
where the option value is to be placed. The procedure should translate
the string to whatever form is appropriate for the option and store the
value in the widget record. It should normally return **TCL_OK**, but if
an error occurs in translating the string to a value then it should
return **TCL_ERROR** and store an error message in interpreter
*interp*\'s result.

The *printProc* procedure is called by **Tk_ConfigureInfo** to produce a
string value describing an existing option. Its *clientData*, *tkwin*,
*widgRec*, and *offset* arguments all have the same meaning as for
Tk_OptionParseProc procedures. The *printProc* procedure should examine
the option whose value is stored at *offset* in *widgRec*, produce a
string describing that option, and return a pointer to the string. If
the string is stored in dynamically-allocated memory, then the procedure
must set *\*freeProcPtr* to the address of a procedure to call to free
the string\'s memory; **Tk_ConfigureInfo** will call this procedure when
it is finished with the string. If the result string is stored in static
memory then *printProc* need not do anything with the *freeProcPtr*
argument.

Once *parseProc* and *printProc* have been defined and a Tk_CustomOption
structure has been created for them, options of this new type may be
manipulated with Tk_ConfigSpec entries whose *type* fields are
**TK_CONFIG_CUSTOM** and whose *customPtr* fields point to the
Tk_CustomOption structure.

# EXAMPLES

Although the explanation of **Tk_ConfigureWidget** is fairly
complicated, its actual use is pretty straightforward. The easiest way
to get started is to copy the code from an existing widget. The library
implementation of frames (tkFrame.c) has a simple configuration table,
and the library implementation of buttons (tkButton.c) has a much more
complex table that uses many of the fancy *specFlags* mechanisms.

# SEE ALSO

Tk_SetOptions(3)

# KEYWORDS

anchor, bitmap, boolean, border, cap style, color, configuration
options, cursor, custom, double, font, integer, join style, justify,
millimeters, pixels, relief, synonym, uid

<!---
Copyright (c) 1990-1994 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

