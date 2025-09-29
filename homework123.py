import pygame

pygame.init()
screen= pygame.display.set_mode((800,800))





background = pygame.image.load('C:/Users/PETER/Desktop/progame_development/beach.png')

character = pygame.image.load('C:/Users/PETER\Desktop/progame_development/cat.webp')






running= True

while running:
    screen.blit(background,(0,0))
    screen.blit(character,(350,600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break
        pygame.display.update()

pygame.quit()

