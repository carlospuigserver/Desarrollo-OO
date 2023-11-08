# EJERCICIO 1

## Contexto:

El SAMUR-Protección Civil despliega un servicio crucial de atención a emergencias sanitarias extrahospitalarias en Madrid, desempeñando un rol esencial en la salvaguarda de la seguridad y bienestar ciudadano en situaciones críticas. A lo largo del año, el SAMUR gestiona numerosas "activaciones" como respuesta a incidentes diversos, desde accidentes de tráfico hasta emergencias médicas.

La ciudad de Madrid, en aras de la transparencia y apertura de datos, pone a disposición un registro detallado de estas activaciones en formato CSV. Este registro contiene información relevante como la fecha, hora, tipo de emergencia y otros datos significativos para cada activación.

## Objetivo:
Desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos.

## Punto 1 - Lectura de Datos:

Para abordar el análisis de esta información, se ha creado un programa que hace uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos. En el primero de los puntos, se efectúa la lectura directa del archivo CSV. El archivo se ha denominado "activaciones_samur_2023(1).csv" y se ubica en la carpeta "datos" dentro del proyecto "EJERCICIO 1". Este archivo alberga detalles como el año, mes, hora de solicitud, hora de intervención, códigos, distritos y hospitales.


## Punto 2 - Modelado de Datos:
En este apartado, a parte de facilitar la información para la Factoria (que es el objetivo), he querido buscar un poco de comparación. La diferencia fundamental entre el enfoque utilizando Pandas y otros módulos en los scripts de la carpeta y el método de factorías radica en la abstracción y estructuración del proceso de análisis de datos.

El uso de los scripts individuales en la carpeta "scripts" implica la escritura de instrucciones específicas en cada archivo para diferentes tareas, como la exploración inicial, el preprocesamiento y la transformación de datos. Cada script realiza operaciones directas sobre el conjunto de datos, llevando a cabo tareas individuales como la limpieza, el análisis exploratorio y la adición de nuevas columnas. Este enfoque basado en scripts demanda una programación detallada y específica para cada tarea.

En cambio, el uso del patrón de diseño de Abstract Factory introduce una abstracción a nivel más alto, permitiendo una modularización y estandarización en el análisis de datos. Las factorías abstraen y encapsulan la creación de objetos y componentes necesarios para cada fase del análisis. Este enfoque permite la creación de instancias de clases relacionadas, como exploradores de datos, limpiadores y transformadores, sin especificar sus clases concretas.

El beneficio principal de las factorías radica en la flexibilidad y la facilidad de cambio. Al adoptar este patrón, se facilita la modificación y ampliación del proceso de análisis, ya que se pueden cambiar las factorías o las implementaciones de sus métodos para adaptarse a diferentes requisitos sin afectar el código existente.

En resumen, mientras que los scripts en la carpeta "scripts" representan un enfoque detallado y específico para cada tarea, el uso de factorías en el análisis de datos introduce una abstracción que ofrece modularidad, flexibilidad y facilidad de mantenimiento en el proceso de análisis.





Este apartado abarca tres scripts alojados en la carpeta "scripts", los cuales modelan y estructuran los datos para el análisis:

### exploracion_analisis.py:

Este script emplea la biblioteca Pandas para la carga del archivo CSV "activaciones_samur_2023(1).csv" situado en la carpeta "datos". Posteriormente, se realiza un resumen estadístico de los datos, facilitando una primera visión del conjunto de información. Además, se utilizan las librerías Seaborn y Matplotlib para generar dos histogramas, uno representando la distribución de valores en la columna "Distrito" y otro en la columna "Hospital". Los gráficos resultantes se almacenan como imágenes en la carpeta "resultados".
```
import pandas as pd

# Leer el archivo CSV para la exploración y análisis inicial
data = pd.read_csv("EJERCICIO 1/datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")

# Resumen de datos estadísticos
summary = data.describe()
print(summary)

import seaborn as sns
import matplotlib.pyplot as plt

# Graficar la distribución de una columna usando Seaborn uy plt
sns.histplot(data['Distrito'], bins=20)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores')
plt.savefig('EJERCICIO 1/resultados/Distrito.png')
plt.show()

# Graficar la distribución de una columna usando Seaborn y plt
sns.histplot(data['Hospital'], bins=20)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Distribución de Valores')
plt.savefig('EJERCICIO 1/resultados/Hospital.png')
plt.show()
```
