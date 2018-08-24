# -*- coding: utf-8 -*-
from scipy.optimize import fsolve

def f(x):
    return x**3-2*x**2
    
x = fsolve(f,3)      # una de las raíces está en x=2.0

print "La raíz x es aproximadamente x = %21.19g" % x
print "El error cometido es exactamente %g." % (2-x)        