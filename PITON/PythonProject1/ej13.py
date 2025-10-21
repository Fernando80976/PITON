import random
numDados = int(input("dime cuantos dados vas a tirar"))
numCaras = int(input("dime cuantas caras son de dados"))
print("Vamos a tirar",numDados,"Dados de ",numCaras,"caras")
while(numCaras%2!=0):
    numCaras = int(input("Mete numero de caras par!!"))

for  _ in range (0,numDados):
    print(random.randint(1,numCaras),end=",")