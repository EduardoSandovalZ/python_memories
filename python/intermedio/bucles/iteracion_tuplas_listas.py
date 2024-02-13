# Listas
numeros_lista = [1,2,3,4]
animales_lista = ['perro','gato','leon','puma']
print('Imprimiendo listas')
for numero in numeros_lista:
    print(numero)
    
# Iterar usando el indice
for animal in enumerate(animales_lista): # -> esto sustituye al in range(len(animales))
    index = animal[0]
    valor = animal[1]
    print(f'El indice es {index} y el valor es {valor}')


# Tuplas
numeros_tupla = (1,2,3,4)
animales_tupla = ('perro','gato','leon','puma')
print()
print('Imprimiendo tuplas')
for numero in numeros_tupla:
    print(numero)
    
# Iterar usando el indice
for animal in enumerate(animales_tupla): # -> esto sustituye al in range(len(animales))
    index = animal[0]
    valor = animal[1]
    print(f'El indice es {index} y el valor es {valor}')


# imprimir ya sea 2 listas, 2 tuplas o 1 de acada una a la vez
print('\n'+'Usando la funcion zip')
for numero, animal in zip(numeros_lista,animales_tupla):
    print(f'El numero es {numero} y el animal es {animal}')