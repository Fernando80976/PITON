import random
numDados = int(input("dime cuantos dados vas a tirar"))
print("Vamos a tirar",numDados,"")
igual=False
tiradas=[]
while igual==False:
    for  i in range (0,numDados):
            tiradas.append(random.randint(1,6))
    print(tiradas)
    for elemento in tiradas:
        if tiradas.count(elemento)==numDados:
            igual=True

print(tiradas)

