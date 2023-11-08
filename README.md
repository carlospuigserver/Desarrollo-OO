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
Los histogramas resultantes de las columnas "Distrito" y "Hospital" son guardados como imágenes en la carpeta "resultados".


### limpieza_procesamiento.py:

Este script utiliza Pandas para cargar el archivo CSV, eliminar filas con valores nulos en cualquier columna y reemplazar valores faltantes o no deseados por un valor por defecto. Posteriormente, los datos procesados se guardan en un archivo CSV llamado "datos_preprocesados.csv" en la carpeta "resultados".
```
import pandas as pd

# Cargar datos para limpieza y preprocesamiento
data = pd.read_csv("EJERCICIO 1/datos/activaciones_samur_2023(1).csv", sep=";", encoding="ISO-8859-1")



# Eliminar filas con valores nulos en cualquier columna
data = data.dropna()

# Reemplazar valores faltantes o no deseados con un valor por defecto
data.fillna(value='ValorPorDefecto', inplace=True)




# Guardar datos preprocesados
data.to_csv('EJERCICIO 1/resultados/datos_preprocesados.csv', sep=';', index=False, encoding='ISO-8859-1')
```
Los datos procesados, libres de valores nulos o no deseados, se almacenan en un nuevo archivo CSV llamado "datos_preprocesados.csv" dentro de la carpeta "resultados".


### modelado_estructuracion.py:

En este script, se carga el archivo de datos preprocesados desde el archivo CSV, se realiza un modelado estructural para el análisis añadiendo una nueva columna que calcula la duración de la intervención y se guardan los resultados en un archivo CSV denominado "datos_con_duracion.csv" en la carpeta "resultados".
```
import pandas as pd

# Cargar datos desde el archivo preprocesado
data = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')



# Realizar modelado y estructuración para análisis,crear una nueva columna calculando la duración de la intervención
data['Duracion Intervencion (min)'] = (pd.to_datetime(data['Hora Intervencion']) - pd.to_datetime(data['Hora Solicitud'])).dt.total_seconds() / 60

# Guardar resultados del modelado o estructuración si es necesario
data.to_csv('EJERCICIO 1/resultados/datos_con_duracion.csv', sep=';', encoding='ISO-8859-1', index=False)
```
Los resultados de este modelado estructural, incluyendo la columna que refleja la duración de la intervención, son almacenados en un archivo CSV llamado "datos_con_duracion.csv" dentro de la carpeta "resultados".


## Punto 3-Abstract Factory:

Aquí se diseña un "Abstract Factory" que permita crear diferentes tipos de análisis o representaciones de los datos


### Abstract Factory para Análisis Estadístico:
Dentro de la carpeta 'AbstractFactoryMethod' se encuentra una subcarpeta denominada 'Fabrica estadistica'. En esta ubicación, se han creado clases y métodos asociados al patrón Abstract Factory para realizar análisis estadísticos sobre los datos. En específico, el archivo 'fabrica_estadistica.py' contiene un ejemplo de implementación de esta fábrica.

Se define una clase Abstracta llamada 'EstadisticasFactory' con un método abstracto para generar un resumen estadístico. A su vez, se crea un producto concreto 'ResumenEstadistico' que implementa este método, permitiendo calcular el promedio, mediana, desviación estándar, valor mínimo y máximo de los datos.

El script interactúa con los datos del archivo CSV 'datos_con_duracion.csv' y, tras procesar la información a través de la clase 'ResumenEstadistico', imprime los resultados estadísticos en la consola y los almacena en un archivo de texto llamado 'resultados_estadisticos_otra_columna.txt' en la misma carpeta.

```
import pandas as pd
from abc import ABC, abstractmethod

# Fábrica Abstracta para Análisis Estadísticos
class EstadisticasFactory(ABC):
    @abstractmethod
    def crear_resumen_estadistico(self, datos):
        pass

# Producto Concreto para Resumen Estadístico
class ResumenEstadistico(EstadisticasFactory):
    def crear_resumen_estadistico(self, datos):
        # Calcula las estadísticas por separado
        promedio = datos.mean()
        mediana = datos.median()
        desviacion_estandar = datos.std()
        minimo = datos.min()
        maximo = datos.max()

        return promedio, mediana, desviacion_estandar, minimo, maximo

# Función que maneja la interacción entre el patrón Abstract Factory y el conjunto de datos
def interactuar_con_datos(producto, datos):
    resultado = producto.crear_resumen_estadistico(datos)
    
    print("Resultados estadísticos de la Duracion Intervencion (min):")
    print("Promedio:", resultado[0])
    print("Mediana:", resultado[1])
    print("Desviaciíon estándar:", resultado[2])
    print("Mínimo:", resultado[3])
    print("Máximo:", resultado[4])

    # Guardar los resultados en un archivo de texto
    with open("EJERCICIO 1/AbstractFactoryMethod/Fabrica Estadistica/resultados_estadisticos_otra_columna.txt", 'w') as f:
        f.write(f"Promedio: {resultado[0]}\n")
        f.write(f"Mediana: {resultado[1]}\n")
        f.write(f"Desviacion estandar: {resultado[2]}\n")
        f.write(f"Minimo: {resultado[3]}\n")
        f.write(f"Maximo: {resultado[4]}\n")

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar la columna deseada
datos_columna = datos['Duracion Intervencion (min)']  

# Crear instancia del producto concreto 
resumen_estadistico = ResumenEstadistico()

# Interactuar con los datos utilizando el producto concreto
interactuar_con_datos(resumen_estadistico, datos_columna)
```


### Abstract Factory para Visualizaciones Gráficas:
En el directorio 'AbstractFactoryMethod/Fabrica grafica' se encuentra el archivo 'fabrica_grafica.py', el cual incorpora una implementación de fábricas abstractas para generar visualizaciones gráficas.

Se define una clase abstracta 'GraficosFactory' con métodos abstractos para crear un histograma y un gráfico de barras. Se implementa el producto concreto 'Histograma' para generar estos tipos de gráficos.

El script carga los datos del archivo 'datos_con_duracion.csv', selecciona un conjunto de datos y calcula estadísticas sobre ellos utilizando una fábrica con métodos estáticos. Posteriormente, crea instancias de la clase 'Histograma' para generar visualizaciones gráficas: un histograma y un gráfico de barras, que representan la distribución de la duración de la intervención.

En resumen, se utilizan las fábricas para generar resúmenes estadísticos y visualizaciones gráficas, ofreciendo flexibilidad para realizar diferentes tipos de análisis de datos de manera modular y estructurada.

```
import pandas as pd
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

# Fábrica para cálculos estadísticos
class EstadisticasFactory:
    @staticmethod
    def calcular_estadisticas(datos):
        return datos.describe()

# Fábrica Abstracta para Visualizaciones Gráficas
class GraficosFactory(ABC):
    @abstractmethod
    def crear_histograma(self, datos):
        pass

    @abstractmethod
    def crear_grafico_barras(self, datos):
        pass

# Producto Concreto para Histograma
class Histograma(GraficosFactory):
    def crear_histograma(self, datos):
        plt.hist(datos)
        plt.title('Histograma')
        plt.show()

    def crear_grafico_barras(self, datos):
        datos.plot(kind='bar')
        plt.title('Gráfico de Barras')

        # Ajustes estéticos para el eje Y
        plt.yticks(fontsize=10)  
        plt.gca().yaxis.grid(True)  

        
        
        plt.gca().set_ylim([0, datos.max() * 1.1])  # Ajustar límites del eje Y
        plt.gca().yaxis.grid(True)  # Mostrar líneas de cuadrícula en el eje Y
        plt.gca().tick_params(axis='y', labelrotation=0)  # Rotar las etiquetas del eje Y
        plt.tight_layout()  # Ajustar el espaciado para evitar superposición

        plt.show()

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar las primeras 30 filas de la columna deseada
datos_columna = datos['Duracion Intervencion (min)'].head(30)  

# Usar la fábrica para calcular estadísticas
resultados = EstadisticasFactory.calcular_estadisticas(datos_columna)

# Crear instancias de las fábricas y productos concretos
fabrica_histograma = Histograma()

# Interactuar con los datos utilizando la fábrica de visualizaciones gráficas
fabrica_histograma.crear_histograma(datos_columna)
fabrica_histograma.crear_grafico_barras(datos_columna)
```



