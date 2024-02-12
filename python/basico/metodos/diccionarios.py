diccionario = {
    'nombre': 'eduardo',
    'apellido': 'sandoval',
    'edad': 23
}

# Obtener las llaves de un diccionario  e iterar los keys
print(f'Llaves de diccionario: {diccionario.keys()}')

# obtener el valor por clave
print(f'Obtener el valor de una llave: {diccionario.get('nombre')}') # este no causa excepcion  
#otra forma de hacerlo
print(f'Obtener el valor de una llave: {diccionario["nombre"]}')

# Volver un diccionario iterable
dict_iterable = diccionario.items()
print(f'Diccionario no iterable: {diccionario}')
print(f'Diccionario iterable: {dict_iterable}')

# Eliminar un elemento del diccionario
diccionario.pop('nombre')
print(f'Eliminando un elemento del dict: {diccionario}')



# Eliminar todos los elementos del dict
diccionario.clear()
print(f'Diccionario vacio: {diccionario}')