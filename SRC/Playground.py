import pygame
import random
import constants
from Ball import Ball
from Grid import Grid

class Playground:

    layer = None
    index = 0

    def __init__(self):
        self.layer = pygame.Surface(constants.PLAYGROUND_DIMENSIONS)
        self.layer.set_colorkey(constants.BLACK)
        self.create_ball()
        self.create_grid()

    def get_layer(self):
        return self.layer

    def get_position(self):
        return self.index

    def set_position(self, position):
        self.index = position

    def update(self):
        self.layer.fill(constants.BLACK)
        self.update_grid()
        self.ball_position = self.ball.get_position()
        self.layer.blit(self.ball_layer, self.ball_position)

    def create_grid(self):
        self.grid = Grid(constants.GRID_DIMENSIONS)

    def update_grid(self):
        self.grid.update()
        self.draw_cells()

    def draw_cells(self):
        graph = self.grid.get_graph()
        for row in range(0,self.grid.rows):
            for column in range(0,self.grid.columns):
                if graph[row][column]:
                    self.draw_cell((row, column))

    def draw_cell(self, position):
        x, y = position
        x = x * constants.BLOCK_SIZE + 1
        y = y * constants.BLOCK_SIZE + 1
        cell_rect = (x, y, constants.BLOCK_SIZE -1 , constants.BLOCK_SIZE-1)
        pygame.draw.rect(self.layer, constants.GREEN, cell_rect)


    def create_ball(self):
        ball_radius = constants.BLOCK_SIZE / 2
        ball_layer_dimensions = (2*ball_radius, 2*ball_radius)
        self.ball_layer = pygame.Surface(ball_layer_dimensions)
        self.ball_layer.set_colorkey(constants.BLACK)
        ball_rect = (0, 0, 2*ball_radius, 2*ball_radius)
        pygame.draw.rect(self.ball_layer, constants.BLUE, ball_rect)
        self.ball = Ball(ball_radius, constants.PLAYGROUND_DIMENSIONS)
