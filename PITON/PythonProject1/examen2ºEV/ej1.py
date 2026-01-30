listaClientes=[]
listaSucursales=[]
listaCuentas=[]
class Sucursal:
    def __init__(self,direccion,provincia,COD):
        self.__direccion=direccion
        self.__provincia=provincia
        self.__COD=COD
    def getCodigo(self):
        return self.__COD
    def getProvincia(self):
        return self.__provincia


class Cuenta:
    def __init__(self,CodIden,saldo,titulares,Sucursal):
        self.__CodIden=CodIden
        self.__saldo=saldo
        self.__titulares=titulares
        self.__Sucursal=Sucursal
    def getTitulares(self):
        return self.__titulares
    def getSaldo(self):
        return self.__saldo
    def getCodigo(self):
        return self.__CodIden
    def MostrarDatos(self):
        return (f" Codigo : {self.__CodIden}"
                f" ,Saldo : {self.__saldo}"
                f" ,Titulares : {self.__titulares}"
                f" ,Sucursal : {self.__Sucursal}")
class Cliente:

    def __init__(self,nombre,apellidos,nif,telefono,Sucursal):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__nif=nif
        self.__telefono=telefono
        self.__Sucursal=Sucursal

    def CrearCuenta(self,saldo,Sucursal):
        c1 = Cuenta(345678910111,saldo,self.__nombre,Sucursal)
        listaCuentas.append(c1)
    def Cuentas(self):
        listaMiCuenta=[]
        for e in listaCuentas:

                listaMiCuenta.append(e)
        return listaMiCuenta
    def MostrarDatos(self):
        c=self.Cuentas()
        suma=0
        datosCuentas=""
        # for e in c:
        #     s=e.getSaldo
        #     suma+=s
        datosCuentas +=str((f" {e.getCodigo} - Saldo: {e.getSaldo()}€ \n"))
        datosCliente= (f" {self.__nombre} {self.__apellidos}. Cliente de la ucursal : {self.__Sucursal.getCodigo()} ({self.__Sucursal.getProvincia()}\n)")
        datos=datosCliente+datosCuentas+str(suma)
        return datos
Sucu1=Sucursal("calle mia","madir",1234)

c1=Cliente("fernando","basanta","1234E",72211133,Sucu1)

c1.CrearCuenta(1000,Sucu1)
print(c1.MostrarDatos())

