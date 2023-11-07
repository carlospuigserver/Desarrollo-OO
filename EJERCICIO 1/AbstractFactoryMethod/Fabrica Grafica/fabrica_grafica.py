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
        plt.yticks(fontsize=10)  # Tamaño de fuente del eje Y
        plt.gca().yaxis.grid(True)  # Líneas de la cuadrícula para el eje Y

        # Mejorar la apariencia del eje Y en el gráfico de barras
        plt.gca().set_ylim([0, datos.max() * 1.1])  # Ajustar límites del eje Y
        plt.gca().yaxis.grid(True)  # Mostrar líneas de cuadrícula en el eje Y
        plt.gca().tick_params(axis='y', labelrotation=0)  # Rotar las etiquetas del eje Y
        plt.tight_layout()  # Ajustar el espaciado para evitar superposición

        plt.show()

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar las primeras 100 filas de la columna deseada
datos_columna = datos['Duracion Intervencion (min)'].head(30)  # Reemplaza 'Nombre de la columna' por el nombre real y limita a 100 filas

# Usar la fábrica para calcular estadísticas
resultados = EstadisticasFactory.calcular_estadisticas(datos_columna)

# Crear instancias de las fábricas y productos concretos
fabrica_histograma = Histograma()

# Interactuar con los datos utilizando la fábrica de visualizaciones gráficas
fabrica_histograma.crear_histograma(datos_columna)
fabrica_histograma.crear_grafico_barras(datos_columna)
