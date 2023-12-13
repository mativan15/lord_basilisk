import pygame
import enemigos
import jugador
import vida
import drop
import random

#configuracion
pygame.init()
#titulo
pygame.display.set_caption("Lord Basilisk")
#reloj
reloj = pygame.time.Clock()
#musica
pygame.mixer.music.load("imagenes/music/Death by Glamour.mp3")
#dimensiones
p_alto = 1080
p_ancho = 1920
#pantalla
pantalla = pygame.display.set_mode((p_ancho,p_alto))
#fondo
fondo_img = pygame.image.load("imagenes/niveles/mapa_1.jpg")
fondo = pygame.transform.scale((fondo_img), (1920, 1080))
#funcion para texto
fuente = pygame.font.Font(None,100)
fuente_danio = pygame.font.Font(None,35)
#fin del juego variables
imagen = pygame.image.load("imagenes/menu/gameover.png")
imagen_ancho, imagen_alto = imagen.get_size()
cuadrado_lado = max(imagen_ancho, imagen_alto)
cuadrado_x = (p_ancho - cuadrado_lado) // 2
cuadrado_y = (p_alto - cuadrado_lado) // 2

#---------------------------------------

#funciones aparicion random
def aleatoriox():
    num = random.randint(-300,-100)
    numx = random.randint(2020,2220)
    selx = random.choice((num,numx))
    return selx
def aleatorioy():
    num = random.randint(-300,-100)
    numy = random.randint(1180,1380)
    sely = random.choice((num,numy))
    return sely

#-------------------------------------------
#LISTAS
#enemigos
minotauros = []
lagartos = []
esqueletos = []
calabacines = []
orcos = []
frankis = []
#bolitas vida
bolitas_vida = []

#-------------------------------------------

#CLASES INTERNAS
#atributos iniciales
velocidad = 3
rango_ataque = 300
danio = 3
#clase personaje
class personaje:
    def __init__(self):
        self.jugador = jugador.Jugador(p_ancho//2, p_alto//2, velocidad, rango_ataque, danio)
    def posicionar(self):
        pantalla.blit(self.jugador.image,self.jugador.rect)
#clase para enemigo
class enemigo:
    def __init__(self, tipo_, velocidad_mult_, vida_mult_, danio_mult_):
    #seleccion de tipo
        self.tipo = tipo_
        if self.tipo == 1:
            self.minotauro = enemigos.Minotauro(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
        if self.tipo == 2:
            self.lagarto = enemigos.Lagarto(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
        if self.tipo == 3:
            self.esqueleto = enemigos.Esqueleto(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
        if self.tipo == 4:
            self.calabacin = enemigos.Calabacin(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
        if self.tipo == 5:
            self.orco = enemigos.Orco(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
        if self.tipo == 6:
            self.franki = enemigos.Franki(aleatoriox(),aleatorioy(),velocidad_mult_,vida_mult_,danio_mult_)
    #colocar enemigo
    def poner_enemigo(self):
        if self.tipo == 1:
            pantalla.blit(self.minotauro.image,self.minotauro.rect)
        if self.tipo == 2:
            pantalla.blit(self.lagarto.image,self.lagarto.rect)
        if self.tipo == 3:
            pantalla.blit(self.esqueleto.image,self.esqueleto.rect)
        if self.tipo == 4:
            pantalla.blit(self.calabacin.image,self.calabacin.rect)
        if self.tipo == 5:
            pantalla.blit(self.orco.image,self.orco.rect)
        if self.tipo == 6:
            pantalla.blit(self.franki.image,self.franki.rect)
    #perseguir al jugador
    def perseguir(self):
        if self.tipo == 1:
            if jugador1.jugador.rect.x > self.minotauro.rect.x:
                self.minotauro.mover_derecha()
            if jugador1.jugador.rect.y > self.minotauro.rect.y and jugador1.jugador.rect.x >= self.minotauro.rect.x:
                self.minotauro.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.minotauro.rect.y and jugador1.jugador.rect.x >= self.minotauro.rect.x:
                self.minotauro.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.minotauro.rect.x:
                self.minotauro.mover_izquierda()
            if jugador1.jugador.rect.y > self.minotauro.rect.y and jugador1.jugador.rect.x <= self.minotauro.rect.x:
                self.minotauro.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.minotauro.rect.y and jugador1.jugador.rect.x <= self.minotauro.rect.x:
                self.minotauro.mover_arriba_izquierda()
        if self.tipo == 2:
            if jugador1.jugador.rect.x > self.lagarto.rect.x:
                self.lagarto.mover_derecha()
            if jugador1.jugador.rect.y > self.lagarto.rect.y and jugador1.jugador.rect.x >= self.lagarto.rect.x:
                self.lagarto.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.lagarto.rect.y and jugador1.jugador.rect.x >= self.lagarto.rect.x:
                self.lagarto.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.lagarto.rect.x:
                self.lagarto.mover_izquierda()
            if jugador1.jugador.rect.y > self.lagarto.rect.y and jugador1.jugador.rect.x <= self.lagarto.rect.x:
                self.lagarto.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.lagarto.rect.y and jugador1.jugador.rect.x <= self.lagarto.rect.x:
                self.lagarto.mover_arriba_izquierda()
        if self.tipo == 3:
            if jugador1.jugador.rect.x > self.esqueleto.rect.x:
                self.esqueleto.mover_derecha()
            if jugador1.jugador.rect.y > self.esqueleto.rect.y and jugador1.jugador.rect.x >= self.esqueleto.rect.x:
                self.esqueleto.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.esqueleto.rect.y and jugador1.jugador.rect.x >= self.esqueleto.rect.x:
                self.esqueleto.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.esqueleto.rect.x:
                self.esqueleto.mover_izquierda()
            if jugador1.jugador.rect.y > self.esqueleto.rect.y and jugador1.jugador.rect.x <= self.esqueleto.rect.x:
                self.esqueleto.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.esqueleto.rect.y and jugador1.jugador.rect.x <= self.esqueleto.rect.x:
                self.esqueleto.mover_arriba_izquierda()
        if self.tipo == 4:
            if jugador1.jugador.rect.x > self.calabacin.rect.x:
                self.calabacin.mover_derecha()
            if jugador1.jugador.rect.y > self.calabacin.rect.y and jugador1.jugador.rect.x >= self.calabacin.rect.x:
                self.calabacin.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.calabacin.rect.y and jugador1.jugador.rect.x >= self.calabacin.rect.x:
                self.calabacin.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.calabacin.rect.x:
                self.calabacin.mover_izquierda()
            if jugador1.jugador.rect.y > self.calabacin.rect.y and jugador1.jugador.rect.x <= self.calabacin.rect.x:
                self.calabacin.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.calabacin.rect.y and jugador1.jugador.rect.x <= self.calabacin.rect.x:
                self.calabacin.mover_arriba_izquierda()
        if self.tipo == 5:
            if jugador1.jugador.rect.x > self.orco.rect.x:
                self.orco.mover_derecha()
            if jugador1.jugador.rect.y > self.orco.rect.y and jugador1.jugador.rect.x >= self.orco.rect.x:
                self.orco.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.orco.rect.y and jugador1.jugador.rect.x >= self.orco.rect.x:
                self.orco.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.orco.rect.x:
                self.orco.mover_izquierda()
            if jugador1.jugador.rect.y > self.orco.rect.y and jugador1.jugador.rect.x <= self.orco.rect.x:
                self.orco.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.orco.rect.y and jugador1.jugador.rect.x <= self.orco.rect.x:
                self.orco.mover_arriba_izquierda()
        if self.tipo == 6:
            if jugador1.jugador.rect.x > self.franki.rect.x:
                self.franki.mover_derecha()
            if jugador1.jugador.rect.y > self.franki.rect.y and jugador1.jugador.rect.x >= self.franki.rect.x:
                self.franki.mover_abajo_derecha()
            if jugador1.jugador.rect.y < self.franki.rect.y and jugador1.jugador.rect.x >= self.franki.rect.x:
                self.franki.mover_arriba_derecha()
            if jugador1.jugador.rect.x < self.franki.rect.x:
                self.franki.mover_izquierda()
            if jugador1.jugador.rect.y > self.franki.rect.y and jugador1.jugador.rect.x <= self.franki.rect.x:
                self.franki.mover_abajo_izquierda()
            if jugador1.jugador.rect.y < self.franki.rect.y and jugador1.jugador.rect.x <= self.franki.rect.x:
                self.franki.mover_arriba_izquierda()

#clase para bola de vida
class bol_vida:
    def __init__(self,x,y,tipo):
        self.vida = drop.Bolita_vida(x,y,tipo)
    def poner_bol_vida(self):
        pantalla.blit(self.vida.image,self.vida.rect)
    def dar_vida(self):
        return self.vida.monto_curacion()

#----------------------------------------------

#CREACION DENTRO
#crear barra y jugador
barra = vida.Barra_vida()
jugador1 = personaje()

#------------------------------------------

#TEXTOS
#danio sobre enemigo
def danio_texto(rect_enemigo):
    texto = fuente_danio.render(str(int(jugador1.jugador.danio)),0,(255,255,255),None)
    pantalla.blit(texto,rect_enemigo)
#cantidad vida
def vida_texto():
    texto = fuente.render("Vida:" + str(int(jugador1.jugador.vida)),0,(0,255,0),None)
    pantalla.blit(texto,(150,0))
#nivel jugador
def nivel_texto():
    texto = fuente.render("Nivel:" + str(int(jugador1.jugador.nivel)),0,(0,0,255),None)
    pantalla.blit(texto,(p_ancho - 300,0))
#contador de tiempo(segundos)
def contador(tiempo):
    seg = int(tiempo)
    texto = fuente.render(str(seg),0,(255,0,0),None)
    pantalla.blit(texto,(p_ancho//2,0))
#contador de puntaje
def puntaje_contador(puntaje):
    texto = fuente.render(str(puntaje),0,(255,255,255),None)
    pantalla.blit(texto,(p_ancho//2,p_alto - 100))
#------------------------------------------

#FUNCIONES

#DEF de JUGADOR

# ataque del jugador
def atacar(tiempo):
    if int(tiempo) % 10 == 0:
        #pygame.draw.rect(pantalla,(0,0,0),jugador1.jugador.ataque(),1)
        pantalla.blit(jugador1.jugador.image_ataque,jugador1.jugador.ataque())
        for i in minotauros:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.minotauro.rect):
                i.minotauro.vida -= jugador1.jugador.danio
                danio_texto(i.minotauro.rect)
        for i in lagartos:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.lagarto.rect):
                i.lagarto.vida -= jugador1.jugador.danio
                danio_texto(i.lagarto.rect)
        for i in esqueletos:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.esqueleto.rect):
                i.esqueleto.vida -= jugador1.jugador.danio
                danio_texto(i.esqueleto.rect)
        for i in calabacines:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.calabacin.rect):
                i.calabacin.vida -= jugador1.jugador.danio
                danio_texto(i.calabacin.rect)
        for i in orcos:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.orco.rect):
                i.orco.vida -= jugador1.jugador.danio
                danio_texto(i.orco.rect)
        for i in frankis:
            ataquejug = jugador1.jugador.ataque()
            if ataquejug.colliderect(i.franki.rect):
                i.franki.vida -= jugador1.jugador.danio
                danio_texto(i.franki.rect)

#cambio de vida
def cambiar_vida():
    pantalla.blit(barra.image,(0,0))
    if jugador1.jugador.vida == 100:
        barra.poner_vida(10)
    if jugador1.jugador.vida < 100 and jugador1.jugador.vida >= 90:
        barra.poner_vida(9)
    if jugador1.jugador.vida < 90 and jugador1.jugador.vida >= 80:
        barra.poner_vida(8)
    if jugador1.jugador.vida < 80 and jugador1.jugador.vida >= 70:
        barra.poner_vida(7)
    if jugador1.jugador.vida < 70 and jugador1.jugador.vida >= 60:
        barra.poner_vida(6)
    if jugador1.jugador.vida < 60 and jugador1.jugador.vida >= 50:
        barra.poner_vida(5)
    if jugador1.jugador.vida < 50 and jugador1.jugador.vida >= 40:
        barra.poner_vida(4)
    if jugador1.jugador.vida < 40 and jugador1.jugador.vida >= 30:
        barra.poner_vida(3)
    if jugador1.jugador.vida < 30 and jugador1.jugador.vida >= 20:
        barra.poner_vida(2)
    if jugador1.jugador.vida < 20 and jugador1.jugador.vida > 0:
        barra.poner_vida(1)
    if jugador1.jugador.vida <= 0:
        barra.poner_vida(0)

#daño al jugador
def danio_jugador():
    for i in minotauros:
        if jugador1.jugador.rect.colliderect(i.minotauro.rect):
            #pygame.draw.rect(pantalla,(255,0,0),jugador1.jugador.rect,4)
            jugador1.jugador.vida -= i.minotauro.danio
            cambiar_vida()
    for i in lagartos:
        if jugador1.jugador.rect.colliderect(i.lagarto.rect):
            jugador1.jugador.vida -= i.lagarto.danio
            cambiar_vida()
    for i in esqueletos:
        if jugador1.jugador.rect.colliderect(i.esqueleto.rect):
            jugador1.jugador.vida -= i.esqueleto.danio
            cambiar_vida()
    for i in calabacines:
        if jugador1.jugador.rect.colliderect(i.calabacin.rect):
            jugador1.jugador.vida -= i.calabacin.danio
            cambiar_vida()
    for i in orcos:
        if jugador1.jugador.rect.colliderect(i.orco.rect):
            jugador1.jugador.vida -= i.orco.danio
            cambiar_vida()
    for i in frankis:
        if jugador1.jugador.rect.colliderect(i.franki.rect):
            jugador1.jugador.vida -= i.franki.danio
            cambiar_vida()

#movimiento jugador
def movimiento():
    #limitacion
    rect2 = pygame.Rect(130,180,1650,740)
    keys = pygame.key.get_pressed()
    dentro_l = jugador1.jugador.rect.colliderect(rect2)
    if dentro_l == False:
        direccion = pygame.math.Vector2(850, 500) - pygame.math.Vector2(jugador1.jugador.rect.center)
        direccion.normalize()
        jugador1.jugador.rect.move_ip(direccion.x//50,direccion.y//50)
    #movimiento normal
    else:
        if keys[pygame.K_w]:
            jugador1.jugador.mover_arriba()
        if keys[pygame.K_s]:
            jugador1.jugador.mover_abajo()
        if keys[pygame.K_a]:
            jugador1.jugador.mover_izquierda()
        if keys[pygame.K_d]:
            jugador1.jugador.mover_derecha()
        #if keys[pygame.K_f]:
            #atacar()

#entrega de bolitas_vida
def dar_bolitas_vida():
    for e in bolitas_vida:
        e.poner_bol_vida()
        if jugador1.jugador.rect.colliderect(e.vida.rect):
            jugador1.jugador.puntaje += e.dar_vida()
            puntaje_contador(jugador1.jugador.puntaje)
            if jugador1.jugador.vida < 100:
                jugador1.jugador.vida += e.dar_vida()
                if jugador1.jugador.vida > 100:
                    jugador1.jugador.vida = 100
                cambiar_vida()
                vida_texto()
            bolitas_vida.remove(e)

#apuntamiento con mouse del jugador
def apuntamiento_raton():
    #posicion mouse
    raton_pos = pygame.mouse.get_pos()
    pantalla.blit(puntero,(raton_pos[0],raton_pos[1]))
    #print(raton_pos[0])#x
    #print(raton_pos[1])#y
    #apuntar con raton
    #deltas de x y
    x_v = raton_pos[0] - jugador1.jugador.rect.x
    y_v = raton_pos[1] - jugador1.jugador.rect.y
    #calculo con triangulo , direccionamiento
    if abs(x_v) <= abs(y_v) and y_v > 0:
        jugador1.jugador.direccion = 3
        #print("abajo")
    if abs(x_v) <= abs(y_v) and y_v < 0:
        jugador1.jugador.direccion = 2
        #print("arriba")
    if abs(x_v) >= abs(y_v) and x_v > 0:
        jugador1.jugador.direccion = 0
        #print("derecha")
    if abs(x_v) >= abs(y_v) and x_v < 0:
        jugador1.jugador.direccion = 1
        #print("izquierda")

#cambio de nivel, aumento de atributos
def cambiar_nivel(tiempo_s):
    #velocidad = 3
    #rango_ataque = 300
    #danio = 3
    if tiempo_s >= 30 and  tiempo_s < 60:
        jugador1.jugador.velocidad = 3.5
        jugador1.jugador.rango_ataque = 330
        jugador1.jugador.danio = 4
    elif tiempo_s >= 60 and  tiempo_s < 90:
        jugador1.jugador.nivel = 1
        jugador1.jugador.velocidad = 4
        jugador1.jugador.rango_ataque = 350
        jugador1.jugador.danio = 4.5
    elif tiempo_s >= 90 and  tiempo_s < 120:
        jugador1.jugador.nivel = 2
        jugador1.jugador.velocidad = 4.5
        jugador1.jugador.rango_ataque = 380
        jugador1.jugador.danio = 5
    elif tiempo_s >= 120 and  tiempo_s < 150:
        jugador1.jugador.nivel = 3
        jugador1.jugador.velocidad = 5
        jugador1.jugador.rango_ataque = 400
        jugador1.jugador.danio = 6
    elif tiempo_s >= 150 and  tiempo_s < 180:
        jugador1.jugador.nivel = 4
        jugador1.jugador.velocidad = 5.5
        jugador1.jugador.rango_ataque = 425
        jugador1.jugador.danio = 7
    elif tiempo_s >= 180 and  tiempo_s < 210:
        jugador1.jugador.nivel = 5
        jugador1.jugador.velocidad = 6
        jugador1.jugador.rango_ataque = 450
        jugador1.jugador.danio = 8

#DEF de ENEMIGOS

#accion enemigos(poner,perseguir,desaparecer,exp soltada)
def accion_enemigo():
    for i in minotauros:
        if i.minotauro.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.minotauro.vida <= 0:
            pos_exp_x = i.minotauro.rect.x
            pos_exp_y = i.minotauro.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,1))
            minotauros.remove(i)
    for i in lagartos:
        if i.lagarto.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.lagarto.vida <= 0:
            pos_exp_x = i.lagarto.rect.x
            pos_exp_y = i.lagarto.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,2))
            lagartos.remove(i)
    for i in esqueletos:
        if i.esqueleto.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.esqueleto.vida <= 0:
            pos_exp_x = i.esqueleto.rect.x
            pos_exp_y = i.esqueleto.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,3))
            esqueletos.remove(i)
    for i in calabacines:
        if i.calabacin.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.calabacin.vida <= 0:
            pos_exp_x = i.calabacin.rect.x
            pos_exp_y = i.calabacin.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,4))
            calabacines.remove(i)
    for i in orcos:
        if i.orco.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.orco.vida <= 0:
            pos_exp_x = i.orco.rect.x
            pos_exp_y = i.orco.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,5))
            orcos.remove(i)
    for i in frankis:
        if i.franki.vida > 0:
            i.poner_enemigo()
            i.perseguir()
        if i.franki.vida <= 0:
            pos_exp_x = i.franki.rect.x
            pos_exp_y = i.franki.rect.y
            bolitas_vida.append(bol_vida(pos_exp_x,pos_exp_y,6))
            frankis.remove(i)
    
#colocar enemigos en pantalla
def poner_enemigos(tiempo,tiempo_s):
    if tiempo_s <= 60 and tiempo_s >= 0:
        mult = 1
    if tiempo_s <=120 and tiempo_s > 60:
        mult = 1.15
    if tiempo_s <=180 and tiempo_s > 120:
        mult = 1.3
    if tiempo_s > 180:
        mult = 2
    if tiempo_s > 210:
        mult = 3
    if tiempo_s > 240:
        mult = 4
        
    if tiempo % 10 == 0 and len(minotauros) < 40:
        minotauros.append(enemigo(1,mult,mult,mult))
        #0.1 - 0.8 - 20
    if tiempo_s >= 10:
        if tiempo % 10 == 0 and tiempo != 0 and len(lagartos) < 35:
            lagartos.append(enemigo(2,mult,mult,mult))
            #0.12 - 1 - 30
    if tiempo_s >= 20:
        if tiempo % 14 == 0 and tiempo != 0 and len(esqueletos) < 30:
            esqueletos.append(enemigo(3,mult,mult,mult))
            #0.15 - 1.2 - 40
    if tiempo_s >= 30:
        if tiempo % 18 == 0 and tiempo != 0 and len(calabacines) < 25:
            calabacines.append(enemigo(4,mult,mult,mult))
                #0.2 - 1.5 - 50
    if tiempo_s >= 40:
        if tiempo % 22 == 0 and tiempo != 0 and len(orcos) < 20:
            orcos.append(enemigo(5,mult,mult,mult))
            #0.3 - 1 - 75
    if tiempo_s >= 50:
        if tiempo % 26 == 0 and tiempo != 0 and len(frankis) < 15:
            frankis.append(enemigo(6,mult,mult,mult))
            #0.5 - 0.5 - 100

#-----------------------------------------------

#OTROS

#puntero mouse, visibilidad
puntero = pygame.image.load("imagenes/cursor.png")
pygame.mouse.set_visible(False)
run = True
pausa = False
#musica
pygame.mixer.music.play(-1)
while run:
    if not pausa:
        #fondo de pantalla
        pantalla.blit(fondo,(0,0))
        #apuntamiento con mouse
        apuntamiento_raton()
        #tiempo para ataque y poner enemigos
        tiempo = pygame.time.get_ticks()/100
        #ataque tiempo y auxiliar de enemigos
        tiempo_s = pygame.time.get_ticks()/1000
        #print(int(tiempo))

        #cambio de nivel
        cambiar_nivel(tiempo_s)

        #ENEMIGO
        #poner enemigos
        poner_enemigos(int(tiempo),int(tiempo_s))
        #enemigo accion
        accion_enemigo()

        #JUGADOR
        if jugador1.jugador.vida > 0:
            jugador1.posicionar()
        else:
            cuadrado_rect = pygame.Rect(cuadrado_x, cuadrado_y, cuadrado_lado, cuadrado_lado)
            pantalla.blit(imagen, cuadrado_rect)
            pygame.mixer.music.pause()
            pausa = not pausa
            sonido = pygame.mixer.Sound("imagenes/music/Undertale OST_ 011 - Determination (320 kbps).mp3")
            sonido.play(-1)

            
        #daño al jugador
        danio_jugador()
        #cambiar nivel
        cambiar_nivel(tiempo_s)
        #vida bolitas
        dar_bolitas_vida()
        #vida
        cambiar_vida()
        #puntaje
        puntaje_contador(jugador1.jugador.puntaje)

        #print(int(tiempo_a))
        atacar(tiempo)
        #textos
        contador(tiempo_s)
        vida_texto()
        nivel_texto()

        #Movimientos con LIMITE DE PANTALLA
        movimiento()

        #salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pausa = not pausa
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()