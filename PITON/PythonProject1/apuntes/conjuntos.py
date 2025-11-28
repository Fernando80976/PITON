#CONJUNTOS
lsitas=[1,2,3]
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

