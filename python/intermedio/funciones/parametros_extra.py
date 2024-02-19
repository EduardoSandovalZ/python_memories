
def saludar(nombre, apellido,adjetivo):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'

# Ccuando tenemos multiples parametros podemos asiignaros de forma ordenada
saludo1 = saludar('Eduardo','Sandoval','dedicado')
print(saludo1)

# O podemos asiignarlo directamente a traves de la llave o clave de parametro
saludo2 = saludar( apellido = 'Sandoval', adjetivo='menso',nombre = 'Eduardo')
print(saludo2)


#Podemos crear un valor por defecto 
def saludar2(nombre, apellido,adjetivo='guapo'):
    return f'Hola {nombre} {apellido} eres muy {adjetivo}'
saludo3 = saludar2('Albert','Zorrilla')
print(saludo3)
