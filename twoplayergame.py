import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800,600))
comic_sans=pygame.font.SysFont('Comic Sans',40)

class Spaceship:
    def __init__(self, imageurl, angle, pos, color):
        self.image  = pygame.image.load(imageurl)
        self.image  = pygame.transform.scale(self.image,(75,75))
        self.image  = pygame.transform.rotate(self.image,angle)
        self.rect   = self.image.get_rect(center = pos)
        self.bullets= []
        self.color = color
        self.health =10
        self.health_text= comic_sans.render(f'Health:{self.health}',1,self.color)
    
    def fire(self,direction):
        for bullet in self.bullets:
            bullet.rect.x+=direction
            bullet.draw()
    
    def detect_collision(self, enemy_ship):
        for bullet in self.bullets:   
            if bullet.rect.colliderect(enemy_ship.rect):
                self.bullets.remove(bullet)  
                enemy_ship.health-=1
                self.health_text= comic_sans.render(f'Health:{enemy_ship.health}',1,enemy_ship.color)

    def movement(self):
        keys = pygame.key.get_pressed() 
        if self.color == 'red':
            if keys[pygame.K_w]:
                self.rect.y-=1
            if keys[pygame.K_s]:
                self.rect.y+=1

        else:
            if keys[pygame.K_UP]:
                self.rect.y-=1
            if keys[pygame.K_DOWN]:
                self.rect.y+=1
    


                                                                                                                                              
        


class Bullet:
    def __init__(self, pos, color):
        self.rect= pygame.Rect(pos,(10,10))
        self.color= color

    def draw(self):
        pygame.draw.rect(screen,self.color,self.rect)



bg = pygame.image.load('twoplayer_game\space.png')
bg = pygame.transform.scale(bg,(800,600))

red_ship= Spaceship('twoplayer_game\spaceship_red.png', +90, (100,300),'red')
yellow_ship= Spaceship('twoplayer_game\spaceship_yellow.png', -90,(700,300),'yellow')



running = True

while running:
    screen.blit(bg, (0,0))
    screen.blit(red_ship.image,red_ship.rect.topleft)
    screen.blit(yellow_ship.image,yellow_ship.rect.topleft)
    screen.blit(red_ship.health_text,(50,50))
    screen.blit(yellow_ship.health_text,(550,50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                red_bullet = Bullet(red_ship.rect.center,'red')
                red_ship.bullets.append(red_bullet)

            if event.key == pygame.K_l:
                yellow_bullet= Bullet(yellow_ship.rect.center,'yellow')
                yellow_ship.bullets.append(yellow_bullet)
    red_ship.fire(+2)
    yellow_ship.fire(-2)
    red_ship.detect_collision(yellow_ship)
    yellow_ship.detect_collision(red_ship)
    red_ship.movement()
    yellow_ship.movement()
    pygame.display.update()                                                                                                                                    
                                                                           