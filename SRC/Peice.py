
class Peice:

    positions = []
    last_fall = 0
    alive = False

    def __init__(self):
        self.positions = [(0,0), (0,1), (0,2), (0,3)]
        self.alive = True

    def update(self, graph):
        self.fall(graph)
        self.try_move(graph)
        self.try_rotate(graph)

    def try_move(self, graph):
        return 0

    def try_rotate(self, graph):
        return 0

    def place(self, graph):
        for i in range(0, 4):
            x, y = self.positions[i]
            graph[x][y] = True

    def fall(self, graph):
       self.last_fall += 1
       if self.last_fall == 10:
           self.move_down(graph)
           self.last_fall = 0

    def move_down(self, graph):
        if self.alive:
            self.remove(graph)
            self.move_position_down(graph)
            self.place(graph)
            self.update_alive(graph)

    def update_alive(self, graph):
        for i in range(0, 4):
            x, y = self.positions[i]
            y += 1
            if y >= len(graph):
                self.alive = False

    def remove(self, graph):
        for i in range(0, 4):
            x, y = self.positions[i]
            graph[x][y] = False

    def move_position_down(self, graph):
        for i in range(0, 4):
            x, y = self.positions[i]
            y += 1
            self.positions[i] = (x,y)
