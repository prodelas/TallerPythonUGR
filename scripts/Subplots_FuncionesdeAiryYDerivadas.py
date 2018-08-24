# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:08:34 2015

@author: pedrogonzalez
"""

from scipy.special import *
from matplotlib.pyplot import *
import numpy as np

xvals = np.linspace(-15,3.0,200)
airyvals = np.array([airy(x) for x in xvals])

ai = (airyvals.T)[0]
dai = (airyvals.T)[1]
bi = (airyvals.T)[2]
dbi = (airyvals.T)[3]

# fig, ((ax1,ax2),(ax3,ax4) )= subplots(nrows=2,ncols=2)
fig, ((ax1,ax3),(ax2,ax4) )= subplots(nrows=2,ncols=2, sharex=True,  sharey=True)

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
# show()

# fig, (ax1,ax2) = subplots(nrows=2,ncols=1,sharex=True)

ax3.plot(xvals,dai,color="black")
ax3.set_ylim(-.75,.75)
ax3.set_title("Derivada funcion_Airy_Ai")
ax3.axhline(0.0,color="black")
ax3.axvline(0.0,color="black")

ax4.plot(xvals,dbi,color="black")
ax4.set_ylim(-.75,.75)
ax4.set_title("Derivada funcion_Airy_Bi")
ax4.axhline(0.0,color="black")
ax4.axvline(0.0,color="black")

show()