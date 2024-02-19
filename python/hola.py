def asignar_compañeros(numero_asistentes):
    lista_alumnos = []
    for alumno in range(numero_asistentes):
        nombre = input(f'Proporciona el nombre del alumno {alumno+1}: ').title()
        edad = int(input(f'Proporciona la edad del alumno {alumno+1}: '))
        tupla_temporal = (nombre,edad)
        lista_alumnos.append(tupla_temporal)
    #funcion sorte te ayuda a order los valores de una lista de listas
    #lista_alumnos = sorted(lista_alumnos, key=lambda x: x[1])
    lista_alumnos.sort(key=lambda x:x[1])
    asistente = lista_alumnos[0]
    profesor = lista_alumnos[-1]
    return asistente,profesor

numero_alumnos = int(input(('Prorciona el numero de alumnos: ')))
asistente,profesor = asignar_compañeros(numero_alumnos)
print(f'El asistente será: {asistente} y el maestro será {profesor}')
    








