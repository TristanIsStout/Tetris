from Engine import Engine
from Screen import Screen
from Painter import Painter

screen = Screen()
painter = Painter()
e = Engine(screen, painter)
e.run()
