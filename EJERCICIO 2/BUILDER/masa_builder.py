from abc import ABC, abstractmethod

# Interfaz de la masa
class Masa(ABC):
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def tiene_ingredientes_especiales(self):
        pass

# Implementaciones concretas de masas
class MasaDelgada(Masa):
    def tipo(self):
        return "Masa delgada"

    def tiene_ingredientes_especiales(self):
        return False

class Masa48Horas(Masa):
    def tipo(self):
        return "Masa fermentada por 48 horas"

    def tiene_ingredientes_especiales(self):
        return False

class MasaMadre(Masa):
    def tipo(self):
        return "Masa de masa madre"

    def tiene_ingredientes_especiales(self):
        return False

class MasaPoolish(Masa):
    def tipo(self):
        return "Masa con poolish"

    def tiene_ingredientes_especiales(self):
        return False

class MasaNapolitana(Masa):
    def tipo(self):
        return "Masa Napolitana"

    def tiene_ingredientes_especiales(self):
        return False

class MasaNewYorkStyle(Masa):
    def tipo(self):
        return "Masa New York Style"

    def tiene_ingredientes_especiales(self):
        return False

class MasaChicagoStyle(Masa):
    def tipo(self):
        return "Masa Chicago Style"

    def tiene_ingredientes_especiales(self):
        return False

class MasaSiciliana(Masa):
    def tipo(self):
        return "Masa Siciliana"

    def tiene_ingredientes_especiales(self):
        return False

class MasaCracker(Masa):
    def tipo(self):
        return "Masa Cracker"

    def tiene_ingredientes_especiales(self):
        return False

class MasaEspecial(Masa):
    def tipo(self):
        return "Masa con ingredientes especiales"

    def tiene_ingredientes_especiales(self):
        return True

# Builder
class MasaBuilder:
    def __init__(self):
        self.masa = None

    def elegir_masa_delgada(self):
        self.masa = MasaDelgada()

    def elegir_masa_48_horas(self):
        self.masa = Masa48Horas()

    def elegir_masa_madre(self):
        self.masa = MasaMadre()

    def elegir_masa_poolish(self):
        self.masa = MasaPoolish()

    def elegir_masa_napolitana(self):
        self.masa = MasaNapolitana()

    def elegir_masa_new_york_style(self):
        self.masa = MasaNewYorkStyle()

    def elegir_masa_chicago_style(self):
        self.masa = MasaChicagoStyle()

    def elegir_masa_siciliana(self):
        self.masa = MasaSiciliana()

    def elegir_masa_cracker(self):
        self.masa = MasaCracker()

    def elegir_masa_especial(self):
        self.masa = MasaEspecial()

    def get_masa(self):
        return self.masa

# Cliente - Preguntar al usuario por la masa
builder = MasaBuilder()

# Solicitar al usuario que elija el tipo de masa
masa_seleccionada = input("Elige el tipo de masa: ")

if masa_seleccionada.lower() == "delgada":
    builder.elegir_masa_delgada()
    print("Masa delgada seleccionada")
elif masa_seleccionada.lower() == "48 horas":
    builder.elegir_masa_48_horas()
    print("Masa fermentada por 48 horas seleccionada")
# Agregar otras opciones de masa
elif masa_seleccionada.lower() == "especial":
    builder.elegir_masa_especial()
    print("Masa especial seleccionada")
elif masa_seleccionada.lower() == "madre":
    builder.elegir_masa_madre()
    print("Masa madre seleccionada")
elif masa_seleccionada.lower() == "poolish":
    builder.elegir_masa_poolish()
    print("Masa poolish seleccionada")
elif masa_seleccionada.lower() == "napolitana":
    builder.elegir_masa_napolitana()
    print("Masa napolitana seleccionada")
elif masa_seleccionada.lower() == "new york style":
    builder.elegir_masa_new_york_style()
    print("Masa New York Style seleccionada")
elif masa_seleccionada.lower() == "chicago style":
    builder.elegir_masa_chicago_style()
    print("Masa Chicago Style seleccionada")
elif masa_seleccionada.lower() == "siciliana":
    builder.elegir_masa_siciliana()
    print("Masa Siciliana seleccionada")
elif masa_seleccionada.lower() == "cracker":
    builder.elegir_masa_cracker()
    print("Masa Cracker seleccionada")

# Después de completar la elección de masa
if builder.get_masa().tiene_ingredientes_especiales():
    # Solicitar al usuario que elija un ingrediente especial
    print("Esta masa permite ingredientes especiales")
    print("¿Deseas añadir un ingrediente especial? (si/no)")
    eleccion_ingrediente = input()

    if eleccion_ingrediente.lower() == "si":
        print("Elige un ingrediente especial:")
        ingredientes = ["trufa", "jamon iberico", "queso gorgonzola", "anchoas", "aceitunas rellenas"]
        for index, ingrediente in enumerate(ingredientes):
            print(f"{index + 1}. {ingrediente}")

        while True:
            seleccion = input("Selecciona un ingrediente (1-5): ")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 1 <= seleccion <= 5:
                    ingrediente_seleccionado = ingredientes[seleccion - 1]
                    print(f"Ha elegido {builder.get_masa().tipo()} con {ingrediente_seleccionado}")
                    break
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            else:
                print("Por favor, ingresa un número válido.")
    else:
        print(f"Ha elegido {builder.get_masa().tipo()}")
else:
    print(f"Ha elegido {builder.get_masa().tipo()}")
