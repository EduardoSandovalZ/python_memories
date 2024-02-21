# para abrir archivos de texto se hace de 2 formas

''''
Forma incorrecta
'''
lista_numeros = (1,2,3,4,5,6,7,8,9,10)
archivo = open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\TXT\\txt_mal.txt',"w",encoding='utf-8')
for numero in lista_numeros:
    archivo.writelines(str(numero)+'\n')

archivo.close()

'''
Forma correcta
'''
with open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\TXT\\txt_bien.txt',"w",encoding='utf-8') as archivo2:
    for numero in lista_numeros:
        archivo2.write(str(numero)+'\n')