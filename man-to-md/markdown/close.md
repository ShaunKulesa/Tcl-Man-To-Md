# NAME

close - Close an open channel

# SYNOPSIS

**close ***channelId* ?r(ead)\|w(rite)?

# DESCRIPTION

Closes or half-closes the channel given by *channelId*.

*ChannelId* must be an identifier for an open channel such as a Tcl
standard channel (**stdin**, **stdout**, or **stderr**), the return
value from an invocation of **open** or **socket**, or the result of a
channel creation command provided by a Tcl extension.

The single-argument form is a simple all buffered output is flushed to
the channel\'s output device, any buffered input is discarded, the
underlying file or device is closed, and *channelId* becomes unavailable
for use.

If the channel is blocking, the command does not return until all output
is flushed. If the channel is nonblocking and there is unflushed output,
the channel remains open and the command returns immediately; output
will be flushed in the background and the channel will be closed when
all the flushing is complete.

If *channelId* is a blocking channel for a command pipeline then
**close** waits for the child processes to complete.

If the channel is shared between interpreters, then **close** makes
*channelId* unavailable in the invoking interpreter but has no other
effect until all of the sharing interpreters have closed the channel.
When the last interpreter in which the channel is registered invokes
**close**, the cleanup actions described above occur. See the **interp**
command for a description of channel sharing.

Channels are automatically closed when an interpreter is destroyed and
when the process exits.

From 8.6 on (TIP#398), nonblocking channels are no longer switched to
blocking mode when exiting; this guarantees a timely exit even when the
peer or a communication channel is stalled. To ensure proper flushing of
stalled nonblocking channels on exit, one must now either (a) actively
switch them back to blocking or (b) use the environment variable
TCL_FLUSH_NONBLOCKING_ON_EXIT, which when set and not equal to \"0\"
restores the previous behavior.

The command returns an empty string, and may generate an error if an
error occurs while flushing output. If a command in a command pipeline
created with **open** returns an error, **close** generates an error
(similar to the **exec** command.)

The two-argument form is a given a bidirectional channel like a socket
or command pipeline and a (possibly abbreviated) direction, it closes
only the sub-stream going in that direction. This means a shutdown() on
a socket, and a close() of one end of a pipe for a command pipeline.
Then, the Tcl-level channel data structure is either kept or freed
depending on whether the other direction is still open.

A single-argument close on an already half-closed bidirectional channel
is defined to just A half-close on an already closed half, or on a
wrong-sided unidirectional channel, raises an error.

In the case of a command pipeline, the child-reaping duty falls upon the
shoulders of the last close or half-close, which is thus allowed to
report an abnormal exit error.

Currently only sockets and command pipelines support half-close. A
future extension will allow reflected and stacked channels to do so.

# EXAMPLE

This illustrates how you can use Tcl to ensure that files get closed
even when errors happen by combining **catch**, **close** and
**return**:

    proc withOpenFile {filename channelVar script} {
        upvar 1 $channelVar chan
        set chan [open $filename]
        catch {
            uplevel 1 $script
        } result options
        close $chan
        return -options $options $result
    }

# SEE ALSO

file(n), open(n), socket(n), eof(n), Tcl_StandardChannels(3)

# KEYWORDS

blocking, channel, close, nonblocking, half-close

<!---
Copyright (c) 1993 The Regents of the University of California
Copyright (c) 1994-1996 Sun Microsystems, Inc
-->

