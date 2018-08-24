# -*- coding: utf-8 -*-
import numpy as np
import scipy.interpolate
import pylab

def create_data(n):
    """ Dado un entero n, devuelve las coordenadas x e y de n puntos como un numpy.array """
    xmax = 5.
    x = np.linspace(0,xmax,n)
    y = -x**2
    
    # usando la orden random.normal podemos introducir cierto ruido blanco en los datos
    y = 1.5 * np.random.normal(size=len(x))
    return x,y
    
# programa principal
n = 10; x,y = create_data(n)

# usaremos una malla algo más fina y regular para el comando plot
xfine = np.linspace(0.1,4.9,n*100)

# ahora interpolaremos con funciones constantes a trozos (p=0)
y0 = scipy.interpolate.interp1d(x,y,kind='nearest')    

# ahora interpolaremos con funciones lineales a trozos (p=1)
y1 = scipy.interpolate.interp1d(x,y,kind='linear')           

# ahora interpolaremos con funciones cuadráticass a trozos (p=2)
y2 = scipy.interpolate.interp1d(x,y,kind='quadratic')    

pylab.plot(x,y,'o',label = 'datos')
pylab.plot(xfine,y0(xfine), label = 'constante')
pylab.plot(xfine,y1(xfine), label = 'lineal')
pylab.plot(xfine,y2(xfine), label = 'cuadratico')
pylab.legend()
pylab.xlabel('x')
pylab.savefig('interpolacion.pdf')
pylab.savefig('interpolacion.eps')
pylab.show()                                                                  