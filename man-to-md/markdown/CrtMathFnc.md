\

# NAME

Tcl_CreateMathFunc, Tcl_GetMathFuncInfo, Tcl_ListMathFuncs - Define,
query and enumerate math functions for expressions

# NOTICE OF EVENTUAL DEPRECATION

The **Tcl_CreateMathFunc** and **Tcl_GetMathFuncInfo** functions are
rendered somewhat obsolete by the ability to create functions for
expressions by placing commands in the **tcl::mathfunc** namespace, as
described in the **mathfunc** manual page; the API described on this
page is not expected to be maintained indefinitely.

# SYNOPSIS

    #include <tcl.h>

    void
    Tcl_CreateMathFunc(interp, name, numArgs, argTypes, proc, clientData)

    int
    Tcl_GetMathFuncInfo(interp, name, numArgsPtr, argTypesPtr, procPtr,
                        clientDataPtr)

    Tcl_Obj *
    Tcl_ListMathFuncs(interp, pattern)

# ARGUMENTS

Interpreter in which new function will be defined.

Name for new function.

Number of arguments to new function; also gives size of *argTypes*
array.

Points to an array giving the permissible types for each argument to
function.

Procedure that implements the function.

Arbitrary one-word value to pass to *proc* when it is invoked.

Points to a variable that will be set to contain the number of arguments
to the function.

Points to a variable that will be set to contain a pointer to an array
giving the permissible types for each argument to the function which
will need to be freed up using *Tcl_Free*.

Points to a variable that will be set to contain a pointer to the
implementation code for the function (or NULL if the function is
implemented directly in bytecode).

Points to a variable that will be set to contain the clientData argument
passed to *Tcl_CreateMathFunc* when the function was created if the
function is not implemented directly in bytecode.

Pattern to match against function names so as to filter them (by passing
to *Tcl_StringMatch*), or NULL to not apply any filter.

\

# DESCRIPTION

Tcl allows a number of mathematical functions to be used in expressions,
such as **sin**, **cos**, and **hypot**. These functions are represented
by commands in the namespace, **tcl::mathfunc**. The
**Tcl_CreateMathFunc** function is an obsolete way for applications to
add additional functions to those already provided by Tcl or to replace
existing functions. It should not be used by new applications, which
should create math functions using **Tcl_CreateObjCommand** to create a
command in the **tcl::mathfunc** namespace.

In the **Tcl_CreateMathFunc** interface, *Name* is the name of the
function as it will appear in expressions. If *name* does not already
exist in the **::tcl::mathfunc** namespace, then a new command is
created in that namespace. If *name* does exist, then the existing
function is replaced. *NumArgs* and *argTypes* describe the arguments to
the function. Each entry in the *argTypes* array must be one of
**TCL_INT**, **TCL_DOUBLE**, **TCL_WIDE_INT**, or **TCL_EITHER** to
indicate whether the corresponding argument must be an integer, a
double-precision floating value, a wide (64-bit) integer, or any,
respectively.

Whenever the function is invoked in an expression Tcl will invoke
*proc*. *Proc* should have arguments and result that match the type
**Tcl_MathProc**:

    typedef int Tcl_MathProc(
            ClientData clientData,
            Tcl_Interp *interp,
            Tcl_Value *args,
            Tcl_Value *resultPtr);

When *proc* is invoked the *clientData* and *interp* arguments will be
the same as those passed to **Tcl_CreateMathFunc**. *Args* will point to
an array of *numArgs* Tcl_Value structures, which describe the actual
arguments to the function:

    typedef struct Tcl_Value {
        Tcl_ValueType type;
        long intValue;
        double doubleValue;
        Tcl_WideInt wideValue;
    } Tcl_Value;

The *type* field indicates the type of the argument and is one of
**TCL_INT**, **TCL_DOUBLE** or **TCL_WIDE_INT**. It will match the
*argTypes* value specified for the function unless the *argTypes* value
was **TCL_EITHER**. Tcl converts the argument supplied in the expression
to the type requested in *argTypes*, if that is necessary. Depending on
the value of the *type* field, the *intValue*, *doubleValue* or
*wideValue* field will contain the actual value of the argument.

*Proc* should compute its result and store it either as an integer in
*resultPtr-\>intValue* or as a floating value in
*resultPtr-\>doubleValue*. It should set also *resultPtr-\>type* to one
of **TCL_INT**, **TCL_DOUBLE** or **TCL_WIDE_INT** to indicate which
value was set. Under normal circumstances *proc* should return
**TCL_OK**. If an error occurs while executing the function, *proc*
should return **TCL_ERROR** and leave an error message in the
interpreter\'s result.

**Tcl_GetMathFuncInfo** retrieves the values associated with function
*name* that were passed to a preceding **Tcl_CreateMathFunc** call.
Normally, the return code is **TCL_OK** but if the named function does
not exist, **TCL_ERROR** is returned and an error message is placed in
the interpreter\'s result.

If an error did not occur, the array reference placed in the variable
pointed to by *argTypesPtr* is newly allocated, and should be released
by passing it to **Tcl_Free**. Some functions (the standard set
implemented in the core, and those defined by placing commands in the
**tcl::mathfunc** namespace) do not have argument type information;
attempting to retrieve values for them causes a NULL to be stored in the
variable pointed to by *procPtr* and the variable pointed to by
*clientDataPtr* will not be modified. The variable pointed to by
*numArgsPointer* will contain -1, and no argument types will be stored
in the variable pointed to by *argTypesPointer*.

**Tcl_ListMathFuncs** returns a Tcl value containing a list of all the
math functions defined in the interpreter whose name matches *pattern*.
The returned value has a reference count of zero.

# SEE ALSO

expr(n), info(n), Tcl_CreateObjCommand(3), Tcl_Free(3),
Tcl_NewListObj(3)

# KEYWORDS

expression, mathematical function
