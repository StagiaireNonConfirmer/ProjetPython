import math
import random
import pygame


class Snake(object):
    def __init__(self, screen):
        self.screen = screen
        self.x = 5
        self.y = 5
        self.tail = []
        self.total = 0
        self.dir = 1
        self.move = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        self.sound_score = pygame.mixer.Sound('assets/sounds/score.wav')

    def pickLocation(self):
        cols = random.randrange(2, 18)
        rows = random.randrange(2, 18)
        if [cols, rows] in self.tail:
            return self.pickLocation()
        return [cols, rows]

    def showSnake(self):
        if self.total > 0:
            for i in range(len(self.tail)):
                pygame.draw.rect(self.screen, [180, 255, 255],
                                 pygame.Rect(self.tail[i][0] * 22 + 16, self.tail[i][1] * 22 + 16, 21, 21))

        pygame.draw.rect(self.screen, [255, 0, 0],
                         pygame.Rect(self.x * 22 + 16, self.y * 22 + 16, 21, 21))

    def update(self):
        if self.total > 0:
            for i in range(len(self.tail) - 1):
                self.tail[i] = self.tail[i + 1]
            self.tail[self.total - 1] = [self.x, self.y]

        self.x += self.move[self.dir % 4][0]
        self.y += self.move[self.dir % 4][1]
        if self.x < 0 :  self.x = 18
        if self.x >= 19: self.x  = 0
        if self.y < 2 : self.y  = 18
        if self.y >= 19: self.y  = 2

    def eat(self, pos):
        d = self.dist(self.x, self.y, pos[0], pos[1])
        if d < 1:
            self.sound_score.play()
            self.sound_score.set_volume(0.1)
            self.total += 1
            self.tail.insert(0, [])
            return True
        return False

    def gameOver(self):
        for i in range(1, len(self.tail)):
            d = self.dist(self.x, self.y, self.tail[i][0], self.tail[i][1])
            if d < 1:
                return (False, self.highscore())
        return True, None

    @staticmethod
    def dist(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
