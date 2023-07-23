# NAME

http - Client-side implementation of the HTTP/1.1 protocol

# SYNOPSIS

**package require http ?2.9?**

**::http::config ?***-option value* \...?

**::http::geturl ***url* ?*-option value* \...?

**::http::formatQuery** *key value* ?*key value* \...?

**::http::quoteString** *value*

**::http::reset** *token* ?*why*?

**::http::wait ***token*

**::http::status ***token*

**::http::size ***token*

**::http::code ***token*

**::http::ncode ***token*

**::http::meta ***token*

**::http::data ***token*

**::http::error ***token*

**::http::cleanup ***token*

**::http::register ***proto port command*

**::http::registerError ***port* ?*message*?

**::http::unregister ***proto*

# EXPORTED COMMANDS

Namespace **http** exports the commands **config**, **formatQuery**,
**geturl**, **quoteString**, **register**, **registerError**, **reset**,
**unregister**, and **wait**.

It does not export the commands **cleanup**, **code**, **data**,
**error**, **meta**, **ncode**, **size**, or **status**.

# DESCRIPTION

The **http** package provides the client side of the HTTP/1.1 protocol,
as defined in RFC 7230 to RFC 7235, which supersede RFC 2616. The
package implements the GET, POST, and HEAD operations of HTTP/1.1. It
allows configuration of a proxy host to get through firewalls. The
package is compatible with the **Safesock** security policy, so it can
be used by untrusted applets to do URL fetching from a restricted set of
hosts. This package can be extended to support additional HTTP transport
protocols, such as HTTPS, by providing a custom **socket** command, via
**::http::register**.

The **::http::geturl** procedure does a HTTP transaction. Its *options *
determine whether a GET, POST, or HEAD transaction is performed. The
return value of **::http::geturl** is a token for the transaction. The
value is also the name of an array in the ::http namespace that contains
state information about the transaction. The elements of this array are
described in the **STATE ARRAY** section.

If the **-command** option is specified, then the HTTP operation is done
in the background. **::http::geturl** returns immediately after
generating the HTTP request and the callback is invoked when the
transaction completes. For this to work, the Tcl event loop must be
active. In Tk applications this is always true. For pure-Tcl
applications, the caller can use **::http::wait** after calling
**::http::geturl** to start the event loop.

**Note:** The event queue is even used without the **-command** option.
As a side effect, arbitrary commands may be processed while
**http::geturl** is running.

# COMMANDS

**::http::config** ?*options*?

:   The **::http::config** command is used to set and query the name of
    the proxy server and port, and the User-Agent name used in the HTTP
    requests. If no options are specified, then the current
    configuration is returned. If a single argument is specified, then
    it should be one of the flags described below. In this case the
    current value of that setting is returned. Otherwise, the options
    should be a set of flags and values that define the configuration:

    **-accept** *mimetypes*

    :   The Accept header of the request. The default is \*/\*, which
        means that all types of documents are accepted. Otherwise you
        can supply a comma-separated list of mime type patterns that you
        are willing to receive. For example,

    **-pipeline** *boolean*

    :   Specifies whether HTTP/1.1 transactions on a persistent socket
        will be pipelined. See the **PERSISTENT SOCKETS** section for
        details. The default is 1.

    **-postfresh** *boolean*

    :   Specifies whether requests that use the **POST** method will
        always use a fresh socket, overriding the **-keepalive** option
        of command **http::geturl**. See the **PERSISTENT SOCKETS**
        section for details. The default is 0.

    **-proxyhost** *hostname*

    :   The name of the proxy host, if any. If this value is the empty
        string, the URL host is contacted directly.

    **-proxyport** *number*

    :   The proxy port number.

    **-proxyfilter** *command*

    :   The command is a callback that is made during **::http::geturl**
        to determine if a proxy is required for a given host. One
        argument, a host name, is added to *command* when it is invoked.
        If a proxy is required, the callback should return a two-element
        list containing the proxy server and proxy port. Otherwise the
        filter should return an empty list. The default filter returns
        the values of the **-proxyhost** and **-proxyport** settings if
        they are non-empty.

        The **::http::geturl** command runs the **-proxyfilter**
        callback inside a **catch** command. Therefore an error in the
        callback command does not call the **bgerror** handler. See the
        **ERRORS** section for details.

    **-repost** *boolean*

    :   Specifies what to do if a POST request over a persistent
        connection fails because the server has half-closed the
        connection. If boolean **true**, the request will be
        automatically retried; if boolean **false** it will not, and the
        application that uses **http::geturl** is expected to seek user
        confirmation before retrying the POST. The value **true** should
        be used only under certain conditions. See the **PERSISTENT
        SOCKETS** section for details. The default is 0.

    **-urlencoding** *encoding*

    :   The *encoding* used for creating the x-url-encoded URLs with
        **::http::formatQuery** and **::http::quoteString**. The default
        is **utf-8**, as specified by RFC 2718. Prior to http 2.5 this
        was unspecified, and that behavior can be returned by specifying
        the empty string (**{}**), although *iso8859-1* is recommended
        to restore similar behavior but without the
        **::http::formatQuery** or **::http::quoteString** throwing an
        error processing non-latin-1 characters.

    **-useragent** *string*

    :   The value of the User-Agent header in the HTTP request. In an
        unsafe interpreter, the default value depends upon the operating
        system, and the version numbers of **http** and **Tcl**, and is
        (for example) A safe interpreter cannot determine its operating
        system, and so the default in a safe interpreter is to use a
        Windows 10 value with the current version numbers of **http**
        and **Tcl**.

    **-zip** *boolean*

    :   If the value is boolean **true**, then by default requests will
        send a header If the value is boolean **false**, then by default
        this header will not be sent. In either case the default can be
        overridden for an individual request by supplying a custom
        **Accept-Encoding** header in the **-headers** option of
        **http::geturl**. The default is 1.

**::http::geturl** *url* ?*options*?

:   The **::http::geturl** command is the main procedure in the package.
    The **-query** option causes a POST operation and the **-validate**
    option causes a HEAD operation; otherwise, a GET operation is
    performed. The **::http::geturl** command returns a *token* value
    that can be used to get information about the transaction. See the
    **STATE ARRAY** and **ERRORS** section for details. The
    **::http::geturl** command blocks until the operation completes,
    unless the **-command** option specifies a callback that is invoked
    when the HTTP transaction completes. **::http::geturl** takes
    several options:

    **-binary** *boolean*

    :   Specifies whether to force interpreting the URL data as binary.
        Normally this is auto-detected (anything not beginning with a
        **text** content type or whose content encoding is **gzip** or
        **compress** is considered binary data).

    **-blocksize** *size*

    :   The block size used when reading the URL. At most *size* bytes
        are read at once. After each block, a call to the **-progress**
        callback is made (if that option is specified).

    **-channel** *name*

    :   Copy the URL contents to channel *name* instead of saving it in
        **state(body)**.

    **-command** *callback*

    :   Invoke *callback* after the HTTP transaction completes. This
        option causes **::http::geturl** to return immediately. The
        *callback* gets an additional argument that is the *token*
        returned from **::http::geturl**. This token is the name of an
        array that is described in the **STATE ARRAY** section. Here is
        a template for the callback:

            proc httpCallback {token} {
                upvar #0 $token state
                # Access state as a Tcl array
            }

        The **::http::geturl** command runs the **-command** callback
        inside a **catch** command. Therefore an error in the callback
        command does not call the **bgerror** handler. See the
        **ERRORS** section for details.

    **-handler** *callback*

    :   Invoke *callback* whenever HTTP data is available; if present,
        nothing else will be done with the HTTP data. This procedure
        gets two additional arguments: the socket for the HTTP data and
        the *token* returned from **::http::geturl**. The token is the
        name of a global array that is described in the **STATE ARRAY**
        section. The procedure is expected to return the number of bytes
        read from the socket. Here is a template for the callback:

            proc httpHandlerCallback {socket token} {
                upvar #0 $token state
                # Access socket, and state as a Tcl array
                # For example...
                ...
                set data [read $socket 1000]
                set nbytes [string length $data]
                ...
                return $nbytes
            }

        The **http::geturl** code for the **-handler** option is not
        compatible with either compression or chunked transfer-encoding.
        If **-handler** is specified, then to work around these issues
        **http::geturl** will reduce the HTTP protocol to 1.0, and
        override the **-zip** option (i.e. it will not send the header
        \"**Accept-Encoding: gzip,deflate,compress**\").

        If options **-handler** and **-channel** are used together, the
        handler is responsible for copying the data from the HTTP socket
        to the specified channel. The name of the channel is available
        to the handler as element **-channel** of the token array.

        The **::http::geturl** command runs the **-handler** callback
        inside a **catch** command. Therefore an error in the callback
        command does not call the **bgerror** handler. See the
        **ERRORS** section for details.

    **-headers** *keyvaluelist*

    :   This option is used to add headers not already specified by
        **::http::config** to the HTTP request. The *keyvaluelist*
        argument must be a list with an even number of elements that
        alternate between keys and values. The keys become header field
        names. Newlines are stripped from the values so the header
        cannot be corrupted. For example, if *keyvaluelist* is **Pragma
        no-cache** then the following header is included in the HTTP
        request:

            Pragma: no-cache

    **-keepalive** *boolean*

    :   If boolean **true**, attempt to keep the connection open for
        servicing multiple requests. Default is 0.

    **-method** *type*

    :   Force the HTTP request method to *type*. **::http::geturl** will
        auto-select GET, POST or HEAD based on other options, but this
        option overrides that selection and enables choices like PUT and
        DELETE for WebDAV support.

        It is the caller\'s responsibility to ensure that the headers
        and request body (if any) conform to the requirements of the
        request method. For example, if using **-method** *POST* to send
        a POST with an empty request body, the caller must also supply
        the option

    **-myaddr** *address*

    :   Pass an specific local address to the underlying **socket** call
        in case multiple interfaces are available.

    **-progress** *callback*

    :   The *callback* is made after each transfer of data from the URL.
        The callback gets three additional arguments: the *token* from
        **::http::geturl**, the expected total size of the contents from
        the **Content-Length** meta-data, and the current number of
        bytes transferred so far. The expected total size may be
        unknown, in which case zero is passed to the callback. Here is a
        template for the progress callback:

            proc httpProgress {token total current} {
                upvar #0 $token state
            }

    **-protocol** *version*

    :   Select the HTTP protocol version to use. This should be 1.0 or
        1.1 (the default). Should only be necessary for servers that do
        not understand or otherwise complain about HTTP/1.1.

    **-query** *query*

    :   This flag (if the value is non-empty) causes **::http::geturl**
        to do a POST request that passes the string *query* verbatim to
        the server as the request payload. The content format (and
        encoding) of *query* is announced by the request header
        **Content-Type** which is set by the option **-type**. Any value
        of **-type** is permitted, and it is the responsibility of the
        caller to supply *query* in the correct format.

        If **-type** is not specified, it defaults to
        *application/x-www-form-urlencoded*, which requires *query* to
        be an x-url-encoding formatted query-string (this **-type** and
        query format are used in a POST submitted from an html form).
        The **::http::formatQuery** procedure can be used to do the
        formatting.

    **-queryblocksize** *size*

    :   The block size used when posting query data to the URL. At most
        *size* bytes are written at once. After each block, a call to
        the **-queryprogress** callback is made (if that option is
        specified).

    **-querychannel** *channelID*

    :   This flag causes **::http::geturl** to do a POST request that
        passes the data contained in *channelID* to the server. The data
        contained in *channelID* must be an x-url-encoding formatted
        query unless the **-type** option below is used. If a
        Content-Length header is not specified via the **-headers**
        options, **::http::geturl** attempts to determine the size of
        the post data in order to create that header. If it is unable to
        determine the size, it returns an error.

    **-queryprogress** *callback*

    :   The *callback* is made after each transfer of data to the URL
        (i.e. POST) and acts exactly like the **-progress** option (the
        callback format is the same).

    **-strict** *boolean*

    :   Whether to enforce RFC 3986 URL validation on the request.
        Default is 1.

    **-timeout** *milliseconds*

    :   If *milliseconds* is non-zero, then **::http::geturl** sets up a
        timeout to occur after the specified number of milliseconds. A
        timeout results in a call to **::http::reset** and to the
        **-command** callback, if specified. The return value of
        **::http::status** is **timeout** after a timeout has occurred.

    **-type** *mime-type*

    :   Use *mime-type* as the **Content-Type** value, instead of the
        default value (**application/x-www-form-urlencoded**) during a
        POST operation.

    **-validate** *boolean*

    :   If *boolean* is non-zero, then **::http::geturl** does an HTTP
        HEAD request. This request returns meta information about the
        URL, but the contents are not returned. The meta information is
        available in the **state(meta) ** variable after the
        transaction. See the **STATE ARRAY** section for details.

**::http::formatQuery** *key value* ?*key value* \...?

:   This procedure does x-url-encoding of query data. It takes an even
    number of arguments that are the keys and values of the query. It
    encodes the keys and values, and generates one string that has the
    proper & and = separators. The result is suitable for the **-query**
    value passed to **::http::geturl**.

**::http::quoteString** *value*

:   This procedure does x-url-encoding of string. It takes a single
    argument and encodes it.

**::http::reset** *token* ?*why*?

:   This command resets the HTTP transaction identified by *token*, if
    any. This sets the **state(status)** value to *why*, which defaults
    to **reset**, and then calls the registered **-command** callback.

**::http::wait** *token*

:   This is a convenience procedure that blocks and waits for the
    transaction to complete. This only works in trusted code because it
    uses **vwait**. Also, it is not useful for the case where
    **::http::geturl** is called *without* the **-command** option
    because in this case the **::http::geturl** call does not return
    until the HTTP transaction is complete, and thus there is nothing to
    wait for.

**::http::data** *token*

:   This is a convenience procedure that returns the **body** element
    (i.e., the URL data) of the state array.

**::http::error** *token*

:   This is a convenience procedure that returns the **error** element
    of the state array.

**::http::status** *token*

:   This is a convenience procedure that returns the **status** element
    of the state array.

**::http::code** *token*

:   This is a convenience procedure that returns the **http** element of
    the state array.

**::http::ncode** *token*

:   This is a convenience procedure that returns just the numeric return
    code (200, 404, etc.) from the **http** element of the state array.

**::http::size** *token*

:   This is a convenience procedure that returns the **currentsize**
    element of the state array, which represents the number of bytes
    received from the URL in the **::http::geturl** call.

**::http::meta** *token*

:   This is a convenience procedure that returns the **meta** element of
    the state array which contains the HTTP response headers. See below
    for an explanation of this element.

**::http::cleanup** *token*

:   This procedure cleans up the state associated with the connection
    identified by *token*. After this call, the procedures like
    **::http::data** cannot be used to get information about the
    operation. It is *strongly* recommended that you call this function
    after you are done with a given HTTP request. Not doing so will
    result in memory not being freed, and if your app calls
    **::http::geturl** enough times, the memory leak could cause a
    performance hit\...or worse.

**::http::register** *proto port command*

:   This procedure allows one to provide custom HTTP transport types
    such as HTTPS, by registering a prefix, the default port, and the
    command to execute to create the Tcl **channel**. E.g.:

        package require http
        package require tls

        ::http::register https 443 ::tls::socket

        set token [::http::geturl https://my.secure.site/]

**::http::registerError** *port* ?*message*?

:   This procedure allows a registered protocol handler to deliver an
    error message for use by **http**. Calling this command does not
    raise an error. The command is useful when a registered protocol
    detects an problem (for example, an invalid TLS certificate) that
    will cause an error to propagate to **http**. The command allows
    **http** to provide a precise error message rather than a general
    one. The command returns the value provided by the last call with
    argument *message*, or the empty string if no such call has been
    made.

**::http::unregister** *proto*

:   This procedure unregisters a protocol handler that was previously
    registered via **::http::register**, returning a two-item list of
    the default port and handler command that was previously installed
    (via **::http::register**) if there was such a handler, and an error
    if there was no such handler.

# ERRORS

The **::http::geturl** procedure will raise errors in the following
cases: invalid command line options, an invalid URL, a URL on a
non-existent host, or a URL at a bad port on an existing host. These
errors mean that it cannot even start the network transaction. It will
also raise an error if it gets an I/O error while writing out the HTTP
request header. For synchronous **::http::geturl** calls (where
**-command** is not specified), it will raise an error if it gets an I/O
error while reading the HTTP reply headers or data. Because
**::http::geturl** does not return a token in these cases, it does all
the required cleanup and there is no issue of your app having to call
**::http::cleanup**.

For asynchronous **::http::geturl** calls, all of the above error
situations apply, except that if there is any error while reading the
HTTP reply headers or data, no exception is thrown. This is because
after writing the HTTP headers, **::http::geturl** returns, and the rest
of the HTTP transaction occurs in the background. The command callback
can check if any error occurred during the read by calling
**::http::status** to check the status and if its *error*, calling
**::http::error** to get the error message.

Alternatively, if the main program flow reaches a point where it needs
to know the result of the asynchronous HTTP request, it can call
**::http::wait** and then check status and error, just as the callback
does.

The **::http::geturl** command runs the **-command**, **-handler**, and
**-proxyfilter** callbacks inside a **catch** command. Therefore an
error in the callback command does not call the **bgerror** handler.
When debugging one of these callbacks, it may be convenient to report
errors by using a **catch** command within the callback command itself,
e.g. to write an error message to stdout.

In any case, you must still call **::http::cleanup** to delete the state
array when you are done.

There are other possible results of the HTTP transaction determined by
examining the status from **::http::status**. These are described below.

**ok**

:   If the HTTP transaction completes entirely, then status will be
    **ok**. However, you should still check the **::http::code** value
    to get the HTTP status. The **::http::ncode** procedure provides
    just the numeric error (e.g., 200, 404 or 500) while the
    **::http::code** procedure returns a value like

**eof**

:   If the server closes the socket without replying, then no error is
    raised, but the status of the transaction will be **eof**.

**error**

:   The error message will also be stored in the **error** status array
    element, accessible via **::http::error**.

**timeout**

:   A timeout occurred before the transaction could complete

**reset**

:   user-reset

Another error possibility is that **::http::geturl** is unable to write
all the post query data to the server before the server responds and
closes the socket. The error message is saved in the **posterror**
status array element and then **::http::geturl** attempts to complete
the transaction. If it can read the server\'s response it will end up
with an **ok** status, otherwise it will have an **eof** status.

# STATE ARRAY

The **::http::geturl** procedure returns a *token* that can be used to
get to the state of the HTTP transaction in the form of a Tcl array. Use
this construct to create an easy-to-use array variable:

    upvar #0 $token state

Once the data associated with the URL is no longer needed, the state
array should be unset to free up storage. The **::http::cleanup**
procedure is provided for that purpose. The following elements of the
array are supported:

> **binary**
>
> :   This is boolean **true** if (after decoding any compression
>     specified by the response header) the HTTP response is binary. It
>     is boolean **false** if the HTTP response is text.
>
> **body**
>
> :   The contents of the URL. This will be empty if the **-channel**
>     option has been specified. This value is returned by the
>     **::http::data** command.
>
> **charset**
>
> :   The value of the charset attribute from the **Content-Type**
>     meta-data value. If none was specified, this defaults to the RFC
>     standard **iso8859-1**, or the value of
>     **\$::http::defaultCharset**. Incoming text data will be
>     automatically converted from this charset to utf-8.
>
> **coding**
>
> :   A copy of the **Content-Encoding** meta-data value.
>
> **currentsize**
>
> :   The current number of bytes fetched from the URL. This value is
>     returned by the **::http::size** command.
>
> **error**
>
> :   If defined, this is the error string seen when the HTTP
>     transaction was aborted.
>
> **http**
>
> :   The HTTP status reply from the server. This value is returned by
>     the **::http::code** command. The format of this value is:
>
>         HTTP/1.1 code string
>
>     The *code* is a three-digit number defined in the HTTP standard. A
>     code of 200 is OK. Codes beginning with 4 or 5 indicate errors.
>     Codes beginning with 3 are redirection errors. In this case the
>     **Location** meta-data specifies a new URL that contains the
>     requested information.
>
> **meta**
>
> :   The HTTP protocol returns meta-data that describes the URL
>     contents. The **meta** element of the state array is a list of the
>     keys and values of the meta-data. This is in a format useful for
>     initializing an array that just contains the meta-data:
>
>         array set meta $state(meta)
>
>     Some of the meta-data keys are listed below, but the HTTP standard
>     defines more, and servers are free to add their own.
>
>     **Content-Type**
>
>     :   The type of the URL contents. Examples include **text/html**,
>         **image/gif,** **application/postscript** and
>         **application/x-tcl**.
>
>     **Content-Length**
>
>     :   The advertised size of the contents. The actual size obtained
>         by **::http::geturl** is available as **state(currentsize)**.
>
>     **Location**
>
>     :   An alternate URL that contains the requested data.
>
> **posterror**
>
> :   The error, if any, that occurred while writing the post query data
>     to the server.
>
> **status**
>
> :   See description in the chapter **ERRORS** above for a list and
>     description of **status**. During the transaction this value is
>     the empty string.
>
> **totalsize**
>
> :   A copy of the **Content-Length** meta-data value.
>
> **type**
>
> :   A copy of the **Content-Type** meta-data value.
>
> **url**
>
> :   The requested URL.

# PERSISTENT CONNECTIONS

## BASICS

See RFC 7230 Sec 6, which supersedes RFC 2616 Sec 8.1.

A persistent connection allows multiple HTTP/1.1 transactions to be
carried over the same TCP connection. Pipelining allows a client to make
multiple requests over a persistent connection without waiting for each
response. The server sends responses in the same order that the requests
were received.

If a POST request fails to complete, typically user confirmation is
needed before sending the request again. The user may wish to verify
whether the server was modified by the failed POST request, before
sending the same request again.

A HTTP request will use a persistent socket if the call to
**http::geturl** has the option **-keepalive true**. It will use
pipelining where permitted if the **http::config** option **-pipeline**
is boolean **true** (its default value).

The http package maintains no more than one persistent connection to
each server (i.e. each value of If **http::geturl** is called to make a
request over a persistent connection while the connection is busy with
another request, the new request will be held in a queue until the
connection is free.

The http package does not support HTTP/1.0 persistent connections
controlled by the **Keep-Alive** header.

## SPECIAL CASES

This subsection discusses issues related to closure of the persistent
connection by the server, automatic retry of failed requests, the
special treatment necessary for POST requests, and the options for
dealing with these cases.

In accordance with RFC 7230, **http::geturl** does not pipeline requests
that use the POST method. If a POST uses a persistent connection and is
not the first request on that connection, **http::geturl** waits until
it has received the response for the previous request; or (if
**http::config** option **-postfresh** is boolean **true**) it uses a
new connection for each POST.

If the server is processing a number of pipelined requests, and sends a
response header with one of the responses (other than the last), then
subsequent responses are unfulfilled. **http::geturl** will send the
unfulfilled requests again over a new connection.

A difficulty arises when a HTTP client sends a request over a persistent
connection that has been idle for a while. The HTTP server may
half-close an apparently idle connection while the client is sending a
request, but before the request arrives at the server: in this case (an
the request will fail. The difficulty arises because the client cannot
be certain whether the POST modified the state of the server. For HEAD
or GET requests, **http::geturl** opens another connection and
retransmits the failed request. However, if the request was a POST, RFC
7230 forbids automatic retry by default, suggesting either user
confirmation, or confirmation by user-agent software that has semantic
understanding of the application. The **http::config** option
**-repost** allows for either possibility.

Asynchronous close events can occur only in a short interval of time.
The **http** package monitors each persistent connection for closure by
the server. Upon detection, the connection is also closed at the client
end, and subsequent requests will use a fresh connection.

If the **http::geturl** command is called with option **-keepalive
true**, then it will both try to use an existing persistent connection
(if one is available), and it will send the server a request header
asking to keep the connection open for future requests.

The **http::config** options **-pipeline**, **-postfresh**, and
**-repost** relate to persistent connections.

Option **-pipeline**, if boolean **true**, will pipeline GET and HEAD
requests made over a persistent connection. POST requests will not be
pipelined - if the POST is not the first transaction on the connection,
its request will not be sent until the previous response has finished.
GET and HEAD requests made after a POST will not be sent until the POST
response has been delivered, and will not be sent if the POST fails.

Option **-postfresh**, if boolean **true**, will override the
**http::geturl** option **-keepalive**, and always open a fresh
connection for a POST request.

Option **-repost**, if **true**, permits automatic retry of a POST
request that fails because it uses a persistent connection that the
server has half-closed (an Subsequent GET and HEAD requests in a failed
pipeline will also be retried. *The -repost option should be used only
if the application understands* that the retry is appropriate -
specifically, the application must know that if the failed POST
successfully modified the state of the server, a repeat POST would have
no adverse effect.

# PROTOCOL UPGRADES

The HTTP/1.1 **Connection** and **Upgrade** client headers inform the
server that the client wishes to change the protocol used over the
existing connection (RFC 7230). This mechanism can be used to request a
WebSocket (RFC 6455), a higher version of the HTTP protocol (HTTP 2), or
TLS encryption. If the server accepts the upgrade request, its response
code will be 101.

To request a protocol upgrade when calling **http::geturl**, the
**-headers** option must supply appropriate values for **Connection**
and **Upgrade**, and the **-command** option must supply a command that
implements the requested protocol and can also handle the server
response if the server refuses the protocol upgrade. For upgrade
requests **http::geturl** ignores the value of option **-keepalive**,
and always uses the value **0** so that the upgrade request is not made
over a connection that is intended for multiple HTTP requests.

The Tcllib library **websocket** implements WebSockets, and makes the
necessary calls to commands in the **http** package.

There is currently no native Tcl client library for HTTP/2.

The **Upgrade** mechanism is not used to request TLS in web browsers,
because **http** and **https** are served over different ports. It is
used by protocols such as Internet Printing Protocol (IPP) that are
built on top of **http(s)** and use the same TCP port number for both
secure and insecure traffic.

In browsers, opportunistic encryption is instead implemented by the
**Upgrade-Insecure-Requests** client header. If a secure service is
available, the server response code is a 307 redirect, and the response
header **Location** specifies the target URL. The browser must call
**http::geturl** again in order to fetch this URL. See
https://w3c.github.io/webappsec-upgrade-insecure-requests/

# EXAMPLE

This example creates a procedure to copy a URL to a file while printing
a progress meter, and prints the meta-data associated with the URL.

    proc httpcopy { url file {chunk 4096} } {
        set out [open $file w]
        set token [::http::geturl $url -channel $out \
                -progress httpCopyProgress -blocksize $chunk]
        close $out

        # This ends the line started by httpCopyProgress
        puts stderr ""

        upvar #0 $token state
        set max 0
        foreach {name value} $state(meta) {
            if {[string length $name] > $max} {
                set max [string length $name]
            }
            if {[regexp -nocase ^location$ $name]} {
                # Handle URL redirects
                puts stderr "Location:$value"
                return [httpcopy [string trim $value] $file $chunk]
            }
        }
        incr max
        foreach {name value} $state(meta) {
            puts [format "%-*s %s" $max $name: $value]
        }

        return $token
    }
    proc httpCopyProgress {args} {
        puts -nonewline stderr .
        flush stderr
    }

# SEE ALSO

safe(n), socket(n), safesock(n)

# KEYWORDS

internet, security policy, socket, www

<!---
Copyright (c) 1995-1997 Sun Microsystems, Inc
Copyright (c) 1998-2000 Ajuba Solutions
Copyright (c) 2004 ActiveState Corporation
-->

