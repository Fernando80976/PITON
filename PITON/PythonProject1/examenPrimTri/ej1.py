def mask_pin(pinr):
    pinr = str(pinr)
    resultado = []
    for d in pinr:
        if d == "0":
            linea = "X" * 10
            linea+="\n"
            resultado.append(linea)
        else:
            pos = int(d)
            for _ in range(0, 10):
                linea = "X" * (10-pos)
                linea += "0" * pos
                linea +="\n"
            resultado.append(linea)
    return tuple(resultado)
pin = input("PIN 4 cifras o menos: ")
if len(pin) > 4 or not pin.isdigit() or len(pin) <0:
    print("pin invalido")
else:
    while len(pin) !=4:
        pin="0"+pin
    salida = mask_pin(pin)
    print("".join(salida))

