import pickle
import mysql.connector


# --- EJERCICIO 1: Clase y Lectura de Fichero de Texto ---

class Pokemon:
    def __init__(self, pokedex_id, nombre, peso, altura, tipos):
        self.pokedex_id = pokedex_id
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.tipos = tipos  # Lista de tipos

    def mostrar(self):
        tipos_str = ", ".join(self.tipos)
        print(f"#{self.pokedex_id} - {self.nombre}")
        print(f"Peso: {self.peso}kg")
        print(f"Altura: {self.altura}m")
        print(f"Tipo: {tipos_str}")
        print("-" * 20)


def ejercicio_1():
    lista_pokemons = []
    lineas_erroneas = []

    try:
        with open("pokemons.txt", "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea: continue

                partes = [p.strip() for p in linea.split(",")]

                # Validación de errores según enunciado
                if not partes[0].isdigit():
                    lineas_erroneas.append(linea)
                    continue

                if len(partes) < 5:
                    lineas_erroneas.append(linea)
                    continue

                p_id = int(partes[0])
                p_nombre = partes[1]
                p_peso = partes[2]
                p_altura = partes[3]
                p_tipos = partes[4:]

                nuevo_pokemon = Pokemon(p_id, p_nombre, p_peso, p_altura, p_tipos)
                lista_pokemons.append(nuevo_pokemon)

    except FileNotFoundError:
        print("Error: El fichero 'pokemons.txt' no existe.")
        return []

    print("\n--- LISTA DE POKEMONS ---")
    for p in lista_pokemons:
        p.mostrar()

    if lineas_erroneas:
        print(f"\n{len(lineas_erroneas)} Líneas erróneas en el fichero:")
        for err in lineas_erroneas:
            print(err)

    return lista_pokemons


# --- EJERCICIO 2: Fichero Binario ---

def ejercicio_2(lista_pokemons):
    archivo_bin = "pokemons.dat"
    with open(archivo_bin, "wb") as f:
        pickle.dump(lista_pokemons, f)

    print("\n--- LECTURA DESDE FICHERO BINARIO ---")
    with open(archivo_bin, "rb") as f:
        objetos_recuperados = pickle.load(f)
        for p in objetos_recuperados:
            p.mostrar()


# --- EJERCICIO 3: Base de Datos (MySQL) ---

# --- EJERCICIO 3: Base de Datos (MySQL) con tus nombres de columna ---

def ejercicio_3(lista_pokemons):
    try:
        conexion = mysql.connector.connect(
            user="root",
            password="fere",
            host="localhost",
            database="pokemondb"
        )
        cursor = conexion.cursor()

        for p in lista_pokemons:
            # 1. Comprobar si existe usando 'numero_pokedex'
            query_check = "SELECT numero_pokedex FROM pokemon WHERE numero_pokedex = %s"
            cursor.execute(query_check, (p.pokedex_id,))

            if cursor.fetchone():
                print(f"ADVERTENCIA: El pokemon con código {p.pokedex_id} ya existe en la base de datos.")
                continue

                # 2. Insertar en tabla 'pokemon' (ajusta los nombres de columnas si varían)
            query_poke = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
            cursor.execute(query_poke, (p.pokedex_id, p.nombre, p.peso, p.altura))

            # 3. Manejar tipos (Tablas 'tipo' y 'pokemon_tipo')
            for t_nombre in p.tipos:
                # Insertar tipo si no existe
                query_tipo = "INSERT IGNORE INTO tipo (nombre) VALUES (%s)"
                cursor.execute(query_tipo, (t_nombre,))

                # Obtener el 'id_tipo'
                cursor.execute("SELECT id_tipo FROM tipo WHERE nombre = %s", (t_nombre,))
                resultado = cursor.fetchone()

                if resultado:
                    id_tipo_db = resultado[0]
                    # Insertar en tabla intermedia usando tus nombres de columna
                    # Asumo que la tabla intermedia usa 'numero_pokedex' e 'id_tipo'
                    query_relacion = "INSERT INTO pokemon_tipo (numero_pokedex, id_tipo) VALUES (%s, %s)"
                    cursor.execute(query_relacion, (p.pokedex_id, id_tipo_db))

        conexion.commit()
        print("\n¡Datos guardados correctamente en MySQL!")

        cursor.close()
        conexion.close()

    except mysql.connector.Error as err:
        print(f"Error en la base de datos: {err}")

# --- MAIN ---

if __name__ == "__main__":
    pokemons_validados = ejercicio_1()

    if pokemons_validados:
        ejercicio_2(pokemons_validados)
        ejercicio_3(pokemons_validados)