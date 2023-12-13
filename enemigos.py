import pygame

class Minotauro(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()
        self.danio = 0.1 * danio_mult_
        self.velocidad = 0.8 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 48
        self.pj_altura = 104

        self.sprites.append(pygame.image.load("imagenes/minotauro/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/minotauro/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        #self.img_muerte1=pygame.image.load("imagenes/minotauro/mu1.png")
        #self.img_muerte2=pygame.image.load("imagenes/minotauro/mu2.png")
        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 20 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    '''def morir(self):
        self.sprite_actual += 0.01
        sprite_conversion = int(self.sprite_actual)
        if sprite_conversion >= 2:
            self.animacion_m = False
            return
        self.image = self.sprites_muerte[sprite_conversion]'''
    
class Lagarto(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()    
        self.danio = 0.12 * danio_mult_
        self.velocidad = 1 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 62
        self.pj_altura = 84
        self.sprites.append(pygame.image.load("imagenes/lagarto/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/lagarto/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 30 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    
class Esqueleto(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()
        self.danio = 0.15 * danio_mult_
        self.velocidad = 1.2 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 48
        self.pj_altura = 92
        self.sprites.append(pygame.image.load("imagenes/esqueleto/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/esqueleto/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 40 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad

class Calabacin(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()
        self.danio = 0.2 * danio_mult_
        self.velocidad = 1.5 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 54
        self.pj_altura = 94
        self.sprites.append(pygame.image.load("imagenes/calabacin/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/calabacin/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 50 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    
class Orco(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()

        self.danio = 0.3 * danio_mult_
        self.velocidad = 1 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 58
        self.pj_altura = 90
        self.sprites.append(pygame.image.load("imagenes/orco/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/orco/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/orco/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 75 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    
class Franki(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, velocidad_mult_, vida_mult_, danio_mult_):
        super().__init__()
        self.danio = 0.5 * danio_mult_
        self.velocidad = 0.5 * velocidad_mult_
        self.sprites = []
        self.sprites_derecha = []
        self.sprites_izquierda =[]
        self.pj_ancho = 58
        self.pj_altura = 90
        self.sprites.append(pygame.image.load("imagenes/franki/de/de1.png"))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_derecha.append(pygame.transform.scale(pygame.image.load("imagenes/franki/de/de9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz1.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz2.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz3.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz4.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz5.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz6.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz7.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz8.png"), (self.pj_ancho, self.pj_altura)))
        self.sprites_izquierda.append(pygame.transform.scale(pygame.image.load("imagenes/franki/iz/iz9.png"), (self.pj_ancho, self.pj_altura)))

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        self.vida = 100 * vida_mult_
    def mover_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.x += self.velocidad
    def mover_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.x -= self.velocidad
    def mover_arriba_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_arriba_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y -= self.velocidad
    def mover_abajo_izquierda(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_izquierda[int(self.sprite_actual)]
        self.rect.y += self.velocidad
    def mover_abajo_derecha(self):
        self.sprite_actual += 0.2
        if self.sprite_actual >= 9:
            self.sprite_actual = 0
        self.image = self.sprites_derecha[int(self.sprite_actual)]
        self.rect.y += self.velocidad