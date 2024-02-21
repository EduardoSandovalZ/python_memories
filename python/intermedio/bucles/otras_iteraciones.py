numeros = [1,2,3,4,5,6,7,8,9]
# Evitamos acceder solo a un elemento, nos lo saltamos
for numero in numeros:
    if numero == 3:
        continue
    #print(numero)

# Rompemos el bucle cuando se cumpla una condiconal
for numero in numeros:
    if numero == 3:
        break
    #print(numero)


# Recorrer una cadena
cadena = 'Hola Eduardo'

for letra in cadena:
    print(letra)
    
    
# Ahora, podemos reducir lineas de codigo usando for
lista_numeros = [12,20,66]
# si quisieras duplicar cada uno de los numeros, se puede hacer de la siguiens formas

lista__duplicados = []
# forma 1
for numero in lista_numeros:
    lista__duplicados.append(numero*2)
print(lista__duplicados)

# forma 2
lista__duplicados = [numero *2 for numero in lista_numeros]
print(lista__duplicados)