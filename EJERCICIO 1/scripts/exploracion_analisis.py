import pandas as pd

# Leer el archivo CSV para la exploración y análisis inicial
data = pd.read_csv("EJERCICIO 1/datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")

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
plt.savefig('EJERCICIO 1/resultados/Distrito.png')
plt.show()

# Graficar la distribución de una columna usando Seaborn
sns.histplot(data['Hospital'], bins=20)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores')
plt.savefig('EJERCICIO 1/resultados/Hospital.png')
plt.show()