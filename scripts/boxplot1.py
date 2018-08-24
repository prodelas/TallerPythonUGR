# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 01:28:25 2015

@author: pedrogonzalez
"""

import numpy as np
from matplotlib.pyplot import *
datos = np.random.random([100,10])
figure()
boxplot(datos)
xticks(range(1,11),list("ABCDEFGHIJ"))
show()