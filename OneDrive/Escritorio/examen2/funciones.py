import random

def generar_mazo():
    palos = ["espada", "basto", "copa", "oro"]
    valores = [] 

    for i in range(1, 13):
        if i != 8 and i != 9: 
            valores.append(i)

    mazo = []
    for palo in palos:
        for valor in valores:
            mazo.append((valor, palo))

    random.shuffle(mazo)
    return mazo

def repartir_cartas(mazo_completo):
    pilas_tablero = [[] for _ in range(7)]
    fundaciones = [[] for _ in range(4)]
    mazo_reserva_temp = list(mazo_completo)
    pila_descarte = []

    for i in range(7):
        for j in range(i + 1):
            if len(mazo_reserva_temp) > 0:
                carta = mazo_reserva_temp[0]
                mazo_reserva_temp = mazo_reserva_temp[1:]
                pilas_tablero[i].append((carta[0], carta[1], j == i)) 
    
    return pilas_tablero, fundaciones, mazo_reserva_temp, pila_descarte