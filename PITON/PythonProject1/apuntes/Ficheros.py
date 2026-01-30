#r -> read
#w -> write lo modifica
#a -> append=añade al final del fichero, si no existe lo crea
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
    lista=["En un lugar de La Mancha \n","de cuyo nombre \n","No quiero acordarme \n"]#[1,3,4,5,] no puedes meter numeros parsealos a string
    fichero.writelines(lista)
    fichero.close()
except:
    print("Error al manipular el fichero")
#Lectura
try:
        fichero = open("quijote.txt", "rt")

        print(fichero.readlines())
        print(fichero.readline())

        fichero.close()
except:
        print("Error al manipular el fichero")

try:
        fichero = open("quijote.txt", "r+")#lectura y escritura

        print(fichero.readline())
        print (fichero.tell())
        fichero.write("XXX")
        print(fichero.tell())
        print(fichero.seek(0))#te regresa la posicion del cursor

        fichero.close()
except:
        print("Error al manipular el fichero")

try:
        fichero = open("quijote.txt", "r+")#lectura y escritura

        print(fichero.readline())
        print("Despues de leer estoy aqui",fichero.tell())
        fichero.write("XXX")
        print("despues de escribir estoy aqui",fichero.tell())
        #te regresa la posicion del cursor al pricnipio

        print(fichero.seek(0))
        print("despues de usar seek",print(fichero.tell()))
        print(fichero.seek(0,2))#al final del fichero
        print(fichero.seek(424))#colocar poscion que desees contadno desde el principio
        fichero.seek(0)
        fichero.seek(fichero.tell()+10)#te suma desde donde esta el cursor actualmente

        fichero.close()
except:
        print("Error al manipular el fi")