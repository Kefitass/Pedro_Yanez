import pygame

from funciones import *
from graficos import *

pygame.init()

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Solitario")
reloj = pygame.time.Clock()

IMAGENES_CARTAS = {}
CARPETA_IMAGENES_CARTAS = 'cartas/'

def cargar_imagen_carta(valor, palo):
    nombre_archivo = f"{valor} de {palo}.jpg"
    ruta_completa = CARPETA_IMAGENES_CARTAS + nombre_archivo
    
    imagen = pygame.image.load(ruta_completa).convert_alpha()
    
    imagen_escalada = pygame.transform.scale(imagen, (90, 120))
    return imagen_escalada

IMAGEN_DORSO_CARTA = pygame.image.load(CARPETA_IMAGENES_CARTAS + "dorso carta.jpg").convert_alpha()
IMAGEN_DORSO_CARTA = pygame.transform.scale(IMAGEN_DORSO_CARTA, (90, 120))


def mostrar_imagen_carta(pantalla_a_dibujar, carta_tupla, x, y):
    valor, palo, boca_arriba = carta_tupla
    
    if boca_arriba:
        imagen_a_mostrar = cargar_imagen_carta(valor, palo)
    else:
        imagen_a_mostrar = IMAGEN_DORSO_CARTA
        
    pantalla_a_dibujar.blit(imagen_a_mostrar, (x, y))

pilas_tablero = []
pilas_de_llegada = []
mazo_reserva = []
pila_descarte = []

def iniciar_juego():
    global pilas_tablero, pilas_de_llegada, mazo_reserva, pila_descarte
    mazo_completo_barajado = generar_mazo()

    pilas_tablero_nuevas, fundaciones_nuevas, mazo_reserva_nuevo, pila_descarte_nueva = repartir_cartas(mazo_completo_barajado)
    pilas_tablero = pilas_tablero_nuevas
    pilas_de_llegada = fundaciones_nuevas 
    mazo_reserva = mazo_reserva_nuevo
    pila_descarte = pila_descarte_nueva


iniciar_juego()
ejecutando = True
while ejecutando:
    reloj.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pantalla.fill(VERDE)

    ancho_carta = 90
    alto_carta = 120
    espacio_horizontal_entre_pilas = 11.6
    espacio_vertical_dentro_pila = 30

    inicio_x_pilas = 20
    inicio_y_pilas = 160

    mazo_reserva_x = inicio_x_pilas + 0 * (ancho_carta + espacio_horizontal_entre_pilas)
    mazo_reserva_y = 20

    pila_descarte_x = mazo_reserva_x + ancho_carta + espacio_horizontal_entre_pilas
    pila_descarte_y = 20

    fundacion_final_x = ANCHO - 20
    fundacion_x_base = fundacion_final_x - (4 * ancho_carta + 3 * espacio_horizontal_entre_pilas)
    fundacion_y = 20


    indice_pila = 0
    while indice_pila < len(pilas_tablero):
        pila_de_cartas = pilas_tablero[indice_pila]
        posicion_x_pila = inicio_x_pilas + indice_pila * (ancho_carta + espacio_horizontal_entre_pilas)
        
        indice_carta = 0
        while indice_carta < len(pila_de_cartas):
            carta_completa = pila_de_cartas[indice_carta]

            posicion_y_carta = inicio_y_pilas + indice_carta * espacio_vertical_dentro_pila
            mostrar_imagen_carta(pantalla, carta_completa, posicion_x_pila, posicion_y_carta)
            
            indice_carta = indice_carta + 1
        
        indice_pila = indice_pila + 1

    if mazo_reserva:
        mostrar_imagen_carta(pantalla, (0, "", False), mazo_reserva_x, mazo_reserva_y)
    
    if pila_descarte:
        mostrar_imagen_carta(pantalla, (pila_descarte[-1][0], pila_descarte[-1][1], True), pila_descarte_x, pila_descarte_y)

    for i in range(4):
        fundacion_x = fundacion_x_base + i * (ancho_carta + espacio_horizontal_entre_pilas)
        if pilas_de_llegada[i]:
            mostrar_imagen_carta(pantalla, (pilas_de_llegada[i][-1][0], pilas_de_llegada[i][-1][1], True), fundacion_x, fundacion_y) # Actualizado aquí

    pygame.display.flip()

pygame.quit()