# -*- coding: utf-8 -*-
import numpy as np
import numpy.linalg as LA
from sympy import *
from sympy.matrices import Matrix

A = Matrix(([-9,1,2,1],[1,2,-1,0],[1,1,0,1],[1,2,1,-3]))
n = np.shape(A)[0]
print A
print
print "matriz de orden"
print n

print

print "Polinomio característico y val. prop. calculados"
x = Symbol('x')
p = A.charpoly(x)
print p
print roots(p,x)

print "Polinomio característico como det(A-x*I)"
print
I = np.eye(n)    # es la matriz identidad de orden 4
print I
print
x = Symbol('x')
D = A - np.dot(x,I)
print D
g = det(D)
print roots(g,x)

z = np.zeros(n)
print z

