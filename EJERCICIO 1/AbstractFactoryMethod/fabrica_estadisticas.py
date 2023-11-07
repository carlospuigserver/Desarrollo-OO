import pandas as pd
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import Label

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

    root = tk.Tk()
    root.title("Resultados Estadísticos")

    etiquetas = [
        f"Promedio: {resultado[0]}",
        f"Mediana: {resultado[1]}",
        f"Desviación Estándar: {resultado[2]}",
        f"Mínimo: {resultado[3]}",
        f"Máximo: {resultado[4]}"
    ]

    for i, etiqueta_texto in enumerate(etiquetas):
        etiqueta = Label(root, text=etiqueta_texto)
        etiqueta.grid(row=i, column=0, sticky='w')

    root.mainloop()

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar la columna deseada
datos_columna = datos['Duracion Intervencion (min)']  # Reemplaza 'Nombre de la columna' por el nombre real

# Crear instancia del producto concreto (en este caso, ResumenEstadistico)
resumen_estadistico = ResumenEstadistico()

# Interactuar con los datos utilizando el producto concreto
interactuar_con_datos(resumen_estadistico, datos_columna)
