import pygame, random
import os

from sprite_sheet import *

class Monstre(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = sprite_get('monstre/alien_blue_sheet.png', 40, 0, 0)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 1
        self.current_image = 0
    
    def update(self):
        if self.rect.x + 50 > 800 or self.rect.x < 0:
            self.speed = - self.speed
            self.rect.y += 10
        self.rect.x += self.speed