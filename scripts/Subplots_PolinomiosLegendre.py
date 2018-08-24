# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:08:34 2015

@author: pedrogonzalez
"""

from scipy.special import *
from matplotlib.pyplot import *
import numpy as np

xvals = np.linspace(-1,1,200)

fig, AX = subplots(nrows=2,ncols=3,sharex=True,sharey=True)

legendre=np.array([list(lpn(6,x)[0]) for x in xvals]).T

i = 1
for fila in AX:
    for ax in fila:
        yvals = legendre[i]
        ax.plot(xvals,yvals,c="black")
        ax.axhline(0.0,c="black")
        ax.axvline(0.0,c="black")
        ax.set_title("Legendre_P"+str(i))
        i+=1
 
show()