import pygame
from pygame.locals import *

class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font_menu      = pygame.font.SysFont("comicsanssms", 42)
        self.font_titre     = pygame.font.SysFont("comicsanssms", 110)
        self.font_highscore = pygame.font.SysFont("comicsanssms", 90)
        self.text   = ["New Game", "High Score", "Quit"]
        self.titre = "SNAKE"
        self.pos    = 0

    def afficher_menu_principal(self):
        self.screen.blit(self.font_titre.render(self.titre, True, (0, 128, 0)), (90, 50))

        for e, index in enumerate(self.text):
            self.screen.blit(self.font_menu.render(index, True, (0, 128, 0)), (150, 50 * e + 200))
        pygame.draw.circle(self.screen, (0, 128, 0), (130, 210 + 50 * self.pos), 10)

    def afficher_menu_highscore(self, tab_score):
        self.screen.blit(self.font_highscore.render("HIGH SCORE", True, (0, 128, 0)), (30, 50))
        for i in range(3):
            self.screen.blit(self.font_menu.render(f'SCORE {i + 1} {tab_score[i]}',
                                                   True, (0, 128, 0)), (100, 50 * i + 150))

        self.screen.blit(self.font_menu.render("[espace] pour continuer", True,
                                               (0, 128, 0)),(50, 300))


