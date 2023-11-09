El link del repositorio es: https://github.com/carlospuigserver/Desarrollo-OO.git

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


## Punto 4-Análisis y Representación:

El script Activaciones_diarias.py, dentro de la carpeta Analisis_y_representación, la cual está en AbstractFactoryMethod, muestra la implementación del análisis y representación de las activaciones utilizando las fábricas previamente creadas en el patrón Abstract Factory. El objetivo es mostrar la media de activaciones por día en cada mes, y un histograma de las activaciones.


### Fábricas Abstractas:

Se utilizan las fábricas definidas previamente para cálculos estadísticos y visualizaciones gráficas en el análisis de los datos.

### Cálculo de la Media de Actividades Diarias:

El script carga el archivo CSV que contiene las activaciones del SAMUR.
Para cada mes ('ENERO', 'FEBRERO', 'MARZO', ..., 'SEPTIEMBRE'), se calcula la media de activaciones por día.
Se realiza este cálculo tomando en cuenta el conteo de activaciones por hora, dividiendo esto por el número de días únicos en ese mes para obtener la media diaria.

### Generación de Histogramas:

Se genera un histograma para cada mes, mostrando la distribución de las activaciones a lo largo del día.
Para cada mes, se toma la hora de solicitud de las activaciones y se crea un histograma para representar esta distribución.

### Resultados:

La información de la media de activaciones por día se imprime en la consola y se guarda en el archivo de texto media_actividades.txt.
Para cada mes, se muestra la media de actividades por día y se generan los histogramas correspondientes, los cuales se guardan en los archivos de imagen (no mencionado explícitamente, pero se asume que se generan).

Este enfoque modular y estructurado, usando fábricas y clases Abstract Factory, permite una manera más clara y organizada de realizar análisis estadísticos y representaciones gráficas sobre los datos, facilitando la comprensión y la reutilización de funcionalidades.


```
import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

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

# Producto Concreto para Histograma
class Histograma(GraficosFactory):
    def crear_histograma(self, datos, titulo):
        plt.hist(datos)
        plt.title(titulo)
        plt.xlabel('Hora del día')
        plt.ylabel('Cantidad de activaciones')
        plt.show()

# Cargar el archivo CSV
datos = pd.read_csv("EJERCICIO 1/datos/activaciones_samur_2023(1).csv", sep=';')

meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE']
fabrica_histograma = Histograma()

with open("EJERCICIO 1/AbstractFactoryMethod/Analisis_y_representación/media_actividades.txt", "w") as archivo_txt:
    for mes in meses:
        datos_mes = datos[datos['Mes'] == mes]
        hora_solicitud = pd.to_datetime(datos_mes['Hora Solicitud'])
        media_actividades = hora_solicitud.dt.hour.count() / hora_solicitud.dt.normalize().nunique()  # Cálculo de la media diaria

        print(f"La media de activaciones por dia en {mes} es: {media_actividades:.2f}")
        archivo_txt.write(f"La media de activaciones por dia en {mes} es: {media_actividades:.2f}\n")
        fabrica_histograma.crear_histograma(hora_solicitud.dt.hour, f'Histograma de Activaciones en {mes} por Hora del Día'
```




# EJERCICIO 2 
Prácticamente todo el trabajo de este ejercicio ha sido realizado en otro repositorio, el cual cree en un momento dado por la incapacidad de hacerlo en este, no me estaba funcionando, así que en este, gran parte de los commits han sido copiar y pegar el código y por supuesto la estructura del otro repositorio. Por el remoto caso de que interese mirar el repositorio. aquí está su link: https://github.com/carlospuigserver/pizza2.git

## Contexto:
Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder

La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.

Características a considerar:

1-Tipo de masa: Variedades premium desde masas delgadas hasta masas fermentadas por 48 horas, con opciones de ingredientes especiales.

2-Salsa base: Desde salsas clásicas hasta salsas de autor, incluyendo opciones veganas y de edición limitada.

3-Ingredientes principales: Una gama que abarca desde ingredientes locales hasta importados de especialidad, todos categorizados por su origen, tipo y rareza.

4-Técnicas de cocción: Diversidad que abarca desde hornos tradicionales hasta técnicas modernas de cocina molecular.

5-Presentación: Opciones que van desde estilos clásicos hasta presentaciones que son verdaderas obras de arte.

6-Maridajes recomendados: Una base de datos con cientos de opciones de vinos, cervezas y cocteles, con recomendaciones basadas en las elecciones de los ingredientes de la pizza.

7-Extras y finalizaciones: Desde bordes especiales hasta acabados con ingredientes gourmet como trufas y caviar.

## Objetivos:
Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.

Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.

Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.

Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.

Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.

Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.

Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.

Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.


## Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.

El patrón de diseño Builder se emplea cuando se necesita crear un objeto complejo, compuesto de partes que deben ensamblarse en varios pasos, mientras se tiene la posibilidad de crear diferentes representaciones del mismo objeto. En el contexto de la programación de pizza, el patrón Builder se adapta bien, ya que una pizza tiene muchos componentes (masa, salsa, ingredientes, etc.) y, dependiendo de las preferencias del cliente, se pueden ensamblar de múltiples maneras para crear distintos tipos de pizza. Los Builders ayudan a separar el proceso de creación de objetos complejos, permitiendo la construcción paso a paso, con la posibilidad de variar los componentes para obtener diferentes configuraciones.

### MasaPizzaBuilder
El MasaPizzaBuilder se enfoca en la construcción de la masa de la pizza. Establece métodos para construir diferentes tipos de masas, como masa delgada, masa de 48 horas, estilo Napolitano, entre otros. Además, proporciona un método para obtener la masa construida. Su finalidad es aislar la construcción de la masa de la pizza de la lógica del negocio general y permitir la variación en la construcción de la masa. Este se implementa en masa_builder.py

```
from abc import ABC, abstractmethod

# Producto
class MasaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de masa elegida: {self.tipo}"

# Builder abstracto
class BuilderMasaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_masa_delgada(self):
        pass

    @abstractmethod
    def construir_masa_48_horas(self):
        pass

    @abstractmethod
    def construir_masa_madre(self):
        pass

    @abstractmethod
    def construir_masa_poolish(self):
        pass

    @abstractmethod
    def construir_masa_napolitana(self):
        pass

    @abstractmethod
    def construir_masa_new_york_style(self):
        pass

    @abstractmethod
    def construir_masa_chicago_style(self):
        pass

    @abstractmethod
    def construir_masa_siciliana(self):
        pass

    @abstractmethod
    def construir_masa_cracker(self):
        pass

    @abstractmethod
    def obtener_masa(self):
        pass

# Concrete Builder
class MasaPizzaBuilder(BuilderMasaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.masa = MasaPizza()

    def construir_masa_delgada(self):
        self.masa.tipo = "Delgada"

    def construir_masa_48_horas(self):
        self.masa.tipo = "48 Horas"

    def construir_masa_madre(self):
        self.masa.tipo = "Madre"

    def construir_masa_poolish(self):
        self.masa.tipo = "Poolish"

    def construir_masa_napolitana(self):
        self.masa.tipo = "Napolitana"

    def construir_masa_new_york_style(self):
        self.masa.tipo = "New York Style"

    def construir_masa_chicago_style(self):
        self.masa.tipo = "Chicago Style"

    def construir_masa_siciliana(self):
        self.masa.tipo = "Siciliana"

    def construir_masa_cracker(self):
        self.masa.tipo = "Cracker"

    def obtener_masa(self):
        return self.masa

# Director (Cliente)
class Cliente:
    def elegir_masa(self, builder):
        print("Tipos de masa disponibles:")
        tipos_masa = [
            "Delgada",
            "48 Horas",
            "Madre",
            "Poolish",
            "Napolitana",
            "New York Style",
            "Chicago Style",
            "Siciliana",
            "Cracker"
        ]

        print("Elija el tipo de masa escribiendo su nombre:")
        for tipo in tipos_masa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido == "Delgada":
            builder.construir_masa_delgada()
        elif tipo_elegido == "48 Horas":
            builder.construir_masa_48_horas()
        elif tipo_elegido == "Madre":
            builder.construir_masa_madre()
        elif tipo_elegido == "Poolish":
            builder.construir_masa_poolish()
        elif tipo_elegido == "Napolitana":
            builder.construir_masa_napolitana()
        elif tipo_elegido == "New York Style":
            builder.construir_masa_new_york_style()
        elif tipo_elegido == "Chicago Style":
            builder.construir_masa_chicago_style()
        elif tipo_elegido == "Siciliana":
            builder.construir_masa_siciliana()
        elif tipo_elegido == "Cracker":
            builder.construir_masa_cracker()
        else:
            print("Tipo de masa no válido")

        return builder.obtener_masa()

if __name__ == "__main__":
    builder = MasaPizzaBuilder()
    cliente = Cliente()

    masa_elegida = cliente.elegir_masa(builder)
    print(masa_elegida)
```



### SalsaPizzaBuilder
El SalsaPizzaBuilder está diseñado para crear distintos tipos de salsas para pizzas. Proporciona métodos para la construcción de salsas como la marinara, de pesto, BBQ, entre otras. Al igual que el MasaPizzaBuilder, su objetivo principal es encapsular la lógica de construcción de la salsa y permitir configuraciones personalizadas. Este se implementa en salsa_builder.py

```
from abc import ABC, abstractmethod

# Producto
class SalsaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de salsa elegida: {self.tipo}"

# Builder abstracto
class BuilderSalsaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_salsa_tomate_clasica(self):
        pass

    @abstractmethod
    def construir_salsa_marinara(self):
        pass

    @abstractmethod
    def construir_salsa_pesto(self):
        pass

    @abstractmethod
    def construir_salsa_blanca(self):
        pass

    @abstractmethod
    def construir_salsa_bbq(self):
        pass

    @abstractmethod
    def construir_salsa_champinones(self):
        pass

    @abstractmethod
    def construir_salsa_tomate_sin_gluten(self):
        pass

    @abstractmethod
    def construir_salsa_autor(self):
        pass

    @abstractmethod
    def construir_salsa_edicion_limitada(self):
        pass

    @abstractmethod
    def obtener_salsa(self):
        pass

# Concrete Builder
class SalsaPizzaBuilder(BuilderSalsaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.salsa = SalsaPizza()

    def construir_salsa_tomate_clasica(self):
        self.salsa.tipo = "Tomate Clásica"

    def construir_salsa_marinara(self):
        self.salsa.tipo = "Marinara"

    def construir_salsa_pesto(self):
        self.salsa.tipo = "Pesto"

    def construir_salsa_blanca(self):
        self.salsa.tipo = "Blanca"

    def construir_salsa_bbq(self):
        self.salsa.tipo = "BBQ"

    def construir_salsa_champinones(self):
        self.salsa.tipo = "Champiñones"

    def construir_salsa_tomate_sin_gluten(self):
        self.salsa.tipo = "Tomate sin gluten"

    def construir_salsa_autor(self):
        self.salsa.tipo = "Autor"

    def construir_salsa_edicion_limitada(self):
        self.salsa.tipo = "Edición Limitada"

    def obtener_salsa(self):
        return self.salsa

# Director (Cliente)
class Cliente:
    def elegir_salsa(self, builder):
        print("Tipos de salsa disponibles:")
        tipos_salsa = [
            "Tomate Clásica",
            "Marinara",
            "Pesto",
            "Blanca",
            "BBQ",
            "Champiñones",
            "Tomate sin gluten",
            "Autor",
            "Edición Limitada"
        ]

        print("Elija el tipo de salsa escribiendo su nombre:")
        for tipo in tipos_salsa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido == "Tomate Clásica":
            builder.construir_salsa_tomate_clasica()
        elif tipo_elegido == "Marinara":
            builder.construir_salsa_marinara()
        elif tipo_elegido == "Pesto":
            builder.construir_salsa_pesto()
        elif tipo_elegido == "Blanca":
            builder.construir_salsa_blanca()
        elif tipo_elegido == "BBQ":
            builder.construir_salsa_bbq()
        elif tipo_elegido == "Champiñones":
            builder.construir_salsa_champinones()
        elif tipo_elegido == "Tomate sin gluten":
            builder.construir_salsa_tomate_sin_gluten()
        elif tipo_elegido == "Autor":
            builder.construir_salsa_autor()
        elif tipo_elegido == "Edición Limitada":
            builder.construir_salsa_edicion_limitada()
        else:
            print("Tipo de salsa no válido")

        return builder.obtener_salsa()

if __name__ == "__main__":
    builder = SalsaPizzaBuilder()
    cliente = Cliente()

    salsa_elegida = cliente.elegir_salsa(builder)
    print(salsa_elegida)
```


### IngredientesPizzaBuilder
Este builder se encarga de la construcción de los ingredientes para la pizza. Define métodos para agregar diferentes tipos de ingredientes, como carne, queso, mariscos y vegetales. Ofrece flexibilidad para añadir o quitar ingredientes de la pizza, permitiendo la personalización de acuerdo a las preferencias del cliente.Es implementado en ingredientes_builder.py

```
from abc import ABC, abstractmethod

# Producto
class IngredientesPizza:
    def __init__(self):
        self.queso = []
        self.carne = []
        self.mariscos = []
        self.vegetales = []
        
    def __str__(self):
        return (f"Ingredientes elegidos: "
                f"\nQueso: {', '.join(self.queso) if self.queso else 'Ninguno'}"
                f"\nCarne: {', '.join(self.carne) if self.carne else 'Ninguno'}"
                f"\nMariscos: {', '.join(self.mariscos) if self.mariscos else 'Ninguno'}"
                f"\nVegetales: {', '.join(self.vegetales) if self.vegetales else 'Ninguno'}")

# Builder abstracto
class BuilderIngredientesPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def anadir_queso(self):
        pass

    @abstractmethod
    def anadir_carne(self):
        pass

    @abstractmethod
    def anadir_mariscos(self):
        pass

    @abstractmethod
    def anadir_vegetales(self):
        pass

    @abstractmethod
    def obtener_ingredientes(self):
        pass

# Concrete Builder
class IngredientesPizzaBuilder(BuilderIngredientesPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.ingredientes = IngredientesPizza()

    def anadir_queso(self):
        print("¿Desea agregar queso? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            quesos = [
                "Mozzarella", "Parmesano", "Cheddar", "Gouda", "Provolone"
            ]
            print("Tipos de queso disponibles:")
            for queso in quesos:
                print(f"- {queso}")
            queso_elegido = input("Elija el tipo de queso: ").capitalize()
            if queso_elegido in quesos:
                self.ingredientes.queso.append(queso_elegido)
            else:
                print("Tipo de queso no válido")

    def anadir_carne(self):
        print("¿Desea agregar carne? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            carnes = [
                "Pepperoni", "Pollo", "Jamon", "Tocino"
            ]
            print("Tipos de carne disponibles:")
            for carne in carnes:
                print(f"- {carne}")
            carne_elegida = input("Elija el tipo de carne: ").capitalize()
            if carne_elegida in carnes:
                self.ingredientes.carne.append(carne_elegida)
            else:
                print("Tipo de carne no válido")

    def anadir_mariscos(self):
        print("¿Desea agregar mariscos? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            mariscos = [
                "Anchoas", "Camarones", "Mejillones", "Calamares"
            ]
            print("Tipos de mariscos disponibles:")
            for marisco in mariscos:
                print(f"- {marisco}")
            marisco_elegido = input("Elija el tipo de marisco: ").capitalize()
            if marisco_elegido in mariscos:
                self.ingredientes.mariscos.append(marisco_elegido)
            else:
                print("Tipo de marisco no válido")

    def anadir_vegetales(self):
        print("¿Desea agregar vegetales? (Sí/No)")
        respuesta = input()
        if respuesta.lower() == "sí" or respuesta.lower() == "si":
            vegetales = [
                "Champiñones", "Pimientos", "Cebolla", "Aceitunas", "Tomate", "Espinacas", "Alcachofas", "Berenjena"
            ]
            print("Tipos de vegetales disponibles:")
            for vegetal in vegetales:
                print(f"- {vegetal}")
            vegetal_elegido = input("Elija el tipo de vegetal: ").capitalize()
            if vegetal_elegido in vegetales:
                self.ingredientes.vegetales.append(vegetal_elegido)
            else:
                print("Tipo de vegetal no válido")

    def obtener_ingredientes(self):
        return self.ingredientes

# Cliente
# Cliente
class Cliente:
    def elegir_ingredientes(self, builder):
        print("Seleccione los ingredientes:")
        builder.anadir_queso()
        builder.anadir_carne()
        builder.anadir_mariscos()
        builder.anadir_vegetales()
        return builder.obtener_ingredientes()

if __name__ == "__main__":
    builder = IngredientesPizzaBuilder()
    cliente = Cliente()

    ingredientes_elegidos = cliente.elegir_ingredientes(builder)
    print(ingredientes_elegidos)
```



### BebidaPizzaPizzaBuilder
La BebidaPizzaBuildder se centra en definir los maridajes de la pizza con bebidas. Proporciona métodos para construir diferentes tipos de bebidas que pueden complementar la pizza, como vino blanco, tinto, cerveza, etc. Permite elegir la bebida más adecuada para acompañar el tipo de pizza seleccionada. Este lo vemos implementado en maridajes_builder.py

```
from abc import ABC, abstractmethod

# Producto
class BebidaPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de bebida elegida: {self.tipo}"

# Builder abstracto
class BuilderBebidaPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_vino_blanco(self):
        pass

    @abstractmethod
    def construir_vino_tinto(self):
        pass

    @abstractmethod
    def construir_vino_rosado(self):
        pass

    @abstractmethod
    def construir_cerveza(self):
        pass

    @abstractmethod
    def construir_coctel(self):
        pass

    @abstractmethod
    def obtener_bebida(self):
        pass

# Concrete Builder
class BebidaPizzaBuilder(BuilderBebidaPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.bebida = BebidaPizza()

    def construir_vino_blanco(self):
        self.bebida.tipo = "Vino Blanco"

    def construir_vino_tinto(self):
        self.bebida.tipo = "Vino Tinto"

    def construir_vino_rosado(self):
        self.bebida.tipo = "Vino Rosado"

    def construir_cerveza(self):
        self.bebida.tipo = "Cerveza"

    def construir_coctel(self):
        self.bebida.tipo = "Coctel"

    def obtener_bebida(self):
        return self.bebida

# Cliente
class Cliente:
    def elegir_bebida(self, builder):
        print("Tipos de bebidas disponibles:")
        tipos_bebida = [
            "Vino Blanco",
            "Vino Tinto",
            "Vino Rosado",
            "Cerveza",
            "Coctel"
        ]

        print("Elija el tipo de bebida escribiendo su nombre:")
        for tipo in tipos_bebida:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido == "Vino Blanco":
            builder.construir_vino_blanco()
        elif tipo_elegido == "Vino Tinto":
            builder.construir_vino_tinto()
        elif tipo_elegido == "Vino Rosado":
            builder.construir_vino_rosado()
        elif tipo_elegido == "Cerveza":
            builder.construir_cerveza()
        elif tipo_elegido == "Coctel":
            builder.construir_coctel()
        else:
            print("Tipo de bebida no válido")

        return builder.obtener_bebida()

if __name__ == "__main__":
    builder = BebidaPizzaBuilder()
    cliente = Cliente()

    bebida_elegida = cliente.elegir_bebida(builder)
    print(bebida_elegida)
```


### CoccionPizzaBuilder
Este builder se encarga de la técnica de cocción de la pizza. Ofrece métodos para construir técnicas de cocción, como el horno de leña, eléctrico, piedra para pizzas y parrilla para pizzas. Permite seleccionar la técnica de cocción deseada para la preparación de la pizza. Este esta implementado en coccion_pizza.py

```
from abc import ABC, abstractmethod

# Producto
class CoccionPizza:
    def __init__(self):
        self.metodo = ""
        
    def __str__(self):
        return f"Método de cocción elegido: {self.metodo}"

# Builder abstracto
class BuilderCoccionPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_horno_lena(self):
        pass

    @abstractmethod
    def construir_horno_electrico(self):
        pass

    @abstractmethod
    def construir_piedra_pizzas(self):
        pass

    @abstractmethod
    def construir_parrilla_pizzas(self):
        pass

    @abstractmethod
    def obtener_coccion(self):
        pass

# Concrete Builder
class CoccionPizzaBuilder(BuilderCoccionPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.coccion = CoccionPizza()

    def construir_horno_lena(self):
        self.coccion.metodo = "Horno de leña"

    def construir_horno_electrico(self):
        self.coccion.metodo = "Horno eléctrico"

    def construir_piedra_pizzas(self):
        self.coccion.metodo = "Piedra para pizzas"

    def construir_parrilla_pizzas(self):
        self.coccion.metodo = "Parrilla para pizzas"

    def obtener_coccion(self):
        return self.coccion

# Director (Cliente)
class Cliente:
    def elegir_coccion(self, builder):
        print("Métodos de cocción disponibles:")
        metodos_coccion = [
            "Horno de leña",
            "Horno eléctrico",
            "Piedra para pizzas",
            "Parrilla para pizzas"
        ]

        print("Elija el método de cocción escribiendo su nombre:")
        for metodo in metodos_coccion:
            print(f"- {metodo}")

        metodo_elegido = input("Su elección: ").capitalize()

        if metodo_elegido == "Horno de leña":
            builder.construir_horno_lena()
        elif metodo_elegido == "Horno eléctrico":
            builder.construir_horno_electrico()
        elif metodo_elegido == "Piedra para pizzas":
            builder.construir_piedra_pizzas()
        elif metodo_elegido == "Parrilla para pizzas":
            builder.construir_parrilla_pizzas()
        else:
            print("Método de cocción no válido")

        return builder.obtener_coccion()

if __name__ == "__main__":
    builder = CoccionPizzaBuilder()
    cliente = Cliente()

    coccion_elegida = cliente.elegir_coccion(builder)
    print(coccion_elegida)
```



### PresentacionPizzaBuilder
El PresentacionPizzaBuilder define cómo se presentará la pizza. Ofrece métodos para construir diferentes tipos de presentaciones, como tabla de madera, plato de cerámica clásica, plato de cristal, entre otros. Facilita la selección de la presentación de la pizza.


```
from abc import ABC, abstractmethod

# Producto
class PresentacionPizza:
    def __init__(self):
        self.tipo = ""
        
    def __str__(self):
        return f"Tipo de presentación elegida: {self.tipo}"

# Builder abstracto
class BuilderPresentacionPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def construir_tabla_madera(self):
        pass

    @abstractmethod
    def construir_plato_ceramica_clasica(self):
        pass

    @abstractmethod
    def construir_plataforma_plata(self):
        pass

    @abstractmethod
    def construir_plataforma_oro(self):
        pass

    @abstractmethod
    def construir_plato_cristal(self):
        pass

    @abstractmethod
    def construir_sobre_piedra(self):
        pass

    @abstractmethod
    def construir_plato_terracota(self):
        pass

    @abstractmethod
    def construir_plato_porcelana(self):
        pass

    @abstractmethod
    def obtener_presentacion(self):
        pass

# Concrete Builder
class PresentacionPizzaBuilder(BuilderPresentacionPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.presentacion = PresentacionPizza()

    def construir_tabla_madera(self):
        self.presentacion.tipo = "Tabla de madera"

    def construir_plato_ceramica_clasica(self):
        self.presentacion.tipo = "Plato de cerámica clásica"

    def construir_plataforma_plata(self):
        self.presentacion.tipo = "Sobre plataforma de plata"

    def construir_plataforma_oro(self):
        self.presentacion.tipo = "Sobre plataforma de oro"

    def construir_plato_cristal(self):
        self.presentacion.tipo = "Plato de cristal"

    def construir_sobre_piedra(self):
        self.presentacion.tipo = "Sobre piedra"

    def construir_plato_terracota(self):
        self.presentacion.tipo = "Plato de terracota"

    def construir_plato_porcelana(self):
        self.presentacion.tipo = "Plato de porcelana"

    def obtener_presentacion(self):
        return self.presentacion

# Director (Cliente)
class Cliente:
    def elegir_presentacion(self, builder):
        print("Opciones de presentación disponibles:")
        opciones_presentacion = [
            "Tabla de madera",
            "Plato de cerámica clásica",
            "Sobre plataforma de plata",
            "Sobre plataforma de oro",
            "Plato de cristal",
            "Sobre piedra",
            "Plato de terracota",
            "Plato de porcelana"
        ]

        print("Elija el tipo de presentación escribiendo su nombre o número:")
        for idx, opcion in enumerate(opciones_presentacion, start=1):
            print(f"{idx}. {opcion}")

        opcion_elegida = input("Su elección: ").capitalize()

        if opcion_elegida == "Tabla de madera" or opcion_elegida == "1":
            builder.construir_tabla_madera()
        elif opcion_elegida == "Plato de cerámica clásica" or opcion_elegida == "2":
            builder.construir_plato_ceramica_clasica()
        elif opcion_elegida == "Sobre plataforma de plata" or opcion_elegida == "3":
            builder.construir_plataforma_plata()
        # Continuar con las demás opciones en un flujo similar

        return builder.obtener_presentacion()

if __name__ == "__main__":
    builder = PresentacionPizzaBuilder()
    cliente = Cliente()

    presentacion_elegida = cliente.elegir_presentacion(builder)
    print(presentacion_elegida)
```

### ExtrasPizzaBuilder
Este builder se dedica a los elementos adicionales de la pizza, como bordes rellenos e ingredientes gourmet. Permite seleccionar bordes rellenos con opciones como queso, ajo y queso parmesano, y ingredientes gourmet como trufas, caviar, jamón ibérico, entre otros. Implementado en extras_builder.py

```
from abc import ABC, abstractmethod

# Producto
class ExtrasPizza:
    def __init__(self):
        self.borde_relleno = ""
        self.ingredientes_gourmet = []

    def __str__(self):
        return f"Borde relleno: {self.borde_relleno}, Ingredientes gourmet: {self.ingredientes_gourmet}"

# Builder abstracto
class BuilderExtrasPizza(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def anadir_borde_relleno(self, opcion):
        pass

    @abstractmethod
    def anadir_ingredientes_gourmet(self, opcion):
        pass

    @abstractmethod
    def obtener_extras(self):
        pass

# Concrete Builder
class ExtrasPizzaBuilder(BuilderExtrasPizza):
    def __init__(self):
        self.reset()

    def reset(self):
        self.extras = ExtrasPizza()

    def anadir_borde_relleno(self, opcion):
        self.extras.borde_relleno = opcion

    def anadir_ingredientes_gourmet(self, opcion):
        self.extras.ingredientes_gourmet.append(opcion)

    def obtener_extras(self):
        return self.extras

# Director (Cliente)
class Cliente:
    def elegir_extras(self, builder):
        quiere_borde_relleno = input("¿Desea su borde relleno? (Sí/No): ")
        if quiere_borde_relleno.lower() == "sí":
            print("¿Qué borde relleno desea?")
            print("1. Relleno de queso")
            print("2. Ajo y queso parmesano")
            print("3. Crust de queso")
            print("4. Relleno de pepperoni o jamón")
            print("5. Relleno de verduras")

            borde = input("Su elección (borde relleno): ")
            opciones_borde = {
                "1": "Relleno de queso",
                "2": "Ajo y queso parmesano",
                "3": "Crust de queso",
                "4": "Relleno de pepperoni o jamón",
                "5": "Relleno de verduras"
            }
            builder.anadir_borde_relleno(opciones_borde.get(borde, ""))

        quiere_ingredientes_gourmet = input("¿Desea algún ingrediente gourmet? (Sí/No): ")
        if quiere_ingredientes_gourmet.lower() == "sí":
            print("¿Qué ingrediente gourmet desea?")
            print("1. Trufas")
            print("2. Caviar")
            print("3. Foie Gras")
            print("4. Jamón Ibérico")
            print("5. Quesos exclusivos")
            print("6. Setas silvestres")
            print("7. Mariscos de alta calidad")
            print("8. Verduras orgánicas y raras")

            ingrediente = input("Su elección (ingrediente gourmet): ")
            opciones_ingredientes = {
                "1": "Trufas",
                "2": "Caviar",
                "3": "Foie Gras",
                "4": "Jamón Ibérico",
                "5": "Quesos exclusivos",
                "6": "Setas silvestres",
                "7": "Mariscos de alta calidad",
                "8": "Verduras orgánicas y raras"
            }
            builder.anadir_ingredientes_gourmet(opciones_ingredientes.get(ingrediente, ""))

        return builder.obtener_extras()

if __name__ == "__main__":
    builder = ExtrasPizzaBuilder()
    cliente = Cliente()

    extras_elegidos = cliente.elegir_extras(builder)
    print(extras_elegidos)
```



## Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.

El módulo cliente.py desencadena una interacción esencial entre los usuarios y el proceso de construcción de una pizza. La implementación de este script sigue varios pasos clave que son fundamentales para el éxito y la utilidad del programa.

### Registro y autenticación de usuarios:

La posibilidad de que los usuarios se registren y autentiquen es vital para un servicio personalizado y seguro. El registro permite a los usuarios guardar sus preferencias y recuerda sus selecciones anteriores. La autenticación garantiza la privacidad y seguridad, al limitar el acceso a la creación de pedidos de pizza solo a usuarios registrados y verificados.
Clase Cliente:

### La clase Cliente 
Actúa como un puente entre las preferencias del usuario y la lógica de construcción de la pizza, permitiendo una interfaz intuitiva y amigable para que los usuarios elijan sus preferencias. Cada método dentro de esta clase se enfoca en un aspecto específico de la pizza, desde la masa hasta los extras, facilitando las decisiones del usuario paso a paso.

### Interacción de usuario con Builders:
Cada método en la clase Cliente interactúa con su Builder respectivo, permitiendo al usuario definir las características de la pizza. La elección de cada componente se almacena en instancias específicas de los builders correspondientes. Esta separación de lógica de construcción de la pizza y selección de preferencias del usuario resulta en un código modular y fácil de mantener.


### Interacción y almacenamiento de datos:
Si el usuario se autentica exitosamente y selecciona las características de la pizza, se almacena el pedido en un archivo CSV. Esta funcionalidad es crucial, ya que permite registrar y rastrear los pedidos realizados por los usuarios. Además, posibilita la personalización de futuras interacciones, aprendiendo de las preferencias pasadas de los usuarios para ofrecer experiencias más adaptadas y satisfactorias.


### Flujo de ejecución:
El flujo de ejecución del programa está estructurado para guiar a los usuarios a través de las distintas etapas de selección de componentes de pizza. Desde el registro inicial hasta la selección de los ingredientes, bebidas y extras, el programa facilita una experiencia de usuario intuitiva y fluida.
Estos pasos, centrados en la experiencia del usuario, la modularidad y el almacenamiento de datos, son vitales para la eficiencia y el éxito del programa. Permiten una interacción ágil y agradable, la gestión eficaz de la información, y la adaptación a las preferencias y necesidades del usuario, lo que conduce a una experiencia de usuario más satisfactoria y personalizada.



```
import csv
from Builders.masa_builder import MasaPizzaBuilder
from Builders.salsa_builder import SalsaPizzaBuilder
from Builders.ingredientes_builder import IngredientesPizzaBuilder
from Builders.maridajes_builder import BebidaPizzaBuilder
from Builders.coccion_builder import CoccionPizzaBuilder
from Builders.presentacion_builder import PresentacionPizzaBuilder
from Builders.extras_builder import ExtrasPizzaBuilder

# Función para registrar un nuevo usuario
def registrar_nuevo_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")

    with open('EJERCICIO 2/Usuario/usuario.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre_usuario, contraseña])
        print(f"El usuario '{nombre_usuario}' se ha registrado con éxito.")

# Función para autenticar un usuario
def autenticar_usuario(nombre_usuario, contraseña):
    with open('EJERCICIO 2/Usuario/usuario.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:  # Verifica si la lista tiene al menos dos elementos
                if row[0] == nombre_usuario and row[1] == contraseña:
                    print(f"¡Bienvenido, {nombre_usuario}!")
                    return True

    print("Nombre de usuario o contraseña incorrectos.")
    return False

class Cliente:
    def elegir_masa(self, builder):
        print("Tipos de masa disponibles:")
        tipos_masa = [
            "Delgada",
            "48 Horas",
            "Madre",
            "Poolish",
            "Napolitana",
            "New York Style",
            "Chicago Style",
            "Siciliana",
            "Cracker"
        ]

        print("Elija el tipo de masa escribiendo su nombre:")
        for tipo in tipos_masa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido in tipos_masa:
            if tipo_elegido == "Delgada":
                builder.construir_masa_delgada()
            elif tipo_elegido == "48 Horas":
                builder.construir_masa_48_horas()
            elif tipo_elegido == "Madre":
                builder.construir_masa_madre()
            elif tipo_elegido == "Poolish":
                builder.construir_masa_poolish()
            elif tipo_elegido == "Napolitana":
                builder.construir_masa_napolitana()
            elif tipo_elegido == "New York Style":
                builder.construir_masa_new_york_style()
            elif tipo_elegido == "Chicago Style":
                builder.construir_masa_chicago_style()
            elif tipo_elegido == "Siciliana":
                builder.construir_masa_siciliana()
            elif tipo_elegido == "Cracker":
                builder.construir_masa_cracker()
            else:
                print("Tipo de salsa no válido")
                return None

            return builder.obtener_masa()

        else:
            print("Tipo de masa no disponible")
            return None
        

    def elegir_salsa(self, builder):
        print("Tipos de salsa disponibles:")
        tipos_salsa = [
            "Tomate Clásica",
            "Marinara",
            "Pesto",
            "Blanca",
            "BBQ",
            "Champiñones",
            "Tomate sin gluten",
            "Autor"
            
        ]

        print("Elija el tipo de salsa escribiendo su nombre:")
        for tipo in tipos_salsa:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido in tipos_salsa:
            if tipo_elegido == "Tomate Clásica":
                builder.construir_salsa_tomate_clasica()
            elif tipo_elegido == "Marinara":
                builder.construir_salsa_marinara()
            elif tipo_elegido == "Pesto":
                builder.construir_salsa_pesto()
            elif tipo_elegido == "Blanca":
                builder.construir_salsa_blanca()
            elif tipo_elegido == "BBQ":
                builder.construir_salsa_bbq()
            elif tipo_elegido == "Champiñones":
                builder.construir_salsa_champinones()
            elif tipo_elegido == "Tomate sin gluten":
                builder.construir_salsa_tomate_sin_gluten()
            elif tipo_elegido == "Autor":
                builder.construir_salsa_autor()
            else:
                print("Tipo de salsa no válido")
                return None

            return builder.obtener_salsa()

        else:
            print("Tipo de salsa no disponible")
            return None

    def elegir_ingredientes(self, builder):
        while True:
            print("Seleccione los ingredientes para la pizza:")
            builder.anadir_queso()
            builder.anadir_carne()
            builder.anadir_mariscos()
            builder.anadir_vegetales()

            respuesta = input("¿Desea agregar más ingredientes? (Sí/No): ").lower()
            if respuesta != 'sí' and respuesta != 'si':
                break
        return builder.obtener_ingredientes()
    
    def elegir_bebida(self, builder):
        print("Tipos de bebidas disponibles:")
        tipos_bebida = [
            "Vino Blanco",
            "Vino Tinto",
            "Vino Rosado",
            "Cerveza",
            "Coctel"
        ]

        print("Elija el tipo de bebida escribiendo su nombre:")
        for tipo in tipos_bebida:
            print(f"- {tipo}")

        tipo_elegido = input("Su elección: ").capitalize()

        if tipo_elegido == "Vino Blanco":
            builder.construir_vino_blanco()
        elif tipo_elegido == "Vino Tinto":
            builder.construir_vino_tinto()
        elif tipo_elegido == "Vino Rosado":
            builder.construir_vino_rosado()
        elif tipo_elegido == "Cerveza":
            builder.construir_cerveza()
        elif tipo_elegido == "Coctel":
            builder.construir_coctel()
        else:
            print("Tipo de bebida no válido")

        return builder.obtener_bebida()

    
    def elegir_coccion(self, builder):
        print("Métodos de cocción disponibles:")
        metodos_coccion = [
            "Horno de lena",
            "Horno eléctrico",
            "Piedra para pizzas",
            "Parrilla para pizzas"
        ]

        print("Elija el método de cocción escribiendo su nombre:")
        for metodo in metodos_coccion:
            print(f"- {metodo}")

        metodo_elegido = input("Su elección: ").capitalize()

        if metodo_elegido == "Horno de lena":
            builder.construir_horno_lena()
        elif metodo_elegido == "Horno electrico":
            builder.construir_horno_electrico()
        elif metodo_elegido == "Piedra para pizzas":
            builder.construir_piedra_pizzas()
        elif metodo_elegido == "Parrilla para pizzas":
            builder.construir_parrilla_pizzas()
        else:
            print("Método de cocción no válido")

        return builder.obtener_coccion()
    
    def elegir_presentacion(self, builder):
        print("Opciones de presentación disponibles:")
        opciones_presentacion = [
            "Tabla de madera",
            "Plato de cerámica clasica",
            "Sobre plataforma de plata",
            "Sobre plataforma de oro",
            "Plato de cristal",
            "Sobre piedra",
            "Plato de terracota",
            "Plato de porcelana"
        ]

        print("Elija el tipo de presentación escribiendo su nombre :")
        for idx, opcion in enumerate(opciones_presentacion, start=1):
            print(f"{idx}. {opcion}")

        opcion_elegida = input("Su elección: ").capitalize()

        if opcion_elegida == "Tabla de madera" :
            builder.construir_tabla_madera()
        elif opcion_elegida == "Plato de cerámica clásica" :
            builder.construir_plato_ceramica_clasica()
        elif opcion_elegida == "Sobre plataforma de plata" :
            builder.construir_plataforma_plata()
        elif opcion_elegida == "Sobre plataforma de oro":
            builder.construir_plataforma_oro()
        elif opcion_elegida == "Plato de cristal" :
            builder.construir_plato_cristal()
        elif opcion_elegida == "Sobre piedra" :
            builder.construir_sobre_piedra()
        elif opcion_elegida == "Plato de terracota" :
            builder.construir_plato_terracota()
        elif opcion_elegida == "Plato de porcelana"  :
            builder.construir_plato_porcelana()
        else:
            print("Opción de presentación no válida")

        return builder.obtener_presentacion()
    
    def elegir_extras(self, builder):
        opciones_borde = {
            "1": "Relleno de queso",
            "2": "Ajo y queso parmesano",
            "3": "Crust de queso",
            "4": "Relleno de pepperoni o jamón",
            "5": "Relleno de verduras"
        }

        opciones_ingredientes = {
            "1": "Trufas",
            "2": "Caviar",
            "3": "Foie Gras",
            "4": "Jamón Iberico",
            "5": "Quesos exclusivos",
            "6": "Setas silvestres",
            "7": "Mariscos de alta calidad",
            "8": "Verduras orgánicas y raras"
        }

        quiere_borde_relleno = input("¿Desea su borde relleno? (Sí/No): ")
        borde_elegido = opciones_borde.get(input("Su elección (borde relleno) (numero 1-5) : "), "")

        quiere_ingredientes_gourmet = input("¿Desea algún ingrediente gourmet? (Sí/No): ")
        ingredientes_elegidos = []
        
        while quiere_ingredientes_gourmet.lower() == "sí":
            ingrediente = input("Su elección (ingrediente gourmet) (numero 1-8): ")
            ingrediente_elegido = opciones_ingredientes.get(ingrediente, "")
            if ingrediente_elegido:
                ingredientes_elegidos.append(ingrediente_elegido)
            else:
                print("Opción de ingrediente no válida.")
            quiere_ingredientes_gourmet = input("¿Desea otro ingrediente gourmet? (Sí/No): ")

        builder.anadir_borde_relleno(borde_elegido)
        builder.anadir_ingredientes_gourmet(ingredientes_elegidos)
        return builder.obtener_extras()


    

if __name__ == "__main__":
    masa_builder = MasaPizzaBuilder()
    salsa_builder = SalsaPizzaBuilder()
    ingredientes_builder = IngredientesPizzaBuilder()
    bebida_builder = BebidaPizzaBuilder()
    coccion_builder = CoccionPizzaBuilder()
    builder = PresentacionPizzaBuilder()
    extras_builder = ExtrasPizzaBuilder()
    cliente = Cliente()

    registrar_nuevo_usuario()  # Registra un nuevo usuario

    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if autenticar_usuario(nombre_usuario, contraseña):
        masa_elegida = cliente.elegir_masa(masa_builder)
        if masa_elegida:
            print(f"El usuario {nombre_usuario} ha elegido la masa {masa_elegida.tipo}")

            salsa_elegida = cliente.elegir_salsa(salsa_builder)
            if salsa_elegida:
                print(f"El usuario {nombre_usuario} ha elegido la salsa {salsa_elegida.tipo}")

                ingredientes_elegidos = cliente.elegir_ingredientes(ingredientes_builder)
                if ingredientes_elegidos:
                    print(f"El usuario {nombre_usuario} ha elegido los siguientes ingredientes:")
                    print(ingredientes_elegidos)
                    
                    bebida_elegida = cliente.elegir_bebida(bebida_builder)
                    if bebida_elegida:
                      print(f"El usuario {nombre_usuario} ha elegido la bebida {bebida_elegida.tipo}")

                      coccion_elegida = cliente.elegir_coccion(coccion_builder)
                      if coccion_elegida:
                        print(f"El usuario {nombre_usuario} ha elegido la técnica de cocción {coccion_elegida.metodo}")

                        presentacion_elegida = cliente.elegir_presentacion(builder)
                        if presentacion_elegida:
                         print(f"El usuario {nombre_usuario} ha elegido la presentación {presentacion_elegida.tipo}")
                        
                        extras_elegidos = cliente.elegir_extras(extras_builder)
                        print(f"Elegidos extras: {extras_elegidos}")
                         
                            
                    # Guardar los detalles del pedido en un archivo CSV (pizzas.csv)
                    with open('EJERCICIO 2/storage/pizzas.csv', 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            nombre_usuario,
                            f"Elegida masa: {masa_elegida.tipo}",
                            f"Elegida salsa: {salsa_elegida.tipo}",
                            f"Elegidos ingredientes: {ingredientes_elegidos}",
                            f"Elegida bebida: {bebida_elegida.tipo}",
                            f"Elegida tecnica de coccion: {coccion_elegida.metodo}",
                            f"Elegida presentación: {presentacion_elegida.tipo}",
                            f"Elegidos extras: {extras_elegidos}"
                            
                            
                        ])
                    print("Detalles del pedido guardados en pizzas.csv")

