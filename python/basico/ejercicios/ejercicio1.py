#actual
curso_actual = 1.5
# Otros
otro_minimo = 2.5
otro_promedio = 4
otro_maximo = 7


crudo_resto = 5
crudo_actual = 3.5


# Resto de cursos
print('Diferencia de duracion contra otros cursos')
print('')

con_el_minimo = 100 - curso_actual / otro_minimo * 100
print(f'El curso actual dura un {con_el_minimo}% menos que el mas rapido')
con_el_promedio = 100 - curso_actual / otro_promedio * 100
print(f'El curso actual dura un {con_el_promedio}% menos que el curso promedio')
con_el_maximo = 100 - curso_actual / otro_maximo * 100
print(f'El curso actual dura un {round(con_el_maximo,1)}% menos que el mas lento')

print('----------------------------------------------------------------------------')

# Parte 2
print("EL porcentaje de material inservible que elimina  otros cursos")
inservible_promedio = 100 - otro_promedio / crudo_resto * 100
print(f'El porcentaje de material inservible promedio es: {inservible_promedio}')

print('----------------------------------------------------------------------------')

# Con este curso
print('Porcentaje de material inservible eliminado de este curso')
inservible_actual = 100 - curso_actual / crudo_actual * 100
print(f'El porcentaje de material inservible de este curso es: {round(inservible_actual,1)}')

print('----------------------------------------------------------------------------')

# Diferencia de 10 horas

diferencia__promedio = otro_promedio / curso_actual *10
print(f'Ver 10 horas de este curso equivale a {round(diferencia__promedio,1)} del curso promedio')