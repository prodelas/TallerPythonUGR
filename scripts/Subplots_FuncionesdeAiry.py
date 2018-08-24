# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:08:34 2015

@author: pedrogonzalez
"""

from scipy.special import airy
from matplotlib.pyplot import *
import numpy as np

xvals = np.linspace(-15,3.0,200)
airyvals = airy(xvals) # np.array([airy(x) for x in xvals])

ai = (airyvals)[0]
dai = (airyvals)[1]
bi = (airyvals)[2]
dbi = (airyvals)[3]

fig, (ax1,ax2) = subplots(nrows=2,ncols=1,sharex=True)

ax1.plot(xvals,ai,color="black")
ax1.set_ylim(-.75,.75)
ax1.set_title("Funcion_Airy_Ai")
ax1.axhline(0.0,color="black")
ax1.axvline(0.0,color="black")

ax2.plot(xvals,bi,color="black")
ax2.set_ylim(-.75,.75)
ax2.set_title("Funcion_Airy_Bi")
ax2.axhline(0.0,color="black")
ax2.axvline(0.0,color="black")
show()

fig, (ax1,ax2) = subplots(nrows=2,ncols=1,sharex=True)

ax1.plot(xvals,dai,color="black")
ax1.set_ylim(-.75,.75)
ax1.set_title("Derivada funcion_Airy_Ai")
ax1.axhline(0.0,color="black")
ax1.axvline(0.0,color="black")

ax2.plot(xvals,dbi,color="black")
ax2.set_ylim(-.75,.75)
ax2.set_title("Derivada funcion_Airy_Bi")
ax2.axhline(0.0,color="black")
ax2.axvline(0.0,color="black")

show()