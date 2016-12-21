import pygame
import random
import constants
from Grid import Grid

class Playground:

    layer = None
    index = 0

    def __init__(self):
        self.layer = pygame.Surface(constants.PLAYGROUND_DIMENSIONS)
        self.layer.set_colorkey(constants.BLACK)
        self.create_grid()

    def get_layer(self):
        return self.layer

    def get_position(self):
        return self.index

    def set_position(self, position):
        self.index = position

    def update(self, time):
        self.layer.fill(constants.BLACK)
        self.update_grid(time)

    def create_grid(self):
        self.grid = Grid(constants.GRID_DIMENSIONS)

    def update_grid(self, time):
        self.grid.update(time)
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
