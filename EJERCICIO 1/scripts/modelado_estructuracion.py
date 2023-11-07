import pandas as pd

# Cargar datos desde el archivo preprocesado
data = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')

# Realizar modelado y estructuración para análisis

# Ejemplo: Crear una nueva columna calculando la duración de la intervención
data['Duracion Intervencion (min)'] = (pd.to_datetime(data['Hora Intervencion']) - pd.to_datetime(data['Hora Solicitud'])).dt.total_seconds() / 60

# Guardar resultados del modelado o estructuración si es necesario
data.to_csv('EJERCICIO 1/resultados/datos_con_duracion.csv', sep=';', encoding='ISO-8859-1', index=False)
