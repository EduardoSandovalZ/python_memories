cadena1= 'Hola me llamo Eduardo'
cadena2 = 'bienvenidos a la clase de programacion 1'
cadena3 = '12345'
cadena4 = 'HolaMeLlamoEduardo'

# DIR -> Te muestra todos los metodos disponibles
#print(dir(cadena1))


# Upper -> Vuelve todo a mayusculas
print(cadena2.upper())

# Lower -> Vuelve todo a minisculas
print(cadena1.lower())

# title -> volver mayuscula la primera letra de cada palabra de una oracion separada por espacios
print(cadena1.title(()))

# Capitalize -> Convertimos la primera letra en mayuscula
print(cadena2.capitalize())

# Find -> Duelvelve la primera concidencia encontrada, si hay pedos dvuelve -1
print(cadena1.find('Eduardo'))

# Index -> Duelvelve el indice la primera concidencia encontrada, si hay pedos se rompe
print(cadena1.index('Eduardo'))

# Isnumeric -> Si el valor es numerico devuelve true, si hay un solo valor no numerico, da false
print(cadena3.isnumeric())

# Isalpha -> verifica que la codena contenga caracteres desde la aA hasta la zZ
print(cadena4.isalpha())

# Count -> cuenta el numero de apariciones de un caracteres en un texto
print(cadena1.count('a'))

# Len -> te devuelve la longitud de una cadena
print(cadena3.__len__()) 
print(len(cadena3))

# Endswith -> verifica si una cadena termina con un caracter en especifico
print(cadena2.endswith('1'))

#Startswith -> verifica si una cadena empieza con un caracter en especifico
print(cadena4.startswith('H'))

# Replace -> permite modificar un valor por otro
print(cadena1.replace('Eduardo','Alberto'))

# Split -> divide una cadena
split = cadena2.split('clase')
print(split)