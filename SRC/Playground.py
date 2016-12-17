import pygame
import constants
from Ball import Ball

class Playground:

    layer = None
    index = 0

    def __init__(self):
        self.layer = pygame.Surface(constants.PLAYGROUND_DIMENSIONS)
        self.layer.set_colorkey(constants.BLACK)
        self.create_ball()

    def get_layer(self):
        return self.layer

    def get_position(self):
        return self.index

    def set_position(self, position):
        self.index = position

    def update(self):
        self.layer.fill(constants.BLACK)
        self.ball_position = self.ball.get_position()
        self.layer.blit(self.ball_layer, self.ball_position)

    def create_ball(self):
        ball_radius = constants.BLOCK_SIZE / 2
        ball_position = (20,20)
        ball_velocity = (0,0)
        ball_acceleration = (0, 0)
        ball_layer_dimensions = (2*ball_radius, 2*ball_radius)
        self.ball_layer = pygame.Surface(ball_layer_dimensions)
        self.ball_layer.set_colorkey(constants.BLACK)
        ball_rect = (0, 0, 2*ball_radius, 2*ball_radius)
        pygame.draw.rect(self.ball_layer, constants.BLUE, ball_rect)
        self.ball = Ball(ball_radius, constants.PLAYGROUND_DIMENSIONS)
        self.ball.set_position(ball_position)
        self.ball.set_velocity(ball_velocity)
        self.ball.set_acceleration(ball_acceleration)
