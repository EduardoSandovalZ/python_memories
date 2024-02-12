# pedilr al usuario que introduzca una frase
# 1:
texto = input('Ingresa un texto: ')
cantidad_palabras = len(texto.split(' '))
tiempo_normal = cantidad_palabras / 2

print(f'El usuario introdujo {cantidad_palabras} palabra(s)')
print(f'Una persona normal tardaria {tiempo_normal} segundo(s) en decirla')


# 2:
if tiempo_normal > 60:
    print('Mucho texto')
    
# 3:
mi_tiempo = tiempo_normal * 0.7
print(f'Yo tardaria en decirlo {mi_tiempo} segundo(s) en decirla')
