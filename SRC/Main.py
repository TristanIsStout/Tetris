from Engine import Engine
from Screen import Screen
from Painter import Painter
from DJ import DJ

screen = Screen()
dj = DJ()
painter = Painter(dj)
e = Engine(screen, painter, dj)
e.run()
