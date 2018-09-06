# -*- coding: utf-8 -*-
"""
Created on Sun Nov096 09:21:53 2016

@author: amcastro@ugr.es

Curso de Python

Alejandro E. Martínez Castro
Departamento de Mecánica de Estructuras e Ingeniería Hidráulica
"""


#==============================================================================
#  Ejemplo 2: Input y raw_input
# 
# En este cuaderno se verán las diferencias entre input() y raw_input
# 
# 
#==============================================================================
print "¿Cuál es tu nombre?"
nombre = input()
print("¡ Encantado de conocerte " + nombre + "!")
print "¿Cuál es tu edad?"
age = input()
print "¡ Por tanto, tienes " + str(age) + " años, " + nombre + "!"
print "---"*10
print "Observe"
print "El argumento \'age\' es de tipo", type(age)
print "Si lo multiplico por 2 obtengo", age * 2

# Observación: es necesario escribir las comillas para los caracteres
# La orden "input" interpreta el tipo de entrada

#==============================================================================
# Comparativa con raw_input()
#==============================================================================

print "¿Cuál es tu nombre (sin comillas)?"
nombre = raw_input()
print("¡ Encantado de conocerte " + nombre + "!")
print "¿Cuál es tu edad?"
age = raw_input()
print "¡ Por tanto, tienes " + str(age) + " años, " + nombre + "!"
print "---"*10
print "Observe"
print "El argumento \'age\' es de tipo", type(age)
print "Si lo multiplico por 2 obtengo", age * 2