import  pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill((255,0,0))
 
        self.rect = self.image.get_rect()
 
    def update(self):
        self.rect.y -= 3