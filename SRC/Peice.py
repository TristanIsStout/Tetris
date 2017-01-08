import pygame
import copy
import random
import constants
from Cell import Cell

            

class Peice:

    time = 0
    time_offset = 0
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
    positions = None

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
        self.peice_type = peice_type
        self.positions = [p1, p2, p3, p4]
        return self.positions


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
        if constants.lines == 0:
            self.fall_threshold = self.SPEED_1
        elif constants.lines == 1:
            self.fall_threshold = self.SPEED_2
        elif constants.lines == 2:
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

    def get_layer(self):
        dimensions = (6*constants.BLOCK_SIZE, 6*constants.BLOCK_SIZE)
        layer = pygame.Surface(dimensions)
        for position in self.positions:
            self.draw_on(layer, position)
        return layer

    def draw_on(self, layer, position):
        x,y = position
        x -= 8
        x = x * constants.BLOCK_SIZE
        y = y * constants.BLOCK_SIZE
        width = constants.BLOCK_SIZE - 1
        height = constants.BLOCK_SIZE - 1
        rect = (x, y, width, height)
        pygame.draw.rect(layer, constants.BLUE, rect)

