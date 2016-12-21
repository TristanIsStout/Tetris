import pygame
import constants

class Menu:

    position = 0
    layer = None
    lines_scored = 0
    caption_text = "Lines: "
    dimensions = constants.MENU_DIMENSIONS
    position = constants.MENU_POSITION
    caption_position = (5, 5)
    next_peice_text = "Next Peice: "
    next_peice_position = (5, 40)

    def __init__(self):
        self.set_up()
        self.draw_caption()
        self.draw_next_peice_caption()
        self.draw_next_peice()
        self.draw_mute_sound_caption()

    def set_up(self):
        self.layer = pygame.Surface(self.dimensions)
        self.layer.fill(constants.BLACK)
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 32)

    def draw_caption(self):
        caption = self.caption_text + str(self.lines_scored)
        self.caption = self.font.render(caption, True, constants.WHITE)
        width,height = self.dimensions
        caption_height = 30
        self.caption_layer = pygame.Surface((width, caption_height))
        self.caption_layer.blit(self.caption, constants.ORIGIN)
        self.layer.blit(self.caption_layer, self.caption_position)

    def draw_next_peice_caption(self):
        self.caption = self.font.render(self.next_peice_text, True, constants.WHITE)
        self.layer.blit(self.caption, self.next_peice_position)

    def draw_next_peice(self):
        peice_position = (40,100)
        if constants.next_peice != None:
            self.peice_layer = constants.next_peice.get_layer()
            self.layer.blit(self.peice_layer, peice_position)

    def draw_mute_sound_caption(self):
        caption = self.font.render("p to toggle sound", True, constants.WHITE)
        position = (5, constants.MENU_HEIGHT - 30)
        self.layer.blit(caption, position)
    
    def update(self, more_lines):
        self.lines_scored = constants.lines
        self.draw_caption()
        self.draw_next_peice()

    def get_toggle_sound(self):
        toggle = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                toggle = True
        return toggle

    def get_layer(self):
        return self.layer

    def set_position(self, position):
        self.position = position
    
    def get_position(self):
        return self.position
