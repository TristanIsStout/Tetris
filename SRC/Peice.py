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


            

class Peice:

    time = 0
    SPEED_1 = 30
    SPEED_2 = 20
    SPEED_3 = 10
    SPEED_4 = 5
    fall_threshold = 30

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

    def __init__(self):
        self.alive = True
        self.cells = []
        positions = self.generate_positions()
        for position in positions:
            cell = Cell(position)
            self.cells.append(cell)

    def generate_positions(self):
        start_x = 10
        start_y = 0
        p1 = None
        p2 = None
        p3 = None
        p4 = None
        peice_type = random.randint(0,6)
        if peice_type == 0:
           p1 = (start_x, start_y + 0)
           p2 = (start_x, start_y + 1)
           p3 = (start_x, start_y + 2)
           p4 = (start_x, start_y + 3)
        if peice_type == 1:
            p1 = (start_x, start_y)
            p2 = (start_x , start_y+1)
            p3 = (start_x + 1, start_y+1)
            p4 = (start_x + 2, start_y+1)
        if peice_type == 2:
            p1 = (start_x, start_y)
            p2 = (start_x, start_y+1)
            p3 = (start_x-1, start_y+1)
            p4 = (start_x-2, start_y+1)
        if peice_type == 3:
            p1 = (start_x, start_y)
            p2 = (start_x, start_y+1)
            p3 = (start_x+1, start_y)
            p4 = (start_x+1, start_y+1)
        if peice_type == 4:
            p1 = (start_x, start_y)
            p2 = (start_x+1, start_y)
            p3 = (start_x, start_y+1)
            p4 = (start_x-1, start_y+1)
        if peice_type == 5:
            p1 = (start_x, start_y)
            p2 = (start_x-1, start_y+1)
            p3 = (start_x, start_y+1)
            p4 = (start_x+1, start_y+1)
        if peice_type == 6:
            p1 = (start_x, start_y)
            p2 = (start_x-1, start_y)
            p3 = (start_x, start_y+1)
            p4 = (start_x+1, start_y+1)

        positions = [p1, p2, p3, p4]
        return positions


    def update(self, grid):
        self.update_speed()
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

    def update_speed(self):
        if self.time < 10:
            self.fall_threshold = self.SPEED_1
        elif self.time < 20:
            self.fall_threshold = self.SPEED_2
        elif self.time < 30:
            self.fall_threshold = self.SPEED_3
        else:
            self.fall_threshold = self.SPEED_4

    def fall(self):
       self.fall_counter += 1
       if self.fall_counter >= self.fall_threshold:
            self.move(constants.DOWN)
            self.fall_counter = 0
    
    left_counter = 0

    def move_left(self):
        if self.pressed_keys[pygame.K_LEFT]:
            self.left_counter +=1
            if self.left_counter > 1:
                self.move(constants.LEFT)
                self.left_counter = 0
        else:
            self.left_counter = 0

    right_counter = 0

    def move_right(self):
        if self.pressed_keys[pygame.K_RIGHT]:
            self.right_counter += 1
            if self.right_counter > 1:
                self.move(constants.RIGHT)
                self.right_counter = 0
        else: 
            self.right_counter = 0

    def move_down(self):
        if self.pressed_keys[pygame.K_DOWN]:
            self.fall_counter += 10


    rotate_counter = 0

    def rotate(self):
        if self.pressed_keys[pygame.K_UP]:
            self.rotate_counter += 1
            if self.rotate_counter > 1:
                self.next_cells = self.get_rotated_cells()
                self.remove()
                if self.can_move_to_next():
                    self.move_to_next()
                else:
                    self.replace()
                self.next_cells = None
                self.rotate_counter = 0
        else: 
            rotate_counter = 0

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
