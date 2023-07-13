\

# NAME

Tcl_IsSafe, Tcl_MakeSafe, Tcl_CreateChild, Tcl_CreateSlave,
Tcl_GetChild, Tcl_GetSlave, Tcl_GetParent, Tcl_GetMaster,
Tcl_GetInterpPath, Tcl_CreateAlias, Tcl_CreateAliasObj, Tcl_GetAlias,
Tcl_GetAliasObj, Tcl_ExposeCommand, Tcl_HideCommand - manage multiple
Tcl interpreters, aliases and hidden commands

# SYNOPSIS

    #include <tcl.h>

    int
    Tcl_IsSafe(interp)

    int
    Tcl_MakeSafe(interp)

    Tcl_Interp *
    Tcl_CreateChild(interp, name, isSafe)


    Tcl_Interp *
    Tcl_CreateSlave(interp, name, isSafe)

    Tcl_Interp *
    Tcl_GetChild(interp, name)


    Tcl_Interp *
    Tcl_GetSlave(interp, name)

    Tcl_Interp *
    Tcl_GetParent(interp)


    Tcl_Interp *
    Tcl_GetMaster(interp)

    int
    Tcl_GetInterpPath(interp, childInterp)

    int
    Tcl_CreateAlias(childInterp, childCmd, targetInterp, targetCmd,
                    argc, argv)

    int
    Tcl_CreateAliasObj(childInterp, childCmd, targetInterp, targetCmd,
                       objc, objv)

    int
    Tcl_GetAlias(interp, childCmd, targetInterpPtr, targetCmdPtr,
                 argcPtr, argvPtr)

    int
    Tcl_GetAliasObj(interp, childCmd, targetInterpPtr, targetCmdPtr,
                    objcPtr, objvPtr)

    int
    Tcl_ExposeCommand(interp, hiddenCmdName, cmdName)

    int
    Tcl_HideCommand(interp, cmdName, hiddenCmdName)

# ARGUMENTS

Interpreter in which to execute the specified command.

Name of child interpreter to create or manipulate.

If non-zero, a child that is suitable for running untrusted code is
created, otherwise a trusted child is created.

Interpreter to use for creating the source command for an alias (see
below).

Name of source command for alias.

Interpreter that contains the target command for an alias.

Name of target command for alias in *targetInterp*.

Count of additional arguments to pass to the alias command.

Vector of strings, the additional arguments to pass to the alias
command. This storage is owned by the caller.

Count of additional value arguments to pass to the aliased command.

Vector of Tcl_Obj structures, the additional value arguments to pass to
the aliased command. This storage is owned by the caller.

Pointer to location to store the address of the interpreter where a
target command is defined for an alias.

Pointer to location to store the address of the name of the target
command for an alias.

Pointer to location to store count of additional arguments to be passed
to the alias. The location is in storage owned by the caller.

Pointer to location to store a vector of strings, the additional
arguments to pass to an alias. The location is in storage owned by the
caller, the vector of strings is owned by the called function.

Pointer to location to store count of additional value arguments to be
passed to the alias. The location is in storage owned by the caller.

Pointer to location to store a vector of Tcl_Obj structures, the
additional arguments to pass to an alias command. The location is in
storage owned by the caller, the vector of Tcl_Obj structures is owned
by the called function.

Name of an exposed command to hide or create.

Name under which a hidden command is stored and with which it can be
exposed or invoked.

\

# DESCRIPTION

These procedures are intended for access to the multiple interpreter
facility from inside C programs. They enable managing multiple
interpreters in a hierarchical relationship, and the management of
aliases, commands that when invoked in one interpreter execute a command
in another interpreter. The return value for those procedures that
return an **int** is either **TCL_OK** or **TCL_ERROR**. If
**TCL_ERROR** is returned then the interpreter\'s result contains an
error message.

**Tcl_CreateSlave** creates a new interpreter as a child of *interp*. It
also creates a child command named *childName* in *interp* which allows
*interp* to manipulate the new child. If *isSafe* is zero, the command
creates a trusted child in which Tcl code has access to all the Tcl
commands. If it is **1**, the command creates a child in which Tcl code
has access only to set of Tcl commands defined as see the manual entry
for the Tcl **interp** command for details. If the creation of the new
child interpreter failed, **NULL** is returned.

**Tcl_CreateChild** is a synonym for **Tcl_CreateSlave**.

**Tcl_IsSafe** returns **1** if *interp* is (was created with the
**TCL_SAFE_INTERPRETER** flag specified), **0** otherwise.

**Tcl_MakeSafe** marks *interp* as so that future calls to
**Tcl_IsSafe** will return 1. It also removes all known
potentially-unsafe core functionality (both commands and variables) from
*interp*. However, it cannot know what parts of an extension or
application are safe and does not make any attempt to remove those
parts, so safety is not guaranteed after calling **Tcl_MakeSafe**.
Callers will want to take care with their use of **Tcl_MakeSafe** to
avoid false claims of safety. For many situations, **Tcl_CreateSlave**
may be a better choice, since it creates interpreters in a known-safe
state.

**Tcl_GetSlave** returns a pointer to a child interpreter of *interp*.
The child interpreter is identified by *childName*. If no such child
interpreter exists, **NULL** is returned.

**Tcl_GetChild** is a synonym for **Tcl_GetSlave**.

**Tcl_GetMaster** returns a pointer to the master interpreter of
*interp*. If *interp* has no master (it is a top-level interpreter) then
**NULL** is returned.

**Tcl_GetParent** is a synonym for **Tcl_GetMaster**.

**Tcl_GetInterpPath** stores in the result of *interp* the relative path
between *interp* and *childInterp*; *childInterp* must be a child of
*interp*. If the computation of the relative path succeeds, **TCL_OK**
is returned, else **TCL_ERROR** is returned and an error message is
stored as the result of *interp*.

**Tcl_CreateAlias** creates a command named *childCmd* in *childInterp*
that when invoked, will cause the command *targetCmd* to be invoked in
*targetInterp*. The arguments specified by the strings contained in
*argv* are always prepended to any arguments supplied in the invocation
of *childCmd* and passed to *targetCmd*. This operation returns
**TCL_OK** if it succeeds, or **TCL_ERROR** if it fails; in that case,
an error message is left in the value result of *childInterp*. Note that
there are no restrictions on the ancestry relationship (as created by
**Tcl_CreateSlave**) between *childInterp* and *targetInterp*. Any two
interpreters can be used, without any restrictions on how they are
related.

**Tcl_CreateAliasObj** is similar to **Tcl_CreateAlias** except that it
takes a vector of values to pass as additional arguments instead of a
vector of strings.

**Tcl_GetAlias** returns information about an alias *aliasName* in
*interp*. Any of the result fields can be **NULL**, in which case the
corresponding datum is not returned. If a result field is non-**NULL**,
the address indicated is set to the corresponding datum. For example, if
*targetNamePtr* is non-**NULL** it is set to a pointer to the string
containing the name of the target command.

**Tcl_GetAliasObj** is similar to **Tcl_GetAlias** except that it
returns a pointer to a vector of Tcl_Obj structures instead of a vector
of strings.

**Tcl_ExposeCommand** moves the command named *hiddenCmdName* from the
set of hidden commands to the set of exposed commands, putting it under
the name *cmdName*. *HiddenCmdName* must be the name of an existing
hidden command, or the operation will return **TCL_ERROR** and leave an
error message as the result of *interp*. If an exposed command named
*cmdName* already exists, the operation returns **TCL_ERROR** and leaves
an error message as the result of *interp*. If the operation succeeds,
it returns **TCL_OK**. After executing this command, attempts to use
*cmdName* in any script evaluation mechanism will again succeed.

**Tcl_HideCommand** moves the command named *cmdName* from the set of
exposed commands to the set of hidden commands, under the name
*hiddenCmdName*. *CmdName* must be the name of an existing exposed
command, or the operation will return **TCL_ERROR** and leave an error
message as the result of *interp*. Currently both *cmdName* and
*hiddenCmdName* must not contain namespace qualifiers, or the operation
will return **TCL_ERROR** and leave an error message as the result of
*interp*. The *CmdName* will be looked up in the global namespace, and
not relative to the current namespace, even if the current namespace is
not the global one. If a hidden command whose name is *hiddenCmdName*
already exists, the operation also returns **TCL_ERROR** and an error
message is left as the result of *interp*. If the operation succeeds, it
returns **TCL_OK**. After executing this command, attempts to use
*cmdName* in any script evaluation mechanism will fail.

For a description of the Tcl interface to multiple interpreters, see
*interp(n)*.

# SEE ALSO

interp

# KEYWORDS

alias, command, exposed commands, hidden commands, interpreter, invoke,
parent, child
