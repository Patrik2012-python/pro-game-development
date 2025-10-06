import pygame

pygame.init()
screen= pygame.display.set_mode((600,600))

running= True

background= pygame.image.load('rocket_game/pictures/background.png')

rocket= pygame.image.load('rocket_game/pictures/rocket.png')

x,y = 300,300

KEYS= [False, False, False, False]

while running:
    screen.blit(background,(0,0))
    screen.blit(rocket,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                KEYS[0]= True
            elif event.key == pygame.K_LEFT:
                 KEYS[1] = True
            elif event.key == pygame.K_RIGHT:
                 KEYS[2] = True
            elif event.key == pygame.K_DOWN:
                 KEYS[3] = True

        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                KEYS[0] = False
            if event.key == pygame.K_LEFT:
                KEYS[1] =  False
            if event.key == pygame.K_RIGHT:
                KEYS[2] =  False
            if event.key == pygame.K_DOWN:
                KEYS[3] =  False


    if KEYS[0]:
        y-=1
    if KEYS[1]:
        x-=1
    if KEYS[2]:
        x+=1
    if KEYS[3]:
        y+=1
    


    pygame.display.update()


pygame.quit()

