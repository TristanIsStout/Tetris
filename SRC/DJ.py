import pygame
import os

class DJ:

    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    soundtrack = parent_dir + "/Tetris/MEDIA/theme.mp3"
    playing = False
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.soundtrack)

    def play(self):
        pygame.mixer.music.play(-1)
        playing = True

    def pause(self):
        pygame.mixer.music.pause()
        playing = False

    def resume(self):
        pygame.mixer.music.unpause()
        playing = True

    def stop(self):
        pygame.mixer.music.stop()
        playing = False

    def toggle(self):
        if self.playing:
            self.pause()
        else:
            self.resume()
        self.playing = not self.playing
