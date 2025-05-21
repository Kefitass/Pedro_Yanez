
def get_int(mensaje: str = "Bienvenido al programa",
            mensaje_error: str = "Error, vuelva a intentar",
            minimo: int = 15,
            maximo: int = 55,
            intentos: int = 3) -> int | None:
    print(mensaje)
    while intentos > 0:
        numero = int(input("Ingrese un número: "))
        if minimo <= numero <= maximo:
            print("\u00a1Número válido!")
            return numero
        else:
            print(mensaje_error)
            intentos -= 1
    return None

def get_float(mensaje: str = "Ingrese un número decimal:",
              mensaje_error: str = "Error, fuera de rango.",
              minimo: float = 0.0,
              maximo: float = 100.0,
              intentos: int = 3) -> float | None:
    print(mensaje)
    while intentos > 0:
        numero = float(input("Ingrese un número decimal: "))
        if minimo <= numero <= maximo:
            print("\u00a1Número válido!")
            return numero
        else:
            print(mensaje_error)
            intentos -= 1
    return None

def get_string(longitud: int) -> str | None:
    texto = input("Ingrese una cadena de texto: ")
    if len(texto) == longitud:
        return texto
    else:
        print("Error: la cadena no tiene la longitud exacta.")
        return None