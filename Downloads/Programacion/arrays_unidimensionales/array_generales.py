from especificas import es_par, es_impar, es_positivo, es_negativo

def contar_positivos_negativos(lista_numeros):
    positivos = 0
    negativos = 0
    for numero in lista_numeros:
        if es_positivo(numero):
            positivos += 1
        elif es_negativo(numero):
            negativos += 1
    return positivos, negativos

def sumar_numeros_pares(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if es_par(numero):
            suma += numero
    return suma

def encontrar_mayor_impar(lista_numeros):
    mayor_impar = None
    for numero in lista_numeros:
        if es_impar(numero):
            if mayor_impar is None or numero > mayor_impar:
                mayor_impar = numero
    return mayor_impar

def listar_numeros_ingresados(lista_numeros):
    print("Números ingresados:")
    for numero in lista_numeros:
        print(numero)

def listar_numeros_pares(lista_numeros):
    print("Números pares ingresados:")
    encontrados = False
    for numero in lista_numeros:
        if es_par(numero):
            print(numero)
            encontrados = True
    if not encontrados:
        print("No se encontraron números pares.")

def listar_numeros_en_posiciones_impares(lista_numeros):
    print("Números en posiciones impares (índice 1, 3, 5...):")
    encontrados = False
    for i in range(len(lista_numeros)):
        if es_impar(i):
            print(lista_numeros[i])
            encontrados = True
    if not encontrados:
        print("No hay números en posiciones impares.")
        