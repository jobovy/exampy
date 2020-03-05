# Tests of the basic math functions available in exampy's top level

def test_square_direct():
    # Direct test that the square works based on known solutions
    import math
    import exampy
    tol = 1e-10
    assert math.fabs(exampy.square(1.)-1.) < tol, \
        "exampy.square does not agree with known solution"
    assert math.fabs(exampy.square(2.)-4.) < tol, \
        "exampy.square does not agree with known solution"
    assert math.fabs(exampy.square(3.)-9.) < tol, \
        "exampy.square does not agree with known solution"
    return None
