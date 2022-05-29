import  pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.radius = 10
        self.speed = 10
        self.x = x
        self.y = y

    def update(self):
        self.y -= self.speed#

    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), self.radius)