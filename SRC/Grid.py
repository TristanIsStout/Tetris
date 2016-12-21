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
        self.peice = Peice()
        self.peice.alive = True
        self.next_peice = Peice()
        self.next_peice.alive = False

    def get_graph(self):
        return self.graph

    def update(self, time):
        constants.next_peice = self.next_peice
        Peice.time = time
        self.handle_horizontal_lines()
        self.handle_vertical_lines(time)
        if self.peice.alive:
            self.graph = self.peice.update(self.graph)
        else:
            self.peice = self.next_peice
            self.peice.alive = True
            self.next_peice = Peice()
            self.next_peice.alive = False

    def handle_horizontal_lines(self):
        for row in range(self.rows):
            if self.is_horizontal_line(row) and not self.peice.alive:
                self.clear_row(row)
                constants.lines += 1
                print(constants.lines)

    def clear_row(self, row):
        self.remove(row)
        self.shift_down(row)

    def remove(self, row):
        for column in range (0, self.columns):
            self.graph[column][row] = False

    def shift_down(self, row):
        for r in range(0, row):
            curr_row = row - r
            next_row = curr_row - 1
            for column in range(0, self.columns):
                if curr_row != 0:
                    self.graph[column][curr_row] = self.graph[column][next_row]
                else:
                    self.graph[column][r] = False

    def handle_vertical_lines(self, time):
        if self.has_vertical_lines():
            self.clear()
            Peice.time_offset = time
            self.peice.alive = False

    def has_vertical_lines(self):
        has_vertical_line = False
        for column in range(0, self.columns):
            has_vertical_line = has_vertical_line or self.graph[column][0]
        if self.peice.alive:
            has_vertical_line = False
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


