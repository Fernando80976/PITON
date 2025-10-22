import  random
tex=input("mete cadena: ")
copCad=tex[::-1]
aux=[]
print(copCad)
for pos in range(0, len(copCad)):
    aux.append(copCad[pos])
print(aux)
random.shuffle(aux)

print(str(aux).replace("'","").replace(",","").replace("[","").replace("]",""))
