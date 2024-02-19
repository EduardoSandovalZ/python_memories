def define_role(number_students):
    list_student= []
    for student in range(number_students):
        name = input(f'Proporcione el nombre del alumno {student+1}: ').title()
        age =  int(input(f'Proporcione el nombre del alumno {student+1}: '))
        list_student.append((name,age))
    list_student.sort(key=lambda x:x[1])
    teacher = list_student[-1]
    assistant = list_student[0]
    return teacher,assistant
    
    
number_students = int(input('Proporcione el numero de alumnos: '))
teacher,assistant = define_role(number_students)

print(f'El maestro es {teacher[0]} y tiene {teacher[1]}')
print(f'El nombre del asistente es {assistant[0]} y  tiene {assistant[1]}')