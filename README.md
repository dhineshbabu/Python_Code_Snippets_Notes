### Generic Python Notes

<hr/>

#### Python Built-in Functions

This document provides an overview of Python's built-in functions. These functions are always available without needing to import any modules.

## A

- `abs()`: Return the absolute value of a number.
- `aiter()`: Return an asynchronous iterator for an async iterable.
- `all()`: Return `True` if all elements of the iterable are true (or if the iterable is empty).
- `anext()`: Return the next item from an asynchronous iterator.
- `any()`: Return `True` if any element of the iterable is true. If the iterable is empty, return `False`.
- `ascii()`: Return a string containing a printable representation of an object, but escape the non-ASCII characters in the string using `\x`, `\u`, or `\U` escapes.

## B

- `bin()`: Convert an integer number to a binary string prefixed with "0b".
- `bool()`: Convert a value to a Boolean, using the standard truth testing procedure.
- `breakpoint()`: Call to the built-in debugger (if any).
- `bytearray()`: Return a new array of bytes.
- `bytes()`: Return a new “bytes” object, which is an immutable sequence of integers in the range 0 <= x < 256.

## C

- `callable()`: Check if the object appears callable.
- `chr()`: Return the string representing a character whose Unicode code point is the integer.
- `classmethod()`: Return a class method for the function.
- `compile()`: Compile the source into a code or AST object.
- `complex()`: Create a complex number with the value real + imag*1j or convert a string or number to a complex number.

## D

- `delattr()`: Delete the named attribute from the object.
- `dict()`: Create a new dictionary.
- `dir()`: Try to return a list of valid attributes for the object.
- `divmod()`: Take two (non-complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder.

## E

- `enumerate()`: Return an enumerate object.
- `eval()`: Evaluate the given source in the context of globals and locals.
- `exec()`: Execute the dynamically created program, which is either a string or a code object.

## F

- `filter()`: Construct an iterator from those elements of iterable for which function returns true.
- `float()`: Convert a string or a number to floating point.
- `format()`: Return the formatted representation of the value controlled by the format specifier.
- `frozenset()`: Return a new frozenset object, optionally with elements taken from iterable.

## G

- `getattr()`: Return the value of the named attribute of object.
- `globals()`: Return a dictionary representing the current global symbol table.

## H

- `hasattr()`: Return `True` if the object has the named attribute, `False` otherwise.
- `hash()`: Return the hash value of the object (if it has one).
- `help()`: Invoke the built-in help system.
- `hex()`: Convert an integer number to a lowercase hexadecimal string prefixed with “0x”.

## I

- `id()`: Return the “identity” of an object.
- `input()`: Read a string from standard input.
- `int()`: Convert a number or string to an integer, or return 0 if no arguments are given.
- `isinstance()`: Check if an object is an instance of a class or of a subclass thereof.
- `issubclass()`: Check if a class is a subclass of another class.
- `iter()`: Return an iterator object.

## L

- `len()`: Return the length (the number of items) of an object.
- `list()`: Construct a list from an iterable.
- `locals()`: Update and return a dictionary representing the current local symbol table.

## M

- `map()`: Return an iterator that applies function to every item of iterable, yielding the results.
- `max()`: Return the largest item in an iterable or the largest of two or more arguments.
- `memoryview()`: Return a “memory view” object created from the given argument.
- `min()`: Return the smallest item in an iterable or the smallest of two or more arguments.

## N

- `next()`: Retrieve the next item from the iterator by calling its `__next__()` method.

## O

- `object()`: Return a new featureless object.
- `oct()`: Convert an integer number to an octal string prefixed with “0o”.
- `open()`: Open file and return a corresponding file object.
- `ord()`: Return an integer representing the Unicode code point of the given Unicode character.

## P

- `pow()`: Return base to the power exp; if mod is present, return base to the power exp, modulo mod.
- `print()`: Print objects to the text stream file, separated by sep and followed by end.
- `property()`: Return a property attribute.

## R

- `range()`: Return an object that produces a sequence of integers from start (inclusive) to stop (exclusive) by step.
- `repr()`: Return a string containing a printable representation of an object.
- `reversed()`: Return a reverse iterator.
- `round()`: Round a number to a given precision in decimal digits.

## S

- `set()`: Return a new set object, optionally with elements taken from iterable.
- `setattr()`: Set the value of the named attribute of object.
- `slice()`: Return a slice object representing the set of indices specified by range(start, stop, step).
- `sorted()`: Return a new sorted list from the items in iterable.
- `staticmethod()`: Return a static method for function.
- `str()`: Return a str version of object.
- `sum()`: Sum of a start value (default: 0) plus an iterable of numbers.
- `super()`: Return a proxy object that delegates method calls to a parent or sibling class of type.

## T

- `tuple()`: Return a tuple whose items are the same and in the same order as iterable's items.
- `type()`: With one argument, return the type of an object. With three arguments, return a new type object.

## V

- `vars()`: Return the `__dict__` attribute for a module, class, instance, or any other object with a `__dict__` attribute.

## Z

- `zip()`: Make an iterator that aggregates elements from each of the iterables.

## _

- `__import__()`: This function is called by the `import` statement.

