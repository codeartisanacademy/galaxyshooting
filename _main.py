import pygame
from hero import Hero
from _bullet import Bullet
# initialize pygame
pygame.init()

# screen
screen_width = 500
screen_height = 700 

screen = pygame.display.set_mode((screen_width,screen_height))

# load background image
bg = pygame.image.load("images/nightskycolor.png")

clock = pygame.time.Clock()

hero = Hero((screen_width/2,screen_height-100))

bullets = []

sprites = pygame.sprite.Group()
sprites.add(hero)

playing = True

while playing:
    screen.blit(bg,(0,0))

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            playing = False
        
        if event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(hero.rect.x+hero.rect.width//2, hero.rect.y))
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        hero.move_left(4, 0)

    if keys[pygame.K_RIGHT]:
        hero.move_right(4, screen_width)
    

    for b in bullets:
        b.update()
    
    for b in bullets:
        b.draw(screen)
    
   

    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    # set the frames per second
    clock.tick(60)

pygame.quit()
