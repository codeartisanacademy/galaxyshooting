import pygame

class Hero(pygame.sprite.Sprite):
    
    def __init__(self, position):
        super().__init__()
        hero_image = pygame.image.load('images/playerShip3_red.png')
        hero_image = pygame.transform.scale(hero_image, (24,24))
        self.image = hero_image
        self.rect = self.image.get_rect(center=position)
        


    def move_left(self, pixels, boundary):
        self.rect.x = self.rect.x - pixels
        if self.rect.x < boundary:
            self.rect.x = boundary
            
    def move_right(self, pixels, boundary):
        self.rect.x = self.rect.x + pixels
        if self.rect.x > boundary - self.rect.width:
            self.rect.x = boundary - self.rect.width


    def shoot(self):
        pass