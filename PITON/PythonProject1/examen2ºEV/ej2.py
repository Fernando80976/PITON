
class biblioteca:

    def __init__(self,codigo,numPags,titulo,autor,prestado):
        self.__codigo=codigo
        self.__numPags=numPags
        self.__titulo=titulo
        self.__autor=autor
        self.__prestado=prestado
        self.stock = {}
class Libro(biblioteca):
    def __init__(self, codigo, numPags, titulo, autor, prestado,digital,NumEjemplaresDisponibles,NumPrestados):
        super().__init__(codigo, numPags, titulo, autor, prestado)
        self.__digital=digital
        self.__NumEjemplaresDisponibles=NumEjemplaresDisponibles
        self.__NumPrestados=NumPrestados
    def AñadirLibro(self):
        if self.stock[super().__titulo] ==self.__titulo and self.stock[super().__autor] ==self.__autor and self.stock["digital"] ==self.__digital:
            self.__NumEjemplaresDisponibles+=1
        else:
            nuevo_libro = {
                'codigo': self.__codigo,
                'NumPags': self.__numPags,
                'titulo': self.__titulo,
                'autor': self.__autor,
                'prestado': self.__prestado,
                'digital': self.__digital,
                'NumEjemplates': self.__NumEjemplaresDisponibles,
                'NumPrestados': self.__NumPrestados
            }
            self.stock[self.__codigo]=nuevo_libro




class Comic(biblioteca):
    def __init__(self, codigo, numPags, titulo, autor, prestado,color):
        super().__init__(codigo, numPags, titulo, autor, prestado)
        self.color=color



l1=Libro(1234,23,"iruma kun","osamu nishi",False,False,2,4)
