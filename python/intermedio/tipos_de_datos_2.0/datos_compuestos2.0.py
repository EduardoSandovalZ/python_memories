# Desempaquetado
datos_tupla = ('Eduardo','Sandoval','23')
datos_lista = ['Eduardo','Sandoval','23']
#nombre, apellido, edad = datos_tupla
nombre, apellido, edad = datos_lista
print(nombre,apellido,edad)

# Crear estructuras de otra forma
tupla = ()
lista = list(['Eduardo','Sandoval',23])
conjunto = set({'Eduardo','Sandoval',23})

tupla = 'Eduardo','Sandoval',23
print(type(tupla),type(lista),type(conjunto))
