from Engine import Engine
from Screen import Screen
from Painter import Painter
from DJ import DJ

screen = Screen()
painter = Painter()
dj = DJ()
e = Engine(screen, painter, dj)
e.run()
