import random
lista=[]
pares=0
impares=0
for _ in range(10):
    azar = random.randint(1, 1000)
    print(azar)
    lista.append(azar)
    if azar % 2 == 0:
        pares+=1
    else:
        impares+=1
print("pares",pares,"impares",impares)
print("el mayor a sido",max(lista),"el menor a sido",min(lista))
