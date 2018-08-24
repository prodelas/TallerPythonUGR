# -*- coding: utf-8 -*-
import numpy as np
import numpy.linalg as LA
from sympy import *
from sympy.matrices import Matrix
A =[[-9,1,2,1.],[1,2,-1,0],[1,1,0,1],[1,2,1,-3]]
# A = Matrix(([-9,1,2,1.],[1,2,-1,0],[1,1,0,1],[1,2,1,-3]))
n = np.shape(A)[0]
print "Cálculo de los valores y vectores propios de la matriz "
print A
print
print "matriz de orden"
print n
print
print "usando la orden eig() del paquete numpy.linalg "
val_prop, vec_prop = LA.eig(A)
print "Valores propios: "
print(val_prop)
print " y vectores propios: "
print(vec_prop)
print "Usando ahora el polinomio característico los valores prop. calculados"
A = Matrix(A)
x = Symbol('x')
p = Matrix(A).charpoly(x)
print p
print roots(p,x)
print
print "Otra forma de obtener el polinomio característico como det(A-x*I)"
print
I = np.eye(n)    # es la matriz identidad de orden 4
# print I
print
x = Symbol('x')
D = A - np.dot(x,I)
print D
g = det(D)
print roots(g,x)
print
z = np.array([1]*n).transpose()
print "Ahora emplearemos el conocido como método de las potencias"
niter = 15
print "Se realizarán ", niter, " iteraciones"
print "con vector inicial", z
print
aprox_valp = []
aprox_vecp = []
for i in range(niter):
    y = A.dot(z)
#    print y[0]/z[0]
    aprox_valp.append(y[0]/z[0])
    aprox_vecp.append(y)
    z = y
print aprox_valp
print
print aprox_vecp
print
print "Ahora realizando la preceptiva normalización"
aprox_valp = []
aprox_vecp = []
y = A.dot(z)
for i in range(niter):
    m = max(np.abs(y))
#    print "el máximo alcanzado es ",  m
#    print
    ind = [i for i, j in enumerate(np.abs(y)) if j == m][0]
#    print "El valor máximo se tiene en el índice ", ind
    z = np.dot(1/y[ind],y)
    y = A.dot(z)
    aprox_valp.append(y[ind])
    aprox_vecp.append(y)
print
print aprox_valp
print
print aprox_vecp
print

print "Usando ahora los denominados cocientes de Rayleigh para la matriz"
print
M = [[4., 1., 0., 0., 0., 0.], [1., 4., 1., 0., 0., 0.],
[0., 1., 4., 1., 0., 0.], [0., 0., 1., 4., 1., 0.],
[0., 0., 0., 1., 4., 1.], [0., 0., 0., 0., 1., 4.]]
val_prop, vec_prop = LA.eig(M)
print M    
print 
# A partir de aquí es mejor redefinir M como un objeto Matrix
M = Matrix(M)
n = np.shape(M)[0]
z = Matrix([1]*n)
aprox_valp = []
aprox_vecp = []
y = Matrix(M.dot(z))
for i in range(niter):
    z = y
    y = Matrix(M.dot(z))
    aprox_valp.append(np.dot(1/(z.dot(z)),y.dot(z)))
    aprox_vecp.append(list(y/sqrt(y.dot(y))))
print
print aprox_valp
print
print aprox_vecp
print
print "Aproximación final del valor propio dominante y vector propio asociado"
print aprox_valp[-1]
print
print aprox_vecp[-1]
print
print "y comparémoslo con lo obtenido mediante la orden eig() "
print " del paquete numpy.linalg "
print
print "Valores propios: "
print(val_prop)
print " y vectores propios: "
print(vec_prop)