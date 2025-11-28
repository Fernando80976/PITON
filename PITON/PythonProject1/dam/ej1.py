def mask_pin(pin):
    pin = str(pin)


    resultado = []
    for d in pin:

        if d == "0":
            pos = 9
        else:
            pos = int(d) - 1

        linea = "X" * 10
        linea = linea[:pos] + "0" + linea[pos+1:] + "\n"
        resultado.append(linea)

    return tuple(resultado)  # ← ahora sí devuelve tupla


# Uso
pin = input("PIN 4 cifras: ")
if len(pin) != 4 or not pin.isdigit():
    print("pin invalido")
else:
    salida = mask_pin(pin)

    print("".join(salida))
