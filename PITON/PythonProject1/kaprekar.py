def kaprekar(numero):
    veces=0
    while numero !=6174:
        num =int("".join(sorted(str(numero).zfill(4))))
        num1 =int("".join(sorted(str(numero).zfill(4),reverse=True)))
        numero=(max(num,num1) -min(num,num1))
        print(max(num,num1),"-", min(num,num1),"=",numero)
        veces+=1
        #*matricula para numero indefinido de argumentos
    return veces
seguir=True
while seguir:
    try:
        numero = int(input("Introduce un numero: "))
        assert 9999 >= numero >= 1000, "Numero de 4 cifras obligatorio"
        cifras = set(list(str(numero)))
        assert len(cifras)>1, "Las cifras deben ser todas diferentes"
    except ValueError:
        print("Introduce valores numericos")
    except:
        print("El numero debe tener 4 cifras y que estas sean diferentes")
    else:
        print("Se ha repetido el proceso",kaprekar(numero),"veces para obtener la constante kaprekar")
        seguir=False
