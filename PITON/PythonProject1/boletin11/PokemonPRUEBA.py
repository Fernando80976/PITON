import random

# --- Clase Pokemon mejorada ---
class Pokemon:
    tipos_validos = ["Normal", "Agua", "Fuego", "Planta", "Volador", "Lucha",
                     "Veneno", "Eléctrico", "Tierra", "Roca", "Psíquico",
                     "Hielo", "Bicho", "Fantasma", "Dragón"]

    def __init__(self, nombre, codigo, tipos, evolucion=None):
        if not (1 <= codigo <= 151):
            raise ValueError("El código debe estar entre 1 y 151")
        self.__codigo = codigo
        self.__nombre = nombre
        if isinstance(tipos, str):
            tipos = [tipos]
        if len(tipos) > 2:
            raise ValueError("Un Pokémon puede tener máximo dos tipos")
        for t in tipos:
            if t not in Pokemon.tipos_validos:
                raise ValueError(f"Tipo no válido: {t}")
        self.__tipos = tipos
        self.__evolucion = evolucion
        self.__pv = random.randint(50, 100)

    # Getters
    def getNombre(self):
        return self.__nombre

    def getCodigo(self):
        return self.__codigo

    def getTipos(self):
        return self.__tipos

    def getPV(self):
        return self.__pv

    # Evolución
    def evoluciona(self):
        if self.__evolucion:
            return self.__evolucion
        print(f"{self.__nombre} no puede evolucionar")
        return self

    # Ficha
    def ficha(self):
        evo = self.__evolucion.getNombre() if self.__evolucion else "No tiene"
        tipos_str = ", ".join(self.__tipos)
        return f"""
Nombre: {self.__nombre}
Código: {self.__codigo}
Tipos: {tipos_str}
PV: {self.__pv}
Evoluciona a: {evo}
"""

    # Combate sencillo
    def combateContra(self, otro):
        print(f"\n--- Combate: {self.getNombre()} VS {otro.getNombre()} ---")
        while self.__pv > 0 and otro.getPV() > 0:
            # Ataque del atacante
            ataque = random.randint(10, 30)
            otro.__pv -= ataque
            print(f"{self.getNombre()} ataca a {otro.getNombre()} por {ataque} PV")
            if otro.__pv <= 0:
                print(f"{otro.getNombre()} se debilitó. {self.getNombre()} gana!")
                break

            # Ataque del defensor
            ataque = random.randint(10, 30)
            self.__pv -= ataque
            print(f"{otro.getNombre()} ataca a {self.getNombre()} por {ataque} PV")
            if self.__pv <= 0:
                print(f"{self.getNombre()} se debilitó. {otro.getNombre()} gana!")
                break
# Crear Pokémon
venusaur = Pokemon("Venusaur", 3, "Planta")
ivysaur = Pokemon("Ivysaur", 2, "Planta", evolucion=venusaur)
bulbasaur = Pokemon("Bulbasaur", 1, "Planta", evolucion=ivysaur)

charmander = Pokemon("Charmander", 4, "Fuego")
charmeleon = Pokemon("Charmeleon", 5, "Fuego", evolucion=None)
# Para simplificar, no evolucionaremos charmander en este ejemplo

# Mostrar fichas
print(bulbasaur.ficha())
print(ivysaur.ficha())
print(venusaur.ficha())
print(charmander.ficha())

# Evolucionar un Pokémon
bulbasaur_evo = bulbasaur.evoluciona()
print("Después de evolucionar:")
print(bulbasaur_evo.ficha())

# Combate
bulbasaur_evo.combateContra(charmander)
