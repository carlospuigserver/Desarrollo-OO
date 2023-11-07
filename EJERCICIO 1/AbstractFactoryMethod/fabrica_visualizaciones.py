import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

# Fábrica Abstracta para Visualizaciones Gráficas
class VisualizacionesFactory(ABC):
    @abstractmethod
    def crear_histograma(self, datos):
        pass

    @abstractmethod
    def crear_grafico_barras(self, datos):
        pass

# Producto Concreto para Histograma
class Histograma(VisualizacionesFactory):
    def crear_histograma(self, datos):
        plt.hist(datos)
        plt.title('Histograma')
        plt.show()

    def crear_grafico_barras(self, datos):
        pass

# Producto Concreto para Gráfico de Barras
class GraficoBarras(VisualizacionesFactory):
    def crear_histograma(self, datos):
        pass

    def crear_grafico_barras(self, datos):
        plt.bar(range(len(datos)), datos)
        plt.title('Gráfico de Barras')
        plt.show()

# Función que maneja la interacción entre el patrón Abstract Factory y el conjunto de datos
def interactuar_con_datos(factory, producto, datos):
    producto.crear_histograma(datos)
    producto.crear_grafico_barras(datos)

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')

# Crear instancias de la fábrica de visualizaciones y productos concretos
factory_visualizaciones = VisualizacionesFactory()
histograma = Histograma()
grafico_barras = GraficoBarras()

# Interactuar con los datos utilizando la fábrica de visualizaciones gráficas
interactuar_con_datos(factory_visualizaciones, histograma, datos)
interactuar_con_datos(factory_visualizaciones, grafico_barras, datos)
