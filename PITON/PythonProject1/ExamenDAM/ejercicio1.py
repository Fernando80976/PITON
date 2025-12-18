# empresa de seguros
class seguros:
    def __init__(self,nombre,puntosCarnet):
        self.__nombre=nombre
        self.puntosCarnet=puntosCarnet
    def setPuntosCarnet(self,puntosCarnet):
        self.puntosCarnet=puntosCarnet
class Coche(seguros):
    def __init__(self,nombre,antiguedad):
        self.__nombre=nombre
        self.__antiguedad=antiguedad
    def getAntiguedad(self):
        return self.__antiguedad
    def setAntiguedad(self,antiguedad):
        self.__antiguedad=antiguedad

class Moto(seguros):
    def __init__(self,nombre,antiguedad):
        self.__nombre=nombre
        self.__antiguedad=antiguedad