import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))

running = True

class Harry:
    def __init__(self,color,radius):
        self.color= color
        self.radius= radius
    
    def drawcircle(self):
        pygame.draw.circle(screen,self.color,(250,250),self.radius)


circle1= Harry('green',30)

while running: 

    pygame.draw.circle(screen,'blue',(250,250),50)
    circle1.drawcircle()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.update()        