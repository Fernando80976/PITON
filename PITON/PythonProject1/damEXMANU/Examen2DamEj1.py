from abc import ABCMeta, abstractmethod
from datetime import date

class Conductor:
    def __init__(self, nombre, nif, ayoNacido, ayoCarnetSacado, puntosCarnet):
        self._nombre = nombre
        self._nif = nif
        self._ayoNacido = ayoNacido
        self._ayoCarnetSacado = ayoCarnetSacado
        self._puntosCarnet = puntosCarnet

    def edad(self):
        return date.today().year - self._ayoNacido

    def ayoCarnet(self):
        return date.today().year - self._ayoCarnetSacado

class Vehiculo(metaclass=ABCMeta):
    def __init__(self, matricula, ayoCompra, conductor):
        self._matricula = matricula
        self._ayoCompra = ayoCompra
        self._conductor = conductor

    @abstractmethod
    def precioSeguro(self):
        pass


class Coche(Vehiculo):
    def precioSeguro(self):
        precioSeguroTercero = 250

        if self._conductor._puntosCarnet < 8:
            precioSeguroTercero += 100

        if self._conductor.edad() < 24:
            precioSeguroTercero += 50

        if self._conductor.ayoCarnet() < 2:
            precioSeguroTercero += 75

        antiguedad = max(1, date.today().year - self._ayoCompra)
        print(antiguedad)
        if antiguedad == 1:
            precioSeguroTodoRiesgo = 400

        if antiguedad == 2:
            precioSeguroTodoRiesgo = 500

        if antiguedad == 3:
            precioSeguroTodoRiesgo = 700

        if antiguedad > 3:
            precioSeguroTodoRiesgo = 250
            precioSeguroTodoRiesgo *= antiguedad

        if self._conductor._puntosCarnet < 8:
            precioSeguroTodoRiesgo += 100

        print(f"Vehiculo: coche. Matricula: {self._matricula}. Año de compra: {self._ayoCompra}")
        print(f"Conductor: {self._conductor._nombre}. Edad: {self._conductor.edad()}. Años de carnet: {self._conductor.ayoCarnet()}. Puntos: {self._conductor._puntosCarnet}")
        print(f"Precio del seguro a todo riesgo: {precioSeguroTodoRiesgo}$")
        print(f"Precio del seguro a terceros: {precioSeguroTercero}$")


class Moto(Vehiculo):
    def precioSeguro(self):
        precioSeguroTercero = 200

        if self._conductor._puntosCarnet < 8:
            precioSeguroTercero += 150

        if self._conductor.edad() < 24:
            precioSeguroTercero += 25

        if self._conductor.ayoCarnet() < 2:
            precioSeguroTercero += 50

        print(f"Vehiculo: moto. Matricula: {self._matricula}. Año de compra: {self._ayoCompra}")
        print(f"Conductor: {self._conductor._nombre}. Edad: {self._conductor.edad()}. Años de carnet: {self._conductor.ayoCarnet()}. Puntos: {self._conductor._puntosCarnet}")
        print(f"Precio del seguro a terceros: {precioSeguroTercero}$")
        print("No se hacen seguros a todo riesgo a motos")

c1 = Coche("12345", 2003, Conductor("pepe", "0987654321", 2002, 2020, 7))
m1 = Moto("12345", 2003, Conductor("pepe", "0987654321", 2002, 2020, 7))

c1.precioSeguro()
print()
m1.precioSeguro()