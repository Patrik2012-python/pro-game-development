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
        self.bullets = []

    def fire(self, direction):
        for bullet in self.bullets:
            bullet.x+=direction
            bullet.draw()





class Bullet:
    def __init__(self, x, y, color):
        self.x = x
        self.y= y
        self.color= color

    def draw(self):
        rect = pygame.Rect(self.x,self.y,20,10)
        pygame.draw.rect(screen, self.color, rect)






background = pygame.image.load('twoplayer_game/space.png')
background = pygame.transform.scale(background , (800,600))

yellow_spaceship= Spaceship('twoplayer_game/spaceship_yellow.png', (150,300), 90)
red_spaceship= Spaceship('twoplayer_game/spaceship_red.png', (600,300), -90)

x,y = 600,300
a,w= 100,300

KEYS= {'up': False, 'down': False}
KEYS2= {'up': False, 'down': False}
running= True

while running:
    screen.blit(background,(0,0))
    screen.blit(yellow_spaceship.image, (a,w))
    screen.blit(red_spaceship.image, (x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            break
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bullet = Bullet(red_spaceship.pos[0],red_spaceship.pos[1],'blue')
                red_spaceship.bullets.append(bullet)
            if event.key == pygame.K_j:
                bullet2 = Bullet(yellow_spaceship.pos[0],yellow_spaceship.pos[1],'red')
                yellow_spaceship.bullets.append(bullet2)
  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                KEYS['up']=True
            if event.key == pygame.K_DOWN:
                KEYS['down']=True
            if event.key == pygame.K_w:
                KEYS2['up']=True
            if event.key == pygame.K_s:
                KEYS2['down']=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                KEYS['up']=False
            if event.key == pygame.K_w:
                KEYS2['up']=False
            if event.key == pygame.K_DOWN:
                KEYS['down']=False
            if event.key == pygame.K_s:
                KEYS2['down']=False


    if KEYS['up']== True:
        y-=1
    if KEYS2['up']== True:
        w-=1
    if KEYS2['down']== True:
        w+=1
    
    if KEYS['down']== True:
        y+=1
    
            

    
    red_spaceship.fire(-2)
    yellow_spaceship.fire(+2)

                
    pygame.display.update()

