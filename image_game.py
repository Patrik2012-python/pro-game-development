import pygame

pygame.init()
screen= pygame.display.set_mode((600,600))

image1= pygame.image.load('subwaysurf.png')
image1= pygame.transform.scale(image1,(600,600))
image2= pygame.image.load('templerun.png')
image2= pygame.transform.scale(image2,(600,600))
image3= pygame.image.load('ludo.png')
image3= pygame.transform.scale(image3,(600,600))

image_number= 1



running= True

while running:
     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type == pygame.MOUSEBUTTONDOWN:
                    if image_number == 1:
                        screen.blit(image1, (0, 0))
                        image_number = 2
                    elif image_number == 2:
                        screen.blit(image2, (0, 0))
                        image_number = 3
                    elif image_number == 3:
                        screen.blit(image3, (0, 0))
                        image_number =1 

    pygame.display.update()
            
