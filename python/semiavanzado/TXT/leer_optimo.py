with open('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Tesis\\ping_test\\test2\\not_ping.txt',encoding='utf-8') as archivo:
    archivo = archivo.readlines()
archivo.pop(0)
archivo.pop(0)
lista = []
for ip in archivo:
    lista.append(str(ip.replace('\n','')))

#print(lista)

for ip in lista:
    print(ip)