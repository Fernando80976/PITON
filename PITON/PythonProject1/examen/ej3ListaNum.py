lista=[20,45,55,29,20,24,14,45,20]


listaRepe=[]

for elemento in lista:
     if  lista.count(elemento)>1 and elemento not in listaRepe:
         listaRepe.append(elemento)
         print("el numero ",elemento,"apareció",lista.count(elemento),"veces")
if len(listaRepe)==0:
    print("no repetidos")
    
