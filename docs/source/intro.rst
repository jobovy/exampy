Introduction
============

``exampy`` is an example Python package that contains some very basic math
functions. As an example, we can compute the square of a number as::

	   >>> import exampy
	   >>> exampy.square(3.)
	   # 9.

Similarly, we can compute the cube of a number:

.. code-block:: python

   >>> exampy.cube(3.)
   # 27.

A general method for raising a number to a given power is given by the
``Pow`` class. For example, to get the fourth power of 3, do::

    >>> po= exampy.Pow(p=4.)
    >>> po(3.)
    # 81.

``exampy`` also includes a simple method for integrating a function,
in the ``exampy.integrate`` submodule. This submodule contains the
function ``riemann`` that approximates the integral of any
one-parameter function as a Riemann sum. ``riemann`` takes as input
(i) the function to integrate, (ii) the integration range's lower
limit and (iii) the upper limit, and (iv) optionally, the number of
intervals to divide the integration range in. For example, the
integrate the square function of the range [0,1], do::

	  >>> from exampy import integrate
	  >>> integrate.riemann(exampy.square,0,1)
	  # 0.35185185185185186

If we increase the number of intervals from the default (which is 10),
we get a better approximation to the correct result (which is 1/3)::

   >>> integrate.riemann(exampy.square,0,1,n=1000)
   # 0.33350016683350014

