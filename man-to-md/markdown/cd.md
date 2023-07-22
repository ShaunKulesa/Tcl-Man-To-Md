# NAME

cd - Change working directory

# SYNOPSIS

**cd **?*dirName*?

# DESCRIPTION

Change the current working directory to *dirName*, or to the home
directory (as specified in the HOME environment variable) if *dirName*
is not given. Returns an empty string. Note that the current working
directory is a per-process resource; the **cd** command changes the
working directory for all interpreters and (in a threaded environment)
all threads.

# EXAMPLES

Change to the home directory of the user **fred**:

    cd ~fred

Change to the directory **lib** that is a sibling directory of the
current one:

    cd ../lib

# SEE ALSO

filename(n), glob(n), pwd(n)

# KEYWORDS

working directory

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

