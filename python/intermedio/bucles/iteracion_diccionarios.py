diccionario = dict(Nombre = 'Eduardo', Apellido = 'Sandoval', Edad = 23)

for key in diccionario.items():
    print(key)

# Igual que antes el [0] es el key y el [1] es el valor

for datos in diccionario.items(): # -> Jala igual que el enumerate
    key = datos[0]
    value = datos[1]
    print(f'La llave es {key} y el valor que contiene es {value}')
    
