texto = input('Ingresa un texto: ')

numero_palabras = len(texto.split(' '))
tiempo_en_decirlas = numero_palabras / 2
tiempo_dalto = tiempo_en_decirlas * 0.7
print('')

if tiempo_en_decirlas > 60:
    print('Pará flaco tampoco te pedí un testamentos' + {'\n'})
else: 
    print(f'Dijiste {numero_palabras} palabra(s) y tardaste {round(tiempo_en_decirlas,2)} segundo(s) en decirlas  {'\n'}')
    print(f'Dijiste {numero_palabras} palabra(s) y dalto tardaría {round(tiempo_dalto,2)} segundo(s) en decirlas  {'\n'}')