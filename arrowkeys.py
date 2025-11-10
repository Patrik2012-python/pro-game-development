import pygame

pygame.init()

screen= pygame.display.set_mode((600,600))

bg= pygame.image.load('twoplayer_game/space.png')

red_ship= pygame.image.load('twoplayer_game/spaceship_red.png')
red_ship= pygame.transform.scale(red_ship, (70,70))





KEYS= {'up': False, 'down': False, 'left':False, 'right': False}

x,y= 300,300

running= True

while running:
    screen.blit(bg, (0,0))
    screen.blit(red_ship, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                KEYS['up']=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                KEYS['up']=False
                


    if KEYS['up']== True:
        y-=1
    pygame.display.update()

