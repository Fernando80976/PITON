import re

#RString
patron=r"[6-8][0-9]{8}"#detras  significa que es una expresion regular significa que tiene q ser el primero del 6-8 incluidos y luego los otros 8 de 0-9
num1="655112233"
num2="912342555"
#3 metodos match te valida si la cadena es valida al principio solo la comprobacion de [6-8] SI EMPIEZA POR EL PATRON
#search busca el patron dentro de la cadena y si se cumplen me da igual dnd esten en cualquier punto
#fullmatch la validacion debe ser en la cadena completa
#NO PONER ==True porque devuelve un OBJ
if re.match(patron,num1):
    print("es un telefono valido")
else:
    print("no lo es")
if re.match(patron, num2):
        print("es un telefono valido")
else:
        print("no lo es")

if re.match(patron, num2)!="none":#o "null"
        print("es un telefono valido")
else:
        print("no lo es")



if re.fullmatch(patron, num1):
        print("es un telefono valido")
else:
        print("no lo es")
if re.fullmatch(patron, num2):
            print("es un telefono valido")
else:
            print("no lo es")
patron2 = r"[A-Za-z\-áéqwéŕýúíóṕĺḱj́hǵǵf.0-9\s]{4,8}"#r"[A-Z]{8}" si quieres validar - pon /- {4,8} esto hace que pueda tener de 4 a 8 de tamaño si quiero incluir espacio en blanco usa /s
texto="CDE.- RY"#con [*!-] es otra
if re.fullmatch(patron2, texto):
            print("es un texto valido")
else:
    print("no lo es")
#? de 0 a 1 * de 0 a x + de 1 a x
patronMatricula=r"[0-9]{4}[\s|-]?[B-DF-HJ-NPR-TV-Z]{3}"
#[\S|-]? esto es un unico espacio en blaco un - o nada
patron3=r"[^579]"#unico
#esto defeberia validar todo menos uno de esos caracteres
texto="0"
if re.fullmatch(patron3, texto):
            print("es un texto valido")
else:
    print("no lo es")