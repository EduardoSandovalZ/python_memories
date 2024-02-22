import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Abrimo el archivo csv
df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\graficos\\dispercion.csv')
#Creamos la grafica 
sb.scatterplot(x='tiempo', y='dinero',data = df)
# Creamos un punto en el dia que mas pedos tuvo

# mostramos el grafico
plt.show()