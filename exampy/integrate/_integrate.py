import numpy as np

def riemann(func,a,b,n=10):
    """A simple Riemann-sum approximation to the integral of a function

Parameters
----------
func: callable
    Function to integrate, should be a function of one parameter
a: float
    Lower limit of the integration range
b: float
    Upper limit of the integration range
n: int, optional
    Number of intervals to split [a,b] into for the Riemann sum

Returns
-------
float
    Integral of func(x) over [a,b]
"""
    return np.sum(func(np.linspace(a,b,n))*(b-a)/n)

def simps(func,a,b,n=10):
    """Integrate a function using Simpson's rule

Parameters
----------
func: callable
    Function to integrate, should be a function of one parameter
a: float
    Lower limit of the integration range
b: float
    Upper limit of the integration range
n: int, optional
    Number of major intervals to split [a,b] into for the Simpson rule

Returns
-------
float
    Integral of func(x) over [a,b]

Notes
-----
Applies Simpson's rule as

.. math::

    \\int_a^b \\mathrm{d}x f(x) \\approx \\frac{(b-a)}{6n}\\,\\left[f(a)+4f(a+h/2)+2f(a+h)+4f(a+3h/2)+
    
    \ldots+2f(b-h)+4f(b-h/2)+f(b)\\right]

See Also
--------
exampy.integrate.riemann: Integrate a function with a simple Riemann sum
"""
    try:
        return (2.*np.sum(func(np.linspace(a,b,n+1)))
                -func(a)-func(b) # adjust double-counted first and last
                +4.*np.sum(func(np.linspace(a+(b-a)/n/2,b-(b-a)/n/2,n))))\
                *(b-a)/n/6.
    except TypeError:
        raise TypeError("Provided func needs to be callable on arrays of inputs")
