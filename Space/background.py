import random

import pygame


class EtoilePhysique:
    def __init__(self, x, y) -> None:
        self.x              = x
        self.y              = y
        self.yspeed         = random.randint(5, 20)



class Etoile(EtoilePhysique):
    def __init__(self, win, dt) -> None:
        self.win            = win
        self.dt             = dt
        self.listeEtoile    = self.loadFond()

    def update(self):
        for etoile in self.listeEtoile:
            etoile.y += etoile.yspeed * self.dt
            if etoile.y > self.win.get_height():
                etoile.y = 0
                etoile.x = random.randint(0, self.win.get_width())
    
    def loadFond(self):
        ls = []
        for i in range(10):
            x = random.randint(0, self.win.get_width())
            y = random.randrange(0, self.win.get_width())
            ls.append(EtoilePhysique(x, y))
        return ls

    def drawEtoile(self):
        for etoile in self.listeEtoile:
            pygame.draw.circle(self.win, (255, 255, 255), (etoile.x, etoile.y), 1)
            
    def run(self):
        self.update()
        self.drawEtoile()
