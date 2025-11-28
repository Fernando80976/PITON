#FUNCIONES
def miFuncion(mensaje):
    print("hola mis amores",mensaje)

miFuncion("DRAGONES")
def miFuncion1(mensaje):
    print("hola mis amores",mensaje)
    return "TE GUSTAN????????"
print(miFuncion1("DRAGONES"))

def miFuncion2(mensaje):
    print(mensaje)
valor=6
miFuncion2([1,2,3])
print(valor)

def saludo(nombre,despedida):
    return "hola"+nombre+despedida
nombre ="JOSE MARIA"
print(saludo(nombre,"Que te vaya bn"))
#peudes devolver varios valores
def devuelveNumeros():
    return 1,2,3,4
n1,n2,n3,n4=devuelveNumeros()#guardar valores devueltos
print(n1,n2,n3,n4,sep=",")

def funcion(valor):
    valor*=5
    print(valor)
n=2
funcion(n)
print(n)#no se modifica n solo se manda una copia a la funcion
def funcionn(valor):
    valor[0]*=5
    print(valor)
n=[2]
funcion(n)
print(n)
nombre2="y"
re=""
def saludar(nombre2,despedida="Te veo pronto bb"):
    print("VAMOS!!")
    return "hola" + nombre2 + despedida
print(saludar(nombre2,"hola"))
print(saludo(despedida="hola",nombre="hola2"))#podemos meter los parametros en distinto orden

def muestraProfes(veces,*nombres):#espera recibir numero variable de argumentos y los recibe empaquetados en una tupla
    for _ in range(veces):
        for n in nombres:
            print(n)
muestraProfes(2,"natalia","Agustin",77)#te devuelve lo quepasaste
muestraProfes(3,"rere","josema",89.9,"tete")

def repiteNombre(veces,nombre):
    for _ in range(veces):
        print(nombre,end=" *** ")
datos=[2,"Pepe"]
datos2=[4,"luis"]
repiteNombre(*datos)#esto es que  variables los elemetnos el primer datos las vces que se repite el name
repiteNombre(*datos2)
repiteNombre(*[3,"eva"])
