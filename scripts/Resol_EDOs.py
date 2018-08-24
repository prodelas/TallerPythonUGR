# -*- coding: utf-8 -*-
from scipy.integrate import odeint
import numpy as N

def f(y,t):
    """ aquí introducimos el segundo miembro de la EDO a integrar numéricamente, dy/dt = f(y,t) """
    return -2*y*t
    
a  = 0    # extremo izqdo. del intervalo de integración
b  = 2    # extremo dcho. del intervalo de integración
y0 = 1    # valor inicial

t = N.arange(a,b,0.01)   # nodos en los que aproximar la solución
y = odeint(f,y0,t)       # cálculo aproximado de la solución en dichos nodos

import pylab            # para poder dibujar la solución
pylab.plot(t,y)
pylab.xlabel('t'); pylab.ylabel('y(t)')
pylab.show()