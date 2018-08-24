# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import curve_fit

def f(x,a,b,c):
    """ Ajusta la función y = f(x,p) con parámetros p = (a,b,c). """
    return a * np.exp(-b*x)+c
    
# creando datos falsos
x = np.linspace(0,4,50)
y = f(x,2.5,1.3,0.5)  # f(x,a=2.5,b=1.3,c=0.5)


# ahora añadimos ruido
yi = y + 0.2*np.random.normal(size=len(x))

# ahora llamamos a la función de ajuste de curvas
popt,prov = curve_fit(f,x,yi)
a,b,c = popt
print "Los parámetros óptimos son a=%g, b=%g y c=%g" % (a,b,c)

# Dibujando los resultados
import pylab
yajustada = f(x,*popt)  # equivalente a f(x, popt[0],popt[1],popt[2]) 
pylab.plot(x,yi,'o',label='datos $y_i$')
pylab.plot(x,yajustada,'-',label='$f(x_i)$ ajustada')
pylab.xlabel('x'); pylab.legend()
pylab.savefig('curva_ajustada.eps')     
pylab.savefig('curva_ajustada.pdf')          