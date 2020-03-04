import numpy as np

def riemann(func,a,b,n=10):
    return np.sum(func(np.linspace(a,b,n))*(b-a)/n)
