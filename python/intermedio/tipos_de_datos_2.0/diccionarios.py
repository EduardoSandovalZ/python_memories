diccionario = dict(Nombre='Eduardo', Apellido = 'Sandoval', Edad = 23)

print(type(diccionario))
print(diccionario)

# Podemos usar tuplas como keys de un dict
diccionario = {('Eduardo','Sandoval'):'Texto'}
print(diccionario)

# podemos usar conjuntos como keys pero debemos usar frozen set
diccionario = {frozenset(['Eduardo','Sandoval']):'Texto2'}
print(diccionario)

# Podemos crear un diccionario con todos los valores None

#diccionario = dict.fromkeys(['Nombre','Apellido'],'None')
diccionario = dict.fromkeys(['Nombre','Apellido'])
print(diccionario)