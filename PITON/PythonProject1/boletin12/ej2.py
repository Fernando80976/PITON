from abc import ABC, abstractmethod
from datetime import datetime

# Clase abstracta
class NotaBase(ABC):
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now()

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def es_urgente(self):
        pass


# Nota normal
class NotaNormal(NotaBase):
    colores_validos = ["amarillo", "verde", "blanco", "cyan"]

    def __init__(self, titulo, descripcion, color):
        super().__init__(titulo, descripcion)
        if color.lower() not in NotaNormal.colores_validos:
            raise ValueError(f"Color inválido: {color}. Debe ser uno de {NotaNormal.colores_validos}")
        self._color = color.lower()

    def mostrar(self):
        return f"[NORMAL] {self.titulo}\nDescripción: {self.descripcion}\nColor: {self._color}\nFecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"

    def color(self):
        return self._color

    def es_urgente(self):
        return False


# Nota urgente
class NotaUrgente(NotaBase):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)
        self._color = "rojo"

    def mostrar(self):
        # Distinguimos las urgentes con !!!
        return f"[URGENTE!!!] {self.titulo.upper()}\nDescripción: {self.descripcion}\nColor: {self._color}\nFecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"

    def color(self):
        return self._color

    def es_urgente(self):
        return True


# Gestor de notas
class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNotaNormal(self, titulo, descripcion, color):
        self.notas.append(NotaNormal(titulo, descripcion, color))
        print(f"Nota normal '{titulo}' creada.")

    def crearNotaUrgente(self, titulo, descripcion):
        self.notas.append(NotaUrgente(titulo, descripcion))
        print(f"Nota URGENTE '{titulo}' creada.")

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                if nota.es_urgente():
                    confirm = input(f"La nota '{titulo}' es urgente. ¿Seguro que quieres eliminarla? (s/n): ").lower()
                    if confirm != 's':
                        print("Operación cancelada.")
                        return
                self.notas.remove(nota)
                print(f"Nota '{titulo}' eliminada.")
                return
        print(f"No se encontró la nota '{titulo}'.")

    def listarNotas(self):
        if not self.notas:
            print("No hay notas.")
            return
        # Primero urgentes
        notas_ordenadas = sorted(self.notas, key=lambda n: n.es_urgente(), reverse=True)
        for nota in notas_ordenadas:
            print(nota.mostrar())
# Crear gestor
gestor = GestorNotas()

# Crear notas normales
gestor.crearNotaNormal("Comprar leche", "Ir al supermercado a comprar leche", "amarillo")
gestor.crearNotaNormal("Estudiar Python", "Repasar clases y hacer ejercicios", "verde")

# Crear nota urgente
gestor.crearNotaUrgente("Reunión importante", "Reunión con el CEO a las 10am")

# Listar todas las notas
print("\n--- Listado de notas ---")
gestor.listarNotas()

# Intentar eliminar nota urgente
gestor.eliminarNota("Reunión importante")

# Listar nuevamente
print("\n--- Listado después de eliminar ---")
gestor.listarNotas()
