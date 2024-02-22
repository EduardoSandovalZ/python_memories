import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Abrimo el archivo csv
df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\graficos\\pedos.csv')
#Creamos la grafica 
sb.lineplot(x='fecha', y='pedos',data = df)
# Creamos un punto en el dia que mas pedos tuvo
plt.plot('01-10',10,'o')
# mostramos el grafico
plt.show()