def cuadrado(x):
    return x**2
print(cuadrado(2))
#funcion lambda
cuadradoLambda=lambda x:x**2#hay que asignar el valor de la funcion lambda
print(cuadradoLambda(2))

sumaLambda=lambda x,y,z:x+y+z
print(sumaLambda(1,2,3))
media=lambda *lista:sum(lista)/len(lista)
print(media(3,4,5,6,7,83,2,4,57,83,24,56,87,2))