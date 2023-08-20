import pygame
from sys import exit

from pygame import mouse

pygame.init()
#initializing pygame 

#display surface
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
FONT = pygame.font.Font(None,50)
hunged_gravity = 300

desert_surface = pygame.image.load("desert_BG.png").convert()
hunged_man = pygame.image.load("Hanging Person 1_1.png").convert_alpha()
text_surface = FONT.render('my Game',False,'yellow').convert()
hunged_x_position = 0

player_surf = pygame.image.load('preview_385.png').convert_alpha()
fire_rect = player_surf.get_rect(midbottom=(500, 350))
hunged_rect = hunged_man.get_rect(bottomright=(0, 360))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #cheecking for the collosion of mouse pos with player or hunged rectangel
        if event.type == pygame.MOUSEMOTION:
            if hunged_rect.collidepoint(event.pos):print('collision')

      if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hunged_gravity = -20

        if event.type == pygame.KEYDOWN:
            print('keydown')

        if event.type == pygame.KEYUP:
            print('key up')

        #cheecking for the collosion of mouse pos with player or hunged rectangel
        if event.type == pygame.MOUSEBUTTONUP:
            if hunged_rect.collidepoint(event.pos):
                hunged_gravity = -20



    screen.blit(desert_surface, (0, 0))

    screen.blit(text_surface,(300,30))
    hunged_rect.x +=2
    if hunged_rect.x >=700:
        hunged_rect.left=0
    screen.blit(hunged_man, hunged_rect)
    fire_rect.left -=1
    screen.blit(player_surf, fire_rect)

    if hunged_rect.colliderect(fire_rect):
        print('collision')#collision happens 1, else 0
    #getting mouse position
    # pygame.mouse
    mouse_pose = pygame.mouse.get_pos()
    if hunged_rect.collidepoint(mouse_pose):
        pygame.mouse.get_pressed()
    #draw all the elements
    #update everything

    #--------surfaces in pygame
    #display surface os the game window
    #anything can be displayed goes here

    pygame.display.update()
    clock.tick(60)

#frame rate how fast is going to run

#TODO--------------creating text , first creat an image of the text
#place it on the display surface



#TODO-------------------COLLOSION WITH RECTANGLE
