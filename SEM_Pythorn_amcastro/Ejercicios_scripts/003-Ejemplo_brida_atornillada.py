# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 07:53:37 2015

         Alejandro Martínez Castro (amcastro@ugr.es),

Análisis tensodeformacional de una brida analizada mediante
el Método de los Elementos Finitos

"""
from __future__ import division   #para no tener problemas de división entera
import csv  # Para importar el fichero en formato .cvs (comma-separated values)
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
# Lectura del "fichero datos.csv", que contiene en formato
# .csv (Comma-separated values) los resultados de postproceso en una línea
# vertical particular
#
#==============================================================================
reader = csv.DictReader(open('datos.csv'), delimiter=',', quotechar='|')


result = {} # Esta variable contedrá un "diccionario" (recurso Python)

for row in reader: 
    
    for column, value in row.items():
        result.setdefault(column, []).append(value)

fieldnames = result.keys() # Contiene las etiquetas

# Verifique el contenido de "result" para ver lo que es un diccionario
# Observe la variable en Spyder


# Abscisa "x·. La lista que está en el diccionario en "arc_length" se 
# convierte aquí en número de punto flotante (por defecto son caracteres)
arco = result['"arc_length"']
arco = np.array(arco).astype('float')

# Ahora observe el contenido de "arco"

#==============================================================================
# TENSIONES
#==============================================================================

#==============================================================================
# Tensiones del tensor de tensiones
#==============================================================================
sigma_xx = np.array(result['"RESU_SIGM_NOEU:0"']).astype('float')
sigma_yy = np.array(result['"RESU_SIGM_NOEU:1"']).astype('float')
sigma_zz = np.array(result['"RESU_SIGM_NOEU:2"']).astype('float')
sigma_xy = np.array(result['"RESU_SIGM_NOEU:3"']).astype('float')
sigma_xz = np.array(result['"RESU_SIGM_NOEU:4"']).astype('float')
sigma_yz = np.array(result['"RESU_SIGM_NOEU:5"']).astype('float')
#==============================================================================
# DEFORMACIONES
#==============================================================================

eps_xx = np.array(result['"RESU_EPSI_NOEU:0"']).astype('float')
eps_yy = np.array(result['"RESU_EPSI_NOEU:1"']).astype('float')
eps_zz = np.array(result['"RESU_EPSI_NOEU:2"']).astype('float')
eps_xy = np.array(result['"RESU_EPSI_NOEU:3"']).astype('float')
eps_xz = np.array(result['"RESU_EPSI_NOEU:4"']).astype('float')
eps_yz = np.array(result['"RESU_EPSI_NOEU:5"']).astype('float')
#==============================================================================
# Figuras TENSIONES
#==============================================================================

#==============================================================================
# Figura tensiones sigma_nx, sigma_ny, sigma_nz
#==============================================================================

plt.figure('Tensiones normales')
plt.title('Tensiones normales')
line, = plt.plot(arco , sigma_xx, label = r"$\sigma_{nx} $", linewidth = 2.0)
line, = plt.plot(arco , sigma_yy, label = r"$\sigma_{ny} $", linewidth = 2.0)
line, = plt.plot(arco , sigma_zz, label = r"$\sigma_{nz} $", linewidth = 2.0)


plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'MPa')                          #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final

plt.figure('Tensiones tangenciales')
plt.title('Tensiones tangenciales')
line, = plt.plot(arco , sigma_xy, label = r"$\tau_{xy} $", linewidth = 2.0)
line, = plt.plot(arco , sigma_xz, label = r"$\tau_{xz} $", linewidth = 2.0)
line, = plt.plot(arco , sigma_yz, label = r"$\tau_{yz} $", linewidth = 2.0)


plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'MPa')                          #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final

#==============================================================================
# Figura Deformaciones eps_xx, eps_ny, eps_nz
#==============================================================================
plt.figure('Deformaciones normales')
plt.title( 'Deformaciones normales')
line, = plt.plot(arco , eps_xx, label = r"$\epsilon_{nx} $", linewidth = 2.0)
line, = plt.plot(arco , eps_yy, label = r"$\epsilon_{ny} $", linewidth = 2.0)
line, = plt.plot(arco , eps_zz, label = r"$\epsilon_{nz} $", linewidth = 2.0)


plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'deformation')                          #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final

#==============================================================================
# Figura Deformaciones eps_xx, eps_ny, eps_nz
#==============================================================================
plt.figure('Deformaciones tangenciales')
plt.title( 'Deformaciones tangenciales')
line, = plt.plot(arco , eps_xy, label = r"$\epsilon_{xy} $", linewidth = 2.0)
line, = plt.plot(arco , eps_xz, label = r"$\epsilon_{xz} $", linewidth = 2.0)
line, = plt.plot(arco , eps_yz, label = r"$\epsilon_{yz} $", linewidth = 2.0)


plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'deformation')                          #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final


#==============================================================================
# Verificación tension Von Mises
#==============================================================================

# Definimos una función que calcula la tensión de VMises sobre el tensor no diagonalizado

def von_mises(sxx, syy, szz, sxy, sxz, syz):
    sigma = sxx**2. + syy**2. + szz**2. 
    sigma -= (sxx*syy + syy*szz + sxx*szz)
    sigma += 3. * (sxy**2. + sxz**2. + syz**2.)
    sigma = np.sqrt(sigma)
    return sigma

# Calculamos la tensión de Von Mises en los puntos de la linea usando la función anterior

s_vm_calculada = von_mises(sigma_xx, sigma_yy, sigma_zz, sigma_xy, sigma_xz, sigma_yz)

# Ahora comparamos la tensión calculada con la que se ha obtenido con Salome-Meca

sigma_vm = np.array(result['"RESU_SIEQ_NOEU:0"']).astype('float')

plt.figure('Tension de Von Mises')
plt.title( 'Tension de Von Mises')
line, = plt.plot(arco , s_vm_calculada, label = r"Calculada", linewidth = 2.0)
line, = plt.plot(arco , sigma_vm, label = r"Salome-Meca", linewidth = 2.0)

plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'MPa')                          #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final

#==============================================================================
# Deformaciones normales a partir de tensiones
#==============================================================================

elast = 210000.0 # Modulo de elasticidad
nu = 0.3

epsilon_xx_calc = 1./elast * (sigma_xx - nu * (sigma_yy + sigma_zz))


plt.figure('Comparativa deformacion epsilon_xx')
plt.title( 'Comparativa deformacion epsilon_xx')
line, = plt.plot(arco ,epsilon_xx_calc , label = r"Calculada ", linewidth = 2.0)
line, = plt.plot(arco ,eps_xx, label = r"Salome-Meca", linewidth = 2.0)

plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'strain')                       #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final

#==============================================================================
# Deformaciones angulares
#==============================================================================

modg = elast / (2.*(1+nu))

epsilon_xz_calc = 1 / 2. * sigma_xz / modg


plt.figure('Comparativa deformacion epsilon_xz')
plt.title( 'Comparativa deformacion epsilon_xz')
line, = plt.plot(arco ,epsilon_xz_calc , label = r"Calculada ", linewidth = 2.0)
line, = plt.plot(arco ,eps_xz, label = r"Salome-Meca", linewidth = 2.0)

plt.xlabel(r'mm')                           #Etiqueta del eje x
plt.ylabel(r'strain')                       #Etiqueta del eje y

plt.legend(loc=0)  # Mostrar leyenda en posición óptima (loc=0)
plt.show()         # Mostrar figura final
