import pygame
import sys
import subprocess

pygame.init()

ancho = 1920
alto = 1080

pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Menú de juego")

# Cargar imagen de fondo
img_fondo = pygame.image.load("imagenes/menu/menu_2.jpg")
img_fondo = pygame.transform.scale(img_fondo, (ancho, alto))

# Cargar imágenes de las opciones
jugar_img = pygame.image.load("imagenes/menu/play1.png")
salir_img = pygame.image.load("imagenes/menu/quit1.png")

# Ajustar las imágenes al tamaño deseado
img_ancho = 180
img_alto = 70

jugar_img = pygame.transform.scale(jugar_img, (img_ancho, img_alto))
salir_img = pygame.transform.scale(salir_img, (img_ancho, img_alto))

# Cargar imágenes de las opciones seleccionadas
jugar_seleccion_img = pygame.image.load("imagenes/menu/play2.png")
salir_seleccion_img = pygame.image.load("imagenes/menu/quit2.png")

seleccion_img_ancho = 190
selected_img_alto = 80

jugar_seleccion_img = pygame.transform.scale(jugar_seleccion_img, (seleccion_img_ancho, selected_img_alto))
salir_seleccion_img = pygame.transform.scale(salir_seleccion_img, (seleccion_img_ancho, selected_img_alto))

background_musica = "imagenes/music/Enter theme.mp3"
pygame.mixer.music.load(background_musica)
pygame.mixer.music.play(-1)

# Colores
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Fuente del menú
menu_fuente = pygame.font.Font("imagenes/fuentes/8083-fontps.ttf", 50)

# Variables para el menú
opciones = [
    (jugar_img, jugar_seleccion_img, "Jugar"),
    (salir_img, salir_seleccion_img, "Salir"),
]
opcion_seleccionada = 0

sound_enabled = True
fullscreen_enabled = False

# Ventana de presentación
def mostrar_presentacion():
    ventana_presentacion = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Presentación")

    # Cargar imagen de fondo para la presentación
    presentacion_background = pygame.image.load("imagenes/menu/presentacion.png")
    presentacion_background = pygame.transform.scale(presentacion_background, (ancho, alto))

    logo_img = pygame.image.load("imagenes/menu/integrantes.jpg")
    logo_img = pygame.transform.scale(logo_img, (1200, 400))

    presentation_fuente = pygame.font.Font("imagenes/fuentes/8083-fontps.ttf", 60)
    texto_ini = "AltF4s ... Presenta"
    texto_fin = ""
    for letra in texto_ini:
        texto_fin += letra
        ventana_presentacion.blit(presentacion_background, (0, 0))
        ventana_presentacion.blit(logo_img, (ancho // 2 - 600, alto // 2 - 70))
        grupo_texto = presentation_fuente.render(texto_fin, True, WHITE)
        grupo_rect = grupo_texto.get_rect(center=(ancho // 2, alto // 2 - 200))
        ventana_presentacion.blit(grupo_texto, grupo_rect)
        pygame.display.flip()
        pygame.time.delay(150)

    pygame.time.wait(3000)


# Mostrar ventana de presentación antes del menú
mostrar_presentacion()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
            elif event.key == pygame.K_RIGHT:
                opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
            elif event.key == pygame.K_RETURN:
                if opcion_seleccionada == 0:
                    pygame.mixer.music.set_volume(0)
                    subprocess.run(["python", "game.py"])
                    pygame.mixer.music.set_volume(1)
                elif opcion_seleccionada == 1:
                    pygame.quit()
                    sys.exit()

    pantalla.blit(img_fondo, (0, 0))
    for i, (image, seleccion_img, option) in enumerate(opciones):
        if i == 0:
            img_rect = image.get_rect(left=ancho // 4, centery=alto // 2 + i * 120)
            seleccion_img_rect = seleccion_img.get_rect(left=ancho // 4, centery=alto // 2 + i * 120)
        else:
            img_rect = image.get_rect(right=ancho - ancho // 4, centery=alto // 2 + i * 120)
            seleccion_img_rect = seleccion_img.get_rect(right=ancho - ancho // 4, centery=alto // 2 + i * 120)

        if i == opcion_seleccionada:
            pantalla.blit(seleccion_img, seleccion_img_rect)
        else:
            pantalla.blit(image, img_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
