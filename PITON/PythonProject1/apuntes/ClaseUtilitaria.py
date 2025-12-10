# de fechas y horas
from datetime import date, time, datetime, timedelta

hoy =date.today()#fecha de hoy en formato ingles
print(hoy)
ahora=datetime.now()#momento actual con millonesimas de segundo
print(ahora)
#fecha especifica y horas que yo quiera
cumpleaños=date(1968,10,8)
citaMedica=datetime(2025,12,15,17,15)
despertador=time(6,15)
print(cumpleaños)
print(citaMedica)
print(despertador)

#formateado

formateado1=ahora.strftime("%H:%M:%S")#aqui especificamos lo que queremos %-M para que no se rellene con 0 de 03 ->3
print(formateado1)
formateado2=ahora.strftime(" %A %B  del %d-%m-%y  - %H:%M dia de la semana en numero %w mes en numero %m semanas del año %W dia del año %j")#  %a dia de la semana abreviado=Wed  %A dia de la semana completo=Wednesday %b mes abreviado=dic %B mes completo=dicember
#%I para la hora en formato 12 horas %H para formato 24 horas
# semanas del año empezando desde domingo %U empezando del primer lunes del año %W
print("la fecha es ",formateado2)

formateado3=ahora.strftime("%c")#formato automatico completo Wed Dec 10 12:16:04 2025

print(formateado3)
formateado3=ahora.strftime("%x")#formato ingles y auntomatico te da fecha fea 12/10/25


print(formateado3)
#OBTENER HORA
formateado3=ahora.strftime("%X")#este te da solo la hora
print(formateado3)

cadena="01-03-2025 14:30"
#lo queremos convertir a obj
#strptime para convertir de cadena a obj
#strftime de obj a cadena
fecha=datetime.strptime(cadena,"%d-%m-%Y %H:%M")
print(cadena)
#puedo operar con ellos individualmente
print(fecha.hour)
print(fecha.day)
print(fecha.minute)

#comparar fechas
if ahora >citaMedica:
    print("la fecha de ahora es posterior a tu cita medica")
else:
    print("La fehca de ahora es anterior a tu cita medica")
#sumar o restar a las fechas valores
nuevaFecha=ahora+timedelta(days=10,hours=2,weeks=1)
print(nuevaFecha)