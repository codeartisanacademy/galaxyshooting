import pygame

class Hero(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super().__init__()
        hero_image = pygame.image.load('images/playerShip3_red.png')
        hero_image = pygame.transform.scale(hero_image, (32,32))    
        self.image = hero_image
        self.rect = hero_image.get_rect(center=position)

    def move_left(self, pixels, boundary):
       self.rect.x = self.rect.x - pixels
       if self.rect.x < boundary:
           self.rect.x = 0
            
    def move_right(self, pixels, boundary):
        self.rect.x = self.rect.x + pixels
        if self.rect.x > boundary - self.rect.width:
            self.rect.x = boundary - self.rect.width

    def shoot(self):
        pass