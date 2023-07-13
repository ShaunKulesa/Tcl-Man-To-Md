\

# NAME

tcl::process - Subprocess management

# SYNOPSIS

**::tcl::process ***option *?*arg arg \...*?

\

# DESCRIPTION

This command provides a way to manage subprocesses created by the
**open** and **exec** commands, as identified by the process identifiers
(PIDs) of those subprocesses. The legal *options* (which may be
abbreviated) are:

**::tcl::process autopurge** ?*flag*?

:   Automatic purge facility. If *flag* is specified as a boolean value
    then it activates or deactivate autopurge. In all cases it returns
    the current status as a boolean value. When autopurge is active,
    **Tcl_ReapDetachedProcs** is called each time the **exec** command
    is executed or a pipe channel created by **open** is closed. When
    autopurge is inactive, **::tcl::process** purge must be called
    explicitly. By default autopurge is active.

**::tcl::process list**

:   Returns the list of subprocess PIDs. This includes all currently
    executing subprocesses and all terminated subprocesses that have not
    yet had their corresponding process table entries purged.

**::tcl::process purge** ?*pids*?

:   Cleans up all data associated with terminated subprocesses. If
    *pids* is specified as a list of PIDs then the command only cleanup
    data for the matching subprocesses if they exist, and raises an
    error otherwise. If a process listed is still active, this command
    does nothing to that process.

**::tcl::process status** ?*switches*? ?*pids*?

:   Returns a dictionary mapping subprocess PIDs to their respective
    status. If *pids* is specified as a list of PIDs then the command
    only returns the status of the matching subprocesses if they exist,
    and raises an error otherwise. For active processes, the status is
    an empty value. For terminated processes, the status is a list with
    the following format: where:

    *code* 

    :   is a standard Tcl return code, i.e., **0** for TCL_OK and **1**
        for TCL_ERROR,

    *msg* 

    :   is the human-readable error message,

    *errorCode* 

    :   uses the same format as the **errorCode** global variable

    Note that **msg** and **errorCode** are only present for abnormally
    terminated processes (i.e. those where the *code* is nonzero). Under
    the hood this command calls **Tcl_WaitPid** with the **WNOHANG**
    flag set for non-blocking behavior, unless the **-wait** switch is
    set (see below).

    Additionally, **::tcl::process status** accepts the following
    switches:

    **-wait** 

    :   By default the command returns immediately (the underlying
        **Tcl_WaitPid** is called with the **WNOHANG** flag set) unless
        this switch is set. If *pids* is specified as a list of PIDs
        then the command waits until the status of the matching
        subprocesses are available. If *pids* was not specified, this
        command will wait for all known subprocesses.

    **- -**

    :   Marks the end of switches. The argument following this one will
        be treated as the first *arg* even if it starts with a **-**.

# EXAMPLES

These show the use of **::tcl::process**. Some of the results from
**::tcl::process status** are split over multiple lines for readability.

    ::tcl::process autopurge
         → true
    ::tcl::process autopurge false
         → false

    set pid1 [exec command1 a b c | command2 d e f &]
         → 123 456
    set chan [open "|command1 a b c | command2 d e f"]
         → file123
    set pid2 [pid $chan]
         → 789 1011

    ::tcl::process list
         → 123 456 789 1011

    ::tcl::process status
         → 123 0
           456 {1 "child killed: write on pipe with no readers" {
             CHILDKILLED 456 SIGPIPE "write on pipe with no readers"}}
           789 {1 "child suspended: background tty read" {
             CHILDSUSP 789 SIGTTIN "background tty read"}}
           1011 {}

    ::tcl::process status 123
         → 123 0

    ::tcl::process status 1011
         → 1011 {}

    ::tcl::process status -wait
         → 123 0
           456 {1 "child killed: write on pipe with no readers" {
             CHILDKILLED 456 SIGPIPE "write on pipe with no readers"}}
           789 {1 "child suspended: background tty read" {
             CHILDSUSP 789 SIGTTIN "background tty read"}}
           1011 {1 "child process exited abnormally" {
             CHILDSTATUS 1011 -1}}

    ::tcl::process status 1011
         → 1011 {1 "child process exited abnormally" {
             CHILDSTATUS 1011 -1}}

    ::tcl::process purge
    exec command1 1 2 3 &
         → 1213
    ::tcl::process list
         → 1213

# SEE ALSO

exec(n), open(n), pid(n), Tcl_DetachPids(3), Tcl_WaitPid(3),
Tcl_ReapDetachedProcs(3)

# KEYWORDS

background, child, detach, process, wait
