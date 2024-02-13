conjunto = set(['Dato1','Dato2'])


# Teoria de conjuntos
# Meter un conjunto dentro de otro
conjunto1 = frozenset(['Elemento1','Elemento2'])
conjunto2 = {conjunto1,'Elemento3'}

print(conjunto2)

# Subconjuntos

conjunto1 = {1,3,5,7,9}
conjunto2 = {1,2,3,4,5,6,7,8,9}
# Saber si conjunto1 es subconjunto de conjunto 2
resultado = conjunto1.issubset(conjunto2)
print(resultado)

# saber si conjunto2 es superconjunto de conjunto1
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

# Encontrar la interseccion entre 2 conjuntos
resultado = conjunto2.intersection(conjunto1,conjunto2)
print(resultado)

# Verificar si no hay algun numero en comun
resultado = conjunto1.isdisjoint(conjunto2)
print(resultado) #-> y hay al menos 1 elemento en comun da False