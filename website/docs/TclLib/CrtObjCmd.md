# NAME

Tcl_CreateObjCommand, Tcl_DeleteCommand, Tcl_DeleteCommandFromToken,
Tcl_GetCommandInfo, Tcl_GetCommandInfoFromToken, Tcl_SetCommandInfo,
Tcl_SetCommandInfoFromToken, Tcl_GetCommandName, Tcl_GetCommandFullName,
Tcl_GetCommandFromObj - implement new commands in C

# SYNOPSIS

**#include \<tcl.h\>**

Tcl_Command **Tcl_CreateObjCommand**(*interp, cmdName, proc, clientData,
deleteProc*)

int **Tcl_DeleteCommand**(*interp, cmdName*)

int **Tcl_DeleteCommandFromToken**(*interp, token*)

int **Tcl_GetCommandInfo**(*interp, cmdName, infoPtr*)

int **Tcl_SetCommandInfo**(*interp, cmdName, infoPtr*)

int **Tcl_GetCommandInfoFromToken**(*token, infoPtr*)

int **Tcl_SetCommandInfoFromToken**(*token, infoPtr*)

const char \* **Tcl_GetCommandName**(*interp, token*)

void **Tcl_GetCommandFullName**(*interp, token, objPtr*)

Tcl_Command **Tcl_GetCommandFromObj**(*interp, objPtr*)

# ARGUMENTS

Interpreter in which to create a new command or that contains a command.

Name of command.

Implementation of the new command: *proc* will be called whenever
*cmdName* is invoked as a command.

Arbitrary one-word value to pass to *proc* and *deleteProc*.

Procedure to call before *cmdName* is deleted from the interpreter;
allows for command-specific cleanup. If NULL, then no procedure is
called before the command is deleted.

Token for command, returned by previous call to
**Tcl_CreateObjCommand**. The command must not have been deleted.

Pointer to structure containing various information about a Tcl command.

Value containing the name of a Tcl command.

# DESCRIPTION

**Tcl_CreateObjCommand** defines a new command in *interp* and
associates it with procedure *proc* such that whenever *name* is invoked
as a Tcl command (e.g., via a call to **Tcl_EvalObjEx**) the Tcl
interpreter will call *proc* to process the command.

**Tcl_CreateObjCommand** deletes any existing command *name* already
associated with the interpreter (however see below for an exception
where the existing command is not deleted). It returns a token that may
be used to refer to the command in subsequent calls to
**Tcl_GetCommandName**. If *name* contains any **::** namespace
qualifiers, then the command is added to the specified namespace;
otherwise the command is added to the global namespace. If
**Tcl_CreateObjCommand** is called for an interpreter that is in the
process of being deleted, then it does not create a new command and it
returns NULL. *proc* should have arguments and result that match the
type **Tcl_ObjCmdProc**:

    typedef int Tcl_ObjCmdProc(
            ClientData clientData,
            Tcl_Interp *interp,
            int objc,
            Tcl_Obj *const objv[]);

When *proc* is invoked, the *clientData* and *interp* parameters will be
copies of the *clientData* and *interp* arguments given to
**Tcl_CreateObjCommand**. Typically, *clientData* points to an
application-specific data structure that describes what to do when the
command procedure is invoked. *Objc* and *objv* describe the arguments
to the command, *objc* giving the number of argument values (including
the command name) and *objv* giving the values of the arguments. The
*objv* array will contain *objc* values, pointing to the argument
values. Unlike *argv*\[*argv*\] used in a string-based command
procedure, *objv*\[*objc*\] will not contain NULL.

Additionally, when *proc* is invoked, it must not modify the contents of
the *objv* array by assigning new pointer values to any element of the
array (for example, *objv*\[**2**\] = **NULL**) because this will cause
memory to be lost and the runtime stack to be corrupted. The **const**
in the declaration of *objv* will cause ANSI-compliant compilers to
report any such attempted assignment as an error. However, it is
acceptable to modify the internal representation of any individual value
argument. For instance, the user may call **Tcl_GetIntFromObj** on
*objv*\[**2**\] to obtain the integer representation of that value; that
call may change the type of the value that *objv*\[**2**\] points at,
but will not change where *objv*\[**2**\] points.

*proc* must return an integer code that is either **TCL_OK**,
**TCL_ERROR**, **TCL_RETURN**, **TCL_BREAK**, or **TCL_CONTINUE**. See
the Tcl overview man page for details on what these codes mean. Most
normal commands will only return **TCL_OK** or **TCL_ERROR**. In
addition, if *proc* needs to return a non-empty result, it can call
**Tcl_SetObjResult** to set the interpreter\'s result. In the case of a
**TCL_OK** return code this gives the result of the command, and in the
case of **TCL_ERROR** this gives an error message. Before invoking a
command procedure, **Tcl_EvalObjEx** sets interpreter\'s result to point
to a value representing an empty string, so simple commands can return
an empty result by doing nothing at all.

The contents of the *objv* array belong to Tcl and are not guaranteed to
persist once *proc* returns: *proc* should not modify them. Call
**Tcl_SetObjResult** if you want to return something from the *objv*
array.

Ordinarily, **Tcl_CreateObjCommand** deletes any existing command *name*
already associated with the interpreter. However, if the existing
command was created by a previous call to **Tcl_CreateCommand**,
**Tcl_CreateObjCommand** does not delete the command but instead
arranges for the Tcl interpreter to call the **Tcl_ObjCmdProc** *proc*
in the future. The old string-based **Tcl_CmdProc** associated with the
command is retained and its address can be obtained by subsequent
**Tcl_GetCommandInfo** calls. This is done for backwards compatibility.

*DeleteProc* will be invoked when (if) *name* is deleted. This can occur
through a call to **Tcl_DeleteCommand**, **Tcl_DeleteCommandFromToken**,
or **Tcl_DeleteInterp**, or by replacing *name* in another call to
**Tcl_CreateObjCommand**. *DeleteProc* is invoked before the command is
deleted, and gives the application an opportunity to release any
structures associated with the command. *DeleteProc* should have
arguments and result that match the type **Tcl_CmdDeleteProc**:

    typedef void Tcl_CmdDeleteProc(
            ClientData clientData);

The *clientData* argument will be the same as the *clientData* argument
passed to **Tcl_CreateObjCommand**.

**Tcl_DeleteCommand** deletes a command from a command interpreter. Once
the call completes, attempts to invoke *cmdName* in *interp* will result
in errors. If *cmdName* is not bound as a command in *interp* then
**Tcl_DeleteCommand** does nothing and returns -1; otherwise it returns
0. There are no restrictions on *cmdName*: it may refer to a built-in
command, an application-specific command, or a Tcl procedure. If *name*
contains any **::** namespace qualifiers, the command is deleted from
the specified namespace.

Given a token returned by **Tcl_CreateObjCommand**,
**Tcl_DeleteCommandFromToken** deletes the command from a command
interpreter. It will delete a command even if that command has been
renamed. Once the call completes, attempts to invoke the command in
*interp* will result in errors. If the command corresponding to *token*
has already been deleted from *interp* then **Tcl_DeleteCommand** does
nothing and returns -1; otherwise it returns 0.

**Tcl_GetCommandInfo** checks to see whether its *cmdName* argument
exists as a command in *interp*. *cmdName* may include **::** namespace
qualifiers to identify a command in a particular namespace. If the
command is not found, then it returns 0. Otherwise it places information
about the command in the **Tcl_CmdInfo** structure pointed to by
*infoPtr* and returns 1. A **Tcl_CmdInfo** structure has the following
fields:

    typedef struct Tcl_CmdInfo {
        int isNativeObjectProc;
        Tcl_ObjCmdProc *objProc;
        ClientData objClientData;
        Tcl_CmdProc *proc;
        ClientData clientData;
        Tcl_CmdDeleteProc *deleteProc;
        ClientData deleteData;
        Tcl_Namespace *namespacePtr;
    } Tcl_CmdInfo;

The *isNativeObjectProc* field has the value 1 if
**Tcl_CreateObjCommand** was called to register the command; it is 0 if
only **Tcl_CreateCommand** was called. It allows a program to determine
whether it is faster to call *objProc* or *proc*: *objProc* is normally
faster if *isNativeObjectProc* has the value 1. The fields *objProc* and
*objClientData* have the same meaning as the *proc* and *clientData*
arguments to **Tcl_CreateObjCommand**; they hold information about the
value-based command procedure that the Tcl interpreter calls to
implement the command. The fields *proc* and *clientData* hold
information about the string-based command procedure that implements the
command. If **Tcl_CreateCommand** was called for this command, this is
the procedure passed to it; otherwise, this is a compatibility procedure
registered by **Tcl_CreateObjCommand** that simply calls the command\'s
value-based procedure after converting its string arguments to Tcl
values. The field *deleteData* is the ClientData value to pass to
*deleteProc*; it is normally the same as *clientData* but may be set
independently using the **Tcl_SetCommandInfo** procedure. The field
*namespacePtr* holds a pointer to the Tcl_Namespace that contains the
command.

**Tcl_GetCommandInfoFromToken** is identical to **Tcl_GetCommandInfo**
except that it uses a command token returned from
**Tcl_CreateObjCommand** in place of the command name. If the *token*
parameter is NULL, it returns 0; otherwise, it returns 1 and fills in
the structure designated by *infoPtr*.

**Tcl_SetCommandInfo** is used to modify the procedures and ClientData
values associated with a command. Its *cmdName* argument is the name of
a command in *interp*. *cmdName* may include **::** namespace qualifiers
to identify a command in a particular namespace. If this command does
not exist then **Tcl_SetCommandInfo** returns 0. Otherwise, it copies
the information from *\*infoPtr* to Tcl\'s internal structure for the
command and returns 1.

**Tcl_SetCommandInfoFromToken** is identical to **Tcl_SetCommandInfo**
except that it takes a command token as returned by
**Tcl_CreateObjCommand** instead of the command name. If the *token*
parameter is NULL, it returns 0. Otherwise, it copies the information
from *\*infoPtr* to Tcl\'s internal structure for the command and
returns 1.

Note that **Tcl_SetCommandInfo** and **Tcl_SetCommandInfoFromToken**
both allow the ClientData for a command\'s deletion procedure to be
given a different value than the ClientData for its command procedure.

Note that neither **Tcl_SetCommandInfo** nor
**Tcl_SetCommandInfoFromToken** will change a command\'s namespace. Use
**Tcl_Eval** to call the **rename** command to do that.

**Tcl_GetCommandName** provides a mechanism for tracking commands that
have been renamed. Given a token returned by **Tcl_CreateObjCommand**
when the command was created, **Tcl_GetCommandName** returns the string
name of the command. If the command has been renamed since it was
created, then **Tcl_GetCommandName** returns the current name. This name
does not include any **::** namespace qualifiers. The command
corresponding to *token* must not have been deleted. The string returned
by **Tcl_GetCommandName** is in dynamic memory owned by Tcl and is only
guaranteed to retain its value as long as the command is not deleted or
renamed; callers should copy the string if they need to keep it for a
long time.

**Tcl_GetCommandFullName** produces the fully qualified name of a
command from a command token. The name, including all namespace
prefixes, is appended to the value specified by *objPtr*.

**Tcl_GetCommandFromObj** returns a token for the command specified by
the name in a **Tcl_Obj**. The command name is resolved relative to the
current namespace. Returns NULL if the command is not found.

# SEE ALSO

Tcl_CreateCommand(3), Tcl_ResetResult(3), Tcl_SetObjResult(3)

# KEYWORDS

bind, command, create, delete, namespace, value

<!---
Copyright (c) 1996-1997 Sun Microsystems, Inc
-->

