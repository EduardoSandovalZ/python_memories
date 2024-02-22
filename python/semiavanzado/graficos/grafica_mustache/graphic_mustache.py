import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Abrimo el archivo csv
df = pd.read_csv('C:\\Users\\EDUARDOSANDOVALZORRI\\Documents\\Dt\\python_memories\\python\\semiavanzado\\graficos\\grafica_mustache\\bigotes.csv')
print(df)

#Creamos la grafica 
sb.boxplot(x='categoria', y='valor',data = df)
# Creamos un punto en el dia que mas pedos tuvo


# mostramos el grafico
plt.show()