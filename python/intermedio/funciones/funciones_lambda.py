# def doble (numero):
#     return numero * 2

# print(doble(5))

# # Funcion lambda que hace lo mismo que la anterior

# lambda_doble = lambda numero:numero*2 # -> si tenemos que haces mas de una expresion, no usar lambda

# print(lambda_doble(5))

'''
Ejemplo 3 usando filter con nuestra funcion lambda
'''
numeros = (0,1,2,3,4,5,6,7,8,9,10)

numeros_pares = filter(lambda numero:numero%2==0,numeros)
numeros_impares = filter(lambda numero:numero%2,numeros)

print(f'Los elementos pares son: \n{tuple(numeros_pares)}\n')
print(f'Los elementos impares son: \n{tuple(numeros_impares)}')