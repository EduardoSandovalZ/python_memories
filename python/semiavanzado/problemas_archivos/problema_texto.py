nombres = ['eduardo','alberto','juan','molly']
apellidos = ['sandoval','zorrilla','lopez','paez']
def lineas():
    return 27*'-'    

with open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\problemas_archivos\\txt.txt',
          'w',encoding='utf-8') as archivo:
    '''
    Forma incorrecta
    '''
    archivo.writelines('Forma incorrecta de escribir\n')
    for nombre, apellido in zip(nombres,apellidos):
        archivo.writelines(f'{nombre.title()} {apellido.title()}\n')
    '''
    Forma Correcta
    '''      
    archivo.writelines(f'\nForma correcta de escribir\n{lineas()}\n')                                                                              
    [archivo.writelines(f'El nombre es: {nombre.title()}\nEl apellido es: {apellido.title()}\n{lineas()}\n') for nombre, apellido in zip(nombres,apellidos)]