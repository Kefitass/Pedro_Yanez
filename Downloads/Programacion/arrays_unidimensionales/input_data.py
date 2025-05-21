def ingresar_10_numeros_enteros():
    numeros = []
    cantidad_ingresada = 0
    while cantidad_ingresada < 10:
        try:
            num = int(input(f"Ingrese el número {cantidad_ingresada + 1}/10 (entre -1000 y 1000): "))
            if -1000 <= num <= 1000:
                numeros.append(num)
                cantidad_ingresada += 1
            else:
                print("¡Error! El número debe estar entre -1000 y 1000.")
        except ValueError:
            print("¡Error! Por favor, ingrese un número entero válido.")
    return numeros