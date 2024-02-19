# Creacion de listas
lista = ['hola','eduardo',23]
print(lista)
lista = list(['hola','eduardo',23])
print(f'Lista original: {lista}')
lista2 = ['hola','eduardo',23]



# Contar los elementos de la lista
print(f'Numero de elementos de la lista: {len(lista)}')

# Agregar un elemento al final de la lista
lista.append('sandoval')
print(f'Agregando un elemento con append: {lista}')

# Agregar un elemento en una posicion especifica
lista.insert(1,'saludos')
print(f'Agregando un elemento con insert: {lista}')

# Agregar multiples elementos al final de la lista
lista.extend(['extend',50])
print(f'Agregando varios elementos con extend: {lista}')

# Eliminar un elemento dando un indice
lista.pop(-1)
lista.pop(2) # -> -1 para eliminar el ultimo, -2 para el panultimo y asi
print(f'Eliminando elementos de la lista por su indice con pop: {lista}')

# Eliminar un elemento de la lista por su valor
lista.remove(23)
print(f'Eliminado elemento por su valor con remove: {lista}')

# Ordenar los elementos de una lista de forma ascendente (con el parametro reverse=True se ordena de reversa)
lista.sort()
print(f'Lista de ordenada de forma ascendente: {lista}')
lista.sort(reverse=True)
print(f'Lista de ordenada de forma desc: {lista}')


# Darle la vuelta a una lista
print(f'Lista bien: {lista2}')
lista2.reverse()
print(f'Lista al reves: {lista2}')



# Eliminar todos los elementos de la lista 
lista.clear()
print(f'Lista vaciada con el metodo clear: {lista}')