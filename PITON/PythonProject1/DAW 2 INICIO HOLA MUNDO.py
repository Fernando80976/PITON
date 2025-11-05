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




#Listas son colecciones
lista1=[]
lista2=list()#ambas son listas vacías es una variable no tipada
lista3=[2,4,589,33,1,44,6,7,2]#lista llena y puede tener elementos repetidos
lista4=["Eva","Alvaro","sara"]
lista5= [1,"eva",False,45.6,2,"Peter",[1,5,"DAM"]]#cada elemento de la lista es lo que a mi me de la gana

#como se recorre la lista
for elemento in lista5:
    print(elemento)

for i in range (0,len(lista5)):
    print(i,"-",lista5[i])

#forma mas eficiente y mejor
for i,nombre in enumerate(lista5):
    print(i,"-",nombre)

#si yo quiero referenciar el tercer elemento d ela ultima posicion
print(lista5[6][2])#segundo elemento del ultimo elemento
matriz=[[1,2,3],[4,5,6],[7,8,9]]#tipo Excel es un bidimensional
print(matriz[2][0])#basicamente array bidimensional

#sumar listas
#1º forma
lista6=lista3+lista4 #sumamos ambas listas primero 3 y luego 4
print(lista6)
#2º Forma
lista3.extend(lista4+lista5)#machacas la lista 3
print(lista3)
lista7=[1,2,3,4,5,6,7,8,9]
lista7.insert(1,333)#delante de la posicion que indique es decir me lo mete
lista7.insert(1111111,333)#si pones un indice que no existe se pone en la ultima pos
print(lista7)
lista7.append(8)#append siempre en la ultima
print(lista7)

#el metodo pop lo recupera
elem=lista7.pop()#eliminas el ultimo elemento y lo recuperas
print(elem)
print(lista7)
elem1=lista7.pop(2)#te recupera el segundo elemento y lo elimina
print(elem1)
print(lista7)

#eliminar un elemento concentro
lista7.remove(1)#si el elemento es unico nos lo elimina,si es repetido elimina el primero ,si no existe da error
print(lista7)

#Ordenacion de lista
lista8=[111,22,333,333,4,55,6.6,7,1234,3]
lista8.sort()#si es numeros de menos a mayor si es alfabetico primero menores luego mayores.Ascendentemente
print(lista8)

lista8.sort(reverse=True)#Ordenar Descentemente de mayor a menor te ordena lista original
print(lista8)

#preguntar si un elmento esta o no esta en la lista
if 333 in lista8: #if 333 not  in lista8: si no esta en la lista el 333

    print("esta en lista")
    print("aparece",lista8.count(333),"veces")
    print("aparece ",lista8.count(2))
else:
    print("no esta")
#CUANDO NECESITAMOS HACER UNA COPIA DE UNA LISTA USAMOS ESTO
num1=[4]
num2=num1.copy()
num2[0]*=2
print(num1)#son referencias asi copiamos una nueva no hacemos referencias a num1

print(lista8.index(333))#devuelve la posicion y si son 2 posiciones te devuelve el del primero
if 0 in lista8:
    print(lista8.index(0))

#convertir entre string y lista
texto3="hola MUndo"
lista9=list(texto3)
print(lista9)
lista10=[1,2,3,4,5,6,7,8]
texto4=str(lista10)#conversion de lsita a string
print(texto4)#parece una lista pero es una cadena de texto
texto4=texto4.replace("[","")
texto4=texto4.replace("]","")
print(texto4)
print(lista10[3:])#imprimir todos a partir del 3
print(lista10[:6])#imprimir todos del 0 al numero q digas no incluido la pos 6
lista11=lista10[::-1]#empeizas desde la derecha
print(lista11)
print(lista10[::2])#mostrar de 2 en 2
#random por lsitas

import random
alumnos = ["Alvaro","sara","eva","fernando","juan"]

print(random.choice(alumnos))#te devuelve 1 al azar
print(random.sample(alumnos,4))#te saca 4 alumnos aleatoriamente SIN REPETIR
random.shuffle(alumnos)#te desordena la lista aleatoriamente cambia el orden
print(alumnos)

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


    #tuplas son como listas pero no se pueden modificar jamas
lsitas=[1,2,3]
tupla=(1,2,3)#tuplas con parentesis
tupla2=("ANA","aanale","Pedro")
tupla3=("maria",28.5,False)
tupla4=4,5,6
print(tupla)
print(tupla4)
tupla5=()#tupla vacia no tiene sentido porque nunca jamas cambiará
pi=(3.14159,)#esto es basicamente decir que esto es una tupla y no una variable una tupla es como una constante pq sino seria variable
print(pi)
#CONVERTIR DE LISTA  A TUPLA
tupla6=tuple(lsitas)
print(tupla6)
#CONVERTIR DE TUPLA  A LISTA
lista2=list(tupla4)
print(lista2)
#CONVERTIR DE TUPLA A STRING
texto=str(tupla6)
print(texto)
tupla7=(1,2,(1,3,4),5,[1,2,3],7)#esto es crear una lista dentro de una tupla con lo cual ese apartado se puede modificar
print(tupla7)
print(tupla7[1])
print(tupla7[4])
tupla7[4][0]=33#aqui modificamos la lista dentro de la tupla
print(tupla7[4])
print(tupla7)
#funciona index,len,la podemos recorrer con for,metodo count

#CONJUNTOS
conjunto1={"ana","pedro","luis","eva","eva","tu mami"}#no te permite repetidos
print(conjunto1)#te los muestra aleatoriamente cada vez diferentes sin repetidos
conjunto2=set(lsitas)#un set no repetidos es un conjunto
print(conjunto2)
for nombre in conjunto1:
    print(nombre)
#no tienen posicion no podemos recuperarla y son mutables y NO DUPLICADOS
#print(conjunto1[0]) da error porque no tiene index
if "ana" in conjunto1:#si puedo averigurar si donde esta pero no se en que posicion
    print("Ana esta")
print(len(conjunto1))
conjunto1.add("pepe")
#provoca error
conjunto1.remove("pepe")
#para borrar un elemento sin error
conjunto1.discard("ana")#te borra el elemento sin error si no existe no hace nada none

conjunto1.add("pepe")
print(conjunto1.pop())#borra el primero pero como el primero cambia todo cambia
conjunto1.clear()#para borrar completamente el conjunto de la misma forma en las listas

profesorPrimero={"Natalia","Jose Maria","Pedro","Yago"}
profesorSegundo={"Jose Maria","Agustin","Puche","Pedro"}

#esto es para obtener la INTERSECCION de ambos conjuntos basicamente te muestra solo los que estan en ambas
print(profesorPrimero & profesorSegundo)
interseccion=profesorPrimero & profesorSegundo
#su metodo correspondiente
print(profesorPrimero.intersection(profesorSegundo))

#te junta ambos y claro los repetidos no se muestran
print(profesorPrimero | profesorSegundo)
#metodo correspontiente
print(profesorPrimero.union(profesorSegundo))


print(profesorPrimero - profesorSegundo)#esto te devuelven los que no esten en los 2 basicamente los no repetidos El primer conjunto que se  mete se compara con el segundo y te muestra lo que en el primero no se repita en el segundo
#metodo correspontiente
print(profesorPrimero.difference(profesorSegundo))


print(profesorSegundo - profesorPrimero)#esto te devuelven los que no esten en los 2 basicamente los no repetidos El primer conjunto que se  mete se compara con el segundo y te muestra lo que en el primero no se repita en el segundo
#metodo correspondiente
print(profesorSegundo.difference(profesorPrimero))


#FUNCIONES
def miFuncion(mensaje):
    print("hola mis amores",mensaje)

miFuncion("DRAGONES")
def miFuncion1(mensaje):
    print("hola mis amores",mensaje)
    return "TE GUSTAN????????"
print(miFuncion1("DRAGONES"))

def miFuncion2(mensaje):
    print(mensaje)
valor=6
miFuncion2([1,2,3])
print(valor)

def saludo(nombre,despedida):
    return "hola"+nombre+despedida
nombre ="JOSE MARIA"
print(saludo(nombre,"Que te vaya bn"))
#peudes devolver varios valores
def devuelveNumeros():
    return 1,2,3,4
n1,n2,n3,n4=devuelveNumeros()#guardar valores devueltos
print(n1,n2,n3,n4,sep=",")

def funcion(valor):
    valor*=5
    print(valor)
n=2
funcion(n)
print(n)#no se modifica n solo se manda una copia a la funcion
def funcionn(valor):
    valor[0]*=5
    print(valor)
n=[2]
funcion(n)
print(n)
nombre2="y"
re=""
def saludar(nombre2,despedida="Te veo pronto bb"):
    print("VAMOS!!")
    return "hola" + nombre2 + despedida
print(saludar(nombre2,"hola"))
print(saludo(despedida="hola",nombre="hola2"))#podemos meter los parametros en distinto orden

def muestraProfes(veces,*nombres):#espera recibir numero variable de argumentos y los recibe empaquetados en una tupla
    for _ in range(veces):
        for n in nombres:
            print(n)
muestraProfes(2,"natalia","Agustin",77)#te devuelve lo quepasaste
muestraProfes(3,"rere","josema",89.9,"tete")

def repiteNombre(veces,nombre):
    for _ in range(veces):
        print(nombre,end=" *** ")
datos=[2,"Pepe"]
datos2=[4,"luis"]
repiteNombre(*datos)#esto es que  variables los elemetnos el primer datos las vces que se repite el name
repiteNombre(*datos2)
repiteNombre(*[3,"eva"])


#tratamientos de excepciones
bien=False
while not bien:
    try:
        numero=int(input("\nintroduce un numero: "))
        resultado=10/numero
        print(resultado)
        if numero<0:
            raise Exception("No es un numero entero")#creamos una excepcion personalizada
        assert numero>=0,"no admito numeros negativos"#si la condicion se evalua como falso no salta solo si es false osea si num es >= no salta
    except ZeroDivisionError:
        print("no se puede dividir por 0")
    except ValueError:
        print("no has metido un entero")
    except:
        print("ha ocurrido una excepcion")#si hay una excepcion  muestra esto
    else:
        print("Todo bien")
        bien=True
    finally:
        print("Seguimos adelante...")
    print("programa finalizado")
#el bloque else se ejecuta si no hubo ninguna excepcion en0 el bloque try OPCIONAL
#finally se va  ejecutar haya o o no haya excepciones
