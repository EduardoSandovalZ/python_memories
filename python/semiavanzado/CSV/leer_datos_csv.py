import csv
print('Archivo abierto como un txt \n')
#Primero importamos el csv pero lo leemos sin csv
with open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\CSV\\txt.csv') as archivo:
    texto = archivo.read()
print(texto)

print('\nArchivo abierto usando csv \n')
# importamos el csv pero lo leemos con csv
with open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\CSV\\txt.csv') as archivo2:
    reader = csv.reader(archivo2)
    for row in reader:
        print(row)

