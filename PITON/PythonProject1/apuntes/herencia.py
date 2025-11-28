#_ para herencia
class Padre:
    def __init__(self):
        self._titulo="Soy la clase padre"#Padre__titulo
    def mostrar(self):
        print("PPP",self._titulo)#Padre__titulo

class Madre:
    def __init__(self):
        self._titulo="Soy la clase Madre"#Padre__titulo
    def mostrar(self):
        print("MMM",self._titulo)#Padre__titulo

class Hijo(Padre,Madre):#si hay 2 herencias cuanto tiene que sobreescribir metodos da preferencia  al de la izquierda en este caso a la izq
    #herencia multiple tamb de la madre
    #hereda las cosas de padre
    def __init__(self):
        self._titulo="soy la clase hijo"
    def mostrar(self,mensaje):#estas sonbreescribiendo la clase
        # super().mostrar() #esto nos da ambas si es herencia multiple
        # #super hace referencia a las clase padre
        Madre.mostrar(self)#esto es decir basicamente usa en esta funcion la de mama
        # Padre.mostrar(self)
        print(mensaje)
objeto1=Padre()
objeto1.mostrar()
objeto3=Madre()
objeto3.mostrar()
objeto2=Hijo()
objeto2.mostrar("holaa")