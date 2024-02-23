import re
email = 'eduardo.sandovalz@alumno.buap.mx'
# el + indica que de ahuevo debe de haber al menos una concidencia de lo que haya antes del +
pattern = r'[a-zA-Z0-9._%+-]+@+[a-z.-]+\.[a-zl]{2,}'

result = re.match(pattern,email)

if result:
    print('email valido')
else:
    print('email no valido')