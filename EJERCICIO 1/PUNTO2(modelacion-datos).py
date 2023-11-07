import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("activaciones_samur_2022.csv",sep=";",encoding="ISO-8859-1")

#resumen datos estadisticos
summary=data.describe()
print(summary)

import seaborn as sns

# Graficar la distribución de una columna usando Seaborn
sns.histplot(data['Nombre_Columna'], bins=20)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores')
plt.show()
