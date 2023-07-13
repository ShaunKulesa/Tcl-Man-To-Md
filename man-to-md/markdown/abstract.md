\

# NAME

oo::abstract - a class that does not allow direct instances of itself

# SYNOPSIS

    package require tcl::oo

    oo::abstract method ?arg ...?

# CLASS HIERARCHY

    oo::object
       → oo::class
           → oo::abstract

\

# DESCRIPTION

Abstract classes are classes that can contain definitions, but which
cannot be directly manufactured; they are intended to only ever be
inherited from and instantiated indirectly. The characteristic methods
of **oo::class** (**create** and **new**) are not exported by an
instance of **oo::abstract**.

Note that **oo::abstract** is not itself an instance of
**oo::abstract**.

## CONSTRUCTOR

The **oo::abstract** class does not define an explicit constructor; this
means that it is effectively the same as the constructor of the
**oo::class** class.

## DESTRUCTOR

The **oo::abstract** class does not define an explicit destructor;
destroying an instance of it is just like destroying an ordinary class
(and will destroy all its subclasses).

## EXPORTED METHODS

The **oo::abstract** class defines no new exported methods.

## NON-EXPORTED METHODS

The **oo::abstract** class explicitly states that **create**,
**createWithNamespace**, and **new** are unexported.

# EXAMPLES

This example defines a simple class hierarchy and creates a new instance
of it. It then invokes a method of the object before destroying the
hierarchy and showing that the destruction is transitive.

    oo::abstract create fruit {
        method eat {} {
            puts "yummy!"
        }
    }
    oo::class create banana {
        superclass fruit
        method peel {} {
            puts "skin now off"
        }
    }
    set b [banana new]
    $b peel              → prints 'skin now off'
    $b eat               → prints 'yummy!'
    set f [fruit new]    → error 'unknown method "new"...'

# SEE ALSO

oo::define(n), oo::object(n)

# KEYWORDS

abstract class, class, metaclass, object
