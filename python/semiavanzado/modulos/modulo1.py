# # Forma 1, tratarlo como un metodo
import funciones_chidas.saludar as saludar

# Mostramos todos los metodos disponibles en nuestro modulo
print(dir(saludar))
print(saludar.__name__)
saludo = saludar.saludar('Juan')
insulto = saludar.insultar('Raul')

print(saludo)
print(insulto)



# forma 2, de esta manera mantenemos la funcion

from funciones_chidas.saludar import *

saludo = saludar('Alberto')
insulto = insultar('Eduardo')
print(saludo)
print(insulto)

# Para enrutar debemos de seleccionar la carpeta y separarlas por puntos
'''
carpeta_raiz.carpeta_rama.nombre_del_modulo
'''