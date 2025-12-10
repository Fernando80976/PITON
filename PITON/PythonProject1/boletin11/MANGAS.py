class mangas:
    def __init__(self, autor, titulo_japones, genero_principal, ultimoTomo,titulo_espanol="Sin título"):
        self.autor = autor
        self.titulo_japones = titulo_japones
        self.titulo_espanol = titulo_espanol
        self.ultimoTomo=ultimoTomo
        generosPrincipales=["shonen","shojo","seinen","josei",
                    "kodomo","yuri","spokon","isekai","hentai"]
        if genero_principal in(generosPrincipales):
            self.genero_principal = genero_principal
        else:
            self.genero_principal="Genero no conocido"