from datetime import datetime

class Nota:
    def __init__(self, titulo, descripcion, color):
        # Colores válidos
        colores_validos = ["amarillo", "verde", "blanco", "cyan"]
        if color.lower() not in colores_validos:
            raise ValueError(f"Color inválido: {color}. Debe ser uno de {colores_validos}")
        self.titulo = titulo
        self.descripcion = descripcion
        self.color = color.lower()
        self.fecha_creacion = datetime.now()

    def mostrar(self):
        return f"--- {self.titulo} ---\nDescripción: {self.descripcion}\nColor: {self.color}\nFecha: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\n"

class GestorNotas:
    def __init__(self):
        self.notas = []

    def crearNota(self, titulo, descripcion, color):
        self.notas.append(Nota(titulo, descripcion, color))
        print(f"Nota '{titulo}' creada.")

    def eliminarNota(self, titulo):
        for nota in self.notas:
            if nota.titulo == titulo:
                self.notas.remove(nota)
                print(f"Nota '{titulo}' eliminada.")
                return
        print(f"No se encontró la nota '{titulo}'.")

    def listarNotas(self):
        if not self.notas:
            print("No hay notas.")
            return
        for nota in self.notas:
            print(nota.mostrar())
# Crear gestor
gestor = GestorNotas()

# Crear notas
gestor.crearNota("Comprar leche", "Ir al supermercado a comprar leche", "amarillo")
gestor.crearNota("Estudiar Python", "Repasar clases y hacer ejercicios", "verde")
gestor.crearNota("Reunión", "Reunión con el equipo a las 10am", "cyan")

# Listar notas
print("\nListado de notas:")
gestor.listarNotas()

# Eliminar una nota
gestor.eliminarNota("Estudiar Python")

# Listar nuevamente
print("\nNotas después de eliminar:")
gestor.listarNotas()
