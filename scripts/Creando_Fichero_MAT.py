import scipy.io
import numpy as np

# Ahora creamos dos arrays con numpy
a = np.linspace(0,50,11)
b = np.ones((4,4))

# y los guardamos como ficheros mat, compatibles con MATLAB y OCTAVE
# usando un diccionario concreto para la orden "savemat"
tmp_d = {'a':a, 'b':b}
scipy.io.savemat('datos.mat',tmp_d)
