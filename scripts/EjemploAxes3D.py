# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:52:05 2015

@author: Pedro
"""

# from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure(figsize=(14,6))

# `ax` es una instancia de los ejes 3D ya que la palabra clave proyection='3d' 
# como argumento de add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# superficie con degradado de color y barra de colores
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)