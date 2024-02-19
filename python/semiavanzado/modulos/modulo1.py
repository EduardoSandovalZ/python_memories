# # Forma 1, tratarlo como un metodo
import modulo_saludar
# Mostramos todos los metodos disponibles en nuestro modulo
print(dir(modulo_saludar))

saludo = modulo_saludar.saludar('Juan')
insulto = modulo_saludar.insultar('Raul')

print(saludo)
print(insulto)



# forma 2, de esta manera mantenemos la funcion
from modulo_saludar import saludar,insultar 

saludo = saludar('Alberto')
insulto = insultar('Eduardo')
print(saludo)
print(insulto)

