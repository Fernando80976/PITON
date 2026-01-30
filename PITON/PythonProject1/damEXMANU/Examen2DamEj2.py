class Tarea:

    __listaTareas = {}

    def __init__(self, id, titulo, prioridad):
        self.__id = id
        self.__titulo = titulo
        self.__completado = False

        if 1 <= prioridad <= 9:
            self.__prioridad = prioridad
        else:
            self.__prioridad = None

        """if self.__id not in Tarea.__listaTareas:
            Tarea.__listaTareas[self.__id] = self
            print("Tarea", "'"+self.__titulo+"'", "("+"ID: "+self.__id+")", "añadida.")
        else:
            print("Error: ID", self.__id, "ya existente")"""

    @classmethod
    def agregarTarea(cls, id, titulo, prioridad):
        if id not in cls.__listaTareas:
            cls.__listaTareas[id] = Tarea(id, titulo, prioridad)
            print(f"Tarea '{titulo}' (ID: {id}) añadida.")
        else:
            print(f"Error: ID {id} ya existente")

    @classmethod
    def mostrarTareasCompletadas(cls):
        print("- LISTADO DE TAREAS:" )
        noHay = True
        for id in cls.__listaTareas:
            if cls.__listaTareas[id].__completado:
                print(f"[{id}] {cls.__listaTareas[id].__titulo} (Prioridad: {cls.__listaTareas[id].__prioridad})")
                noHay = False
        if noHay:
            print("No hay tareas completadas")

    @classmethod
    def mostrarTareasNoCompletadas(cls):
        print("- LISTADO DE TAREAS:" )
        noHay = True
        for id in cls.__listaTareas:
            if not cls.__listaTareas[id].__completado:
                print(f"[{id}] {cls.__listaTareas[id].__titulo} (Prioridad: {cls.__listaTareas[id].__prioridad})")
                noHay = False
        if noHay:
            print("No hay tareas completadas")

    @classmethod
    def eliminarTarea(cls, id):
        if id in cls.__listaTareas:
            valor=cls.__listaTareas.pop(id).__titulo
            print(f"Tarea con ID {id} ('{valor}') eliminada.")
        else:
            print(f"Error: No se encontro una tarea con ID {id}.")

    @classmethod
    def marcarComoCompletada(cls, id):
        if id in cls.__listaTareas:
            cls.__listaTareas[id].__completado = True
            print(f"Tarea ID {id} '{cls.__listaTareas[id].__titulo}' marcada como completada.")
        else:
            print(f"Error: No se encontro una tarea con ID {id}.")

Tarea.agregarTarea("T1", "Comprar Manga", 9)
Tarea.agregarTarea("T2", "Comprar Juego", 5)

#Tarea.eliminarTarea("T2")
#Tarea.marcarComoCompletada("T1")

Tarea.mostrarTareasCompletadas()
print()
Tarea.mostrarTareasNoCompletadas()