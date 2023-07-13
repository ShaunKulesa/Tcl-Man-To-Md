\

# NAME

zipfs - Mount and work with ZIP files within Tcl

# SYNOPSIS

    package require tcl::zipfs ?1.0?

    zipfs canonical ?mntpnt? filename ?ZIPFS?
    zipfs exists filename
    zipfs find directoryName
    zipfs info filename
    zipfs list ?(-glob|-regexp)? ?pattern?
    zipfs lmkimg outfile inlist ?password infile?
    zipfs lmkzip outfile inlist ?password?
    zipfs mkimg outfile indir ?strip? ?password? ?infile?
    zipfs mkkey password
    zipfs mkzip outfile indir ?strip? ?password?
    zipfs mount ?mountpoint? ?zipfile? ?password?
    zipfs root
    zipfs unmount mountpoint

\

# DESCRIPTION

The **zipfs** command (the sole public command provided by the built-in
package with the same name) provides Tcl with the ability to mount the
contents of a ZIP archive file as a virtual file system. ZIP archives
support simple encryption, sufficient to prevent casual inspection of
their contents but not able to prevent access by even a moderately
determined attacker.

**zipfs canonical** ?*mountpoint*? *filename* ?*inZipfs*?

:   This takes the name of a file, *filename*, and produces where it
    would be mapped into a zipfs mount as its result. If specified,
    *mountpoint* says within which mount the mapping will be done; if
    omitted, the main root of the zipfs system is used. The *inZipfs*
    argument is a an optional boolean which controls whether to fully
    canonicalise the name; it defaults to true.

**zipfs exists** *filename*

:   Return 1 if the given filename exists in the mounted zipfs and 0 if
    it does not.

**zipfs find** *directoryName*

:   Recursively lists files including and below the directory
    *directoryName*. The result list consists of relative path names
    starting from the given directory. This command is also used by the
    **zipfs mkzip** and **zipfs** mkimg commands.

**zipfs info** *file*

:   Return information about the given *file* in the mounted zipfs. The
    information consists of:

    (1) the name of the ZIP archive file that contains the file,

    (2) the size of the file after decompressions,

    (3) the compressed size of the file, and

    (4) the offset of the compressed data in the ZIP archive file.

    Note: querying the mount point gives the start of the zip data as
    the offset in (4), which can be used to truncate the zip information
    from an executable.

**zipfs list** ?(**-glob**\|**-regexp**)? ?*pattern*?

:   Return a list of all files in the mounted zipfs, or just those
    matching *pattern* (optionally controlled by the option parameters).
    The order of the names in the list is arbitrary.

**zipfs mount** ?*mountpoint*? ?*zipfile*? ?*password*?

:   The **zipfs mount** command mounts a ZIP archive file as a Tcl
    virtual filesystem at *mountpoint*. After this command executes,
    files contained in *zipfile* will appear to Tcl to be regular files
    at the mount point.

    With no *zipfile*, returns the zipfile mounted at *mountpoint*. With
    no *mountpoint*, return all zipfile/mount pairs. If *mountpoint* is
    specified as an empty string, mount on file path.

    **NB:** because the current working directory is a concept
    maintained by the operating system, using **cd** into a mounted
    archive will only work in the current process, and then not entirely
    consistently (e.g., if a shared library uses direct access to the OS
    rather than through Tcl\'s filesystem API, it will not see the
    current directory as being inside the mount and will not be able to
    access the files inside the mount).

**zipfs root**

:   Returns a constant string which indicates the mount point for zipfs
    volumes for the current platform. On Windows, this value is On Unix,
    this value is

**zipfs unmount ***mountpoint*

:   Unmounts a previously mounted ZIP archive mounted to *mountpoint*.

## ZIP CREATION COMMANDS

This package also provides several commands to aid the creation of ZIP
archives as Tcl applications.

**zipfs mkzip** *outfile indir* ?*strip*? ?*password*?

:   Creates a ZIP archive file named *outfile* from the contents of the
    input directory *indir* (contained regular files only) with optional
    ZIP password *password*. While processing the files below *indir*
    the optional file name prefix given in *strip* is stripped off the
    beginning of the respective file name. When stripping, it is common
    to remove either the whole source directory name or the name of its
    parent directory.

    **Caution:** the choice of the *indir* parameter (less the optional
    stripped prefix) determines the later root name of the archive\'s
    content.

**zipfs mkimg** *outfile indir* ?*strip*? ?*password*? ?*infile*?

:   Creates an image (potentially a new executable file) similar to
    **zipfs** mkzip; see that command for a description of most
    parameters to this command, as they behave identically here.

    If the *infile* parameter is specified, this file is prepended in
    front of the ZIP archive, otherwise the file returned by **info
    nameofexecutable** (i.e., the executable file of the running
    process) is used. If the *password* parameter is not empty, an
    obfuscated version of that password (see **zipfs mkkey**) is placed
    between the image and ZIP chunks of the output file and the contents
    of the ZIP chunk are protected with that password. If the starting
    image has a ZIP archive already attached to it, it is removed from
    the copy in *outfile* before the new ZIP archive is added.

    If there is a file, **main.tcl**, in the root directory of the
    resulting archive and the image file that the archive is attached to
    is a **tclsh** (or **wish**) instance (true by default, but depends
    on your configuration), then the resulting image is an executable
    that will **source** the script in that **main.tcl** after mounting
    the ZIP archive, and will **exit** once that script has been
    executed.

    **Caution:** highly experimental, not usable on Android, only
    partially tested on Linux and Windows.

**zipfs mkkey** *password*

:   Given the clear text *password* argument, an obfuscated string
    version is returned with the same format used in the **zipfs mkimg**
    command.

**zipfs lmkimg** *outfile inlist* ?*password infile*?

:   This command is like **zipfs mkimg**, but instead of an input
    directory, *inlist* must be a Tcl list where the odd elements are
    the names of files to be copied into the archive in the image, and
    the even elements are their respective names within that archive.

**zipfs lmkzip** *outfile inlist* ?*password*?

:   This command is like **zipfs mkzip**, but instead of an input
    directory, *inlist* must be a Tcl list where the odd elements are
    the names of files to be copied into the archive, and the even
    elements are their respective names within that archive.

# EXAMPLES

Mounting an ZIP archive as an application directory and running code out
of it before unmounting it again:

    set zip myApp.zip
    set base [file join [zipfs root] myApp]

    zipfs mount $base $zip
    # $base now has the contents of myApp.zip

    source [file join $base app.tcl]
    # use the contents, load libraries from it, etc...

    zipfs unmount $zip

Creating a ZIP archive, given that a directory exists containing the
content to put in the archive. Note that the source directory is given
twice, in order to strip the exterior directory name from each filename
in the archive.

    set sourceDirectory [file normalize myApp]
    set targetZip myApp.zip

    zipfs mkzip $targetZip $sourceDirectory $sourceDirectory

Encryption can be applied to ZIP archives by providing a password when
building the ZIP and when mounting it.

    set zip myApp.zip
    set sourceDir [file normalize myApp]
    set password "hunter2"
    set base [file join [zipfs root] myApp]

    # Create with password
    zipfs mkzip $targetZip $sourceDir $sourceDir $password

    # Mount with password
    zipfs mount $base $zip $password

When creating an executable image with a password, the password is
placed within the executable in a shrouded form so that the application
can read files inside the embedded ZIP archive yet casual inspection
cannot read it.

    set appDir [file normalize myApp]
    set img "myApp.bin"
    set password "hunter2"

    # Create some simple content to define a basic application
    file mkdir $appDir
    set f [open $appDir/main.tcl]
    puts $f {
        puts "Hi. This is [info script]"
    }
    close $f

    # Create the executable
    zipfs mkimg $img $appDir $appDir $password

    # Launch the executable, printing its output to stdout
    exec $img >@stdout
    #    prints: Hi. This is //zipfs:/app/main.tcl

# SEE ALSO

tclsh(1), file(n), zipfs(3), zlib(n)

# KEYWORDS

compress, filesystem, zip
