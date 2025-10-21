import random

valor_max = int(input("Escribe un numero: "))
valores = []
while valor_max <10:
    valor_max = int(input("Escribe un numero mayor a 10!!!!: "))
while len(valores) < 5:
    azar = random.randint(1, valor_max)
    if azar % 2 == 0 and azar not in valores:
        valores.append(azar)

print("5 numeros pares entre 1 y ",valor_max)

var=valores

while var:
    print(var.pop(0))