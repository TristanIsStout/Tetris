import pygame
import time
from Painter import Painter


class Engine:

    DEFAULT_FPS = 30
    fps = DEFAULT_FPS
    START_TIME = 0.0
    playtime = None

    def __init__(self, screen, painter, fps = DEFAULT_FPS):
        self.screen = screen
        self.painter = painter
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.playtime = self.START_TIME

    def run(self):
        self.playing = True
        while self.playing:
            self.update()
        self.stop()

    def update(self):
        self.update_time()
        time = self.playtime
        caption = self.painter.generate_caption(time)
        surfaces_with_positions = self.painter.generate_surfaces_with_positions(time)
        self.screen.update(surfaces_with_positions, caption)
        self.update_playing()

    def update_time(self):
        miliseconds = self.clock.tick(self.fps)
        self.playtime += miliseconds / 1000.0

    def update_playing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.playing = False


    def stop(self):
        self.screen.quit()
