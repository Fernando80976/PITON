import random
numDados = int(input("dime cuantos dados vas a tirar"))
numCaras = int(input("dime cuantas caras son de dados"))
print("Vamos a tirar",numDados,"Dados de ",numCaras,"caras")
for  _ in range (0,numDados):
    print(random.randint(1,numCaras),end=",")