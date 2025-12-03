from abc import ABCMeta, abstractmethod


class Abstracta(metaclass=ABCMeta):
        def metodoNormal(self):
                print("Hola mundo")
        @abstractmethod #clase abstracta
        def metodoAbstracto(self):
              pass
class Hija(Abstracta):
    def metodoAbstracto(self):
        print("HOLA soy la clase hija de la clase abstracta")
elemento=Hija()
elemento.metodoAbstracto()