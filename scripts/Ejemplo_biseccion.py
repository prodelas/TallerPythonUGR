# -*- coding: utf-8 -*-
from scipy.optimize import bisect

def f(x):
    """ devuelve f(x) = x^3-2x^2, que tiene como raíces x=0 (doble) y x=2 """
    return x**3-2*x**2
    
# aquí empieza realmente el programa principal
x = bisect(f,1.5,3,xtol=1e-6)

print  "La raíz x buscada es aproximadamente x=%14.12g,\n"\
       "el error es inferior a 1e-6." % (x)
print  "El error cometido es exactamente %g." % (2-x)        