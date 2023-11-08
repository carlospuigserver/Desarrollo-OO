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
masa_seleccionada = input("ELIGE TIPO DE MASA : delgada , 48 horas , especial(a elegir ingredientes especiales) , madre , poolish , napolitana , new york style , chicago style , siciliana , cracker :")

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


from abc import ABC, abstractmethod

# Interfaz para las salsas base
class SalsaBase(ABC):
    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def es_vegana(self):
        pass

# Implementaciones concretas de salsas
class SalsaTomateClasica(SalsaBase):
    def tipo(self):
        return "Salsa de Tomate Clásica"

    def es_vegana(self):
        return True

class SalsaMarinara(SalsaBase):
    def tipo(self):
        return "Salsa Marinara"

    def es_vegana(self):
        return True

class SalsaPesto(SalsaBase):
    def tipo(self):
        return "Salsa de Pesto"

    def es_vegana(self):
        return True

class SalsaBlanca(SalsaBase):
    def tipo(self):
        return "Salsa Blanca"

    def es_vegana(self):
        return False

class SalsaBBQ(SalsaBase):
    def tipo(self):
        return "Salsa BBQ"

    def es_vegana(self):
        return True

class SalsaChampinones(SalsaBase):
    def tipo(self):
        return "Salsa de Champiñones"

    def es_vegana(self):
        return True

class SalsaTomateSinGluten(SalsaBase):
    def tipo(self):
        return "Salsa de Tomate sin Gluten"

    def es_vegana(self):
        return True

class SalsasAutor(SalsaBase):
    def tipo(self):
        return "Salsas de Autor"

    def es_vegana(self):
        return True

class EdicionLimitada(SalsaBase):
    def tipo(self):
        return "Edición Limitada"

    def es_vegana(self):
        return True

# Builder de salsas
class SalsaBuilder:
    def __init__(self):
        self.salsa = None

    def elegir_salsa_tomate_clasica(self):
        self.salsa = SalsaTomateClasica()

    def elegir_salsa_marinara(self):
        self.salsa = SalsaMarinara()

    def elegir_salsa_pesto(self):
        self.salsa = SalsaPesto()

    def elegir_salsa_blanca(self):
        self.salsa = SalsaBlanca()

    def elegir_salsa_bbq(self):
        self.salsa = SalsaBBQ()

    def elegir_salsa_champinones(self):
        self.salsa = SalsaChampinones()

    def elegir_salsa_tomate_sin_gluten(self):
        self.salsa = SalsaTomateSinGluten()

    def elegir_salsas_autor(self):
        self.salsa = SalsasAutor()

    def elegir_edicion_limitada(self):
        self.salsa = EdicionLimitada()

    def get_salsa(self):
        return self.salsa

# Cliente - Preguntar al usuario por la salsa
builder = SalsaBuilder()

# Solicitar al usuario que elija el tipo de salsa
salsa_seleccionada = input("ELIGE TIPO DE SALSA : tomate clasica , marinara , pesto , blanca , bbq , champinones , tomate sin gluten , autor , edicion limitada(a elegir ingredientes) :")

if salsa_seleccionada.lower() == "tomate clasica":
    builder.elegir_salsa_tomate_clasica()
    print("Salsa de Tomate Clásica seleccionada")
# Otras opciones para elegir salsas
elif salsa_seleccionada.lower() == "marinara":
    builder.elegir_salsa_marinara()
    print("Salsa Marinara seleccionada")
elif salsa_seleccionada.lower() == "pesto":
    builder.elegir_salsa_pesto()
    print("Salsa de Pesto seleccionada")
elif salsa_seleccionada.lower() == "blanca":
    builder.elegir_salsa_blanca()
    print("Salsa Blanca seleccionada")
elif salsa_seleccionada.lower() == "bbq":
    builder.elegir_salsa_bbq()
    print("Salsa BBQ seleccionada")
elif salsa_seleccionada.lower() == "champinones":
    builder.elegir_salsa_champinones()
    print("Salsa de Champiñones seleccionada")
elif salsa_seleccionada.lower() == "tomate sin gluten":
    builder.elegir_salsa_tomate_sin_gluten()
    print("Salsa de Tomate sin Gluten seleccionada")
elif salsa_seleccionada.lower() == "autor":
    builder.elegir_salsas_autor()
    print("Salsas de Autor seleccionada")
elif salsa_seleccionada.lower()  == "edicion limitada":
    print("Esta es una edición limitada. Elige una opción para los ingredientes:")
    print("1. Ingredientes tropicales")
    print("2. Ingredientes de temporada")

    while True:
        seleccion = input("Selecciona una opción (1-2): ")
        if seleccion.isdigit():
            seleccion = int(seleccion)
            if seleccion == 1:
                print("Ha elegido ingredientes tropicales para la Salsa Edición Limitada")
                break
            elif seleccion == 2:
                print("Ha elegido ingredientes de temporada para la Salsa Edición Limitada")
                break
            else:
                print("Selección inválida. Inténtalo de nuevo.")
        else:
            print("Por favor, ingresa un número válido.")
    builder.elegir_edicion_limitada()
else:
    print("Opción de salsa no reconocida")
    

    
salsa_elegida = builder.get_salsa().tipo()


from abc import ABC, abstractmethod

# Clase abstracta para los ingredientes
class Ingrediente(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Implementaciones concretas de ingredientes
class Queso(Ingrediente):
    def tipo(self):
        return "Queso"

class Mozzarella(Queso):
    def tipo(self):
        return "Mozzarella"

class Parmesano(Queso):
    def tipo(self):
        return "Parmesano"

class Cheddar(Queso):
    def tipo(self):
        return "Cheddar"

# Implementaciones para otros tipos de ingredientes
class Carne(Ingrediente):
    def tipo(self):
        return "Carne"

class Pepperoni(Carne):
    def tipo(self):
        return "Pepperoni"

class Pollo(Carne):
    def tipo(self):
        return "Pollo"

class Tocino(Carne):
    def tipo(self):
        return "Tocino"

class Vegetal(Ingrediente):
    def tipo(self):
        return "Vegetal"

class Champinones(Vegetal):
    def tipo(self):
        return "Champiñones"

class Pimientos(Vegetal):
    def tipo(self):
        def tipo(self):
            return "Pimientos"

class Cebolla(Vegetal):
    def tipo(self):
        return "Cebolla"

class Aceitunas(Vegetal):
    def tipo(self):
        return "Aceitunas"

class Tomate(Vegetal):
    def tipo(self):
        return "Tomate"

class Espinacas(Vegetal):
    def tipo(self):
        return "Espinacas"

class Alcachofas(Vegetal):
    def tipo(self):
        return "Alcachofas"

class Berenjena(Vegetal):
    def tipo(self):
        return "Berenjena"

class Mariscos(Ingrediente):
    def tipo(self):
        return "Mariscos"

class Anchoas(Mariscos):
    def tipo(self):
        return "Anchoas"

class Camarones(Mariscos):
    def tipo(self):
        return "Camarones"

class Mejillones(Mariscos):
    def tipo(self):
        return "Mejillones"

class Calamares(Mariscos):
    def tipo(self):
        return "Calamares"

class EspeciasYHierbas(Ingrediente):
    def tipo(self):
        return "Especias y Hierbas"

class AlbahacaFresca(EspeciasYHierbas):
    def tipo(self):
        return "Albahaca fresca"

class Oregano(EspeciasYHierbas):
    def tipo(self):
        return "Orégano"

class Perejil(EspeciasYHierbas):
    def tipo(self):
        return "Perejil"

class Ajo(EspeciasYHierbas):
    def tipo(self):
        return "Ajo"

class AderezosYOtros(Ingrediente):
    def tipo(self):
        return "Aderezos y Otros"

class AceiteDeOliva(AderezosYOtros):
    def tipo(self):
        return "Aceite de oliva"

class SalsaBBQ(AderezosYOtros):
    def tipo(self):
        return "Salsa BBQ"

class Pesto(AderezosYOtros):
    def tipo(self):
        return "Pesto"

class SalsaPicante(AderezosYOtros):
    def tipo(self):
        return "Salsa picante"

# Builder de Ingredientes
class IngredienteBuilder:
    def __init__(self):
        self.ingredientes_seleccionados = []

    def elegir_queso(self, queso):
        if queso:
            self.ingredientes_seleccionados.append(Queso())

    def elegir_pepperoni(self, pepperoni):
        if pepperoni:
            self.ingredientes_seleccionados.append(Pepperoni())

    # Implementar métodos similares para otros tipos de ingredientes

    def get_ingredientes(self):
        return self.ingredientes_seleccionados

# Cliente para elegir los ingredientes
builder = IngredienteBuilder()

# Solicitar al usuario que elija los ingredientes
print("Elige los ingredientes para tu pizza:")

elegir_queso = input("¿Deseas agregar queso? (si/no): ")
builder.elegir_queso(elegir_queso.lower() == "si")

# Ejemplo de elección de pepperoni
elegir_pepperoni = input("¿Deseas agregar pepperoni? (si/no): ")
builder.elegir_pepperoni(elegir_pepperoni.lower() == "si")

# Obtener la lista de ingredientes seleccionados
ingredientes_seleccionados = builder.get_ingredientes()
print("Ingredientes seleccionados:")
for ingrediente in ingredientes_seleccionados:
    print(ingrediente.tipo())

from abc import ABC, abstractmethod

# Clase abstracta para los ingredientes
class Ingrediente(ABC):
    @abstractmethod
    def tipo(self):
        pass

# Implementaciones concretas de ingredientes
class Queso(Ingrediente):
    def tipo(self):
        return "Queso"

class Mozzarella(Queso):
    def tipo(self):
        return "Mozzarella"

class Parmesano(Queso):
    def tipo(self):
        return "Parmesano"

class Cheddar(Queso):
    def tipo(self):
        return "Cheddar"

class Gouda(Queso):
    def tipo(self):
        return "Gouda"

class Provolone(Queso):
    def tipo(self):
        return "Provolone"

class Carne(Ingrediente):
    def tipo(self):
        return "Carne"

class Pepperoni(Carne):
    def tipo(self):
        return "Pepperoni"

class Pollo(Carne):
    def tipo(self):
        return "Pollo"

class Jamon(Carne):
    def tipo(self):
        return "Jamón"

class Tocino(Carne):
    def tipo(self):
        return "Tocino"

class Marisco(Ingrediente):
    def tipo(self):
        return "Marisco"

class Anchoas(Marisco):
    def tipo(self):
        return "Anchoas"

class Camarones(Marisco):
    def tipo(self):
        return "Camarones"

class Mejillones(Marisco):
    def tipo(self):
        return "Mejillones"

class Calamares(Marisco):
    def tipo(self):
        return "Calamares"

class Vegetal(Ingrediente):
    def tipo(self):
        return "Vegetal"

class Champinones(Vegetal):
    def tipo(self):
        return "Champiñones"

class Pimientos(Vegetal):
    def tipo(self):
        return "Pimientos"

class Cebolla(Vegetal):
    def tipo(self):
        return "Cebolla"

class Aceitunas(Vegetal):
    def tipo(self):
        return "Aceitunas"

class Tomate(Vegetal):
    def tipo(self):
        return "Tomate"

class Espinacas(Vegetal):
    def tipo(self):
        return "Espinacas"

class Alcachofas(Vegetal):
    def tipo(self):
        return "Alcachofas"

class Berenjena(Vegetal):
    def tipo(self):
        return "Berenjena"

# Builder de Ingredientes
class IngredienteBuilder:
    def __init__(self):
        self.ingredientes_seleccionados = []

    def elegir_queso(self, tipo_queso):
        if tipo_queso:
            if tipo_queso == "Mozzarella":
                self.ingredientes_seleccionados.append(Mozzarella())
            elif tipo_queso == "Parmesano":
                self.ingredientes_seleccionados.append(Parmesano())
            elif tipo_queso == "Cheddar":
                self.ingredientes_seleccionados.append(Cheddar())
            elif tipo_queso == "Gouda":
                self.ingredientes_seleccionados.append(Gouda())
            elif tipo_queso == "Provolone":
                self.ingredientes_seleccionados.append(Provolone())

    def elegir_carne(self, tipo_carne):
        if tipo_carne:
            if tipo_carne == "Pepperoni":
                self.ingredientes_seleccionados.append(Pepperoni())
            elif tipo_carne == "Pollo":
                self.ingredientes_seleccionados.append(Pollo())
            elif tipo_carne == "Jamon":
                self.ingredientes_seleccionados.append(Jamon())
            elif tipo_carne == "Tocino":
                self.ingredientes_seleccionados.append(Tocino())

    def elegir_marisco(self, tipo_marisco):
        if tipo_marisco:
            if tipo_marisco == "Anchoas":
                self.ingredientes_seleccionados.append(Anchoas())
            elif tipo_marisco == "Camarones":
                self.ingredientes_seleccionados.append(Camarones())
            elif tipo_marisco == "Mejillones":
                self.ingredientes_seleccionados.append(Mejillones())
            elif tipo_marisco == "Calamares":
                self.ingredientes_seleccionados.append(Calamares())

    def elegir_vegetal(self, tipo_vegetal):
        if tipo_vegetal:
            if tipo_vegetal == "Champinones":
                self.ingredientes_seleccionados.append(Champinones())
            elif tipo_vegetal == "Pimientos":
                self.ingredientes_seleccionados.append(Pimientos())
            elif tipo_vegetal == "Cebolla":
                self.ingredientes_seleccionados.append(Cebolla())
            elif tipo_vegetal == "Aceitunas":
                self.ingredientes_seleccionados.append(Aceitunas())
            elif tipo_vegetal == "Tomate":
                self.ingredientes_seleccionados.append(Tomate())
            elif tipo_vegetal == "Espinacas":
                self.ingredientes_seleccionados.append(Espinacas())
            elif tipo_vegetal == "Alcachofas":
                self.ingredientes_seleccionados.append(Alcachofas())
            elif tipo_vegetal == "Berenjena":
                self.ingredientes_seleccionados.append(Berenjena())

    def get_ingredientes(self):
        return self.ingredientes_seleccionados

# Cliente para elegir los ingredientes
builder = IngredienteBuilder()

# Solicitar al usuario que elija los ingredientes
print("Elige los ingredientes para tu pizza:")

# Elegir un queso
elegir_queso = input("¿Deseas agregar queso? (si/no): ")
if elegir_queso.lower() == "si":
    print("Elige un tipo de queso (Mozzarella, Parmesano, Cheddar, Gouda, Provolone):")
    tipo_queso = input()
    builder.elegir_queso(tipo_queso)

# Elegir una carne
elegir_carne = input("¿Deseas agregar carne? (si/no): ")
if elegir_carne.lower() == "si":
    print("Elige un tipo de carne (Pepperoni, Pollo, Jamon, Tocino):")
    tipo_carne = input()
    builder.elegir_carne(tipo_carne)

# Elegir un marisco
elegir_marisco = input("¿Deseas agregar mariscos? (si/no): ")
if elegir_marisco.lower() == "si":
    print("Elige un tipo de marisco (Anchoas, Camarones, Mejillones, Calamares):")
    tipo_marisco = input()
    builder.elegir_marisco(tipo_marisco)

# Elegir un vegetal
elegir_vegetal = input("¿Deseas agregar vegetales? (si/no): ")
if elegir_vegetal.lower() == "si":

    print("Elige un tipo de vegetal (Champiñones, Pimientos, Cebolla, Aceitunas, Tomate, Espinacas, Alcachofas, Berenjena):")
    tipo_vegetal = input()
    builder.elegir_vegetal(tipo_vegetal)
