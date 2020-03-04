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

Returns:
--------
float
    Integral of func(x) over [a,b]
"""

    return np.sum(func(np.linspace(a,b,n))*(b-a)/n)
