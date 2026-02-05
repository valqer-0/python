import pygame
import random
import math
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

# Fondo e Imágenes
fondo = pygame.image.load('Fondo.jpg')
img_jugador = pygame.image.load('cohete.png')
img_balas = pygame.image.load('bala.png')

# --- SONIDOS ---
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

sonido_disparo = mixer.Sound('disparo.mp3')
sonido_colision = mixer.Sound('Golpe.mp3')

# --- PUNTAJE ---
puntaje = 0
fuente = pygame.font.Font('Fastest.ttf', 32)
texto_x = 10
texto_y = 10

# --- TEXTO FINAL DE JUEGO ---
fuente_final = pygame.font.Font('Fastest.ttf', 64)

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

def texto_game_over():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (130, 250))

# --- VARIABLES DE JUEGO ---
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

bala_x = 0
bala_y = 500
bala_y_cambio = 3
bala_visible = False

# --- FUNCIONES ---
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_balas, (x + 16, y + 10))

def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt((math.pow(x_1 - x_2, 2)) + (math.pow(y_1 - y_2, 2)))
    return distancia < 27

# --- BUCLE PRINCIPAL ---
se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_disparo.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Movimiento Jugador
    jugador_x += jugador_x_cambio
    if jugador_x <= 0: jugador_x = 0
    elif jugador_x >= 736: jugador_x = 736

    # Movimiento y Colisión de Enemigos
    for e in range(cantidad_enemigos):
        
        # --- CONDICIÓN DE FIN DE JUEGO ---
        # Si un enemigo baja más de 450 (cerca del jugador)
        if enemigo_y[e] > 450:
            for i in range(cantidad_enemigos):
                enemigo_y[i] = 1000 # Los mandamos lejos de la pantalla
            texto_game_over()
            break # Salimos del bucle de enemigos

        enemigo_x[e] += enemigo_x_cambio[e]

        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # Verificar Colisión
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Lógica de la Bala
    if bala_y <= -32:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Dibujar elementos
    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)

    pygame.display.update()