# -*- coding: utf-8 -*-
import numpy as np
import numpy.random
import numpy.linalg as LA
from sympy import *
from sympy.matrices import Matrix

A = np.random.rand(4,4)
x = np.random.rand(4)
b = np.dot(A,x)

v = np.array([0,0.5,1,1.5])
w = np.arange(0,2,0.5)
z = np.zeros(4)

print v
print w
print z
print np.sin(v)
print
print b
print
print LA.solve(A,b)
print x