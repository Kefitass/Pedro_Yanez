import random

def mostrar_elemento(eleccion):
    if eleccion == 1:
        return "Piedra"
    elif eleccion == 2:
        return "Papel"
    elif eleccion == 3:
        return "Tijera"
    else:
        return "Invalido"

def verificar_ganador_ronda(jugador, maquina):
    if jugador == maquina:
        return "Empate"
    elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
        return "Jugador"
    else:
        return "Maquina"

def verificar_estado_partida(g1, g2, ronda_actual):
    if g1 >= 2 or g2 >= 2:
        return False
    if ronda_actual >= 3:
        return False
    return True

def verificar_ganador_partida(aciertos_jugador, aciertos_maquina):
    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    elif aciertos_maquina > aciertos_jugador:
        return "Maquina"
    else:
        return "Empate"

def jugar_piedra_papel_tijera():
    ronda = 1
    aciertos_jugador = 0
    aciertos_maquina = 0
    ganadores = []

    print("Bienvenido al juego Piedra, Papel o Tijera")
    print("Primer jugador en ganar dos veces seguidas o el mejor de 3 gana la partida")

    while True:
        print("Ronda", ronda)

        while True:
            try:
                jugador = int(input("Elige: 1 (Piedra), 2 (Papel), 3 (Tijera): "))
                if jugador in [1, 2, 3]:
                    break
                else:
                    print("Solo puedes elegir 1, 2 o 3")
            except:
                print("Ingresa un numero valido")

        maquina = random.randint(1, 3)

        print("Jugador elige:", mostrar_elemento(jugador))
        print("Maquina elige:", mostrar_elemento(maquina))

        resultado = verificar_ganador_ronda(jugador, maquina)
        print("Resultado de la ronda:", resultado)

        if resultado == "Jugador":
            aciertos_jugador += 1
        elif resultado == "Maquina":
            aciertos_maquina += 1

        ganadores.append(resultado)

        if len(ganadores) >= 2:
            if ganadores[-1] == ganadores[-2] and ganadores[-1] != "Empate":
                print("Victoria por dos rondas seguidas")
                break

        if not verificar_estado_partida(aciertos_jugador, aciertos_maquina, ronda):
            break

        ronda += 1

    print("Rondas ganadas - Jugador:", aciertos_jugador, "| Maquina:", aciertos_maquina)

    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina)
    if ganador == "Empate":
        print("Empate total. Se sigue jugando hasta que alguien gane")
        while ganador == "Empate":
            jugador = int(input("Elige: 1 (Piedra), 2 (Papel), 3 (Tijera): "))
            maquina = random.randint(1, 3)
            print("Jugador elige:", mostrar_elemento(jugador))
            print("Maquina elige:", mostrar_elemento(maquina))
            resultado = verificar_ganador_ronda(jugador, maquina)
            print("Resultado:", resultado)
            if resultado == "Jugador":
                ganador = "Jugador"
            elif resultado == "Maquina":
                ganador = "Maquina"
        print("Gana el desempate:", ganador)
    else:
        print("El ganador de la partida es:", ganador)

jugar_piedra_papel_tijera()
