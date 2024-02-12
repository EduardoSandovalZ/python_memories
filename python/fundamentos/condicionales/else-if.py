persona1 =  {
    'Nombre': 'Eduarda',
    'Apellido': 'Sandoval',
    'Edad': 7,
    'Genero': 'F',
    'INE': True
}

if persona1['Genero'] == 'F':
    if persona1['Edad'] >= 18:
        print('Hoy las muejeres tienen barra libre')
        print('Buenas noches señorita, necesito ver tu INE')
        if persona1['INE']:
            print('Puedes pasar')
        else:
            print('Sin INE no se puede pasar')
    else:
        print('Saquese chamaca miada')
else:
    if persona1['Edad'] >= 18:
        print('Buenas noches joven, necesito ver tu INE')
        if persona1['INE']:
            print('Puedes pasar')
        else:
            print('Sin INE no se puede pasar')
    else:
        print('Saquese chamaco miada')
        
    