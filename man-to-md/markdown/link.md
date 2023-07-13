\

# NAME

link - create link from command to method of object

# SYNOPSIS

    package require tcl::oo

    link methodName ?...?
    link {commandName methodName} ?...?

\

# DESCRIPTION

The **link** command is available within methods. It takes a series of
one or more method names (*methodName \...*) and/or pairs of command-
and method-name (**{***commandName methodName***}**) and makes the named
methods available as commands without requiring the explicit use of the
name of the object or the **my** command. The method does not need to
exist at the time that the link is made; if the link command is invoked
when the method does not exist, the standard **unknown** method handling
system is used.

The command name under which the method becomes available defaults to
the method name, except where explicitly specified through an
alias/method pair. Formally, every argument must be a list; if the list
has two elements, the first element is the name of the command to create
and the second element is the name of the method of the current object
to which the command links; otherwise, the name of the command and the
name of the method are the same string (the first element of the list).

If the name of the command is not a fully-qualified command name, it
will be resolved with respect to the current namespace (i.e., the object
namespace).

# EXAMPLES

This demonstrates linking a single method in various ways. First it
makes a simple link, then a renamed link, then an external link. Note
that the method itself is unexported, but that it can still be called
directly from outside the class.

    oo::class create ABC {
        method Foo {} {
            puts "This is Foo in [self]"
        }

        constructor {} {
            link Foo
            # The method Foo is now directly accessible as Foo here
            link {bar Foo}
            # The method Foo is now directly accessible as bar
            link {::ExternalCall Foo}
            # The method Foo is now directly accessible in the global
            # namespace as ExternalCall
        }

        method grill {} {
            puts "Step 1:"
            Foo
            puts "Step 2:"
            bar
        }
    }

    ABC create abc
    abc grill
            → Step 1:
            → This is Foo in ::abc
            → Step 2:
            → This is Foo in ::abc
    # Direct access via the linked command
    puts "Step 3:"; ExternalCall
            → Step 3:
            → This is Foo in ::abc

This example shows that multiple linked commands can be made in a call
to **link**, and that they can handle arguments.

    oo::class create Ex {
        constructor {} {
            link a b c
            # The methods a, b, and c (defined below) are all now
            # directly accessible within methods under their own names.
        }

        method a {} {
            puts "This is a"
        }
        method b {x} {
            puts "This is b($x)"
        }
        method c {y z} {
            puts "This is c($y,$z)"
        }

        method call {p q r} {
            a
            b $p
            c $q $r
        }
    }

    set o [Ex new]
    $o 3 5 7
            → This is a
            → This is b(3)
            → This is c(5,7)

# SEE ALSO

interp(n), my(n), oo::class(n), oo::define(n)

# KEYWORDS

command, method, object
