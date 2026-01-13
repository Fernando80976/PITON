from abc import ABC, abstractmethod
from datetime import datetime

# ==========================
# CLASE CONDUCTOR
# ==========================
class Conductor:
    def __init__(self, nombre, anio_nacimiento, anio_carnet, puntos):
        self.nombre = nombre
        self.anio_nacimiento = anio_nacimiento
        self.anio_carnet = anio_carnet
        self.puntos = puntos

    def edad(self):
        return datetime.now().year - self.anio_nacimiento

    def anios_carnet(self):
        return datetime.now().year - self.anio_carnet


# ==========================
# CLASE ABSTRACTA VEHICULO
# ==========================
class Vehiculo(ABC):
    def __init__(self, matricula, anio_compra, conductor):
        self.matricula = matricula
        self.anio_compra = anio_compra
        self.conductor = conductor

    def antiguedad(self):
        return datetime.now().year - self.anio_compra

    @abstractmethod
    def seguro_terceros(self):
        pass

    @abstractmethod
    def seguro_todo_riesgo(self):
        pass


# ==========================
# CLASE COCHE
# ==========================
class Coche(Vehiculo):

    def seguro_todo_riesgo(self):
        a = self.antiguedad()

        if a == 1:
            precio = 400
        elif a == 2:
            precio = 500
        elif a == 3:
            precio = 700
        else:
            precio = 250 * a

        if self.conductor.puntos < 8:
            precio += 100

        return precio

    def seguro_terceros(self):
        precio = 250

        if self.conductor.puntos < 8:
            precio += 100
        if self.conductor.edad() < 24:
            precio += 50
        if self.conductor.anios_carnet() < 2:
            precio += 75

        return precio


# ==========================
# CLASE MOTO
# ==========================
class Moto(Vehiculo):

    def seguro_terceros(self):
        precio = 200

        if self.conductor.puntos < 8:
            precio += 150
        if self.conductor.edad() < 24:
            precio += 25
        if self.conductor.anios_carnet() < 2:
            precio += 50

        return precio

    def seguro_todo_riesgo(self):
        return "No se hacen seguros a todo riesgo a motos"
# EJEMPLO 1
c1 = Conductor("José María Morales", 1968, 1986, 10)
coche = Coche("6310NXB", 2024, c1)

print("Precio todo riesgo:", coche.seguro_todo_riesgo(), "€")
print("Precio terceros:", coche.seguro_terceros(), "€")

# EJEMPLO 2
c2 = Conductor("Inés Perado", 2007, 2024, 8)
moto = Moto("6309NXB", 2025, c2)

print("Precio terceros:", moto.seguro_terceros(), "€")
print(moto.seguro_todo_riesgo())
