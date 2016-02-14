import pygame, sys, math

from entities.player import player


class game:
    def __init__(self, width, height, title):
        pygame.init()

        self.width = width
        self.height = height
        self.title = title

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()

        self.player = player(300, 300, 10, 10, 200, 200)

    def run(self):
        fps = 0
        elapsed = 0
        totElapsed = 0

        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_SPACE:
                        self.player.set_new_turn()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.player.set_destination(pygame.mouse.get_pos())

            elapsed = self.clock.tick(120)
            totElapsed += elapsed
            if totElapsed > 1000:
                pygame.display.set_caption(self.title + ' ~ ' + str(fps) + ' Fps')
                totElapsed = 0
                fps = 0
            else:
                fps += 1

            self.update(elapsed / 1000)
            self.draw()


    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self, elapsed):
        self.player.update(elapsed)

    def draw(self):
        self.screen.fill(0x000000)
        self.player.draw(self.screen)

        pygame.display.flip()