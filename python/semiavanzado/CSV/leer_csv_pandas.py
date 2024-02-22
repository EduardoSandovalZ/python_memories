import pandas as pd

df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\CSV\\txt.csv')

print(f'{df}\n')

'''
Podemos asignar cada columna
'''

# nombre = df['nombre']
# print(nombre)

'''
Igualmente podemos ordenar las filas por odern ascendente o descendente
'''

# df_ascend = df.sort_values('edad')
# print(f'{df_ascend}\n')

# df_desc = df.sort_values('edad',ascending=False)
# print(f'{df_desc}\n')


'''
Si quisieramos concatenar 2 df se hace de la siguiente forma
'''
df2 = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\CSV\\txt.csv')

df_concatenado = pd.concat([df,df2])
print(f'{df_concatenado}\n')


'''
podemos obtener separar por el numero de filas ya sea de arriba para abajo o de abajo para arriba
'''

# primeras_filas = df_concatenado.head(0)
# print(primeras_filas)


# ultimas_filas = df_concatenado.tail(2)
# print(ultimas_filas)

# ''' 
# Accediendo a la cantidad de filas o columnas
# '''
# filasycolumas = df_concatenado.shape
# print(filasycolumas)

'''
Si qusieramos datos estadisticos 
'''

# df_info = df_concatenado.describe()
# print(df_info)

'''
Podemos acceder por valores especificos
[fila,columna]
'''
# Este imprimos los valores que tenga
elemento_especifico_loc = df_concatenado.loc[2,'edad'] # -> en el concatenado hay 2 vergas quer tienen el indice 2, por eso imprime 2 22
print(elemento_especifico_loc)

elemento_especifico_iloc = df_concatenado.iloc[2,2] # -> esto nos devuelve 2 por que lo busca por el indice forzoso
print(elemento_especifico_iloc)


'''
Podemos imprimir solo los apellidos por ejemplo
'''
apellidos = str(df_concatenado.iloc[:,1]) # -> al poner : indicamos que recorra todas las filas de esa columna
print(type(apellidos))

df3 = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\CSV\\txt3.csv')
print(f'df3 original:\n{df3}\n')
'''
Reemplazar datos
'''
df3_nombre = df3['nombre'].replace('eduardo','chingon')
print(f'df3 con el nombre eduardo reemplazado:\n{df3_nombre}\n')
'''
Eliminar filas con datos faltantes
'''
df3_faltantes = df3.dropna()
df3 = df3.dropna(axis = 1) #-> Este se usa si la columa es la que tiene datos faltantes
print(f'df3 eliminando las filas con datos faltantes:\n{df3_faltantes}\n')
'''
Eliminar filas duplicadas
'''
df3_duplicados = df3.drop_duplicates()
print(f'df eliminando filas duplicadas:\n{df3_duplicados}\n')
