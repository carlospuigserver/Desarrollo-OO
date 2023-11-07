import pandas as pd

# Cargar datos para limpieza y preprocesamiento
data = pd.read_csv("datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")

# Realizar limpieza y preprocesamiento de datos

# Eliminar filas con valores nulos en cualquier columna
data = data.dropna()

# Reemplazar valores faltantes o no deseados con un valor por defecto
data.fillna(value='ValorPorDefecto', inplace=True)

# Convertir tipos de datos si es necesario
data['Año'] = data['Año'].astype(int)
data['Mes'] = data['Mes'].astype(str)

# Realizar más operaciones de limpieza y preprocesamiento si es necesario

# Guardar datos preprocesados
data.to_csv('resultados/datos_preprocesados.csv', sep=';', index=False, encoding='ISO-8859-1')
