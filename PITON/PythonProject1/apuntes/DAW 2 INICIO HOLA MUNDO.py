from struct import pack_into

print("hola\n MUndo")
#comentario
#comentario de bloque
'''
comentario blque
 deddedededede 
'''
"""
RERE
"""
edad=56
print(edad)
edad="cincuenta y seis"
print(edad)
texto="golo"
print(texto)
precio=56.6
acertado=True
#si quiero intentar hacer una constante aunque realmente no existan se pone
MESES_ANYO=12
#operaciones  aritmeticas +-*/ % == -= += /= =
# no existen ++ --
#operadores nuevos
# // calcula cociente de la division entera
# ** para calcular potencias 2 elevado a 3 = 2**3
nuevo =precio *5 +MESES_ANYO
print(5//2)
print(5%2)
print(5/2)
texto="y"+"y"
print(texto)
print(texto,"mundo")
texto=("hola")
curso=2
ciclo ="saw"
print(texto,"mundo")
print("hola bien",curso,ciclo)
#en define el caracter q se va a utilizar como definidor de espacio en blanco en vez salto de linea
print(texto,"Mundo","cruel","siempre","pepe",end=" *** ",sep="-")# sin salto de linea
#sep no cambia el separador entre variables y textos y argumentos por defecto sep es caracteren blanco
# input()#nuestro scanner
# edad=input("mete name q te ")
# print(edad)

''' '''
# edad1=int(input("mete edad "))
# if int(edad1) < 10:
#     print("eres menor")
# else:
#     print("Eres mayo")

# sueldo = float(input("mete edad "))
# tiene q estar pegaqdo en forma de escalera o dara error es necesario tabulacion
# if sueldo > 10000.56:
#     print("debes ser rico")
# elif sueldo==10:
#     pass#si quiero q en este bloque no salga nada no se puede dejar vacio
# else:
#     print("SISASS")

# for n in range(0,10):#n va a tomar los rangos entre el parentesis de 0 a 10 (0 incluido) (0,10]
#     print(n)
#     print("FIN de programa")
# for p in range(0, 10, 2):#esto es de 0 a 10 de 2 en 2
#         print(p)
#         print("FIN de programa")
# for n in range(0, -10, -1):  # esto es de 0 a -10 de 1 en 1
#     print(n)
#     print("FIN de programa")
#
# for c in "holas":
#     print(c)


#
# print("\n")
# cad=input("mete cad\n")# recorrer una cadena
# cadsinEsp=""
# for e in cad:
#     if(e==" "):
#         pass
#     else:# si no es un espacio lo muestro y añado
#         print(e)
#         cadsinEsp +=e
#
# print(cadsinEsp)




#bucle while
print("\n")
i=0
while i<10 :#los : para abrir bloque no necesario parentesis
    print(i)
    i+=1

#numeros aleatorios libreria random
import random
# print(random.randint(1,2))
azar =random.randint(1,6)#numeros randoms entre 1 y 6 ambos incluidos
print(azar)


#como redondear matematicamente nos deveuleve valor redondeado sin modificar valor original
pi = 3.14159
print(round(pi,2))
print(round(pi,3))
print(round(pi,4))
print(pi)

import random
for i in range(0,5):
    print(random.randint(1,6))

for _ in range(0,5):#cuando la variable del for no la uso ponemos _ necesitamos un for de 5 vueltas no una variable auxiliar
    print(random.randint(1,6))

 #si creas una variable dentro de un bloque(if,for,while,etc) aqui si existe fuera
for j in range(0,5):
    azar=random.randint(1,6)
    print(azar)

# print(j)
print(azar)
#para mostrar 2 variables juntos     print(dado1,dado2) la , es el espacio

#max y min
mayor=max(34.5,4,5,56,7,4,332,5,0.43)
print(mayor)
menor=min(34.5,4,5,56,7,4,332,5,0.43)
print(menor)

# #convertir a string cualquier cosa con str
# texto ="el numero es "+str(45)
# print(texto)
#
# #como se comportan las cadenas de textos
# texto1 ="hola mundo"
# print(texto1[3:8])#te devuelve una cadena nueva con solo del 3 al 8 "a mun"
# print(texto1[:8])#empieza del 0 hasta el 8
# print(texto1[3:])#empieza del 3 hasta el final
# print(texto1[3])#muestra solo el 3
# print(texto1[-1])#empieza del final y te devuelve o
# print(texto1[-5:-2])#para RECORRER CADENAS  AL REVES
# print(texto1[5:-2])
# #esto nos va a pemitir  dar saltos
# print(texto1[2:-2:2])#CON EL TECER PARAMETRO ESPECIFICAS EL SALTO DE CARACTERES
# print(texto1[::2])#si quieres mostrar solo los de posicion par
# print(texto1[1::2])#si quieres mostrar solo los de posicion inpar
# #con - empiezas desde la derecha
# print(texto1[::-1])#para dar la vuelta a al cadena
# #las cadenas no se pueden modificar directamente
#

#errores frecuentes
# texto2="hola"+"munfo" + "mi ammor"#concateniar
# print(texto2)
# print("hola","que","tal")#este es un print con 3 arguemtnos
# print("hola"+"que"+"tal")#concatenar
# texto2="hola"+"munfo" + "mi ammor"#concateniar
# texto3="hola","munfo" , "mi ammor"#tupla aqui pilla todo ('hola', 'munfo', 'mi ammor') esto es lo que muestra si la uso fuera de los parentesis y sirve para crear una tupla
# print(texto3)


texto2="hola "+"munfo " + "mi aMmor"+str(33)#concateniar
print(texto2)
print("hola",33)
for caracter in texto2 :
    print(caracter,end="-")
print("\n",len(texto2))#te devuelve la longitud  de lo que sea
for posicion in range(0,len(texto2)):#rrecorremos cadena
    print(posicion,"-", texto2[posicion])

#para mayusculas
print(texto2.upper())
print(texto2[2:4].upper())

#minusculas
print(texto2.lower())
#cambiar mayus minus invirtiendolas
print(texto2.swapcase())

#find me permite encontrar una subcadena dentro de una cadena y me devuelve la posicion si no aparece me devuelve -1
print(texto2.find("a"))#te devuelve posicion
#si hay mas de 1 encontrados te devuelve la posicion del primero
print(texto2.find("x"))
print(texto2.find("xxxx"))#busca una subcadena
# count me devuelve cuantas veces aparece
print(texto2.count("a"))
#iterar es meterlas en un bucle
print(texto2[4:].find("a"))# aqui buscamos la segunda a

#replace sustituir
print(texto2.replace("a","ge"))

print(texto2[4:].find("a"))# esto esto es una cadena nueva creada cadena !!MAL NO USAR da resultado erroneo!!
print( texto2.find("o",4))#usar este metodo ya que el otro te la la poscion respecto a la subcadena es decir que la posicion no es correcta

print(texto2.replace("a","e",1)) #aqui solo cambia la primera a es un limite

# switch de  pyton que se llama match


# salir =False
# while salir==False:
#     numero =input("mete opci")
#
#     match numero:
#         case "sigue":
#             print("numero 1")
#         case "n":## si es  2 o 3
#             print("numero 2")
#         case "S":
#             print()
#             salir=True
#         case _:
#             print("holiii")#valor por defecto y ya no se usan breaks
#     print("FIN")
# print("saliste")






#metodo que nos permite que si
texto5="33"
if texto5.isdigit():#nos dice si todo son numeros , no letras
    print("puedo convertirlo a entero")
else:
    print("no puedo  convertirlo a entero")

if texto5.isalpha() == True:  # nos dice si tiene o no numeros
    print("no tiene numeros")
else:
    print("Si tiene numeros")




#IMPORTANTE PARA TRAATAR TIPOS DE DATOS

#sirve para comparar tipo de dato y devuelve booleano
if isinstance(5,int):
    print("es un entero")
hola="hola"
if isinstance(hola,int):
    print("es un entero")
else:
    print("no lo es")
