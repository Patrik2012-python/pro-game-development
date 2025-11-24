import pygame 


pygame.init()
screen= pygame.display.set_mode((600,600))

class Animal():
    def __init__(self, imageurl):
        self.image  = pygame.image.load(imageurl)
        self.image  = pygame.transform.scale(self.image,(150,150))
        
bg= pygame.image.load('vector-cartoon-illustration-background-morning-rainforest-bright-jungle-ferns-flowers-design-game-websites-82207249.webp')

animal1= Animal('Porcupine-RF-1.webp')
animal2= Animal('great.jpg')



running= True

while running:
    screen.blit(bg, (0,0))
    screen.blit(animal1.image,(100,100))
    screen.blit(animal2.image,(300,450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()