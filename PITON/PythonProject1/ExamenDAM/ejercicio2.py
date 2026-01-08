ListaTareas= {}
class Tarea:
    def __init__(self,id,tarea,prioridad):
        self.__id=id
        self.__tarea=tarea
        self.__prioridad=prioridad
        self.__completado=False
        ListaTareas[self.__id]=str(self.__id),"Tarea: "+self.__tarea,"Prioridad: "+self.__prioridad,"Completado: ",self.__completado
    def getId(self):
        return self.__id
    def getTarea(self):
        return self.__tarea
    def getPrioridad(self):
        return self.__prioridad
    def getCompletado(self):
        return self.__completado
    def setId(self,id):
        self.__id=id
    def setTarea(self,tarea):
        self.__tarea=tarea
    def setPrioridad(self,prioridad):
        self.__prioridad=prioridad
    def setCompletado(self,completado):
        self.__completado=completado


area=Tarea(1,"Jugar pokemon","Alta")
print(ListaTareas)
Tarea1=Tarea(2,"Jugar pokemon","Alta")
print(ListaTareas)