import pygame
from Ball import Ball
from Background import Background
import constants

class Painter:

    DEFAULT_DIMENSIONS = constants.SCREEN_DIMENSIONS
    dimensions = None
    background_layer = None
    foreground_layer = None
    ball = None
    layers = []

    def __init__(self, dimensions = DEFAULT_DIMENSIONS):
        self.dimensions = dimensions
        self.create_background()
        self.create_ball()

    def generate_surfaces_with_positions(self, playtime):
        self.update()
        return self.layers

    def update(self):
        position = self.ball.get_position()
        self.layers[1] = (self.ball_layer, position)

    def generate_caption(self, playtime):
        return "Tetris"

    def create_background(self):
        background = Background()
        self.background_layer = background.get_layer()
        self.layers.append((self.background_layer, constants.ORIGIN))

    def create_ball(self):
        ball_radius = 20
        ball_position = (20,20)
        ball_velocity = (0,0)
        ball_acceleration = (0, 0)
        ball_layer_dimensions = (2*ball_radius, 2*ball_radius)
        self.ball_layer = pygame.Surface(ball_layer_dimensions)
        self.ball_layer.set_colorkey(constants.BLACK)
        ball_rect = (0, 0, 2*ball_radius, 2*ball_radius)
        # pygame.draw.circle(self.ball_layer, self.BLUE, ball_position,  ball_radius)
        rect = (0, 0, 20, 20)
        pygame.draw.rect(self.ball_layer, constants.BLUE, rect)
        self.ball = Ball(ball_radius, self.dimensions)
        self.ball.set_position(ball_position)
        self.ball.set_velocity(ball_velocity)
        self.ball.set_acceleration(ball_acceleration)
        self.layers.append((self.ball_layer, ball_position))
