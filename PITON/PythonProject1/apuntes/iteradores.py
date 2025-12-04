#!/usr/bin/python3
#cuando un iterador llega al final salta el error
profesores=["Jose maria","Natalia","Agustin"]
iterador=iter(profesores)
#no hace falta index y eso cada vez que lo pones pasa al siguiente
print(next(iterador))

print(next(iterador))
print(next(iterador))
print(next(iterador,"STOP"))#cuando quiero usar un iterador pero no quiero reccibir una excepcion poongo segundo paramentro

class DiasdelaSemana:
    def __init__(self,dia=0):
        self._dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
        self._dia=dia
    def __iter__(self):#iterador
        return self#esto solo es devolver
    def __next__(self,stop=None):
        if self._dia==7:
            self._dia=0
        # if self._dia >=len(self._dias):
        #     if stop==None:
        #         raise StopIteration
        #     else:
        #         print(stop)
        dia_actual=self._dias[self._dia]
        self._dia+=1
        return dia_actual
semana=DiasdelaSemana(1)
iterador=iter(semana)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

print(next(iterador,"ya no hay mas dias"))
#ahora quiero que despues del domingo venga siempre el lunes
