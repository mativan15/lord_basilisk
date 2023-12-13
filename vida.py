import pygame

class Barra_vida(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("imagenes/barra_vida/00.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/01.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/02.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/03.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/04.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/05.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/06.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/07.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/08.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/09.png"))
        self.sprites.append(pygame.image.load("imagenes/barra_vida/10.png"))
        self.sprite_actual = 10
        self.image = self.sprites[self.sprite_actual]
        self.rect = self.image.get_rect()
    def poner_vida(self, valor_):
        self.sprite_actual = valor_
        self.image = self.sprites[self.sprite_actual]