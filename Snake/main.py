import sys, pygame
from pygame.locals import *
from snake import Snake


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.snake  = Snake(self.screen)
        self.hit    = self.snake.pickLocation()
        self.clock  = pygame.time.Clock()

        # we load the image of the food and the background with the function pygame.image.load().

        self.background = pygame.image.load('assets/images/background.jpg')
        self.nourriture = pygame.image.load('assets/images/nourriture.png')

        # And we put in a dictionary, the controls that will be used to move the snake.
        self.controle = {
            'DROITE' : K_RIGHT,
            'GAUCHE'   : K_LEFT,
        }


    def process_event(self, event: pygame.event):

        # Quit program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Action snake
        if event.type == KEYDOWN:
            if event.key == self.controle['DROITE']:
                self.snake.dir += 1
                if self.snake.dir > 3:
                    self.snake.dir = 0
            if event.key == self.controle['GAUCHE']:
                self.snake.dir -= 1
                if self.snake.dir < 0:
                    self.snake.dir = 3
                
    def run(self):
        if self.snake.eat(self.hit):
            self.hit = self.snake.pickLocation()

        self.start = self.snake.gameOver()
        self.snake.update()
        self.snake.showSnake()
        self.screen.blit(self.nourriture, pygame.Rect(self.hit[0] * 22 + 16, self.hit[1] * 22 + 15, 21, 21))

    def main(self):
        while True:
            for event in pygame.event.get():
                self.process_event(event)

            self.screen.blit(self.background, (0, 0))

            self.run()

            pygame.display.update()
            self.clock.tick(10)



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("SNAKE")
    screen = pygame.display.set_mode((450, 450), 1)
    Game(screen).main()
