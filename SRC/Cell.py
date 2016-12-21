import pygame
import copy
import random
import constants


class Cell:

    position = None

    def __init__(self, position):
        self.position = position
        x,y = self.position

    def get_adjacent_cell(self, direction):
        adjacent_cell = None
        x, y = self.position
        if direction == constants.UP:
            y -= 1
        if direction == constants.DOWN:
            y += 1
        if direction == constants.LEFT:
            x -= 1
        if direction == constants.RIGHT:
            x += 1
        adjacent_cell = Cell((x,y))
        return adjacent_cell

    def can_fit_in_grid(self, grid):
        fits = False
        if not self.is_out_of_bounds(grid):
            x,y = self.position
            fits = not grid[x][y]
        return fits

    def is_out_of_bounds(self, grid):
        out_of_bounds = True
        x,y = self.position
        x_max = len(grid) - 1
        y_max = len(grid[0]) - 1
        if x >= 0 and x <= x_max and y >= 0 and y <= y_max:
            out_of_bounds = False
        return out_of_bounds

    def place(self, grid):
        x,y = self.position
        grid[x][y] = True

    def remove(self, grid):
        x,y = self.position
        grid[x][y] = False

    def rotate_about(self, center):
        rotated_cell = None
        c_x, c_y = center
        x, y = self.position
        dx = c_x - x
        dy = c_y - y
        rotated_x = c_x - dy
        rotated_y = c_y + dx
        rotated_position = (rotated_x, rotated_y)
        rotated_cell = Cell(rotated_position)
        return rotated_cell
