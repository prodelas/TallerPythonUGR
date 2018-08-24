# -*- coding: utf-8 -*-
from scipy import arange, cos, exp
from scipy.optimize import fmin
import pylab

def f(x):
    return cos(x)-3*exp(-(x-0.2)**2)
    
# Ahora vamos a encontrar el mínimo de f(x),
# empezando desde x1=1.0 y x2=2.0, respectivamente.
x1   = 1.0 ; x2  = 2.0
min1 = fmin(f,x1)
print "Empezando a buscar en x=1.  se encuentra el mínimo ",min1
min2 = fmin(f,x2)
print "Empezando a buscar en x=2.  se encuentra el mínimo ",min2

# Ahora dibujamos la función
x = arange(-10,10,0.1)
y = f(x)

pylab.plot(x,y,label='$\cos(x)-3e^{-(x-0.2)^2}$')
pylab.xlabel('x'); pylab.grid()
pylab.axis([-5,5,-2.2,0.5])

# Ahora añadimos min1 al gráfico
pylab.plot(min1,f(min1),'vr',label='primer minimo')

# Ahora añadimos x1 al gráfico
pylab.plot(x1,f(x1),'or',label='x1')

# Ahora añadimos min2 al gráfico
pylab.plot(min2,f(min2),'vg',label='segundo minimo')

# Ahora añadimos x1 al gráfico
pylab.plot(x2,f(x2),'og',label='x2')
pylab.legend(loc='lower left')
pylab.savefig('fmins.pdf')
pylab.show()