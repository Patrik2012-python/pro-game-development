import pygame

pygame.init()
screen= pygame.display.set_mode((800,600))

beach = pygame.image.load('C:/Users/PETER/Desktop/progame_development/beach.png')
beach = pygame.transform.scale(beach , (800,600))

cat = pygame.image.load('C:/Users/PETER/Desktop/progame_development/cat.webp')
cat = pygame.transform.scale(cat  , (200,150))






running= True

while running:
    screen.blit(beach,(0,0))
    screen.blit(cat,(400,300))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break

    pygame.display.update()
