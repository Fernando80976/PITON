#tratamientos de excepciones
bien=False
while not bien:
    try:
        numero=int(input("\nintroduce un numero: "))
        resultado=10/numero
        print(resultado)
        if numero<0:
            raise Exception("No es un numero entero")#creamos una excepcion personalizada
        assert numero>=0,"no admito numeros negativos"#si la condicion se evalua como falso no salta solo si es false osea si num es >= no salta
    except ZeroDivisionError:
        print("no se puede dividir por 0")
    except ValueError:
        print("no has metido un entero")
    except:
        print("ha ocurrido una excepcion")#si hay una excepcion  muestra esto
    else:
        print("Todo bien")
        bien=True
    finally:
        print("Seguimos adelante...")
    print("programa finalizado")
#el bloque else se ejecuta si no hubo ninguna excepcion en0 el bloque try OPCIONAL
#finally se va  ejecutar haya o o no haya excepciones
