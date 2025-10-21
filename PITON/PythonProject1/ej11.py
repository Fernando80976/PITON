dado1=100
dado2=0
ntiradas=0
import random
while(dado1!=dado2):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print(dado1,dado2)

    ntiradas+=1
print(ntiradas,"numero de tiradas")