# NAME

Tcl_ConditionNotify, Tcl_ConditionWait, Tcl_ConditionFinalize,
Tcl_GetThreadData, Tcl_MutexLock, Tcl_MutexUnlock, Tcl_MutexFinalize,
Tcl_CreateThread, Tcl_JoinThread - Tcl thread support

# SYNOPSIS

**#include \<tcl.h\>**

void **Tcl_ConditionNotify**(*condPtr*)

void **Tcl_ConditionWait**(*condPtr, mutexPtr, timePtr*)

void **Tcl_ConditionFinalize**(*condPtr*)

Void \* **Tcl_GetThreadData**(*keyPtr, size*)

void **Tcl_MutexLock**(*mutexPtr*)

void **Tcl_MutexUnlock**(*mutexPtr*)

void **Tcl_MutexFinalize**(*mutexPtr*)

int **Tcl_CreateThread**(*idPtr, proc, clientData, stackSize, flags*)

int **Tcl_JoinThread**(*id, result*)

# ARGUMENTS

A condition variable, which must be associated with a mutex lock.

A mutex lock.

A time limit on the condition wait. NULL to wait forever. Note that a
polling value of 0 seconds does not make much sense.

This identifies a block of thread local storage. The key should be
static and process-wide, yet each thread will end up associating a
different block of storage with this key.

The size of the thread local storage block. This amount of data is
allocated and initialized to zero the first time each thread calls
**Tcl_GetThreadData**.

The referred storage will contain the id of the newly created thread as
returned by the operating system.

Id of the thread waited upon.

This procedure will act as the **main()** of the newly created thread.
The specified *clientData* will be its sole argument.

Arbitrary information. Passed as sole argument to the *proc*.

The size of the stack given to the new thread.

Bitmask containing flags allowing the caller to modify behavior of the
new thread.

The referred storage is used to place the exit code of the thread waited
upon into it.

# INTRODUCTION

Beginning with the 8.1 release, the Tcl core is thread safe, which
allows you to incorporate Tcl into multithreaded applications without
customizing the Tcl core. Starting with the 8.6 release, Tcl
multithreading support is on by default. To disable Tcl multithreading
support, you must include the **- -disable-threads** option to
**configure** when you configure and compile your Tcl core.

An important constraint of the Tcl threads implementation is that *only
the thread that created a Tcl interpreter can use that* interpreter. In
other words, multiple threads can not access the same Tcl interpreter.
(However, a single thread can safely create and use multiple
interpreters.)

# DESCRIPTION

Tcl provides **Tcl_CreateThread** for creating threads. The caller can
determine the size of the stack given to the new thread and modify the
behavior through the supplied *flags*. The value
**TCL_THREAD_STACK_DEFAULT** for the *stackSize* indicates that the
default size as specified by the operating system is to be used for the
new thread. As for the flags, currently only the values
**TCL_THREAD_NOFLAGS** and **TCL_THREAD_JOINABLE** are defined. The
first of them invokes the default behavior with no special settings.
Using the second value marks the new thread as *joinable*. This means
that another thread can wait for the such marked thread to exit and join
it.

Restrictions: On some UNIX systems the pthread-library does not contain
the functionality to specify the stack size of a thread. The specified
value for the stack size is ignored on these systems. Windows currently
does not support joinable threads. This flag value is therefore ignored
on this platform.

Tcl provides the **Tcl_ExitThread** and **Tcl_FinalizeThread** functions
for terminating threads and invoking optional per-thread exit handlers.
See the **Tcl_Exit** page for more information on these procedures.

The **Tcl_JoinThread** function is provided to allow threads to wait
upon the exit of another thread, which must have been marked as joinable
through usage of the **TCL_THREAD_JOINABLE**-flag during its creation
via **Tcl_CreateThread**.

Trying to wait for the exit of a non-joinable thread or a thread which
is already waited upon will result in an error. Waiting for a joinable
thread which already exited is possible, the system will retain the
necessary information until after the call to **Tcl_JoinThread**. This
means that not calling **Tcl_JoinThread** for a joinable thread will
cause a memory leak.

The **Tcl_GetThreadData** call returns a pointer to a block of
thread-private data. Its argument is a key that is shared by all threads
and a size for the block of storage. The storage is automatically
allocated and initialized to all zeros the first time each thread asks
for it. The storage is automatically deallocated by
**Tcl_FinalizeThread**.

## SYNCHRONIZATION AND COMMUNICATION

Tcl provides **Tcl_ThreadQueueEvent** and **Tcl_ThreadAlert** for
handling event queuing in multithreaded applications. See the
**Notifier** manual page for more information on these procedures.

A mutex is a lock that is used to serialize all threads through a piece
of code by calling **Tcl_MutexLock** and **Tcl_MutexUnlock**. If one
thread holds a mutex, any other thread calling **Tcl_MutexLock** will
block until **Tcl_MutexUnlock** is called. A mutex can be destroyed
after its use by calling **Tcl_MutexFinalize**. The result of locking a
mutex twice from the same thread is undefined. On some platforms it will
result in a deadlock. The **Tcl_MutexLock**, **Tcl_MutexUnlock** and
**Tcl_MutexFinalize** procedures are defined as empty macros if not
compiling with threads enabled. For declaration of mutexes the
**TCL_DECLARE_MUTEX** macro should be used. This macro assures correct
mutex handling even when the core is compiled without threads enabled.

A condition variable is used as a signaling mechanism: a thread can lock
a mutex and then wait on a condition variable with
**Tcl_ConditionWait**. This atomically releases the mutex lock and
blocks the waiting thread until another thread calls
**Tcl_ConditionNotify**. The caller of **Tcl_ConditionNotify** should
have the associated mutex held by previously calling **Tcl_MutexLock**,
but this is not enforced. Notifying the condition variable unblocks all
threads waiting on the condition variable, but they do not proceed until
the mutex is released with **Tcl_MutexUnlock**. The implementation of
**Tcl_ConditionWait** automatically locks the mutex before returning.

The caller of **Tcl_ConditionWait** should be prepared for spurious
notifications by calling **Tcl_ConditionWait** within a while loop that
tests some invariant.

A condition variable can be destroyed after its use by calling
**Tcl_ConditionFinalize**.

The **Tcl_ConditionNotify**, **Tcl_ConditionWait** and
**Tcl_ConditionFinalize** procedures are defined as empty macros if not
compiling with threads enabled.

## INITIALIZATION

All of these synchronization objects are self-initializing. They are
implemented as opaque pointers that should be NULL upon first use. The
mutexes and condition variables are either cleaned up by process exit
handlers (if living that long) or explicitly by calls to
**Tcl_MutexFinalize** or **Tcl_ConditionFinalize**. Thread local storage
is reclaimed during **Tcl_FinalizeThread**.

# SCRIPT-LEVEL ACCESS TO THREADS

Tcl provides no built-in commands for scripts to use to create, manage,
or join threads, nor any script-level access to mutex or condition
variables. It provides such facilities only via C interfaces, and leaves
it up to packages to expose these matters to the script level. One such
package is the **Thread** package.

# EXAMPLE

To create a thread with portable code, its implementation function
should be declared as follows:

    static Tcl_ThreadCreateProc MyThreadImplFunc;

It should then be defined like this example, which just counts up to a
given value and then finishes.

    static Tcl_ThreadCreateType
    MyThreadImplFunc(
        ClientData clientData)
    {
        int i, limit = (int) clientData;
        for (i=0 ; i<limit ; i++) {
            /* doing nothing at all here */
        }
        TCL_THREAD_CREATE_RETURN;
    }

To create the above thread, make it execute, and wait for it to finish,
we would do this:

    int limit = 1000000000;
    ClientData limitData = (void*)((intptr_t) limit);
    Tcl_ThreadId id;    /* holds identity of thread created */
    int result;

    if (Tcl_CreateThread(&id, MyThreadImplFunc, limitData,
            TCL_THREAD_STACK_DEFAULT,
            TCL_THREAD_JOINABLE) != TCL_OK) {
        /* Thread did not create correctly */
        return;
    }
    /* Do something else for a while here */
    if (Tcl_JoinThread(id, &result) != TCL_OK) {
        /* Thread did not finish properly */
        return;
    }
    /* All cleaned up nicely */

# SEE ALSO

Tcl_GetCurrentThread(3), Tcl_ThreadQueueEvent(3), Tcl_ThreadAlert(3),
Tcl_ExitThread(3), Tcl_FinalizeThread(3),
Tcl_CreateThreadExitHandler(3), Tcl_DeleteThreadExitHandler(3), Thread

# KEYWORDS

thread, mutex, condition variable, thread local storage

<!---
Copyright (c) 1999 Scriptics Corporatio
Copyright (c) 1998 Sun Microsystems, Inc
-->

