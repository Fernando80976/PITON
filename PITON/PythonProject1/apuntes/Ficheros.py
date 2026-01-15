#r -> read
#w -> write
#a -> append=añade al final del fichero
#usar r+w para lectura y estructura
#como grabamos el fichero
#t -> Texto no puedes grabar un objeto
#b -> Binario  puedes grabarlo

#SIEMPRE en un bloque de excepciones para evitar errores externos
try:
    fichero =open("quijote.txt","rt")
#read lee el fichero de golpe completo devuelve string,readlines una lista que cada linea es una lista del fichero
#readline() sin arugmentos lee la linea completa con (4) lee 4 caracteres
    linea=fichero.readline()
    while linea != "":
        if linea[-1]=="\n":#evitamos salto de linea
            print(linea[:-1])
        else:
            print(linea)
        linea=fichero.readline()


    fichero.close()
except:
    print("Error al manipular el fichero")

try:
    fichero =open("quijote.txt","wt")
    fichero.write("En un lugar de La Mancha \n")
    fichero.write("de cuyo nombre \n")
    fichero.write("No quiero acordarme \n")

    fichero.close()
except:
    print("Error al manipular el fichero")

try:
    fichero =open("quijote.txt","wt")
    lista=["En un lugar de La Mancha \n","de cuyo nombre \n","No quiero acordarme \n"]
    fichero.writelines(lista)
    fichero.close()
except:
    print("Error al manipular el fichero")