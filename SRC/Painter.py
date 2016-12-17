import pygame
from Ball import Ball

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
    ball = None
    layers = [None for x in range(0, 3)]

    def __init__(self, dimensions = DEFAULT_DIMENSIONS):
        self.dimensions = dimensions
        self.create_background()
        self.create_foreground()
        self.create_ball()

    def generate_surfaces_with_positions(self, playtime):
        self.update()
        return self.layers

    def update(self):
        position = self.ball.get_position()
        self.layers[2] = (self.ball_layer, position)

    def generate_caption(self, playtime):
        return "Tetris"

    def create_background(self):
        background = pygame.Surface(self.dimensions)
        background.fill(self.background_color)
        background = background.convert()
        background_layer = background
        self.layers[0] = (background, self.ORIGIN)
    
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
        self.foreground_layer = foreground
        self.layers[1] = (foreground, position)

    def create_ball(self):
        ball_radius = 20
        ball_position = (20,20)
        ball_velocity = (0,0)
        ball_acceleration = (0, 0)
        ball_layer_dimensions = (2*ball_radius, 2*ball_radius)
        self.ball_layer = pygame.Surface(ball_layer_dimensions)
        self.ball_layer.set_colorkey(self.BLACK)
        ball_rect = (0, 0, 2*ball_radius, 2*ball_radius)
        pygame.draw.circle(self.ball_layer, self.BLUE, ball_position,  ball_radius)
        self.ball = Ball(ball_radius, self.dimensions)
        self.ball.set_position(ball_position)
        self.ball.set_velocity(ball_velocity)
        self.ball.set_acceleration(ball_acceleration)
        self.layers[2] = (self.ball_layer, ball_position)

