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

for mes in meses:
    datos_mes = datos[datos['Mes'] == mes]
    hora_solicitud = pd.to_datetime(datos_mes['Hora Solicitud'])
    media_actividades = hora_solicitud.dt.hour.count() / hora_solicitud.dt.normalize().nunique()  # Cálculo de la media diaria

    print(f"La media de activaciones por día en {mes} es: {media_actividades:.2f}")
    fabrica_histograma.crear_histograma(hora_solicitud.dt.hour, f'Histograma de Activaciones en {mes} por Hora del Día')
