import pygame

class Ball:
    
    x = 0
    y = 0
    dx = 0
    dy = 0
    ddx = 0
    ddy = 0
    
    x_limit = 0
    y_limit = 0


    def __init__(self, radius, playground_dimensions):
        playground_width, playground_height = playground_dimensions
        self.x_limit = playground_width - 2*radius
        self.y_limit = playground_height - 2*radius

    def set_position(self, position):
        self.x, self.y = position

    def set_velocity(self, velocity):
        self.dx, self.dy = velocity

    def set_acceleration(self, acceleration):
        self.ddx, self.ddy = acceleration
    
    def inc_acceleration(self, inc):
        x_change, y_change = inc
        self.ddx += x_change
        self.ddy += y_change

    def get_position(self):
        self.update()
        position = (int(self.x), int(self.y))
        return position

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.dx += -2
        if pressed[pygame.K_RIGHT]:
            self.dx += 2
        if pressed[pygame.K_UP]:
            self.dy += -2
        if pressed[pygame.K_DOWN]:
            self.dy += 2
        if self.dy < -12:
            self.dy = -12
        if self.dy > 12:
            self.dy = 12
        if self.dx < -12:
            self.dx = -12
        if self.dx > 12:
            self.dx = 12
        self.update_y()
        self.update_x()

    def update_x(self):
        self.dx += self.ddx
        self.x += self.dx
        if self.x > self.x_limit:
            self.x = self.x_limit
            self.dx = -self.dx
        elif self.x < 0:
            self.x = 0
            self.dx = -self.dx

    def update_y(self):
        self.dy += self.ddy
        self.y += self.dy
        if self.y > self.y_limit:
            self.y = self.y_limit
            self.dy = - self.dy
        elif self.y < 0:
            self.y = 0
            self.dy = -self.dy


