# NAME

Tk_CreateOptionTable, Tk_DeleteOptionTable, Tk_InitOptions,
Tk_SetOptions, Tk_FreeSavedOptions, Tk_RestoreSavedOptions,
Tk_GetOptionValue, Tk_GetOptionInfo, Tk_FreeConfigOptions, Tk_Offset -
process configuration options

# SYNOPSIS

**#include \<tk.h\>**

Tk_OptionTable **Tk_CreateOptionTable(***interp, templatePtr***)**

**Tk_DeleteOptionTable(***optionTable***)**

int **Tk_InitOptions(***interp, recordPtr, optionTable, tkwin***)**

int **Tk_SetOptions(***interp, recordPtr, optionTable, objc, objv,
tkwin, savePtr, maskPtr***)**

**Tk_FreeSavedOptions(***savedPtr***)**

**Tk_RestoreSavedOptions(***savedPtr***)**

Tcl_Obj \* **Tk_GetOptionValue(***interp, recordPtr, optionTable,
namePtr, tkwin***)**

Tcl_Obj \* **Tk_GetOptionInfo(***interp, recordPtr, optionTable,
namePtr, tkwin***)**

**Tk_FreeConfigOptions(***recordPtr, optionTable, tkwin***)**

int **Tk_Offset(***type, field***)**

# ARGUMENTS

A Tcl interpreter. Most procedures use this only for returning error
messages; if it is NULL then no error messages are returned. For
**Tk_CreateOptionTable** the value cannot be NULL; it gives the
interpreter in which the option table will be used.

Points to an array of static information that describes the
configuration options that are supported. Used to build a
Tk_OptionTable. The information pointed to by this argument must exist
for the lifetime of the Tk_OptionTable.

Token for an option table. Must have been returned by a previous call to
**Tk_CreateOptionTable**.

Points to structure in which values of configuration options are stored;
fields of this record are modified by procedures such as
**Tk_SetOptions** and read by procedures such as **Tk_GetOptionValue**.

For options such as **TK_OPTION_COLOR**, this argument indicates the
window in which the option will be used. If *optionTable* uses no
window-dependent options, then a NULL value may be supplied for this
argument.

Number of values in *objv*.

Command-line arguments for setting configuring options.

If not NULL, the structure pointed to by this argument is filled in with
the old values of any options that were modified and old values are
restored automatically if an error occurs in **Tk_SetOptions**.

If not NULL, the word pointed to by *maskPtr* is filled in with the
bit-wise OR of the *typeMask* fields for the options that were modified.

Points to a structure previously filled in by **Tk_SetOptions** with old
values of modified options.

The value of this object is the name of a particular option. If NULL is
passed to **Tk_GetOptionInfo** then information is returned for all
options. Must not be NULL when **Tk_GetOptionValue** is called.

The name of the type of a record.

The name of a field in records of type *type*.

# DESCRIPTION

These procedures handle most of the details of parsing configuration
options such as those for Tk widgets. Given a description of what
options are supported, these procedures handle all the details of
parsing options and storing their values into a C structure associated
with the widget or object. The procedures were designed primarily for
widgets in Tk, but they can also be used for other kinds of objects that
have configuration options. In the rest of this manual page will be used
to refer to the object whose options are being managed; in practice the
object may not actually be a widget. The term is used to refer to the
C-level structure in which information about a particular widget or
object is stored.

Note: the easiest way to learn how to use these procedures is to look at
a working example. In Tk, the simplest example is the code that
implements the button family of widgets, which is in **tkButton.c**.
Other examples are in **tkSquare.c** and **tkMenu.c**.

In order to use these procedures, the code that implements the widget
must contain a static array of Tk_OptionSpec structures. This is a
template that describes the various options supported by that class of
widget; there is a separate template for each kind of widget. The
template contains information such as the name of each option, its type,
its default value, and where the value of the option is stored in the
widget record. See TEMPLATES below for more detail.

In order to process configuration options efficiently, the static
template must be augmented with additional information that is available
only at runtime. The procedure **Tk_CreateOptionTable** creates this
dynamic information from the template and returns a Tk_OptionTable token
that describes both the static and dynamic information. All of the other
procedures, such as **Tk_SetOptions**, take a Tk_OptionTable token as
argument. Typically, **Tk_CreateOptionTable** is called the first time
that a widget of a particular class is created and the resulting
Tk_OptionTable is used in the future for all widgets of that class. A
Tk_OptionTable may be used only in a single interpreter, given by the
*interp* argument to **Tk_CreateOptionTable**. When an option table is
no longer needed **Tk_DeleteOptionTable** should be called to free all
of its resources. All of the option tables for a Tcl interpreter are
freed automatically if the interpreter is deleted.

**Tk_InitOptions** is invoked when a new widget is created to set the
default values for all of the widget\'s configuration options that do
not have **TK_OPTION_DONT_SET_DEFAULT** set in their *flags* field.
**Tk_InitOptions** is passed a token for an option table (*optionTable*)
and a pointer to a widget record (*recordPtr*), which is the C structure
that holds information about this widget. **Tk_InitOptions** uses the
information in the option table to choose an appropriate default for
each option, except those having **TK_OPTION_DONT_SET_DEFAULT** set,
then it stores the default value directly into the widget record,
overwriting any information that was already present in the widget
record. **Tk_InitOptions** normally returns **TCL_OK**. If an error
occurred while setting the default values (e.g., because a default value
was erroneous) then **TCL_ERROR** is returned and an error message is
left in *interp*\'s result if *interp* is not NULL.

**Tk_SetOptions** is invoked to modify configuration options based on
information specified in a Tcl command. The command might be one that
creates a new widget, or a command that modifies options on an existing
widget. The *objc* and *objv* arguments describe the values of the
arguments from the Tcl command. *Objv* must contain an even number of
objects: the first object of each pair gives the name of an option and
the second object gives the new value for that option. **Tk_SetOptions**
looks up each name in *optionTable*, checks that the new value of the
option conforms to the type in *optionTable*, and stores the value of
the option into the widget record given by *recordPtr*.
**Tk_SetOptions** normally returns **TCL_OK**. If an error occurred
(such as an unknown option name or an illegal option value) then
**TCL_ERROR** is returned and an error message is left in *interp*\'s
result if *interp* is not NULL.

**Tk_SetOptions** has two additional features. First, if the *maskPtr*
argument is not NULL then it points to an integer value that is filled
in with information about the options that were modified. For each
option in the template passed to **Tk_CreateOptionTable** there is a
*typeMask* field. The bits of this field are defined by the code that
implements the widget; for example, each bit might correspond to a
particular configuration option. Alternatively, bits might be used
functionally. For example, one bit might be used for redisplay: all
options that affect the widget\'s display, such that changing the option
requires the widget to be redisplayed, might have that bit set. Another
bit might indicate that the geometry of the widget must be recomputed,
and so on. **Tk_SetOptions** OR\'s together the *typeMask* fields from
all the options that were modified and returns this value at
\**maskPtr*; the caller can then use this information to optimize itself
so that, for example, it does not redisplay the widget if the modified
options do not affect the widget\'s appearance.

The second additional feature of **Tk_SetOptions** has to do with error
recovery. If an error occurs while processing configuration options,
this feature makes it possible to restore all the configuration options
to their previous values. Errors can occur either while processing
options in **Tk_SetOptions** or later in the caller. In many cases the
caller does additional processing after **Tk_SetOptions** returns; for
example, it might use an option value to set a trace on a variable and
may detect an error if the variable is an array instead of a scalar.
Error recovery is enabled by passing in a non-NULL value for the
*savePtr* argument to **Tk_SetOptions**; this should be a pointer to an
uninitialized Tk_SavedOptions structure on the caller\'s stack.
**Tk_SetOptions** overwrites the structure pointed to by *savePtr* with
information about the old values of any options modified by the
procedure. If **Tk_SetOptions** returns successfully, the caller uses
the structure in one of two ways. If the caller completes its processing
of the new options without any errors, then it must pass the structure
to **Tk_FreeSavedOptions** so that the old values can be freed. If the
caller detects an error in its processing of the new options, then it
should pass the structure to **Tk_RestoreSavedOptions**, which will copy
the old values back into the widget record and free the new values. If
**Tk_SetOptions** detects an error then it automatically restores any
options that had already been modified and leaves \**savePtr* in an
empty state: the caller need not call either **Tk_FreeSavedOptions** or
**Tk_RestoreSavedOptions**. If the *savePtr* argument to
**Tk_SetOptions** is NULL then **Tk_SetOptions** frees each old option
value immediately when it sets a new value for the option. In this case,
if an error occurs in the third option, the old values for the first two
options cannot be restored.

**Tk_GetOptionValue** returns the current value of a configuration
option for a particular widget. The *namePtr* argument contains the name
of an option; **Tk_GetOptionValue** uses *optionTable* to lookup the
option and extract its value from the widget record pointed to by
*recordPtr*, then it returns an object containing that value. If an
error occurs (e.g., because *namePtr* contains an unknown option name)
then NULL is returned and an error message is left in *interp*\'s result
unless *interp* is NULL.

**Tk_GetOptionInfo** returns information about configuration options in
a form suitable for **configure** widget commands. If the *namePtr*
argument is not NULL, it points to an object that gives the name of a
configuration option; **Tk_GetOptionInfo** returns an object containing
a list with five elements, which are the name of the option, the name
and class used for the option in the option database, the default value
for the option, and the current value for the option. If the *namePtr*
argument is NULL, then **Tk_GetOptionInfo** returns information about
all options in the form of a list of lists; each sublist describes one
option. Synonym options are handled differently depending on whether
*namePtr* is NULL: if *namePtr* is NULL then the sublist for each
synonym option has only two elements, which are the name of the option
and the name of the other option that it refers to; if *namePtr* is
non-NULL and names a synonym option then the object returned is the
five-element list for the other option that the synonym refers to. If an
error occurs (e.g., because *namePtr* contains an unknown option name)
then NULL is returned and an error message is left in *interp*\'s result
unless *interp* is NULL.

**Tk_FreeConfigOptions** must be invoked when a widget is deleted. It
frees all of the resources associated with any of the configuration
options defined in *recordPtr* by *optionTable*.

The **Tk_Offset** macro is provided as a safe way of generating the
*objOffset* and *internalOffset* values for entries in Tk_OptionSpec
structures. It takes two arguments: the name of a type of record, and
the name of a field in that record. It returns the byte offset of the
named field in records of the given type.

# TEMPLATES

The array of Tk_OptionSpec structures passed to **Tk_CreateOptionTable**
via its *templatePtr* argument describes the configuration options
supported by a particular class of widgets. Each structure specifies one
configuration option and has the following fields:

    typedef struct {
        Tk_OptionType type;
        const char *optionName;
        const char *dbName;
        const char *dbClass;
        const char *defValue;
        int objOffset;
        int internalOffset;
        int flags;
        const void *clientData;
        int typeMask;
    } Tk_OptionSpec;

The *type* field indicates what kind of configuration option this is
(e.g. **TK_OPTION_COLOR** for a color value, or **TK_OPTION_INT** for an
integer value). *Type* determines how the value of the option is parsed
(more on this below). The *optionName* field is a string such as
**-font** or **-bg**; it is the name used for the option in Tcl commands
and passed to procedures via the *objc* or *namePtr* arguments. The
*dbName* and *dbClass* fields are used by **Tk_InitOptions** to look up
a default value for this option in the option database; if *dbName* is
NULL then the option database is not used by **Tk_InitOptions** for this
option. The *defValue* field specifies a default value for this
configuration option if no value is specified in the option database.
The *objOffset* and *internalOffset* fields indicate where to store the
value of this option in widget records (more on this below); values for
the *objOffset* and *internalOffset* fields should always be generated
with the **Tk_Offset** macro. The *flags* field contains additional
information to control the processing of this configuration option (see
below for details). *ClientData* provides additional type-specific data
needed by certain types. For instance, for **TK_OPTION_COLOR** types,
*clientData* is a string giving the default value to use on monochrome
displays. See the descriptions of the different types below for details.
The last field, *typeMask*, is used by **Tk_SetOptions** to return
information about which options were modified; see the description of
**Tk_SetOptions** above for details.

When **Tk_InitOptions** and **Tk_SetOptions** store the value of an
option into the widget record, they can do it in either of two ways. If
the *objOffset* field of the Tk_OptionSpec is greater than or equal to
zero, then the value of the option is stored as a (Tcl_Obj \*) at the
location in the widget record given by *objOffset*. If the
*internalOffset* field of the Tk_OptionSpec is greater than or equal to
zero, then the value of the option is stored in a type-specific internal
form at the location in the widget record given by *internalOffset*. For
example, if the option\'s type is **TK_OPTION_INT** then the internal
form is an integer. If the *objOffset* or *internalOffset* field is
negative then the value is not stored in that form. At least one of the
offsets must be greater than or equal to zero.

The *flags* field consists of one or more bits ORed together. The
following flags are supported:

**TK_OPTION_NULL_OK**

:   If this bit is set for an option then an empty string will be
    accepted as the value for the option and the resulting internal form
    will be a NULL pointer, a zero value, or **None**, depending on the
    type of the option. If the flag is not set then empty strings will
    result in errors. **TK_OPTION_NULL_OK** is typically used to allow a
    feature to be turned off entirely, e.g. set a cursor value to
    **None** so that a window simply inherits its parent\'s cursor. Not
    all option types support the **TK_OPTION_NULL_OK** flag; for those
    that do, there is an explicit indication of that fact in the
    descriptions below.

**TK_OPTION_DONT_SET_DEFAULT**

:   If this bit is set for an option then no default value will be set
    in **Tk_InitOptions** for this option. Neither the option database,
    nor any system default value, nor *optionTable* are used to give a
    default value to this option. Instead it is assumed that the caller
    has already supplied a default value in the widget code.

The *type* field of each Tk_OptionSpec structure determines how to parse
the value of that configuration option. The legal value for *type*, and
the corresponding actions, are described below. If the type requires a
*tkwin* value to be passed into procedures like **Tk_SetOptions**, or if
it uses the *clientData* field of the Tk_OptionSpec, then it is
indicated explicitly; if not mentioned, the type requires neither
*tkwin* nor *clientData*.

**TK_OPTION_ANCHOR**

:   The value must be a standard anchor position such as **ne** or
    **center**. The internal form is a Tk_Anchor value like the ones
    returned by **Tk_GetAnchorFromObj**.

**TK_OPTION_BITMAP**

:   The value must be a standard Tk bitmap name. The internal form is a
    Pixmap token like the ones returned by **Tk_AllocBitmapFromObj**.
    This option type requires *tkwin* to be supplied to procedures such
    as **Tk_SetOptions**, and it supports the **TK_OPTION_NULL_OK**
    flag.

**TK_OPTION_BOOLEAN**

:   The value must be a standard boolean value such as **true** or
    **no**. The internal form is an integer with value 0 or 1.

**TK_OPTION_BORDER**

:   The value must be a standard color name such as **red** or
    **#ff8080**. The internal form is a Tk_3DBorder token like the ones
    returned by **Tk_Alloc3DBorderFromObj**. This option type requires
    *tkwin* to be supplied to procedures such as **Tk_SetOptions**, and
    it supports the **TK_OPTION_NULL_OK** flag.

**TK_OPTION_COLOR**

:   The value must be a standard color name such as **red** or
    **#ff8080**. The internal form is an (XColor \*) token like the ones
    returned by **Tk_AllocColorFromObj**. This option type requires
    *tkwin* to be supplied to procedures such as **Tk_SetOptions**, and
    it supports the **TK_OPTION_NULL_OK** flag.

**TK_OPTION_CURSOR**

:   The value must be a standard cursor name such as **cross** or
    **\@foo**. The internal form is a Tk_Cursor token like the ones
    returned by **Tk_AllocCursorFromObj**. This option type requires
    *tkwin* to be supplied to procedures such as **Tk_SetOptions**, and
    when the option is set the cursor for the window is changed by
    calling **XDefineCursor**. This option type also supports the
    **TK_OPTION_NULL_OK** flag.

**TK_OPTION_CUSTOM**

:   This option allows applications to define new option types. The
    clientData field of the entry points to a structure defining the new
    option type. See the section **CUSTOM OPTION TYPES** below for
    details.

**TK_OPTION_DOUBLE**

:   The string value must be a floating-point number in the format
    accepted by **strtol**. The internal form is a C **double** value.
    This option type supports the **TK_OPTION_NULL_OK** flag; if a NULL
    value is set, the internal representation is set to zero.

**TK_OPTION_END**

:   Marks the end of the template. There must be a Tk_OptionSpec
    structure with *type* **TK_OPTION_END** at the end of each template.
    If the *clientData* field of this structure is not NULL, then it
    points to an additional array of Tk_OptionSpec\'s, which is itself
    terminated by another **TK_OPTION_END** entry. Templates may be
    chained arbitrarily deeply. This feature allows common options to be
    shared by several widget classes.

**TK_OPTION_FONT**

:   The value must be a standard font name such as **Times 16**. The
    internal form is a Tk_Font handle like the ones returned by
    **Tk_AllocFontFromObj**. This option type requires *tkwin* to be
    supplied to procedures such as **Tk_SetOptions**, and it supports
    the **TK_OPTION_NULL_OK** flag.

**TK_OPTION_INT**

:   The string value must be an integer in the format accepted by
    **strtol** (e.g. **0** and **0x** prefixes may be used to specify
    octal or hexadecimal numbers, respectively). The internal form is a
    C **int** value.

**TK_OPTION_JUSTIFY**

:   The value must be a standard justification value such as **left**.
    The internal form is a Tk_Justify like the values returned by
    **Tk_GetJustifyFromObj**.

**TK_OPTION_PIXELS**

:   The value must specify a screen distance such as **2i** or **6.4**.
    The internal form is an integer value giving a distance in pixels,
    like the values returned by **Tk_GetPixelsFromObj**. Note: if the
    *objOffset* field is not used then information about the original
    value of this option will be lost. See **OBJOFFSET VS.
    INTERNALOFFSET** below for details. This option type supports the
    **TK_OPTION_NULL_OK** flag; if a NULL value is set, the internal
    representation is set to zero.

**TK_OPTION_RELIEF**

:   The value must be standard relief such as **raised**. The internal
    form is an integer relief value such as **TK_RELIEF_RAISED**. This
    option type supports the **TK_OPTION_NULL_OK** flag; if a NULL value
    is set, the internal representation is set to **TK_RELIEF_NULL**.

**TK_OPTION_STRING**

:   The value may be any string. The internal form is a (char \*)
    pointer that points to a dynamically allocated copy of the value.
    This option type supports the **TK_OPTION_NULL_OK** flag.

**TK_OPTION_STRING_TABLE**

:   For this type, *clientData* is a pointer to an array of strings
    suitable for passing to **Tcl_GetIndexFromObj**. The value must be
    one of the strings in the table, or a unique abbreviation of one of
    the strings. The internal form is an integer giving the index into
    the table of the matching string, like the return value from
    **Tcl_GetStringFromObj**. This option type supports the
    **TK_OPTION_NULL_OK** flag; if a NULL value is set, the internal
    representation is set to -1.

**TK_OPTION_SYNONYM**

:   This type is used to provide alternative names for an option (for
    example, **-bg** is often used as a synonym for **-background**).
    The **clientData** field is a string that gives the name of another
    option in the same table. Whenever the synonym option is used, the
    information from the other option will be used instead.

**TK_OPTION_WINDOW**

:   The value must be a window path name. The internal form is a
    **Tk_Window** token for the window. This option type requires
    *tkwin* to be supplied to procedures such as **Tk_SetOptions** (in
    order to identify the application), and it supports the
    **TK_OPTION_NULL_OK** flag.

# STORAGE MANAGEMENT ISSUES

If a field of a widget record has its offset stored in the *objOffset*
or *internalOffset* field of a Tk_OptionSpec structure then the
procedures described here will handle all of the storage allocation and
resource management issues associated with the field. When the value of
an option is changed, **Tk_SetOptions** (or **Tk_FreeSavedOptions**)
will automatically free any resources associated with the old value,
such as Tk_Fonts for **TK_OPTION_FONT** options or dynamically allocated
memory for **TK_OPTION_STRING** options. For an option stored as an
object using the *objOffset* field of a Tk_OptionSpec, the widget record
shares the object pointed to by the *objv* value from the call to
**Tk_SetOptions**. The reference count for this object is incremented
when a pointer to it is stored in the widget record and decremented when
the option is modified. When the widget is deleted
**Tk_FreeConfigOptions** should be invoked; it will free the resources
associated with all options and decrement reference counts for any
objects.

However, the widget code is responsible for storing NULL or **None** in
all pointer and token fields before invoking **Tk_InitOptions**. This is
needed to allow proper cleanup in the rare case where an error occurs in
**Tk_InitOptions**.

# OBJOFFSET VS. INTERNALOFFSET

In most cases it is simplest to use the *internalOffset* field of a
Tk_OptionSpec structure and not the *objOffset* field. This makes the
internal form of the value immediately available to the widget code so
the value does not have to be extracted from an object each time it is
used. However, there are two cases where the *objOffset* field is
useful. The first case is for **TK_OPTION_PIXELS** options. In this
case, the internal form is an integer pixel value that is valid only for
a particular screen. If the value of the option is retrieved, it will be
returned as a simple number. For example, after the command **.b
configure -borderwidth 2m**, the command **.b configure -borderwidth**
might return 7, which is the integer pixel value corresponding to
**2m**. Unfortunately, this loses the original screen-independent value.
Thus for **TK_OPTION_PIXELS** options it is better to use the
*objOffset* field. In this case the original value of the option is
retained in the object and can be returned when the option is retrieved.
In most cases it is convenient to use the *internalOffset* field as
well, so that the integer value is immediately available for use in the
widget code (alternatively, **Tk_GetPixelsFromObj** can be used to
extract the integer value from the object whenever it is needed). Note:
the problem of losing information on retrievals exists only for
**TK_OPTION_PIXELS** options.

The second reason to use the *objOffset* field is in order to implement
new types of options not supported by these procedures. To implement a
new type of option, you can use **TK_OPTION_STRING** as the type in the
Tk_OptionSpec structure and set the *objOffset* field but not the
*internalOffset* field. Then, after calling **Tk_SetOptions**, convert
the object to internal form yourself.

# CUSTOM OPTION TYPES

Applications can extend the built-in configuration types with additional
configuration types by writing procedures to parse, print, free, and
restore saved copies of the type and creating a structure pointing to
those procedures:

    typedef struct Tk_ObjCustomOption {
        char *name;
        Tk_CustomOptionSetProc *setProc;
        Tk_CustomOptionGetProc *getProc;
        Tk_CustomOptionRestoreProc *restoreProc;
        Tk_CustomOptionFreeProc *freeProc;
        ClientData clientData;
    } Tk_ObjCustomOption;

    typedef int Tk_CustomOptionSetProc(
        ClientData clientData,
        Tcl_Interp *interp,
        Tk_Window tkwin,
        Tcl_Obj **valuePtr,
        char *recordPtr,
        int internalOffset,
        char *saveInternalPtr,
        int flags);

    typedef Tcl_Obj *Tk_CustomOptionGetProc(
        ClientData clientData,
        Tk_Window tkwin,
        char *recordPtr,
        int internalOffset);

    typedef void Tk_CustomOptionRestoreProc(
        ClientData clientData,
        Tk_Window tkwin,
        char *internalPtr,
        char *saveInternalPtr);

    typedef void Tk_CustomOptionFreeProc(
        ClientData clientData,
        Tk_Window tkwin,
        char *internalPtr);

The Tk_ObjCustomOption structure contains six fields: a name for the
custom option type; pointers to the four procedures; and a *clientData*
value to be passed to those procedures when they are invoked. The
*clientData* value typically points to a structure containing
information that is needed by the procedures when they are parsing and
printing options. *RestoreProc* and *freeProc* may be NULL, indicating
that no function should be called for those operations.

The *setProc* procedure is invoked by **Tk_SetOptions** to convert a
Tcl_Obj into an internal representation and store the resulting value in
the widget record. The arguments are:

> *clientData*
>
> :   A copy of the *clientData* field in the Tk_ObjCustomOption
>     structure.
>
> *interp*
>
> :   A pointer to a Tcl interpreter, used for error reporting.
>
> *Tkwin*
>
> :   A copy of the *tkwin* argument to **Tk_SetOptions**
>
> *valuePtr*
>
> :   A pointer to a reference to a Tcl_Obj describing the new value for
>     the option; it could have been specified explicitly in the call to
>     **Tk_SetOptions** or it could come from the option database or a
>     default. If the objOffset for the option is non-negative (the
>     option value is stored as a (Tcl_Obj \*) in the widget record),
>     the Tcl_Obj pointer referenced by *valuePtr* is the pointer that
>     will be stored at the objOffset for the option. *SetProc* may
>     modify the value if necessary; for example, *setProc* may change
>     the value to NULL to support the **TK_OPTION_NULL_OK** flag.
>
> *recordPtr*
>
> :   A pointer to the start of the widget record to modify.
>
> *internalOffset*
>
> :   Offset in bytes from the start of the widget record to the
>     location where the internal representation of the option value is
>     to be placed.
>
> *saveInternalPtr*
>
> :   A pointer to storage allocated in a Tk_SavedOptions structure for
>     the internal representation of the original option value. Before
>     setting the option to its new value, *setProc* should set the
>     value referenced by *saveInternalPtr* to the original value of the
>     option in order to support **Tk_RestoreSavedOptions**.
>
> *flags*
>
> :   A copy of the *flags* field in the Tk_OptionSpec structure for the
>     option

*SetProc* returns a standard Tcl result: **TCL_OK** to indicate
successful processing, or **TCL_ERROR** to indicate a failure of any
kind. An error message may be left in the Tcl interpreter given by
*interp* in the case of an error.

The *getProc* procedure is invoked by **Tk_GetOptionValue** and
**Tk_GetOptionInfo** to retrieve a Tcl_Obj representation of the
internal representation of an option. The *clientData* argument is a
copy of the *clientData* field in the Tk_ObjCustomOption structure.
*Tkwin* is a copy of the *tkwin* argument to **Tk_GetOptionValue** or
**Tk_GetOptionInfo**. *RecordPtr* is a pointer to the beginning of the
widget record to query. *InternalOffset* is the offset in bytes from the
beginning of the widget record to the location where the internal
representation of the option value is stored. *GetProc* must return a
pointer to a Tcl_Obj representing the value of the option.

The *restoreProc* procedure is invoked by **Tk_RestoreSavedOptions** to
restore a previously saved internal representation of a custom option
value. The *clientData* argument is a copy of the *clientData* field in
the Tk_ObjCustomOption structure. *Tkwin* is a copy of the *tkwin*
argument to **Tk_GetOptionValue** or **Tk_GetOptionInfo**. *InternalPtr*
is a pointer to the location where internal representation of the option
value is stored. *SaveInternalPtr* is a pointer to the saved value.
*RestoreProc* must copy the value from *saveInternalPtr* to
*internalPtr* to restore the value. *RestoreProc* need not free any
memory associated with either *internalPtr* or *saveInternalPtr*;
*freeProc* will be invoked to free that memory if necessary.
*RestoreProc* has no return value.

The *freeProc* procedure is invoked by **Tk_SetOptions** and
**Tk_FreeSavedOptions** to free any storage allocated for the internal
representation of a custom option. The *clientData* argument is a copy
of the *clientData* field in the Tk_ObjCustomOption structure. *Tkwin*
is a copy of the *tkwin* argument to **Tk_GetOptionValue** or
**Tk_GetOptionInfo**. *InternalPtr* is a pointer to the location where
the internal representation of the option value is stored. The
*freeProc* must free any storage associated with the option. *FreeProc*
has no return value.

# KEYWORDS

anchor, bitmap, boolean, border, color, configuration option, cursor,
double, font, integer, justify, pixels, relief, screen distance, synonym
