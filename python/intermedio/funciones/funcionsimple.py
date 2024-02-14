# Funcion simple
def saludar():
    print("Monstruo")
    
    
saludar()


# Funcion que recibe un parametro
def saludar(nombre, sexo):
    if sexo.upper() == 'F':
        print(f'Hola {nombre}, hermosa como estas?')
    elif sexo.upper() == 'M':
        print(f'Hola {nombre}, hermoso como estas?')
    
saludar('Eduardo','f')