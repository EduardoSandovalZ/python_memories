def suma():
    # Hacemos un bucle que se ejecute infinitas veces hasta que el try y el else se cumplan
    while True:
        # intentamos que a y b sean numeros enteros
        try:
            a = int(input('Numero 1: '))
            b = int(input('Numero 2: '))
        # Si el pendejo ingresa otra cosa, se le notifica
        except:
            print('La estas cagando maestro')
        # si se ejecuta el try se va a ejecuta el else
        else:
            break
        # Este se ejcuta siempre, ya sea que nos de try o except
        finally:
            print('Esto se ejecuta siempre')
    resultado = a + b
    return resultado  


print(suma())