# -*- coding: utf-8 -*-
from math import cos, exp, pi
from scipy.integrate import quad

# función que queremos integrar
def f(x):
    return exp(cos(-2*x*pi))+3.2
    
# ahora llamamos a "quad"  para integrar "f" entre -2 y 2
res, err = quad(f,-2,2)

print("El resultado de la integración numérica es {:f} (+-{:g})" .format(res,err))        