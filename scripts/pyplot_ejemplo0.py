# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:37:48 2015

@author: pedrogonzalez
"""

from matplotlib.pyplot import *
import numpy as np

x  = np.linspace(0,2*np.pi,200)
y1 = np.cos(x)
y2 = np.sin(x)

figure()
plot(x,y1)    # para realizar una gráfica de la función coseno

# figure()
plot(x,y2)    # para realizar una gráfica de la función seno
axes().set_aspect("equal") # fijar el mismo ratio entre ambos ejes
xlim(0,2*np.pi) # indicamos los límites en el eje Ox
xticks([x for x in np.arange(0,2.5*np.pi,np.pi/2)],
        [0,r"$\frac{\pi}{2}}$",r"$\pi$",r"3$\pi$/2"])
        # marcas en el eje Ox
yticks([-1,0,1],["-1","0","1"]) # marcas en el eje Oy
show()    # muestra  las gráficas