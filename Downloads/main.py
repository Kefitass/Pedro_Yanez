from input import get_int, get_float, get_string

# Prueba de get_int
entero = get_int("Ingrese un entero entre 10 y 20:", "Error: fuera de rango.", 10, 20, 3)
print("Resultado entero:", entero)

# Prueba de get_float
decimal = get_float("Ingrese un número decimal entre 0.5 y 5.5:", "Error: fuera de rango.", 0.5, 5.5, 3)
print("Resultado decimal:", decimal)

# Prueba de get_string
texto = get_string(5)
print("Cadena ingresada:", texto)
