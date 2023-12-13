import pygame

class Bolita_vida:
    def __init__(self,x,y,tipo_):
        self.tipo = tipo_
        if self.tipo == 1:
            self.image = pygame.image.load("imagenes/experiencia/1.png")
        if self.tipo == 2:
            self.image = pygame.image.load("imagenes/experiencia/2.png")
        if self.tipo == 3:
            self.image = pygame.image.load("imagenes/experiencia/3.png")
        if self.tipo == 4:
            self.image = pygame.image.load("imagenes/experiencia/4.png")
        if self.tipo == 5:
            self.image = pygame.image.load("imagenes/experiencia/5.png")
        if self.tipo == 6:
            self.image = pygame.image.load("imagenes/experiencia/6.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
    def monto_curacion(self):
        if self.tipo == 1:
            return 0.5
        if self.tipo == 2:
            return 1
        if self.tipo == 3:
            return 1.5
        if self.tipo == 4:
            return 2
        if self.tipo == 5:
            return 3
        if self.tipo == 6:
            return 5
        