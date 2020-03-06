# Tests of the integration routines in exampy.integrate
import pytest
import numpy as np
import exampy.integrate

def test_simps_against_riemann():
    # Test that simps and riemann give approximately the same answer 
    # for complicated functions
    complicated_func= lambda x: x*np.cos(x**2)/(1+np.exp(-x))
    tol= 1e-4
    n_int= 1000
    assert np.fabs(exampy.integrate.simps(complicated_func,0,1,n=n_int)
                   -exampy.integrate.riemann(complicated_func,0,1,n=n_int)) \
                   < tol, \
                   """exampy.integrate.simps gives a different result from """\
                   """exampy.integrate.riemann for a complicated function"""
    return None

def test_simps_against_scipy():
    # Test that exampy.integrate.simps integration agrees with 
    # scipy.integrate.quad
    from scipy import integrate as sc_integrate
    complicated_func= lambda x: x*np.cos(x**2)/(1+np.exp(-x))
    tol= 1e-14
    n_int= 1000
    assert np.fabs(exampy.integrate.simps(complicated_func,0,1,n=n_int)
                   -sc_integrate.quad(complicated_func,0,1)[0])\
                   < tol, \
                   """exampy.integrate.simps gives a different result from """\
                   """scipy.integrate.quad for a complicated function"""
    return None

def test_simps_typerror():
    # Test that exampy.integrate.simps properly raises a TypeError
    # when called with a non-array function
    import math
    import pytest
    with pytest.raises(TypeError,match="Provided func needs to be callable on arrays of inputs") as excinfo:
        out= exampy.integrate.simps(lambda x: math.exp(x),0,1)
    return None

@pytest.mark.xfail(strict=True,raises=TypeError)
def test_simps_scalarfunc():
    # Test that exampy.integrate.simps works even when called with a 
    # non-array function
    import math
    tol= 1e-7
    assert np.fabs(exampy.integrate.simps(lambda x: math.exp(x),0,1)
                   -(math.e-1.)) < tol, \
                   """exampy.integrate.simps does not work for scalar-input"""\
                   """functions"""
    return None
    
