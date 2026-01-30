#se usan cuando quieres dificultar las manipulaciones
import pickle
class Persona:
    def __init__(self,nombre):
        self.__nombre = nombre
    @property
    def nombre(self):
        return self.__nombre
persona1= Persona("Pepe")
p2=Persona("jose")
try:
        fichero=open("binario.bin","wb")
        lista=[]
        lista.append(persona1)
        lista.append(p2)
        pickle.dump(lista,fichero)
        fichero.close()
        fichero=open("binario.bin","rb")
        l=pickle.load(fichero)
        for elemento in l:
            print(elemento.nombre)
        print(l[1].nombre)
        fichero.close()
        # pickle.dump(persona1,fichero)
        # pickle.dump(p2,fichero)

        # p2=pickle.load(fichero)
        # persona1=pickle.load(fichero)
        # print(persona1.nombre)
        # print(p2.nombre)
        # fichero.close()
except:
        print("Error al manipular el fi")