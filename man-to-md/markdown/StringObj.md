\

# NAME

Tcl_NewStringObj, Tcl_NewUnicodeObj, Tcl_SetStringObj,
Tcl_SetUnicodeObj, Tcl_GetStringFromObj, Tcl_GetString,
Tcl_GetUnicodeFromObj, Tcl_GetUnicode, Tcl_GetUniChar,
Tcl_GetCharLength, Tcl_GetRange, Tcl_AppendToObj,
Tcl_AppendUnicodeToObj, Tcl_AppendObjToObj, Tcl_AppendStringsToObj,
Tcl_AppendStringsToObjVA, Tcl_AppendLimitedToObj, Tcl_Format,
Tcl_AppendFormatToObj, Tcl_ObjPrintf, Tcl_AppendPrintfToObj,
Tcl_SetObjLength, Tcl_AttemptSetObjLength, Tcl_ConcatObj - manipulate
Tcl values as strings

# SYNOPSIS

    #include <tcl.h>

    Tcl_Obj *
    Tcl_NewStringObj(bytes, length)

    Tcl_Obj *
    Tcl_NewUnicodeObj(unicode, numChars)

    void
    Tcl_SetStringObj(objPtr, bytes, length)

    void
    Tcl_SetUnicodeObj(objPtr, unicode, numChars)

    char *
    Tcl_GetStringFromObj(objPtr, lengthPtr)

    char *
    Tcl_GetString(objPtr)

    Tcl_UniChar *
    Tcl_GetUnicodeFromObj(objPtr, lengthPtr)

    Tcl_UniChar *
    Tcl_GetUnicode(objPtr)

    Tcl_UniChar
    Tcl_GetUniChar(objPtr, index)

    int
    Tcl_GetCharLength(objPtr)

    Tcl_Obj *
    Tcl_GetRange(objPtr, first, last)

    void
    Tcl_AppendToObj(objPtr, bytes, length)

    void
    Tcl_AppendUnicodeToObj(objPtr, unicode, numChars)

    void
    Tcl_AppendObjToObj(objPtr, appendObjPtr)

    void
    Tcl_AppendStringsToObj(objPtr, string, string, ... (char *) NULL)

    void
    Tcl_AppendStringsToObjVA(objPtr, argList)

    void
    Tcl_AppendLimitedToObj(objPtr, bytes, length, limit, ellipsis)

    Tcl_Obj *
    Tcl_Format(interp, format, objc, objv)

    int
    Tcl_AppendFormatToObj(interp, objPtr, format, objc, objv)

    Tcl_Obj *
    Tcl_ObjPrintf(format, ...)

    void
    Tcl_AppendPrintfToObj(objPtr, format, ...)

    void
    Tcl_SetObjLength(objPtr, newLength)

    int
    Tcl_AttemptSetObjLength(objPtr, newLength)

    Tcl_Obj *
    Tcl_ConcatObj(objc, objv)

# ARGUMENTS

Points to the first byte of an array of UTF-8-encoded bytes used to set
or append to a string value. This byte array may contain embedded null
characters unless *numChars* is negative. (Applications needing null
bytes should represent them as the two-byte sequence *\\300\\200*, use
**Tcl_ExternalToUtf** to convert, or **Tcl_NewByteArrayObj** if the
string is a collection of uninterpreted bytes.)

The number of bytes to copy from *bytes* when initializing, setting, or
appending to a string value. If negative, all bytes up to the first null
are used.

Points to the first byte of an array of Unicode characters used to set
or append to a string value. This byte array may contain embedded null
characters unless *numChars* is negative.

The number of Unicode characters to copy from *unicode* when
initializing, setting, or appending to a string value. If negative, all
characters up to the first null character are used.

The index of the Unicode character to return.

The index of the first Unicode character in the Unicode range to be
returned as a new value.

The index of the last Unicode character in the Unicode range to be
returned as a new value.

Points to a value to manipulate.

The value to append to *objPtr* in **Tcl_AppendObjToObj**.

If non-NULL, the location where **Tcl_GetStringFromObj** will store the
length of a value\'s string representation.

Null-terminated string value to append to *objPtr*.

An argument list which must have been initialized using **va_start**,
and cleared using **va_end**.

Maximum number of bytes to be appended.

Suffix to append when the limit leads to string truncation. If NULL is
passed then the suffix is used.

Format control string including % conversion specifiers.

The number of elements to format or concatenate.

The array of values to format or concatenate.

New length for the string value of *objPtr*, not including the final
null character.

\

# DESCRIPTION

The procedures described in this manual entry allow Tcl values to be
manipulated as string values. They use the internal representation of
the value to store additional information to make the string
manipulations more efficient. In particular, they make a series of
append operations efficient by allocating extra storage space for the
string so that it does not have to be copied for each append. Also,
indexing and length computations are optimized because the Unicode
string representation is calculated and cached as needed. When using the
**Tcl_Append\*** family of functions where the interpreter\'s result is
the value being appended to, it is important to call Tcl_ResetResult
first to ensure you are not unintentionally appending to existing data
in the result value.

**Tcl_NewStringObj** and **Tcl_SetStringObj** create a new value or
modify an existing value to hold a copy of the string given by *bytes*
and *length*. **Tcl_NewUnicodeObj** and **Tcl_SetUnicodeObj** create a
new value or modify an existing value to hold a copy of the Unicode
string given by *unicode* and *numChars*. **Tcl_NewStringObj** and
**Tcl_NewUnicodeObj** return a pointer to a newly created value with
reference count zero. All four procedures set the value to hold a copy
of the specified string. **Tcl_SetStringObj** and **Tcl_SetUnicodeObj**
free any old string representation as well as any old internal
representation of the value.

**Tcl_GetStringFromObj** and **Tcl_GetString** return a value\'s string
representation. This is given by the returned byte pointer and (for
**Tcl_GetStringFromObj**) length, which is stored in *lengthPtr* if it
is non-NULL. If the value\'s UTF string representation is invalid (its
byte pointer is NULL), the string representation is regenerated from the
value\'s internal representation. The storage referenced by the returned
byte pointer is owned by the value manager. It is passed back as a
writable pointer so that extension author creating their own
**Tcl_ObjType** will be able to modify the string representation within
the **Tcl_UpdateStringProc** of their **Tcl_ObjType**. Except for that
limited purpose, the pointer returned by **Tcl_GetStringFromObj** or
**Tcl_GetString** should be treated as read-only. It is recommended that
this pointer be assigned to a (const char \*) variable. Even in the
limited situations where writing to this pointer is acceptable, one
should take care to respect the copy-on-write semantics required by
**Tcl_Obj**\'s, with appropriate calls to **Tcl_IsShared** and
**Tcl_DuplicateObj** prior to any in-place modification of the string
representation. The procedure **Tcl_GetString** is used in the common
case where the caller does not need the length of the string
representation.

**Tcl_GetUnicodeFromObj** and **Tcl_GetUnicode** return a value\'s value
as a Unicode string. This is given by the returned pointer and (for
**Tcl_GetUnicodeFromObj**) length, which is stored in *lengthPtr* if it
is non-NULL. The storage referenced by the returned byte pointer is
owned by the value manager and should not be modified by the caller. The
procedure **Tcl_GetUnicode** is used in the common case where the caller
does not need the length of the unicode string representation.

**Tcl_GetUniChar** returns the *index*\'th character in the value\'s
Unicode representation. The index is assumed to be in the appropriate
range.

**Tcl_GetRange** returns a newly created value comprised of the
characters between *first* and *last* (inclusive) in the value\'s
Unicode representation. If the value\'s Unicode representation is
invalid, the Unicode representation is regenerated from the value\'s
string representation. If *first* \< 0, then the returned string starts
at the beginning of the value. If *last* \< 0, then the returned string
ends at the end of the value.

**Tcl_GetCharLength** returns the number of characters (as opposed to
bytes) in the string value.

**Tcl_AppendToObj** appends the data given by *bytes* and *length* to
the string representation of the value specified by *objPtr*. If the
value has an invalid string representation, then an attempt is made to
convert *bytes* is to the Unicode format. If the conversion is
successful, then the converted form of *bytes* is appended to the
value\'s Unicode representation. Otherwise, the value\'s Unicode
representation is invalidated and converted to the UTF format, and
*bytes* is appended to the value\'s new string representation.

**Tcl_AppendUnicodeToObj** appends the Unicode string given by *unicode*
and *numChars* to the value specified by *objPtr*. If the value has an
invalid Unicode representation, then *unicode* is converted to the UTF
format and appended to the value\'s string representation. Appends are
optimized to handle repeated appends relatively efficiently (it
over-allocates the string or Unicode space to avoid repeated
reallocations and copies of value\'s string value).

**Tcl_AppendObjToObj** is similar to **Tcl_AppendToObj**, but it appends
the string or Unicode value (whichever exists and is best suited to be
appended to *objPtr*) of *appendObjPtr* to *objPtr*.

**Tcl_AppendStringsToObj** is similar to **Tcl_AppendToObj** except that
it can be passed more than one value to append and each value must be a
null-terminated string (i.e. none of the values may contain internal
null characters). Any number of *string* arguments may be provided, but
the last argument must be a NULL pointer to indicate the end of the
list.

**Tcl_AppendStringsToObjVA** is the same as **Tcl_AppendStringsToObj**
except that instead of taking a variable number of arguments it takes an
argument list.

**Tcl_AppendLimitedToObj** is similar to **Tcl_AppendToObj** except that
it imposes a limit on how many bytes are appended. This can be handy
when the string to be appended might be very large, but the value being
constructed should not be allowed to grow without bound. A common usage
is when constructing an error message, where the end result should be
kept short enough to be read. Bytes from *bytes* are appended to
*objPtr*, but no more than *limit* bytes total are to be appended. If
the limit prevents all *length* bytes that are available from being
appended, then the appending is done so that the last bytes appended are
from the string *ellipsis*. This allows for an indication of the
truncation to be left in the string. When *length* is **-1**, all bytes
up to the first zero byte are appended, subject to the limit. When
*ellipsis* is NULL, the default string **\...** is used. When *ellipsis*
is non-NULL, it must point to a zero-byte-terminated string in Tcl\'s
internal UTF encoding. The number of bytes appended can be less than the
lesser of *length* and *limit* when appending fewer bytes is necessary
to append only whole multi-byte characters.

**Tcl_Format** is the C-level interface to the engine of the **format**
command. The actual command procedure for **format** is little more than

    Tcl_Format(interp, Tcl_GetString(objv[1]), objc-2, objv+2);

The *objc* Tcl_Obj values in *objv* are formatted into a string
according to the conversion specification in *format* argument,
following the documentation for the **format** command. The resulting
formatted string is converted to a new Tcl_Obj with refcount of zero and
returned. If some error happens during production of the formatted
string, NULL is returned, and an error message is recorded in *interp*,
if *interp* is non-NULL.

**Tcl_AppendFormatToObj** is an appending alternative form of
**Tcl_Format** with functionality equivalent to:

    Tcl_Obj *newPtr = Tcl_Format(interp, format, objc, objv);
    if (newPtr == NULL) return TCL_ERROR;
    Tcl_AppendObjToObj(objPtr, newPtr);
    Tcl_DecrRefCount(newPtr);
    return TCL_OK;

but with greater convenience and efficiency when the appending
functionality is needed.

**Tcl_ObjPrintf** serves as a replacement for the common sequence

    char buf[SOME_SUITABLE_LENGTH];
    sprintf(buf, format, ...);
    Tcl_NewStringObj(buf, -1);

but with greater convenience and no need to determine
**SOME_SUITABLE_LENGTH**. The formatting is done with the same core
formatting engine used by **Tcl_Format**. This means the set of
supported conversion specifiers is that of the **format** command and
not that of the **sprintf** routine where the two sets differ. When a
conversion specifier passed to **Tcl_ObjPrintf** includes a precision,
the value is taken as a number of bytes, as **sprintf** does, and not as
a number of characters, as **format** does. This is done on the
assumption that C code is more likely to know how many bytes it is
passing around than the number of encoded characters those bytes happen
to represent. The variable number of arguments passed in should be of
the types that would be suitable for passing to **sprintf**. Note in
this example usage, *x* is of type **int**.

    int x = 5;
    Tcl_Obj *objPtr = Tcl_ObjPrintf("Value is %d", x);

If the value of *format* contains internal inconsistencies or invalid
specifier formats, the formatted string result produced by
**Tcl_ObjPrintf** will be an error message describing the error. It is
impossible however to provide runtime protection against mismatches
between the format and any subsequent arguments. Compile-time protection
may be provided by some compilers.

**Tcl_AppendPrintfToObj** is an appending alternative form of
**Tcl_ObjPrintf** with functionality equivalent to

    Tcl_Obj *newPtr = Tcl_ObjPrintf(format, ...);
    Tcl_AppendObjToObj(objPtr, newPtr);
    Tcl_DecrRefCount(newPtr);

but with greater convenience and efficiency when the appending
functionality is needed.

The **Tcl_SetObjLength** procedure changes the length of the string
value of its *objPtr* argument. If the *newLength* argument is greater
than the space allocated for the value\'s string, then the string space
is reallocated and the old value is copied to the new space; the bytes
between the old length of the string and the new length may have
arbitrary values. If the *newLength* argument is less than the current
length of the value\'s string, with *objPtr-\>length* is reduced without
reallocating the string space; the original allocated size for the
string is recorded in the value, so that the string length can be
enlarged in a subsequent call to **Tcl_SetObjLength** without
reallocating storage. In all cases **Tcl_SetObjLength** leaves a null
character at *objPtr-\>bytes\[newLength\]*.

**Tcl_AttemptSetObjLength** is identical in function to
**Tcl_SetObjLength** except that if sufficient memory to satisfy the
request cannot be allocated, it does not cause the Tcl interpreter to
**panic**. Thus, if *newLength* is greater than the space allocated for
the value\'s string, and there is not enough memory available to satisfy
the request, **Tcl_AttemptSetObjLength** will take no action and return
0 to indicate failure. If there is enough memory to satisfy the request,
**Tcl_AttemptSetObjLength** behaves just like **Tcl_SetObjLength** and
returns 1 to indicate success.

The **Tcl_ConcatObj** function returns a new string value whose value is
the space-separated concatenation of the string representations of all
of the values in the *objv* array. **Tcl_ConcatObj** eliminates leading
and trailing white space as it copies the string representations of the
*objv* array to the result. If an element of the *objv* array consists
of nothing but white space, then that value is ignored entirely. This
white-space removal was added to make the output of the **concat**
command cleaner-looking. **Tcl_ConcatObj** returns a pointer to a
newly-created value whose ref count is zero.

# SEE ALSO

Tcl_NewObj(3), Tcl_IncrRefCount(3), Tcl_DecrRefCount(3), format(n),
sprintf(3)

# KEYWORDS

append, internal representation, value, value type, string value, string
type, string representation, concat, concatenate, unicode
