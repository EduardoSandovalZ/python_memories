def asignar_rol(numero_alumnos):
    lista_alumnos = []
    for alumno in range(numero_alumnos):
        nombre = input(f'Proporciona el nombre del alumno {alumno+1}: ').title()
        edad = int(input(f'Proporciona la edad del alumno {alumno+1}: '))
        lista_alumnos.append((nombre,edad))
        
    lista_alumnos.sort(key = lambda x:x[1])
    profesor = lista_alumnos[-1]
    asistente = lista_alumnos[0]
    
    return profesor,asistente




numero_alumnos = int(input('Proporciona el numero de alumnos: '))
profesor,asistente = asignar_rol(numero_alumnos)
print(f'El nombre del profesor es {profesor[0]} y tiene {profesor[1]} años de edad')
print(f'El nombre del asistente es {asistente[0]} y tiene {asistente[1]} años de edad')
