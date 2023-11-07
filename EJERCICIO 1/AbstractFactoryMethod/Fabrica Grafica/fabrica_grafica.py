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
        pass

# Producto Concreto para Gráfico de Barras
class GraficoBarras(GraficosFactory):
    def crear_histograma(self, datos):
        pass

    def crear_grafico_barras(self, datos):
        plt.bar(range(len(datos)), datos)
        plt.title('Gráfico de Barras')
        plt.show()

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_preprocesados.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar la columna deseada
datos_columna = datos['Hora Solicitud']  # Reemplaza 'Nombre de la columna' por el nombre real

# Usar la fábrica para calcular estadísticas
resultados = EstadisticasFactory.calcular_estadisticas(datos_columna)

# Crear instancias de las fábricas y productos concretos
fabrica_histograma = Histograma()
fabrica_grafico_barras = GraficoBarras()

# Interactuar con los datos utilizando la fábrica de visualizaciones gráficas
fabrica_histograma.crear_histograma(datos_columna)
fabrica_grafico_barras.crear_grafico_barras(datos_columna)
