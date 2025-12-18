class mangas:
    def __init__(self, autor, titulo_japones, genero_principal, ultimoTomo,titulo_espanol="Sin título"):
        self.__autor = autor
        self.__titulo_japones = titulo_japones
        self.__titulo_espanol = titulo_espanol
        self.__ultimoTomo=ultimoTomo
        self.__tomos_Poseidos=[]
        generosPrincipales=["shonen","shojo","seinen","josei",
        "kodomo","yuri","spokon","isekai","hentai"]
        if genero_principal in(generosPrincipales):
            self.__genero_principal = genero_principal
        else:
            self.__genero_principal="Genero no conocido"
    def getTitulo_japones(self):
        return self.__titulo_japones
    def getTitulo_espanol(self):
        return self.__titulo_espanol
    def getAutor(self):
        return self.__autor
    def getUltimoTomo(self):
        return self.__ultimoTomo
    def getGenero_principal(self):
        return self.__genero_principal

    def setTitulo_espanol(self,titulo_espanol):
         self.__titulo_espanol=titulo_espanol


    def setUltimoTomo(self,ultimoTomo):
         self.__ultimoTomo=ultimoTomo
    def tomosObtenidos(self,*Ntomos):#Añadir tomos
            for tomo in Ntomos:
                if tomo > self.__ultimoTomo:
                    print("No puedes meter  un tomo invalido")
                else:
                    if tomo in self.__tomos_Poseidos:
                        print("Ya tienes este tomo! BOBO no repitas  y compra la coleccion completa")
                    else:
                        self.__tomos_Poseidos.append(tomo)
    def tomosFaltantes(self):
        tomosFaltantes=[]
        for i in range(1,self.__ultimoTomo+1):
            if i not in self.__tomos_Poseidos:
                tomosFaltantes.append(i)
        return tomosFaltantes
mi_manga = mangas(
    autor="Eiichiro Oda",
    titulo_japones="One Piece",
    genero_principal="shonen",
    ultimoTomo=15,
    titulo_espanol="One Piece"
)
#PRUEBAS
print(mi_manga.getAutor())             # Eiichiro Oda
print(mi_manga.getTitulo_japones())    # One Piece
print(mi_manga.getTitulo_espanol())    # One Piece
print(mi_manga.getGenero_principal())  # shonen
print(mi_manga.getUltimoTomo())        # 15

mi_manga.setTitulo_espanol("One Piece Español")
mi_manga.setUltimoTomo(20)
print(mi_manga.getTitulo_espanol())    # One Piece Español
print(mi_manga.getUltimoTomo())        # 20

mi_manga.tomosObtenidos(1, 2, 3, 3, 21)  # 3 repetido y 21 inválido

# Resultado esperado:
# Tomo 3 ya añadido a la colección.
# Tomo 21 no válido en la colección.

faltantes = mi_manga.tomosFaltantes()
print(faltantes)

# Resultado esperado si ultimoTomo=20 y tomos poseídos = [1,2,3]:
# [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mi_manga.tomosObtenidos(4,5,6)
print(mi_manga.tomosFaltantes())
# Ahora los faltantes empezarán desde 7 hasta 20
