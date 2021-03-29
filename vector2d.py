# example from the Python Data Model chapter of Fluent Python by Luciano Ramalho
import math

# A basic vector API

"""
vector2d.py: a simplistic class demonstrating some special methods

For demonstration purposes as it lacks proper error handling

Supports the following actions:

Addition::
    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

Absolute value::
    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

Scalar multiplication::
    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0

"""

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __repr__ is called by the repr build-in to get the string representation of the object for inspection
    # If we did not implement __repr__, vector instances would be shown in the console like
    # <Vector object at 0x10e100080>
    # uses !r to get the standard representation of the attributes to be displayed. Difference between showing
    # Vector(1, 2) and Vector('1', '2')
    # contrast with __str__, which is implicitly used by the print function. __str__ should return string
    # suitable for display to end users.
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r}'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    # determines whether a value x is truthy or falsy. Pythons applies bool(x), which returns either True or False
    # returns False if the magnitude of the vector is zero. True otherwise. We convert the magnitude to a Boolean using
    # bool(abs(self)), because __bool__ is expected to return a boolean.
    def __bool__(self):
        return bool(abs(self))

    # Faster implementation that's harder to read. Avoids the trip through abs, __abs__, the squares and square root.
    # def __bool__(self):
    #    return bool(self.x or self.y)


    # add and scalar multiplication. Implements two operators, + and *. Both methods create and return a new instance
    # of Vector, and do not modify either operand -- self or other are read. This is the expected behavior
    # of infix operators: to create new objects and not touch their operands.
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# six special methods have been implemented. These are not called directly. The Python interpreter is the only frequent
# caller of most special methods.