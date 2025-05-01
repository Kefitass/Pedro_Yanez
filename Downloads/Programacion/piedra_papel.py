import random

def jugar():
    aciertos_jugador = 0
    aciertos_maquina = 0
    ronda = 1
    ganador_anterior = ""

    while True:
        jugador = int(input("Elige: 1 (Piedra), 2 (Papel), 3 (Tijera): "))
        maquina = random.randint(1, 3)

        print(f"Vos: {jugador} | Maquina: {maquina}")

        if jugador == maquina:
            print("Empate")
            ganador_anterior = ""
        elif (jugador == 1 and maquina == 3) or (jugador == 2 and maquina == 1) or (jugador == 3 and maquina == 2):
            print("Ganaste la ronda")
            aciertos_jugador += 1
            if ganador_anterior == "Jugador":
                print("Ganaste dos seguidas")
                break
            ganador_anterior = "Jugador"
        else:
            print("Perdiste la ronda")
            aciertos_maquina += 1
            if ganador_anterior == "Maquina":
                print("La maquina gano dos seguidas")
                break
            ganador_anterior = "Maquina"

        ronda += 1
        if ronda > 3:
            break

    if aciertos_jugador > aciertos_maquina:
        print("Ganaste la partida")
    elif aciertos_maquina > aciertos_jugador:
        print("La maquina gano la partida")
    else:
        print("Empate total")

jugar()
