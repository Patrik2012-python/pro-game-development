import pygame

pygame.init()
screen= pygame.display.set_mode((800,600))


class Spaceship:
    def __init__(self, image, pos, angle):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(70,70))
        self.angle = angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.pos = pos





background = pygame.image.load('twoplayer_game/space.png')
background = pygame.transform.scale(background , (800,600))

yellow_spaceship= Spaceship('twoplayer_game/spaceship_yellow.png', (150,300), 90)
red_spaceship= Spaceship('twoplayer_game/spaceship_red.png', (600,300), -90)







running= True

while running:
    screen.blit(background,(0,0))
    screen.blit(yellow_spaceship.image, yellow_spaceship.pos)
    screen.blit(red_spaceship.image, red_spaceship.pos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break

    pygame.display.update()

