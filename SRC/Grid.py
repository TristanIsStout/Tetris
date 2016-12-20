import pygame
import constants
from Peice import Peice
from Peice import Cell

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
        p1 = (10,0)
        p2 = (10,1)
        p3 = (10,2)
        p4 = (10,3)
        self.ps = [p1, p2, p3, p4]
        self.peice = Peice(self.ps)

    def get_graph(self):
        return self.graph

    def update(self):
        self.handle_horizontal_lines()
        self.handle_vertical_lines()
        if self.peice.alive:
            self.graph = self.peice.update(self.graph)
        else:
            self.peice = Peice(self.ps)

    def handle_horizontal_lines(self):
        for row in range(self.rows):
            if self.is_horizontal_line(row) and not self.peice.alive:
                self.clear_row(row)

    def clear_row(self, row):
        self.remove(row)
        self.shift_down(row)

    def remove(self, row):
        for column in range (0, self.columns):
            self.graph[column][row] = False

    def shift_down(self, row):
        return 0

    def handle_vertical_lines(self):
        if self.has_vertical_lines():
            self.clear()
            self.peice.alive = False

    def has_vertical_lines(self):
        has_vertical_line = False
        is_vertical_line = True
        for column in range(0, self.columns):
            is_vertical_line = True
            for row in range(0, self.rows):
                is_vertical_line = is_vertical_line and self.graph[column][row]
            has_vertical_line = has_vertical_line or is_vertical_line
        return has_vertical_line

    def is_horizontal_line(self, row):
        is_horizontal_line = True
        for column in range(0, self.columns):
            is_horizontal_line = is_horizontal_line and self.graph[column][row]
        return is_horizontal_line


    def clear(self):
        for row in range(0,self.rows):
            for column in range(0,self.columns):
                self.graph[row][column] = False

    def set_occupied(self, position):
        x, y = position
        self.graph[x][y] = True

    def set_empty(self, position):
        x, y = position
        self.graph[x][y] = False


