# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:37:48 2015

@author: pedrogonzalez
"""

from matplotlib.pyplot import *
import numpy as np

xvals = np.linspace(0,10,25) # malla en x
yvals = 10*xvals - xvals**2  # ordenadas de una parabola
# Notese que hemos realizado calculos de tipo vectorial

figure()
plot(xvals,yvals,c="black",label=r"$y=10x-x^2$") 
# grafico de la parabola indicada
title("Grafica de la parabola  $y=10x-x^2$")
# show()    # muestra  las graficas

# generación de datos con ruido
ruido  = 10*(np.random.rand(25)-0.5)
yruido = yvals + ruido

# pongamos ahora marcas para cada uno de los ptos. con ruido
scatter(xvals,yruido,marker="D",c="black")
show() 

# fig = gcf()   # obtener la figura en curso
# fig.set_size_inches(6,4)  # tamaño opcional en pulgadas
# fig.savefig("grafica_parabola.png",dpi=300)
