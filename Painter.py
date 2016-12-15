import pygame

class Painter:

    DEFAULT_DIMENSIONS = (640, 480)
    dimensions = None
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    ORIGIN = (0,0)
    background_color = BLACK
    background_layer = None
    foreground_layer = None

    def __init__(self, dimensions = DEFAULT_DIMENSIONS):
        self.dimensions = dimensions

    def generate_surfaces_with_positions(self, playtime):
        self.create_background()
        self.create_foreground()
        return [self.background_layer, self.foreground_layer]

    def generate_caption(self, playtime):
        return "Tetris"

    def create_background(self):
        background = pygame.Surface(self.dimensions)
        background.fill(self.background_color)
        background = background.convert()
        self.background_layer = (background, self.ORIGIN)
    
    def create_foreground(self):
        width, height = self.dimensions
        foreground_width = int(0.9 * width)
        foreground_height = int(0.9 * height)
        foreground_dimensions = (foreground_width, foreground_height)
        x_position = (width - foreground_width)/2
        y_position = 0
        position = (x_position, y_position)
        foreground = pygame.Surface(foreground_dimensions)
        foreground.fill(self.WHITE)
        rect_width = foreground_width - 100
        rect_height = foreground_height - 100
        rect = (50, 50, rect_width, rect_height)
        pygame.draw.ellipse(foreground, (0,150,0),rect) 
        foreground.convert()
        self.foreground_layer = (foreground, position)
