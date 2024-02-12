#listas o arreglos #
lista = [10,"eduardo",False,60.0,]
print(lista)

# Las listas se pueden modificar
lista[1] = "La mera verga"
print(lista)

#tuplas#
tupla = (20,"Alberto",True,170.0)

#tupla[1] = "La mera verga" -> las tuplas no son modificables

print(tupla)

#Conjunto#

# crear un set o conjunto
conjunto = {20,"Alberto",True,170.0}


#conjunto[1] = "La mera verga" -> No se puede modificar, igual que la tupla


#print(conjunto[1]) -> Los conjuntos no se pueden acceder mediante indice

#No almacena datos duplicados
conjunto = {20,"Alberto",True,170.0,"Alberto"} 

# Y por ultimo los datos no mantienen el orden en el que fueron declarados
print(conjunto)

#Diccionarios#
diccionario = {
    'nombre': 'eduardo',
    'apellido': 'sandoval',
    'edad': 22,
    'sexo': 'masculino',
    'casado': False
}

#esta madre es igual a un json

print(diccionario)

print(diccionario['nombre'])
diccionario['nombre'] = 'Alberto' # -> Los valores son mutables, como en las listas
print(diccionario['nombre'])

print(type(lista))
print(type(tupla))
print(type(diccionario))
print(type(conjunto))