# NAME

Tk_CreateBindingTable, Tk_DeleteBindingTable, Tk_CreateBinding,
Tk_DeleteBinding, Tk_GetBinding, Tk_GetAllBindings,
Tk_DeleteAllBindings, Tk_BindEvent - invoke scripts in response to X
events

# SYNOPSIS

**#include \<tk.h\>**

Tk_BindingTable **Tk_CreateBindingTable(***interp***)**

**Tk_DeleteBindingTable(***bindingTable***)**

unsigned long **Tk_CreateBinding(***interp, bindingTable, object,
eventString, script, append***)**

int **Tk_DeleteBinding(***interp, bindingTable, object,
eventString***)**

const char \* **Tk_GetBinding(***interp, bindingTable, object,
eventString***)**

**Tk_GetAllBindings(***interp, bindingTable, object***)**

**Tk_DeleteAllBindings(***bindingTable, object***)**

**Tk_BindEvent(***bindingTable, eventPtr, tkwin, numObjects,
objectPtr***)**

# ARGUMENTS

Interpreter to use when invoking bindings in binding table. Also used
for returning results and errors from binding procedures.

Token for binding table; must have been returned by some previous call
to **Tk_CreateBindingTable**.

Identifies object with which binding is associated.

String describing event sequence.

Tcl script to invoke when binding triggers.

Non-zero means append *script* to existing script for binding, if any;
zero means replace existing script with new one.

X event to match against bindings in *bindingTable*.

Identifier for any window on the display where the event occurred. Used
to find display-related information such as key maps.

Number of object identifiers pointed to by *objectPtr*.

Points to an array of object identifiers: bindings will be considered
for each of these objects in order from first to last.

# DESCRIPTION

These procedures provide a general-purpose mechanism for creating and
invoking bindings. Bindings are organized in terms of *binding tables*.
A binding table consists of a collection of bindings plus a history of
recent events. Within a binding table, bindings are associated with
*objects*. The meaning of an object is defined by clients of the binding
package. For example, Tk keeps uses one binding table to hold all of the
bindings created by the **bind** command. For this table, objects are
pointers to strings such as window names, class names, or other binding
tags such as **all**. Tk also keeps a separate binding table for each
canvas widget, which manages bindings created by the canvas\'s **bind**
widget command; within this table, an object is either a pointer to the
internal structure for a canvas item or a Tk_Uid identifying a tag.

The procedure **Tk_CreateBindingTable** creates a new binding table and
associates *interp* with it (when bindings in the table are invoked, the
scripts will be evaluated in *interp*). **Tk_CreateBindingTable**
returns a token for the table, which must be used in calls to other
procedures such as **Tk_CreateBinding** or **Tk_BindEvent**.

**Tk_DeleteBindingTable** frees all of the state associated with a
binding table. Once it returns the caller should not use the
*bindingTable* token again.

**Tk_CreateBinding** adds a new binding to an existing table. The
*object* argument identifies the object with which the binding is to be
associated, and it may be any one-word value. Typically it is a pointer
to a string or data structure. The *eventString* argument identifies the
event or sequence of events for the binding; see the documentation for
the **bind** command for a description of its format. *script* is the
Tcl script to be evaluated when the binding triggers. *append* indicates
what to do if there already exists a binding for *object* and
*eventString*: if *append* is zero then *script* replaces the old
script; if *append* is non-zero then the new script is appended to the
old one. **Tk_CreateBinding** returns an X event mask for all the events
associated with the bindings. This information may be useful to invoke
**XSelectInput** to select relevant events, or to disallow the use of
certain events in bindings. If an error occurred while creating the
binding (e.g., *eventString* refers to a non-existent event), then 0 is
returned and an error message is left as the result of interpreter
*interp*.

**Tk_DeleteBinding** removes from *bindingTable* the binding given by
*object* and *eventString*, if such a binding exists.
**Tk_DeleteBinding** always returns **TCL_OK**. In some cases it may
reset the interpreter result to the default empty value.

**Tk_GetBinding** returns a pointer to the script associated with
*eventString* and *object* in *bindingTable*. If no such binding exists
then NULL is returned and an error message is left as the result of
interpreter *interp*.

**Tk_GetAllBindings** returns in *interp*\'s result a list of all the
event strings for which there are bindings in *bindingTable* associated
with *object*. If there are no bindings for *object*, the result will be
an empty string.

**Tk_DeleteAllBindings** deletes all of the bindings in *bindingTable*
that are associated with *object*.

**Tk_BindEvent** is called to process an event. It makes a copy of the
event in an internal history list associated with the binding table,
then it checks for bindings that match the event. **Tk_BindEvent**
processes each of the objects pointed to by *objectPtr* in turn. For
each object, it finds all the bindings that match the current event
history, selects the most specific binding using the priority mechanism
described in the documentation for **bind**, and invokes the script for
that binding. If there are no matching bindings for a particular object,
then the object is skipped. **Tk_BindEvent** continues through all of
the objects, handling exceptions such as errors, **break**, and
**continue** as described in the documentation for **bind**.

# KEYWORDS

binding, event, object, script
