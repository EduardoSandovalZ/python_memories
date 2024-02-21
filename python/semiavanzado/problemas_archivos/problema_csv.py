import pandas as pd

df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\problemas_archivos\\txt.csv')
df['edad'] = df['edad'].astype(str)

#print(type(df['edad'][0]))
print(f'{df}\n')
df['nombre']= df['nombre'].replace('eduardo','chingon')
print(df)
df.to_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\problemas_archivos\\txt2.csv')