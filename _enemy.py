import pygame
import random

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super().__init__()
        enemy_image = pygame.image.load('images/ufoRed.png')
        enemy_image = pygame.transform.scale((enemy_image), (32,32))
        self.image = enemy_image
        self.screen = screen
        self.rect = enemy_image.get_rect()
        self.rect.x = random.randrange(0, 200)
        self.rect.y = random.randrange(0, 100)

    
    def update(self):
        self.rect.y += 5

        if self.rect.top > self.screen.get_height():
            self.rect.x = random.randrange(0, 200)
            self.rect.y = random.randrange(0, 100)
    