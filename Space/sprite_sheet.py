
import pygame
import math
import random


def sprite_get(filename, size, x, y):
    sheet = pygame.image.load(f"images/{filename}")
    image = pygame.Surface((size, size))
    image.set_colorkey([0, 0, 0])
    image.blit(sheet, (0, 0), (x * size, y * size, size, size))
    return image

def sprite_animation(sprite, dt):
    sprite.current_image += dt*0.1
    if sprite.current_image > len(sprite.ls_sprite):
        sprite.current_image = 0
    return sprite.ls_sprite[math.floor(sprite.current_image)]


def text_object(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def draw_text(surface, text, size):
    font = pygame.font.SysFont(None, size)
    textSurface, textRect = text_object(text, font)
    textRect.center = ((surface.get_width() / 2, surface.get_height() / 2))
    surface.blit(textSurface, textRect)