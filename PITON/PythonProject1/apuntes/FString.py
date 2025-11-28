def devuelveN():
    return "Jose maria morales"
nombre="Jose maria"
edad=57
sueldo=10000.556
print("mi nombre %s,tengo %d años y cobro %.2f euros al mes"%(nombre,edad,10000.55))
#Fstring f antes de la cadena
print(f"mi nombre {nombre},tengo {edad} años y cobro {sueldo :.2f} euros al mes")#:.2f limita a 2 decimales esa variable
ratio=0.08394
print(f"Porcentaje :{ratio :.2%}")#para pone porcentajes solo : % para porcentajes con 2 deciamles :.2%
habitantes=12433732940
print(f"Poblacion : {habitantes:,}".replace(",","."))#separador de millares
num1=45
num2=123
print(f"{num1:04d}\n{num2:04d}")#le deja 4 digitos al numero si quieres que no autocomplete con 0 -> : 4d

#ALINEAR TEXTO le dedica 20 espacios y luego lo alinea
texto="Python"
print(f"***{texto:<20}***")
print(f"***{texto:>20}***")
print(f"***{texto:^20}***")

#queremos que nos muestre el nombre de la variable junto a su valor
print(f"{num1=}\n{num2=}")#sirve para debuggear te devuleve en este caso num1=45 num2=123
texto=f"{num1=}\n{num2=}"#fstring es un tipo de dato con lo cual se puede guardar en variable
print(texto)

ficha=f"""
Ficha del Profesor/a:
===========================
Nombre: {devuelveN()}
Edad: {edad} años
Salario: {sueldo:.2f} {{euros}}
===========================

"""#fString de varias lineas
print(ficha)
#Condicionales
numero=32
print(f"numero par?\n{'verdadero'if numero%2==0 else 'false'}")

print(f"Validacion: {'Alto' if numero>50 else 'Medio' if numero>25 else 'Bajo'}")