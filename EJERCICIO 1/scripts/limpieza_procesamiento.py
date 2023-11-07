import pandas as pd

# Cargar datos para limpieza y preprocesamiento
data = pd.read_csv("EJERCICIO 1/datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")



# Eliminar filas con valores nulos en cualquier columna
data = data.dropna()

# Reemplazar valores faltantes o no deseados con un valor por defecto
data.fillna(value='ValorPorDefecto', inplace=True)




# Guardar datos preprocesados
data.to_csv('EJERCICIO 1/resultados/datos_preprocesados.csv', sep=';', index=False, encoding='ISO-8859-1')
