import pygame
from Ball import Ball
import constants

class Painter:

    DEFAULT_DIMENSIONS = constants.SCREEN_DIMENSIONS
    dimensions = None
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
        self.background_layer = pygame.Surface(self.dimensions)
        self.background_layer.fill(constants.BACKGROUND_COLOR)
        self.background_layer = self.background_layer.convert()
        self.draw_black_rect(constants.PLAYGROUND_RECT)
        self.draw_playground_grid()
        self.draw_black_rect(constants.MENU_RECT)
        self.layers[0] = (self.background_layer, constants.ORIGIN)
    
    def draw_black_rect(self, rect):
        pygame.draw.rect(self.background_layer, constants.BLACK, rect)

    def draw_playground_grid(self):
        horizontal_lines = constants.SCREEN_HEIGHT / constants.BLOCK_SIZE + 1
        for line_number in range(1, horizontal_lines):
            start_x = 0
            start_y = line_number * constants.BLOCK_SIZE
            start_pos = (start_x, start_y)
            end_x = constants.SCREEN_WIDTH
            end_y = start_y
            end_pos = (end_x, end_y)
            pygame.draw.line(self.background_layer, constants.LIGHT_GREY, start_pos, end_pos)
        vertical_lines = constants.SCREEN_WIDTH / constants.BLOCK_SIZE + 1
        for line_number in range(1, vertical_lines):
            start_x = line_number * constants.BLOCK_SIZE
            start_y = 0
            start_pos = (start_x, start_y)
            end_x = start_x
            end_y = constants.SCREEN_WIDTH
            end_pos = (end_x, end_y)
            pygame.draw.line(self.background_layer, constants.LIGHT_GREY, start_pos, end_pos)

    def create_foreground(self):
        width, height = self.dimensions
        foreground = pygame.Surface(self.dimensions)
        foreground.set_colorkey(constants.BLACK)
        position = (0,0)
        self.foreground_layer = foreground
        self.layers[1] = (foreground, position)

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
        self.layers[2] = (self.ball_layer, ball_position)

