import random
class pokemon:
        def __init__(self,nombre,codigo,tipo,evolucion=None):
            self.__nombre=nombre
            self.__codigo=codigo
            self.__pv=random.randint(50,100)
            self.__evolucion=evolucion
            self.__tipo=tipo
        def ficha(self):
            evoluciones="No tiene"
            if self.__evolucion!=None:
                evoluciones=self.__evolucion.__nombre
            ficha = f"""
            Ficha del Profesor/a:
            ===========================
            Nombre: {self.__nombre}
            Código: {self.__codigo}
            PV : {self.__pv}
            Evoluciona a: {str(evoluciones)}
            ===========================

            """
            return ficha
        def evoluciona(self):
            if self.__evolucion==None:
                evo=self
                print("Este pokemon no sabe evolucionar")

            else:
                evo=self.__evolucion
            return evo
        def combateContra(self,pokemon):
            if pokemon.__pv > 0 and self.__pv > 0:
                print("Uno de los pokemon está si PV  dale un revivir no seas rata")
                terminado = False
            else:
                ataque=random.randint(25,75)
                pokemon.__pv=pokemon.__pv-ataque
                print("ataque de ",self.__nombre,ataque)
                terminado=True

                while terminado==False:

                    if pokemon.__pv <=0:
                        print("Ganó el pokemon atacante",self.__nombre)
                        terminado = True
                    else:
                        ataque = random.randint(25, 75)
                        print("ataque de ",pokemon.__nombre,ataque)

                        self.__pv=self.__pv-ataque
                    if(self.__pv<=0):
                        print("Gano el pokemon atacado",pokemon.__nombre)
                        terminado = True
                    # if(self.__pv>0 and pokemon.__pv>0):
                    #     print("FUE EMPATE!!! AMIGOS")
        # def multiplicadores(self):
            
p3=pokemon("Venusaur",3,"Planta")
p2=pokemon("Ivysaur",2,"Planta",p3)#evoluciona a p3
p1=pokemon("Bulbasaur",1,"Planta",p2)

print(p1.ficha())
print(p2.ficha())
print(p3.ficha())
p1=p1.evoluciona()
p3=p3.evoluciona()
p1.ficha()
p1.combateContra(p3)#primero ataca pokemon atacante
print(p1.ficha())
p1.combateContra(p3)