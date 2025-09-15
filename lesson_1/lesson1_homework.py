import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))

running = True



class John:
    def __init__(self,color,radius):
        self.color= color
        self.radius= radius
    
    def drawrectangle(self):
        pygame.draw.rect(screen,self.color,(400,400),self.radius)



rectangle1= John('green',30)

while running: 
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
             break
     pygame.display.update()