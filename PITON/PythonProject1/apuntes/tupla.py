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
