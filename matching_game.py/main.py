import pygame
import random

pygame.init()
pygame.font.init()
screen= pygame.display.set_mode((600,600))
font= pygame.font.SysFont('Arial',30,'Bold')

game1= pygame.image.load('candycrush.jpg')
game2= pygame.image.load('ludo.png')
game3= pygame.image.load('subwaysurf.png')
game4= pygame.image.load('templerun.png')


Candy_crush= font.render('Candy crush',1,'Black')
Ludo= font.render('Ludo',1,'Black')
Temple_run= font.render('Temple run',1,'Black')
Subway_surfers= font.render('Subway surfers',1,'Black')


games=[game1,game2,game3,game4]
games_text=[Candy_crush,Ludo,Temple_run,Subway_surfers]
random.shuffle(games_text)









running= True

start = []
end= []


while running:
    screen.fill('white')
    y= 25
    for game in games:
        screen.blit(game,(100,y))
        y+=150
    y=50
    for text in games_text:
        screen.blit(text,(300,y))
        y+=150

    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running= False
            break
        if event.type== pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            start.append(start_pos)
        if event.type== pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            end.append(end_pos)
    for pos in start:
        pygame.draw.circle(screen, color='red',center=pos,radius=15)
    for pos in end:
        pygame.draw.circle(screen,color='red',center=pos,radius=15)
    for i in range(len(end)):
        pygame.draw.line(screen,color='red',start_pos=start[i],end_pos=end[i],width= 10)


    pygame.display.update()
