# Forma no optima de realizarlo

def sumaCulera(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

numeros = [213,123,123,432,12]
print(sumaCulera(numeros))

# cuando queremos pasar parametros debemos de usar el metodo *args cuando usamos multiples parametros (lista, arreglo,tupla,etc)
def suma(*numeros):
    return sum(numeros)
resultado = suma(213,123,123,432,12)
print(resultado)

# Ahora bien, podemos usarlo para regresar una lista
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([213,123,123,432,12])
print(resultado2)


'''
Tanto suma como suma total hacen exactamente lo mismo, la diferencia es que en uno pasas multiples argumentos con args, y con el otro ingresas una 
lista y te devuelve una lista usando igualmentr args

'''




