import pandas as pd

# Cargar datos para modelado y estructura para análisis
data = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')

# Realizar modelado y estructuración para análisis

# Ejemplo: Agregar una nueva columna calculada
data['Nueva_Columna'] = data['Columna_A'] * data['Columna_B']

# Ejemplo: Agrupar datos para un análisis resumido
resumen = data.groupby('Columna_C').agg({'Columna_D': 'mean', 'Columna_E': 'sum'})

# Guardar resultados del modelado o estructuración si es necesario
resumen.to_csv('EJERCICIO 1/resultados/resultados_analisis_resumen.csv', sep=';', encoding='ISO-8859-1')
