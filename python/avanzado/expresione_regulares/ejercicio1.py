import re

text = 'The quick brown fox jumps over the lazy dog'
# El operador * indica, omite todo el texto que no sea lo que buscamos
# significa la cadena debe empezar con The, omite los saltos de linea, si hay caracteres entre The y dog ignoralos y la palabra debe terminar en dog
x = re.search(r'^The.*dog$',text)

if x:
    print('SI')
else:
    print('NO')