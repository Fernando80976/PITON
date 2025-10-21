while True:
    fraccion = input("Escribe tu fracción: ").strip()

    # Comprobaciones básicas
    if fraccion.count("/") != 1:
        print("Error: la fracción debe tener exactamente una barra '/'.")
        continue

    if fraccion.startswith("/") or fraccion.endswith("/") :
        print("Error: la barra no puede estar al inicio ni al final.")
        continue

    numerador, denominador = fraccion.split("/")

    # Verificar que solo contengan dígitos enteros
    if not numerador.isdigit() or not denominador.isdigit():
        print("Error: solo se permiten números enteros, sin letras ni decimales.")
        continue

    numerador = int(numerador)
    denominador = int(denominador)

    if denominador == 0:
        print("❌ Error: el denominador no puede ser 0.")
        continue

    # Calcular la fracción
    resultado = round(numerador / denominador, 3)

    print("Solución: ",resultado)
    break
