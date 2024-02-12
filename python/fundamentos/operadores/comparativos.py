a = 1
b = 2

igualdad = a == a

distinto = a != b

menor = a < b

mayor = b > a

menor_igual = a <= b

mayor_igual = b >= a 

#Todos los resultos nos deben de dar true

# print(igualdad)
# print(distinto)
# print(menor)
# print(mayor)
# print(menor_igual)
# print(mayor_igual)


# Esto tambien aplica para char por el codigo asci

igualdad = 'a' == 'a'

distinto = 'a' != 'b'

menor = 'a' < 'b'

mayor = 'b' > 'a'

menor_igual = 'a' <= 'b'

mayor_igual = 'b' >= 'a' 

# print(igualdad)
# print(distinto)
# print(menor)
# print(mayor)
# print(menor_igual)
# print(mayor_igual)

# y aplica para cadenas

a = 'Eduardo'
b = 'Alberto'

# print(a==b)

#practicamente aplica para variables simples y compuestas

lista = [20,"Alberto",True,170.0]
tupla = (20,"Alberto",True,170.0)
conjunto = {20,"Alberto",True,170.0} 



print(lista[0] == tupla[0])

print(tupla == conjunto)