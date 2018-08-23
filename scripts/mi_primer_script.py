import matplotlib.pyplot as plt
     
print("¡Hola gente del taller de Python!")
print("¿Cuántos de vosotros sois completamente novatos con Python?")
nnovatos = input()
nnovatos = int(nnovatos)

if nnovatos > 20:
    print("¡¡Ufff, eso es un montón!! Espero que aprendáis mucho hoy... \n")


print("¿Cuántos de vosotros ya os habéis iniciado un poquito en Python?")
niniciados = input()
niniciados = int(niniciados)
print("Bueno, ¡siempre hay algo nuevo que aprender!\n")


print("¿Cuántos de vosotros ya sabéis bastante de Python?")
navanzados = input()
navanzados  = int(navanzados)
print("Bueno, en todo caso ¡espero que también aprendáis algo nuevo hoy!\n")

print("Y por último, ¿cuántos de vosotros ya sois casi unos expertos en Python?")
nexpertos = input()
nexpertos  = int(nexpertos)
if nexpertos > 2:
    print("Bueno,¡en realidad no se qué hacéis vosotros aquí! \n")


# Datos a mostrar
labels = 'Neófitos', 'Iniciados', 'Avanzados', 'Expertos'
sizes = [nnovatos, niniciados, navanzados, nexpertos]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode 1st slice


# Gráfico por sectores
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show();
