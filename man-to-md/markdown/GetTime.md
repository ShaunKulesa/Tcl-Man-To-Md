# NAME

Tcl_GetTime, Tcl_SetTimeProc, Tcl_QueryTimeProc - get date and time

# SYNOPSIS

**#include \<tcl.h\>**

**Tcl_GetTime**(*timePtr*)

**Tcl_SetTimeProc**(*getProc, scaleProc, clientData*)

**Tcl_QueryTimeProc**(*getProcPtr, scaleProcPtr, clientDataPtr*)

# ARGUMENTS

Points to memory in which to store the date and time information.

Pointer to handler function replacing **Tcl_GetTime**\'s access to the
OS.

Pointer to handler function for the conversion of time delays in the
virtual domain to real-time.

Value passed through to the two handler functions.

Pointer to place the currently registered get handler function into.

Pointer to place the currently registered scale handler function into.

Pointer to place the currently registered pass-through value into.

# DESCRIPTION

The **Tcl_GetTime** function retrieves the current time as a *Tcl_Time*
structure in memory the caller provides. This structure has the
following definition:

    typedef struct Tcl_Time {
        long sec;
        long usec;
    } Tcl_Time;

On return, the *sec* member of the structure is filled in with the
number of seconds that have elapsed since the *epoch:* the epoch is the
point in time of 00:00 UTC, 1 January 1970. This number does *not* count
leap seconds - an interval of one day advances it by 86400 seconds
regardless of whether a leap second has been inserted.

The *usec* member of the structure is filled in with the number of
microseconds that have elapsed since the start of the second designated
by *sec*. The Tcl library makes every effort to keep this number as
precise as possible, subject to the limitations of the computer system.
On multiprocessor variants of Windows, this number may be limited to the
10- or 20-ms granularity of the system clock. (On single-processor
Windows systems, the *usec* field is derived from a performance counter
and is highly precise.)

## VIRTUALIZED TIME

The **Tcl_SetTimeProc** function registers two related handler functions
with the core. The first handler function is a replacement for
**Tcl_GetTime**, or rather the OS access made by **Tcl_GetTime**. The
other handler function is used by the Tcl notifier to convert wait/block
times from the virtual domain into real time.

The **Tcl_QueryTimeProc** function returns the currently registered
handler functions. If no external handlers were set then this will
return the standard handlers accessing and processing the native time of
the OS. The arguments to the function are allowed to be NULL; and any
argument which is NULL is ignored and not set.

The signatures of the handler functions are as follows:

    typedef void Tcl_GetTimeProc(
            Tcl_Time *timebuf,
            ClientData clientData);
    typedef void Tcl_ScaleTimeProc(
            Tcl_Time *timebuf,
            ClientData clientData);

The *timebuf* fields contain the time to manipulate, and the
*clientData* fields contain a pointer supplied at the time the handler
functions were registered.

Any handler pair specified has to return data which is consistent
between them. In other words, setting one handler of the pair to
something assuming a 10-times slowdown, and the other handler of the
pair to something assuming a two-times slowdown is wrong and not
allowed.

The set handler functions are allowed to run the delivered time
backwards, however this should be avoided. We have to allow it as the
native time can run backwards as the user can fiddle with the system
time one way or other. Note that the insertion of the hooks will not
change the behavior of the Tcl core with regard to this situation, i.e.
the existing behavior is retained.

# SEE ALSO

clock(n)

# KEYWORDS

date, time

<!---
Copyright (c) 2001 Kevin B. Kenny <kennykb@acm.org>
-->

