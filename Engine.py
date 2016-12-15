import pygame
import time


class Engine:
    
    DEFAULT_SIZE = (640, 480)
    DEFAULT_FPS = 30
    background_color = (255, 255, 255)

    def __init__(self, size = DEFAULT_SIZE, fps = DEFAULT_FPS):
        self.size = size
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.playtime = 0.0

    def set_up(self):
        pygame.init()
        self.set_up_screen()
        self.set_up_background()

    def set_up_screen(self):
        self.screen = pygame.display.set_mode(self.size)

    def set_up_background(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(self.background_color)
        self.background = self.background.convert()
        origin = (0, 0)
        self.screen.blit(self.background, origin)

    def run(self):
        self.set_up()
        self.playing = True
        while self.playing:
            self.update()
        self.stop()

    def update(self):
        self.update_time()
        self.update_caption()
        self.update_display()
        self.update_playing()

    def update_time(self):
        miliseconds = self.clock.tick(self.fps)
        self.playtime += miliseconds / 1000.0

    def update_caption(self):
        self.caption = "FPS: {0:.2f} Playtime: {1: .2f}".format(self.clock.get_fps(), self.playtime)
        pygame.display.set_caption(self.caption)

    def update_display(self):
        pygame.display.flip()

    def update_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
                self.playing = False


    def stop(self):
        print("This game was played for {0:.2f} seconds".format(self.playtime))
        pygame.display.quit()

g = Engine()
g.run()
