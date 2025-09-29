import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((800,800))


class Henry:
    def __init__(self,color,radius):
        self.color= color
        self.radius= radius
       # self.width= w
       # self.height= h
       # self.dimensions= (self.width, self.height)
    
    
    def drawcircle(self):
        pygame.draw.circle(screen,self.color,(400,400),self.radius)


    def growcircle(self):
        self.radius+=10

    def changecolor(self):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        self.color=(r,g,b)

circle= Henry( 'red',50)

running= True

while running:
        circle.drawcircle()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                circle.growcircle()
                circle.changecolor()

        pygame.display.update()



pygame.quit()
