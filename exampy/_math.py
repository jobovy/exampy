
def square(x):
    """The square of a number

Parameters
----------
x: float
    Number to square

Returns
-------
float
    Square of x
"""
    return x**2.

def cube(x):
    """The cube of a number

Calculates and returns the cube of any floating-point number;
note that, as currently written, the function also works for
arrays of floats, ints, arrays of ints, and more generally,
any number or array of numbers.

Parameters
----------
x: float
    Number to cube

Returns
-------
float
    Cube of x

Raises
------
No exceptions are raised.

See Also
--------
exampy.square: Square of a number
exampy.Pow: a number raised to an arbitrary power

Notes
-----
Implements the standard cube function

.. math:: f(x) = x^3

History:

2020-03-04: First implementation - Bovy (UofT)


References
----------
.. [1] A. Mathematician, "x to the p-th power: squares, cubes, and their 
   general form," J. Basic Math., vol. 2, pp. 2-3, 1864.

"""
    return x**3.

class Pow(object):
    """A class to compute the power of a number"""
    def __init__(self,p=2.):
        """Initialize a PowClass instance

Parameters
----------
p: float, optional
    Power to raise x to
"""
        self._p= p

    def __call__(self,x):
        """Evaluate x^p

Parameters
----------
x: float
    Number to raise to the power p

Returns
-------
float
    x^p
"""
        return x**self._p
