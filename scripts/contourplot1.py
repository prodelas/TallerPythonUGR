# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:31:31 2015

@author: pedrogonzalez
"""

from matplotlib.pyplot import *
import numpy as np
from math import *

A = [[x+cos(.5+x*y)+cos(.5*y)*cos(.5*x)
     for y in np.linspace(0,6,100)]
     for x in np.linspace(0,6,100)]
        
axis("equal")
axis([0,100,0,100])
xticks([])
yticks([])

cp = contour(A, colors="k", levels = np.linspace(0,6,7))
clabel(cp,fontsize=9,fmt="%.f")

cp = contour(A, levels = np.linspace(-1,7,9))
colorbar(cp)