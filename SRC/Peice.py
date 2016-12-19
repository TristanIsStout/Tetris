import pygame
import copy
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


            

class Peice:

    cells = None
    next_cells = None
    grid = None
    rows = 0
    columns = 0
    alive = False
    fall_counter = 0
    left_counter = 0
    right_counter = 0
    MOVE_AFTER = 3
    FALL_AFTER = 10
    pressed_keys = None

    def __init__(self, positions):
        self.alive = True
        self.cells = []
        for position in positions:
            cell = Cell(position)
            self.cells.append(cell)

    def update(self, grid):
        self.grid = grid
        if self.alive:
            self.pressed_keys = pygame.key.get_pressed()
            self.fall()
            self.move_left()
            self.move_right()
            self.move_down()
            self.rotate()
            self.replace()
        return self.grid

    def fall(self):
       self.fall_counter += 1
       if self.fall_counter >= self.FALL_AFTER:
            self.move(constants.DOWN)
            self.fall_counter = 0

    def move_left(self):
        if self.pressed_keys[pygame.K_LEFT]:
            self.move(constants.LEFT)

    def move_right(self):
        if self.pressed_keys[pygame.K_RIGHT]:
            self.move(constants.RIGHT)

    def move_down(self):
        if self.pressed_keys[pygame.K_DOWN]:
            self.fall_counter += 10

    def rotate(self):
        if self.pressed_keys[pygame.K_UP]:
            self.next_cells = self.get_rotated_cells()
            self.remove()
            if self.can_move_to_next():
                self.move_to_next()
            else:
                self.replace()
            self.next_cells = None

    def get_rotated_cells(self):
        rotated_cells = []
        first_cell = self.cells[0]
        center = first_cell.position
        for cell in self.cells:
            rotated_cell = cell.rotate_about(center)
            rotated_cells.append(rotated_cell)
        return rotated_cells

    def adjacent_cells(self, direction):
        adjacent_cells = []
        for cell in self.cells:
            adjacent_cell = cell.get_adjacent_cell(direction)
            adjacent_cells.append(adjacent_cell)
        return adjacent_cells

    def move(self, direction):
        self.next_cells = self.adjacent_cells(direction)
        self.remove()
        if self.can_move_to_next():
            self.move_to_next()
        elif direction == constants.DOWN:
            self.alive = False
            self.replace()
        else:
            self.replace()
        self.next_cells = None

    def can_move_to_next(self):
        can_move = True
        for next_cell in self.next_cells:
            if not next_cell.can_fit_in_grid(self.grid):
                can_move = False
        return can_move

    def move_to_next(self):
        self.cells = self.next_cells
        for cell in self.cells:
            cell.place(self.grid)

    def replace(self):
        for cell in self.cells:
            cell.place(self.grid)

    def remove(self):
        for cell in self.cells:
            cell.remove(self.grid)
