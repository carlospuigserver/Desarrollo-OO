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
    # Presentar los resultados de la manera que desees
    print("Resultados estadísticos de la Duracion Intervencion (min):")
    print("Promedio:", resultado[0])
    print("Mediana:", resultado[1])
    print("Desviaciíon estándar:", resultado[2])
    print("Mínimo:", resultado[3])
    print("Máximo:", resultado[4])

    # Guardar los resultados en un archivo de texto
    with open("EJERCICIO 1/AbstractFactoryMethod/resultados_estadisticos_otra_columna.txt", 'w') as f:
        f.write(f"Promedio: {resultado[0]}\n")
        f.write(f"Mediana: {resultado[1]}\n")
        f.write(f"Desviacion estandar: {resultado[2]}\n")
        f.write(f"Minimo: {resultado[3]}\n")
        f.write(f"Maximo: {resultado[4]}\n")

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar la columna deseada
datos_columna = datos['Duracion Intervencion (min)']  # Reemplaza 'Nombre de la columna' por el nombre real

# Crear instancia del producto concreto (en este caso, ResumenEstadistico)
resumen_estadistico = ResumenEstadistico()

# Interactuar con los datos utilizando el producto concreto
interactuar_con_datos(resumen_estadistico, datos_columna)







