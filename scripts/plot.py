Python 2.7.5 (default, May 15 2013, 22:43:36) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1+1
2
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> x = np.arange(-3.14, 3.14, 0.01)
>>> y = np.sin(x)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x046E1790>]
>>> plt.show()
