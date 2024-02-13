set_numeros = {1,2,3,4}
set_animales = {'perro','gato','lobo','ardilla'}

for animal in set_animales:
    print(animal)

for numero in enumerate(set_numeros):
    print(numero)
    
for animal,numero in zip(set_animales,set_numeros):
    print(f'El numero es {numero} y el animal es {set_animales}')
    
    
# Solo no funcionaria lo siguiente

# for i in range(len(set_animales)):
#     print(set_animales[i])