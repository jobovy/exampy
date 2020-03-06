# Tests of the integration routines in exampy.integrate
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
