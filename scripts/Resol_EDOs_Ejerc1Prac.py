# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import numpy as N

def f(y,t):
    """ aquí introducimos el segundo miembro de la EDO a integrar numéricamente, dy/dt = f(y,t) """
    return 3.*t*t+2.-y*t/(1.+39*t*t)

a  = 1.                        # extremo izqdo. del intervalo de integración
b  = 2.                        # extremo dcho. del intervalo de integración
y0 = 4.875                     # valor inicial
n  = 50
h  = (b-a)/n                      # paso espacial
 

y1 = y0+h*f(y0,a)
print y1
y2 = y1+h*f(y1,a+h)
print y2

aprox = [y0]
for i in range(n):
    y1 = y0+h*f(y0,a+i*h)
    y0 = y1
    aprox.append(y1)
    
print aprox

t = N.arange(a,b,h)            # nodos en los que aproximar la solución
y = odeint(f,y0,t)             # cálculo aproximado de la solución en dichos nodos

import pylab                  # para poder dibujar la solución
pylab.plot(t,y)
pylab.xlabel('t'); pylab.ylabel('y(t)')
pylab.show()

# from sympy import Symbol, dsolve, Function, Derivative, Eq
# y = Function("y")
# x = Symbol('x')
# y_ = Derivative(y(t),t)
# print dsolve(y_ - f(y(t),t))