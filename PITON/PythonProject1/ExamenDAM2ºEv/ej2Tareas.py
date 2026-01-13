class GestorTareas:
    def __init__(self):
        # Guardaremos todo en un diccionario llamado 'tareas'
        self.tareas = {}

    def agregarTarea(self, identificador, titulo, prioridad):
        # 1. Comprobamos si el ID ya existe
        if identificador in self.tareas:
            print(f"Error: ID {identificador} ya existente")
        else:
            # 2. Creamos un mini-diccionario para la nueva tarea
            nueva_tarea = {
                'titulo': titulo,
                'prioridad': prioridad,
                'completada': False
            }
            # 3. La guardamos usando su ID como "llave"
            self.tareas[identificador] = nueva_tarea
            print(f"Tarea '{titulo}' (ID: {identificador}) añadida.")

    def eliminarTarea(self, identificador):
        if identificador in self.tareas:
            tarea = self.tareas.pop(identificador)  # .pop quita la tarea y nos la da
            print(f"Tarea con ID {identificador} ('{tarea['titulo']}') eliminada.")
        else:
            print(f"Error: No se encontró una tarea con ID {identificador}.")

    def marcarComoCompletada(self, identificador):
        if identificador in self.tareas:
            self.tareas[identificador]['completada'] = True
            print(f"Tarea ID {identificador} '{self.tareas[identificador]['titulo']}' marcada como completada.")
        else:
            print(f"Error: No se encontró una tarea con ID {identificador}")

    def mostrarTareasCompletadas(self):
        print("- LISTADO DE TAREAS:")
        encontrada = False

        for id_tarea, datos in self.tareas.items():
            if datos['completada'] == True:
                print(f"[{id_tarea}] {datos['titulo']} (Prioridad: {datos['prioridad']})")
                encontrada = True

        if not encontrada:
            print("No hay tareas completadas.")

    def mostrarTareasNoCompletadas(self):
        print("- LISTADO DE TAREAS:")
        encontrada = False

        for id_tarea, datos in self.tareas.items():
            if datos['completada'] == False:
                print(f"[{id_tarea}] {datos['titulo']} (Prioridad: {datos['prioridad']})")
                encontrada = True

        if not encontrada:
            print("No hay tareas no completadas.")

# --- Ejemplo de uso basado en tus imágenes ---
gestor = GestorTareas()
gestor.agregarTarea("P10", "Comprar billetes", 5)
gestor.agregarTarea("P10", "Repetida", 1)  # Debería dar error
gestor.marcarComoCompletada("D055")  # Debería dar error (no existe)
gestor.mostrarTareasCompletadas()
gestor.mostrarTareasNoCompletadas()