import pandas as pd

# Leer el archivo CSV para la exploración y análisis inicial
data = pd.read_csv("datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")

# Resumen de datos estadísticos
summary = data.describe()
print(summary)

import seaborn as sns
import matplotlib.pyplot as plt

# Graficar la distribución de una columna usando Seaborn
sns.histplot(data['Distrito'], bins=20)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores')
plt.savefig('resultados/visualizaciones/histograma.png')
plt.show()
