import pygame
import constants
from Peice import Peice

class Grid:

    dimensions = None
    graph = []
    rows = 0
    columns = 0

    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.rows, self.columns = dimensions
        self.graph = [[False for row in range(0, self.rows)] for column in range(0, self.columns)]
        self.create_peice()

    def create_peice(self):
        self.peice = Peice()
        self.peice.place(self.graph)

    def get_graph(self):
        return self.graph

    def update(self):
        self.peice.update(self.graph)

    def set_occupied(self, position):
        x, y = position
        self.graph[x][y] = True

    def set_empty(self, position):
        x, y = position
        self.graph[x][y] = False


