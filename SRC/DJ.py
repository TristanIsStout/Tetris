import pygame

class DJ:

    soundtrack = "../MEDIA/Jackpot_By_The_Fat_Rat.mp3"
    
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
