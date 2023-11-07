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
        return datos.describe()

# Función que maneja la interacción entre el patrón Abstract Factory y el conjunto de datos
def interactuar_con_datos(producto, datos):
    resultado = producto.crear_resumen_estadistico(datos)
    print(resultado)  # Puedes adaptar esto para guardar o mostrar los resultados de la manera que desees

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICO 1/datos/activaciones_samur_2023(1).csv", sep=';', encoding='ISO-8859-1')

# Crear instancia del producto concreto (en este caso, ResumenEstadistico)
resumen_estadistico = ResumenEstadistico()

# Interactuar con los datos utilizando el producto concreto
interactuar_con_datos(resumen_estadistico, datos)
