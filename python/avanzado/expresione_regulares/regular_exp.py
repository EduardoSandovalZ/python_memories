import re


texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat 231. 
Duis aute irure dolor in reprehenderit in 231 voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 231 officia deserunt mollit anim id est laborum.
'''
# # la funcion search nos permite buscar en un texto algo en especidivo, ademas de brindarnos la ubicacion del mismo
# print(re.search('in',texto))
# # la funcion findall nos devuelve una lista con todas las concidencias encontradas.
# print(re.findall('in',texto,flags=re.IGNORECASE))




# Ahora si vamos con las regex

# \d -> Busca los caracteres numericos del 1 al 9
print('Busca los caracteres numericos del 1 al 9')
print(re.findall(r'\d',texto))

# \D -> Busca TODO MENOS los caracteres numericos del 1 al 9
print('Busca TODO MENOS los caracteres numericos del 1 al 9')
print(f'{re.findall(r'\D',texto)}\n')

# \w -> Busca los caracteres alfa-numericos [a-z A-Z 0-9 _]
print('Busca los caracteres alfa-numericos [a-z A-Z 0-9 _]')
print(f'{re.findall(r'\w',texto)}\n')

# \w -> Busca TODO MENOS los caracteres alfa-numericos [a-z A-Z 0-9 _]
print('Busca TODO MENOS los caracteres alfa-numericos [a-z A-Z 0-9 _]')
print(f'{re.findall(r'\W',texto)}\n')

# \s -> Busca los espacios en blanco
print('Busca los espacios en blanco')
print(f'{re.findall(r'\s',texto)}\n')

# \S -> Busca TODO MENOS los espacios en blanco
print('Busca TODO MENOS los espacios en blanco')
print(f'{re.findall(r'\S',texto)}\n')

# . -> Busca TODO MENOS los saltos de linea
print('Busca TODO MENOS los saltos de linea')
print(f'{re.findall(r'.',texto)}\n')

# \n -> Busca los saltos de linea
print('Busca los saltos de linea')
print(f'{re.findall(r'\n',texto)}\n')

# \ -> Cancelar caracteres especiales 
# ejemplo: \. -> cancelamos la funcion del punto y buscamos puntos
print('Busca puntos')
print(f'{re.findall(r'\.',texto)}\n')


# Ejercicio1 buscar un numero, seguido de un punto y seguido por un espacio
print(f'{re.findall(r'\d\.\s',texto)}\n')
print(f'{re.search(r'\d\.\s',texto)}\n')


# parte 2
# ^ -> Busca el comienzo de una linea
print('Busca el comienzo de una linea')
print(f'{re.findall(r'^Lorem',texto)}\n')
# -> el flags=re.M permite la multilinea
print(f'{re.findall(r'^Duis',texto,flags=re.M)}\n')

# ^ -> Busca el final de una linea
print('Busca el final de una linea')
# -> el flags=re.M permite la multilinea
print(f'{re.findall(r'laborum.$',texto,flags=re.M)}\n')


# Si quisieramos por ejemplo que solo nos encuentre numeros de mas de 3 cifras seguidos de un punto
print(f'{re.findall(r'\d{3}\.',texto,flags=re.M)}\n')

# La funcion anterior se puede modificar para que funcione con rangos
print(f'{re.findall(r'\d{1,3}',texto,flags=re.M)}\n') #-> buscame un valor numerico que tenga entre 1 a 3 cifras