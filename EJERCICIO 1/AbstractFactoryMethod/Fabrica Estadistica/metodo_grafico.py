import pandas as pd
from tkinter import Tk, Label, StringVar

# Fábrica para cálculos estadísticos
class EstadisticasFactory:
    @staticmethod
    def calcular_estadisticas(datos):
        return datos.describe()

# Función para crear la interfaz gráfica con Tkinter y guardar los resultados en un archivo
def mostrar_resultados_tkinter(resultados):
    root = Tk()
    root.title("Resultados Estadísticos")
    root.geometry("400x300")

    labels = ['Promedio:', 'Mediana:', 'Desviación Estándar:', 'Mínimo:', 'Máximo:']
    resultados_vars = [StringVar() for _ in labels]

    for i, (label, result) in enumerate(zip(labels, resultados)):
        Label(root, text=label, font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
        Label(root, textvariable=resultados_vars[i], font=("Arial", 12, "bold")).grid(row=i, column=1, padx=10, pady=5)
        resultados_vars[i].set(str(resultados[label]))

    # Guardar los resultados en un archivo de texto
    with open("resultados_estadisticos.txt", 'w') as f:
        for label, result in resultados.items():
            f.write(f"{label} {result}\n")

    root.mainloop()

# Cargar los datos del archivo CSV
datos = pd.read_csv("EJERCICIO 1/resultados/datos_con_duracion.csv", sep=';', encoding='ISO-8859-1')

# Seleccionar la columna deseada
datos_columna = datos['Duracion Intervencion (min)']

# Usar la fábrica para calcular estadísticas
resultados_estadisticos = EstadisticasFactory.calcular_estadisticas(datos_columna)

# Mostrar los resultados en Tkinter y guardar en un archivo
mostrar_resultados_tkinter(resultados_estadisticos)
