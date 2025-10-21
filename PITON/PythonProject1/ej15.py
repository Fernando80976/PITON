import random
num =int(input("mete n"))
num2 =int(input("mete n"))
if(num>num2):
    azar = random.randint(num2, num)
    print(azar)
else:
    print("mete n1 es mayor q n2")