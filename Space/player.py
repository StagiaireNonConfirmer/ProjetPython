import pygame
from pygame.locals import *


class Missile():
    def __init__(self, x, y):
        self.image = pygame.image.load('images/player/bomb.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/player/ship.png')
        self.rect  = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_UP]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN]:
            self.rect.y += self.speed
