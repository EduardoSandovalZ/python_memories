import sys

# print(sys.path)
sys.path.append('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\modulos_eduardo')
# print(sys.path)
from ping_range import *

lista_ping, lista_not_ping = ping_range('142.251.116.100', '142.251.116.120',2)
print(f'Los elementos que respondieron fueron: \n{lista_ping}')
print(f'Los elementos que no respondieron fueron: \n{lista_not_ping}')