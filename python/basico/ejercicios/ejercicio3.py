# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas 
# veces como el número introducido.
texto = input('Introduce una palabra: ')
cantidad_de_repeticiones = int(input('Introduce la cantidad de veces que la palbra se va a repetir: '))
# cantidad_de_repeticiones = input('Introduce la cantidad de veces que la palbra se va a repetir: ')
# print((texto + '\n') * int(cantidad_de_repeticiones))

print(f'{(texto + '\n') * cantidad_de_repeticiones}')