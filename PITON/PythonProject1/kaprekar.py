def Kaprekar(numer):
    print()

numero=0
#objetivo 6174b
valido = False
while not valido:
        try:
            numero = int(input("introduce un numero: "))
            numS=str(numero)
            cifra = set(numS)
            if len(numS)!=4:
                print("No esta bien, son 4 cifras")

                raise Exception("no tiene 4 cifras")  # creamos una excepcion personalizada
            if len(set(numS)) == 1:
                print("Todos los dígitos son iguales, debe haber al menos uno diferente")
                raise Exception

        except:
            print("Hazlo de nuevo porfavor")

        else:
            print("Todo bien")
            valido=True





