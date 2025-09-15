import pygame

pygame.init()
screen = pygame.display.set_mode((800,800))

running = True



class John:
    def __init__(self,color,w , h , x , y):
        self.color= color
        self.width= w
        self.height= h
        self.x= x
        self.y= y
        self.dimensions= (self.x , self.y, self.width, self.height)

    
    def drawrectangle(self):
        pygame.draw.rect(screen,self.color,self.dimensions)


    def growshape(self):
        self.width+=500
        self.height+=500




 


rectangle1= John('green',356,213,60,200)
rectangle2= John( 'red', 545,123,120,357)

while running:
     rectangle1.drawrectangle()
     rectangle2.drawrectangle()
     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.MOUSEBUTTONDOWN:
             rectangle1.growshape()
             
             break
     pygame.display.update()
