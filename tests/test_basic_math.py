# Tests of the basic math functions available in exampy's top level
import math
import exampy

def test_square_direct():
    # Direct test that the square works based on known solutions
    tol = 1e-10
    assert math.fabs(exampy.square(1.)-1.) < tol, \
        "exampy.square does not agree with known solution"
    assert math.fabs(exampy.square(2.)-4.) < tol, \
        "exampy.square does not agree with known solution"
    assert math.fabs(exampy.square(3.)-9.) < tol, \
        "exampy.square does not agree with known solution"
    return None

def test_cube_oddfunction():
    # Test of the cube function by checking that it is an odd function
    tol= 1e-10
    for nn in range(1,10):
        assert math.fabs(exampy.cube(nn)+exampy.cube(-nn)) < tol, \
            "exampy.cube is not an odd function"
    return None

     
