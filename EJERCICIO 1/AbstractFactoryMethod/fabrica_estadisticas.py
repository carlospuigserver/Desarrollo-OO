from abc import ABC, abstractmethod
import pandas as pd

# Fábrica Abstracta para Análisis Estadísticos
class EstadisticasFactory(ABC):
    @abstractmethod
    def crear_resumen_estadistico(self, datos):
        pass

# Producto Concreto para Resumen Estadístico
class ResumenEstadistico(EstadisticasFactory):
    def crear_resumen_estadistico(self, datos):
        return datos.describe()

# Función que maneja la interacción entre el patrón Abstract Factory y el conjunto de datos
def interactuar_con_datos(factory, producto, datos):
    resultado = factory.crear_resumen_estadistico(datos)
    print(resultado)  # Puedes adaptar esto para guardar o mostrar los resultados de la manera que desees

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')

# Crear instancia de la fábrica de análisis estadísticos y producto concreto
factory_estadisticas = EstadisticasFactory()
resumen_estadistico = ResumenEstadistico()

# Interactuar con los datos utilizando la fábrica de análisis estadísticos
interactuar_con_datos(factory_estadisticas, resumen_estadistico, datos)
