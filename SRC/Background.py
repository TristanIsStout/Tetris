import pygame
import constants

class Background:
    
    layer = None
    dimensions = constants.SCREEN_DIMENSIONS

    def __init__(self):
        self.set_up_screen()
        self.draw_playground()
        self.draw_grid()
        self.draw_playground()

    def set_up_screen(self):
        self.layer = pygame.Surface(self.dimensions)
        self.layer.fill(constants.BACKGROUND_COLOR)
        self.layer = self.layer.convert()

    def draw_playground(self):
        pygame.draw.rect(self.layer, constants.BLACK, constants.PLAYGROUND_RECT)

    def draw_grid(self):
        self.draw_horizontal_lines()
        self.draw_vertical_lines()

    def draw_horizontal_lines(self):
        horizontal_lines = constants.SCREEN_HEIGHT / constants.BLOCK_SIZE + 1
        for line_number in range(1, horizontal_lines):
            start_x = 0
            start_y = line_number * constants.BLOCK_SIZE
            start_pos = (start_x, start_y)
            end_x = constants.SCREEN_WIDTH
            end_y = start_y
            end_pos = (end_x, end_y)
            pygame.draw.line(self.layer, constants.LIGHT_GREY, start_pos, end_pos)

    def draw_vertical_lines(self):
        vertical_lines = constants.SCREEN_WIDTH / constants.BLOCK_SIZE + 1
        for line_number in range(1, vertical_lines):
            start_x = line_number * constants.BLOCK_SIZE
            start_y = 0
            start_pos = (start_x, start_y)
            end_x = start_x
            end_y = constants.SCREEN_WIDTH
            end_pos = (end_x, end_y)
            pygame.draw.line(self.layer, constants.LIGHT_GREY, start_pos, end_pos)

    def get_layer(self):
        return self.layer
