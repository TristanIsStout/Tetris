import pygame
from Ball import Ball
from Background import Background
from Menu import Menu
from Playground import Playground
import constants


class Painter:

    DEFAULT_DIMENSIONS = constants.SCREEN_DIMENSIONS
    dimensions = None
    background_layer = None
    foreground_layer = None
    ball = None
    layers = []

    def __init__(self, dj, dimensions = DEFAULT_DIMENSIONS):
        self.dj = dj
        self.dimensions = dimensions
        self.create_background()
        self.create_menu()
        self.create_playground()

    def generate_surfaces_with_positions(self, playtime):
        self.update(playtime)
        return self.layers

    def update(self, time):
        self.update_menu()
        self.update_playground(time)

    def update_menu(self):
        self.menu.update(0)
        if self.menu.get_toggle_sound():
            self.dj.toggle()

    def update_playground(self, time):
        self.playground.update(time)

    def generate_caption(self, playtime):
        return "Tetris"

    def create_background(self):
        background = Background()
        self.background_layer = background.get_layer()
        background.set_position(len(self.layers))
        self.layers.append((self.background_layer, constants.ORIGIN))

    def create_menu(self):
        self.menu = Menu()
        self.menu.set_position(len(self.layers))
        self.layers.append((self.menu.get_layer(), constants.MENU_POSITION))

    def create_playground(self):
        playground = Playground()
        layer = playground.get_layer()
        index = len(self.layers)
        playground.set_position(index)
        self.playground = playground
        self.layers.append((layer, constants.PLAYGROUND_POSITION))
