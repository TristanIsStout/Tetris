import pygame
import time

class Screen:
    
    DEFAULT_DIMENSIONS = (640, 480)
    screen = None
    dimensions = DEFAULT_DIMENSIONS

    def __init__(self, dimensions = DEFAULT_DIMENSIONS):
        pygame.init()
        self.dimensions = dimensions
        self.create_screen()

    def create_screen(self):
        self.screen = pygame.display.set_mode(self.dimensions)

    def update(self, surfaces_with_positions, caption = None):
        if not caption == None:
            pygame.display.set_caption(caption)
        self.draw(surfaces_with_positions)
        pygame.display.flip()

    def draw(self, surfaces_with_positions):
        for surface_with_position in surfaces_with_positions:
            surface, position = surface_with_position
            self.screen.blit(surface, position)

    def quit(self):
        pygame.display.quit()
