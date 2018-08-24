import numpy
from sympy import *
from sympy.matrices import Matrix
x = Symbol('x')
A = Matrix(([-5,-5,-9],[8,9,18],[-2,-3,-7]))
# list_eye = lambda n: numpy.eye(n).tolist()
p = A.charpoly(x)
print roots(p,x)