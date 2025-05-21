# main.py

from input_data import ingresar_10_numeros_enteros
from array_generales import (
    contar_positivos_negativos,
    sumar_numeros_pares,
    encontrar_mayor_impar,
    listar_numeros_ingresados,
    listar_numeros_pares,
    listar_numeros_en_posiciones_impares
)

def mostrar_menu():
    print("\n----- MENU DE OPCIONES -----")
    print("1 Ingresar datos (10 numeros)")
    print("2 Cantidad de positivos y negativos")
    print("3 Suma de los numeros pares")
    print("4 Mayor numero impar")
    print("5 Listar los numeros ingresados")
    print("6 Listar los numeros pares")
    print("7 Listar los numeros en posiciones impares")
    print("8 Salir del programa")
    print("--------------------------")

def main():
    numeros_ingresados = []
    datos_cargados = False

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            numeros_ingresados = ingresar_10_numeros_enteros()
            datos_cargados = True
            print("Numeros ingresados correctamente!")
        elif opcion == '8':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        elif not datos_cargados:
            print("⚠️ Primero debe ingresar los numeros (Opcion 1) antes de acceder a otras opciones.")
        elif opcion == '2':
            positivos, negativos = contar_positivos_negativos(numeros_ingresados)
            print(f"Cantidad de positivos: {positivos}")
            print(f"Cantidad de negativos: {negativos}")
        elif opcion == '3':
            suma = sumar_numeros_pares(numeros_ingresados)
            print(f"La sumatoria de los numeros pares es: {suma}")
        elif opcion == '4':
            mayor_impar = encontrar_mayor_impar(numeros_ingresados)
            if mayor_impar is not None:
                print(f"El mayor numero impar ingresado es: {mayor_impar}")
            else:
                print("No se encontraron numeros impares en la lista.")
        elif opcion == '5':
            listar_numeros_ingresados(numeros_ingresados)
        elif opcion == '6':
            listar_numeros_pares(numeros_ingresados)
        elif opcion == '7':
            listar_numeros_en_posiciones_impares(numeros_ingresados)
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()