import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,600))

pygame.display.set_caption('birthday greeting card')

image1= pygame.image.load('birthday_animation/birthday_pictures/page1.jpg')
image1= pygame.transform.scale(image1,(600,600))






running = True

while running:
    screen.blit(image1, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    
    font=pygame.font.SysFont('arial',50)
    text=font.render('Happy birthday',True,'black')
    screen.blit(text,(150,300))
    pygame.display.update()
    time.sleep(3)
    




    
    image2= pygame.image.load('birthday_animation/birthday_pictures/page2.jpg')
    image2= pygame.transform.scale(image2,(600,600))
    screen.fill('blue')
    screen.blit(image2, (0,0))
    text2=font.render('Have a good birthday',True,'black')
    screen.blit(text2,(100,300))

    pygame.display.update()
    time.sleep(3)

    image3= pygame.image.load('birthday_animation/birthday_pictures/page3.jpg')
    image3= pygame.transform.scale(image3,(600,600))
    screen.fill('blue')
    screen.blit(image3, (0,0))
    text3=font.render('i wish you a good birthday',True,'black')
    screen.blit(text3,(50,300))
    pygame.display.update()
    time.sleep(4)
    
