import pygame
import constants

class Grid:

    dimensions = None
    graph = []
    rows = 0
    columns = 0

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.rows, self.columns = dimensions
        self.graph = [[False for row in range(0, self.rows)] for column in range(0, self.columns)]

    def get_graph(self):
        return self.graph

    def update(self):
        return 0

    def set_occupied(self, position):
        x, y = position
        self.graph[x][y] = True

    def set_empty(self, position):
        x, y = position
        self.graph[x][y] = False


