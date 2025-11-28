def macsValidas(*macs):
    validas = 0
    invalidas = 0

    for m in macs:
        original = m  # Para mostrarlo igual que entró
        m = m.upper()

        # Procesar posibles separadores
        if " " in m:
            partes = m.split(" ")
            if len(partes) != 2 or partes[0] == "" or partes[1] == "":
                print(original, "no es válida")
                invalidas += 1
                continue
            numeros, letras = partes

        letras_invalidas = "AEIOUÑQ"
        mala = False


        if mala:
            print(original, "no es válida")
            invalidas += 1
        else:
            print(original, "es válida")
            validas += 1

    print("\nTotal válidas:", validas)
    print("Total no válidas:", invalidas)
macsValidas("F48E38AFFa1C")
