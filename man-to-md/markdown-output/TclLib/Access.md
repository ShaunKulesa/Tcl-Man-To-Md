# NAME

Tcl_Access, Tcl_Stat - check file permissions and other attributes

# SYNOPSIS

**#include \<tcl.h\>**

int **Tcl_Access**(*path*, *mode*)

int **Tcl_Stat**(*path*, *statPtr*)

# ARGUMENTS

Native name of the file to check the attributes of.

Mask consisting of one or more of **R_OK**, **W_OK**, **X_OK** and
**F_OK**. **R_OK**, **W_OK** and **X_OK** request checking whether the
file exists and has read, write and execute permissions, respectively.
**F_OK** just requests a check for the existence of the file.

The structure that contains the result.

# DESCRIPTION

As of Tcl 8.4, the object-based APIs **Tcl_FSAccess** and **Tcl_FSStat**
should be used in preference to **Tcl_Access** and **Tcl_Stat**,
wherever possible. Those functions also support Tcl\'s virtual
filesystem layer, which these do not.

## OBSOLETE FUNCTIONS

There are two reasons for calling **Tcl_Access** and **Tcl_Stat** rather
than calling system level functions **access** and **stat** directly.
First, the Windows implementation of both functions fixes some bugs in
the system level calls. Second, both **Tcl_Access** and **Tcl_Stat** (as
well as **Tcl_OpenFileChannelProc**) hook into a linked list of
functions. This allows the possibility to reroute file access to
alternative media or access methods.

**Tcl_Access** checks whether the process would be allowed to read,
write or test for existence of the file (or other file system object)
whose name is *path*. If *path* is a symbolic link on Unix, then
permissions of the file referred by this symbolic link are tested.

On success (all requested permissions granted), zero is returned. On
error (at least one bit in mode asked for a permission that is denied,
or some other error occurred), -1 is returned.

**Tcl_Stat** fills the stat structure *statPtr* with information about
the specified file. You do not need any access rights to the file to get
this information but you need search rights to all directories named in
the path leading to the file. The stat structure includes info regarding
device, inode (always 0 on Windows), privilege mode, nlink (always 1 on
Windows), user id (always 0 on Windows), group id (always 0 on Windows),
rdev (same as device on Windows), size, last access time, last
modification time, and creation time.

If *path* exists, **Tcl_Stat** returns 0 and the stat structure is
filled with data. Otherwise, -1 is returned, and no stat info is given.

# KEYWORDS

stat, access

# SEE ALSO

Tcl_FSAccess(3), Tcl_FSStat(3)

<!---
Copyright (c) 1998-1999 Scriptics Corporatio
-->

