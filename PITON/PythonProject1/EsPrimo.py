import random

num= random.randint(10,50)
def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False

while(es_primo(num)==False):
    es_primo(num)