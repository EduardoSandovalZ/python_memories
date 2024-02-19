# este me regresa todo el archivo complero
archvivo_sin_leer = open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\TXT\\txt_mal.txt',encoding='utf-8')
archivo = archvivo_sin_leer.read()
print(archivo)
archvivo_sin_leer.close()

# este regresa casa renglon como un elemento de una lista
archvivo_sin_leer = open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\TXT\\txt_mal.txt',encoding='utf-8')
lineas = archvivo_sin_leer.readlines()
print(lineas)
archvivo_sin_leer.close()

# este nos regresa una sola linea, si no puede leer una linea, lee el numero de caracteres que le pasemos como parametro
archvivo_sin_leer = open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\TXT\\txt_mal.txt',encoding='utf-8')
linea1 = archvivo_sin_leer.readline(2)
print(linea1)
archvivo_sin_leer.close()



