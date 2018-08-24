# -*- coding: utf-8 -*-
from math import cos, exp, pi
from scipy.integrate import quad

# función que queremos integrar
def f(x):
    return cos(2*x*pi)
    
# ahora llamamos a "quad"  para integrar "f" entre 0 y 1
res, err = quad(f,0,1)

print("El resultado de la integración numérica es {:f} (+-{:g})" .format(res,err))        