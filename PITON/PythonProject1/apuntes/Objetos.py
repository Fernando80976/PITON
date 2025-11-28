from mimetypes import inited


class CuentaCorriente:
    __numCuentas=0
    def __init__(self,codigo,titular,saldo=5000):#self siempre debe estar ahi
#LOS CONSTRUCTORES SIEMPRE VAN ASÍ self es el this de java saldo por defecto 5000
        self.__codigo=codigo
        self.__saldo=saldo
        self.__titular=[]
        self.__titular.append(titular)
        CuentaCorriente.__numCuentas+=1#este atributo es comun a todos y cada vez que se cree un constructor aumenta se hace referencia con la clase
        #Getters y Setters aunque no son necesarios es una bueana practica

    @property  # decorador estamos definiendo un metodo que parezca un atributo
    def saldo(self):  # hay que poner el mismo nombre que el atributo
        return self.__saldo
    @saldo.setter#con esto definimos otra variable que es
    def saldo(self,saldo):
        self.__saldo=saldo

    @classmethod
    def getNumCuentas(cls):#cls simboliza  a la clase
        return (cls.__numCuentas)
    @staticmethod#funcion que pertenece a la clase pero no puede manipular nada ni objeto ni nada es por seguridad
    def devolverDatosSucursal():#no toca nada de la clase es un metodo auxiliar
        print("Calle del Pez ,7 ,2043, Madrid")
    def __str__(self):#la funcion que redifina debe seguir las reglas por ejemplo no recibe nada y devuelve str
        txt=str(self.__codigo)+" - "+str(self.__titular)+" : "+str(self.__saldo)+"€"
        return txt
    def __add__(self, segundaCuenta):#sumamos 2 cuentas la que pasamos y la actual
        self.__saldo+=segundaCuenta.__saldo
        self.__titular+=segundaCuenta.__titular
        return self
c1=CuentaCorriente(2323,"jose Maria morales",10000)
c2=CuentaCorriente(234424,titular="Kerin Aguilera")#acuerdate que solo se pone el nombre si quieres cambiar el orden titutal= se pone si no quieres orden sino no es necesario
# print(c1.__saldo)
# print(c2.__saldo)
# c2.saldo=2000
print(c2.saldo)#esto parece que estamos manipulando el atributo pero realmente no lo es ,la idea es creer que estamos manipulando un atributo pero realmente es una funcion

c2.saldo=2222222222222222 #aqui realmente llamamos al setter con el decorador @saldo.setter y cambiamos su valor aunque parezca que es el atributo
# print(c2.getSaldo())#hay que crear metodos  pq es una buena practica
print(CuentaCorriente.getNumCuentas())
c2.devolverDatosSucursal()
c1.devolverDatosSucursal()
CuentaCorriente.devolverDatosSucursal()
#convenciones solo para saberlo
#__saldo privado
#_codigo protegido
#RECOmendacion los atributos de clase siempre con __
print(c1._CuentaCorriente__saldo)# con el doble __ estan protegidos por manipulacion por error  y ahora este es el verdadero nombre de __saldo
print(c2.saldo)

#yo quiero una clase de alumnos pero sin funcionalidad solo que los guarde
class Alumno:
     pass#cuando lo quiero vacio
 #ahora nos ponemos  a meter datos en una clase vacia
alumno1=Alumno()
alumno1.nombre="Juan"
alumno1.apellidos="Balas"
alumno1.edad=24
alumno1.telefono=653533828

#METODOS MAGICOs
#constructor __init__
#destructor __del__
#salida en tipo de cadena __str__
#permite devolver longitud del objeto __len__

#podemos sobrescibir operadores aritmeticos
# __add__,__mul__,__sub__,__truediv__

#podemos sobrescibir operadores logicos
# __eq__ __ne__ __gt__ __it__
print(str(c1))
print(c2)
division=14/3
print(division.__round__(3))#esta mal esta practica

print(round(division,3))
c1=c1+c2
print(str(c1))
def funcionSobrecargada(valor):
    if isinstance(valor,int):
        print("recibo entero")
    elif isinstance(valor,str):
        print("String")
    else:
        print("no se que recibo")


funcionSobrecargada(10)
funcionSobrecargada("")
funcionSobrecargada(1.6)