def validar_matriculas(*matriculas):
    validas = 0
    invalidas = 0

    for m in matriculas:
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

        elif "-" in m:
            partes = m.split("-")
            if len(partes) != 2 or partes[0] == "" or partes[1] == "":
                print(original, "no es válida")
                invalidas += 1
                continue
            numeros, letras = partes

        else:
            numeros = m[:4]
            letras = m[4:]

        # Comprobar 4 números y 3 letras
        if len(numeros) != 4 or len(letras) != 3 or not numeros.isdigit():
            print(original, "no es válida")
            invalidas += 1
            continue

        # Comprobar letras no permitidas
        letras_invalidas = "AEIOUÑQ"
        mala = False
        for L in letras:
            if not L.isalpha() or L in letras_invalidas:
                mala = True

        if mala:
            print(original, "no es válida")
            invalidas += 1
        else:
            print(original, "es válida")
            validas += 1

    # Resumen final
    print("\nTotal válidas:", validas)
    print("Total no válidas:", invalidas)
validar_matriculas(
    "7474-MXP",
    "5454 BCF",
    "4534FRT",
    "22CDR",
    "3567BAC",
    "4534       FRT",
    "4534   -  FRT",
    "1234mxt"
)
