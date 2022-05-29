import pygame
import random 

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super().__init__()
        enemy_image = pygame.image.load('images/ufoRed.png')
        enemy_image = pygame.transform.scale(enemy_image, (32,32))    
        self.image = enemy_image
        self.rect = enemy_image.get_rect()
        self.rect.x = random.randrange(0, screen.get_width())
        self.rect.y = random.randrange(0, 100)
        self.screen = screen

    def update(self):
        self.rect.y += 5

        if self.rect.y > self.screen.get_height():
            self.rect.x = random.randrange(0, self.screen.get_width())
            self.rect.y = random.randrange(0, 100)