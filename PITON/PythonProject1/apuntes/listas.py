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
print("HOLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
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