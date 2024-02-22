import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Abrimo el archivo csv
df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\graficos\\ingresos.csv')
#Creamos la grafica 
sb.barplot(x='fuente', y='ingresos',data = df)
# Creamos un punto en el dia que mas pedos tuvo

total_ingresos = df['ingresos'].sum()
print(total_ingresos)
# mostramos el grafico
plt.show()