import pygame
import os

class DJ:

    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    soundtrack = parent_dir + "/Tetris/MEDIA/theme.mp3"
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.soundtrack)

    def play(self):
        pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
