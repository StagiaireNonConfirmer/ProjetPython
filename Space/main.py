import pygame, sys

from sprite_sheet import sprite_get
from background import Etoile
from alien import Monstre
from player import Player, Missile

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600), 1)
clock = pygame.time.Clock()


# Liste Monstre
explosion = pygame.mixer.Sound("assets/sounds/explosion.ogg")
all_sprites = pygame.sprite.Group()
for i in range(10):
    for n in range(5):
        all_sprites.add(Monstre(i * 50, 42 * n))



# Initialisation Joueur
missiles_sprite = []
player = Player(400, 300)
ship_shoot = pygame.mixer.Sound("assets/sounds/ship_shoot.ogg")


# Initialisation Backgroud
etoiles    = Etoile(screen, 0.16)

while True:
    key = pygame.key.get_pressed()
    dt = clock.tick(144) * 0.01
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_SPACE:
                ship_shoot.set_volume(0.2)
                ship_shoot.play()
                missiles_sprite.append(Missile(player.rect.x + 20, player.rect.y))
            if evt.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    screen.fill((0, 0, 0))

    etoiles.run()

    for missile in missiles_sprite:
        hit = pygame.sprite.spritecollide(missile, all_sprites, True, pygame.sprite.collide_rect)
        if hit:
            explosion.set_volume(0.1)
            explosion.play()
            missiles_sprite.remove(missile)

    all_sprites.update()
    all_sprites.draw(screen)

    for missile in missiles_sprite:
        if missile.rect.y < 0:
            missiles_sprite.remove(missile)
        missile.rect.y -= missile.speed

    for missile in missiles_sprite:
        screen.blit(missile.image, missile.rect)

    player.update()
    screen.blit(player.image, player.rect)


    pygame.display.flip()

