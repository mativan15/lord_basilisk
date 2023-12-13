import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_, rango_, danio_):
        super().__init__()
        self.nivel = 0
        self.puntaje = 0
        self.danio = danio_
        self.rango_ataque = rango_
        self.velocidad = velocidad_
        self.img_base_n0 = pygame.image.load("imagenes/jugador/nivel0/ab/ab1.png")
        self.img_base_n1 = pygame.image.load("imagenes/jugador/nivel1/ab/ab1.png")
        self.img_base_n2 = pygame.image.load("imagenes/jugador/nivel2/ab/ab1.png")
        self.n0_img_alt = self.img_base_n0.get_height()
        self.n0_img_anc = self.img_base_n0.get_width()
        self.n1_img_alt = self.img_base_n1.get_height()
        self.n1_img_anc = self.img_base_n1.get_width()
        self.n2_img_alt = self.img_base_n2.get_height()
        self.n2_img_anc = self.img_base_n2.get_width()

        self.sprites = []
        self.sprites_derecha1 = []
        self.sprites_izquierda1 =[]
        self.sprites_arriba1 = []
        self.sprites_abajo1 = []

        self.sprites1=[pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab1.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)),self.sprites_izquierda1,self.sprites_derecha1,self.sprites_arriba1,self.sprites_abajo1]

        self.sprites_derecha2 = []
        self.sprites_izquierda2 =[]
        self.sprites_arriba2 = []
        self.sprites_abajo2 = []
        self.sprites2=[pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab1.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)),self.sprites_izquierda2,self.sprites_derecha2,self.sprites_arriba2,self.sprites_abajo2]

        self.sprites_derecha3 = []
        self.sprites_izquierda3 =[]
        self.sprites_arriba3 = []
        self.sprites_abajo3 = []
        self.sprites3=[pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab1.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)),self.sprites_izquierda3,self.sprites_derecha3,self.sprites_arriba3,self.sprites_abajo3]
        
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz1.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz2.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz3.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz4.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz5.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz6.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz7.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz8.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_izquierda1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/iz/iz9.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de1.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de2.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de3.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de4.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de5.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de6.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de7.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de8.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_derecha1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/de/de9.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))

        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar1.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar2.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar3.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar4.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar5.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar6.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar7.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar8.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_arriba1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ar/ar9.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))

        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab1.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab2.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab3.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab4.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab5.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab6.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab7.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab8.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
        self.sprites_abajo1.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel0/ab/ab9.png"), (self.n0_img_anc*2.2, self.n0_img_alt*2)))
    

        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz1.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz2.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz3.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz4.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz5.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz6.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz7.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz8.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_izquierda2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/iz/iz9.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de1.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de2.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de3.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de4.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de5.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de6.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de7.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de8.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_derecha2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/de/de9.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))

        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar1.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar2.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar3.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar4.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar5.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar6.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar7.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar8.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_arriba2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ar/ar9.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))

        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab1.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab2.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab3.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab4.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab5.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab6.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab7.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab8.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
        self.sprites_abajo2.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel1/ab/ab9.png"), (self.n1_img_anc*2.2, self.n1_img_alt*2)))
    
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz1.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz2.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz3.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz4.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz5.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz6.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz7.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz8.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_izquierda3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/iz/iz9.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de1.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de2.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de3.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de4.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de5.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de6.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de7.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de8.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_derecha3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/de/de9.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))

        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar1.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar2.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar3.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar4.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar5.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar6.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar7.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar8.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_arriba3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ar/ar9.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))

        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab1.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab2.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab3.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab4.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab5.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab6.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab7.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab8.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
        self.sprites_abajo3.append(pygame.transform.scale(pygame.image.load("imagenes/jugador/nivel2/ab/ab9.png"), (self.n2_img_anc*2.2, self.n2_img_alt*2)))
    
        self.sprite_ataque_de = []
        self.sprite_ataque_iz = []
        self.sprite_ataque_ar = []
        self.sprite_ataque_ab = []

        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/1.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/2.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/3.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/4.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/5.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/6.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/7.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/8.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_de.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/de/9.png"), (self.rango_ataque, self.rango_ataque)))

        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/1.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/2.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/3.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/4.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/5.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/6.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/7.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/8.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_iz.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/iz/9.png"), (self.rango_ataque, self.rango_ataque)))
        
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/1.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/2.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/3.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/4.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/5.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/6.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/7.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/8.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ar.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ar/9.png"), (self.rango_ataque, self.rango_ataque)))

        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/1.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/2.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/3.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/4.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/5.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/6.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/7.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/8.png"), (self.rango_ataque, self.rango_ataque)))
        self.sprite_ataque_ab.append(pygame.transform.scale(pygame.image.load("imagenes/ataque/ab/9.png"), (self.rango_ataque, self.rango_ataque)))

        self.sprite_actual = 0
        self.image = self.sprites1[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.jugador_pos = pygame.Vector2(self.rect.x,self.rect.y)
        self.direccion = 3
        self.vida = 100
        self.sprite_actual_ataque = 0
        self.image_ataque = self.sprite_ataque_de[self.sprite_actual_ataque]
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        
        if self.nivel == 0:
            self.sprites_derecha = self.sprites_derecha1
        elif self.nivel == 1:
            self.sprites_derecha = self.sprites_derecha2
        else: 
            self.sprites_derecha = self.sprites_derecha3
        
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        
        if self.nivel == 0:
            self.sprites_izquierda = self.sprites_izquierda1
        elif self.nivel == 1:
            self.sprites_izquierda = self.sprites_izquierda2
        else: 
            self.sprites_izquierda = self.sprites_izquierda3
        
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        
        if self.nivel == 0:
            self.sprites_arriba = self.sprites_arriba1
        elif self.nivel == 1:
            self.sprites_arriba = self.sprites_arriba2
        else: 
            self.sprites_arriba = self.sprites_arriba3
        
        self.image = self.sprites_arriba[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        
        if self.nivel == 0:
            self.sprites_abajo = self.sprites_abajo1
        elif self.nivel == 1:
            self.sprites_abajo = self.sprites_abajo2
        else: 
            self.sprites_abajo = self.sprites_abajo3
        
        self.image = self.sprites_abajo[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def ataque(self):
        self.sprite_actual_ataque += 0.4
        if self.sprite_actual_ataque >= 9:
                self.sprite_actual_ataque = 0
    
        resta_y1 = int(self.rango_ataque * 0.3)
        resta_x1 = int(self.rango_ataque * 0.4)
        resta_xy = int(self.rango_ataque * 0.7)

        if self.direccion == 0:
            self.image_ataque = self.sprite_ataque_de[int(self.sprite_actual_ataque)]
            self.ataque1 = pygame.Rect(self.rect.x ,self.rect.y - resta_y1,self.rango_ataque,self.rango_ataque)
        if self.direccion == 1:
            self.image_ataque = self.sprite_ataque_iz[int(self.sprite_actual_ataque)]
            self.ataque1 = pygame.Rect(self.rect.x - resta_xy,self.rect.y - resta_y1,self.rango_ataque,self.rango_ataque)
        if self.direccion == 2:
            self.image_ataque = self.sprite_ataque_ar[int(self.sprite_actual_ataque)]
            self.ataque1 = pygame.Rect(self.rect.x - resta_x1,self.rect.y - resta_xy,self.rango_ataque,self.rango_ataque)
        if self.direccion == 3:
            self.image_ataque = self.sprite_ataque_ab[int(self.sprite_actual_ataque)]
            self.ataque1 = pygame.Rect(self.rect.x - resta_x1,self.rect.y + 10,self.rango_ataque,self.rango_ataque)

        return self.ataque1
    #def morir(self):
    #    self.sprite_actual = 0
    #    if self.sprite_actual >= 2:
            #print(self.sprite_actual)
    #       self.sprite_actual += 0.04
    #       self.image = self.sprites_muerte[int(self.sprite_actual)]