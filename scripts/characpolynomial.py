# import numpy as np
from sympy import *
# import numpy.linalg as LA
from sympy.matrices import Matrix
x = Symbol('x')
A = Matrix(([-5,-5,-9],[8,9,18],[-2,-3,-7]))
# list_eye = lambda n: numpy.eye(n).tolist()
p = A.charpoly(x)
print p
print roots(p,x)
print
# evals, evecs = np.linalg.eig(A)
# idx = evals.argsort()
# evals = evals(idx)
# evecs = evecs[:,idx]