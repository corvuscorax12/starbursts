import numpy as np
import pygame
import random

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#each particle is called a star
class Star(pygame.Rect):
    def __init__(self,r,theta,scale):
        super().__init__(0,0,scale,scale)
        self.r = r
        self.theta = theta
        #this is the solution
        self.life = 0.0
    #cartisan to polar cordinates to make them spit out in a circle
    def cartopol(self):
        x = (WIDTH/2)+self.r * np.cos(self.theta)
        y = (HEIGHT/2)+ self.r * np.sin(self.theta)
        self.left = x
        self.top = y
    def draw(self,color,surface):
        self.cartopol()
        #color by life turns blue the older it gets :)
        pygame.draw.rect(surface,(255-self.life,255 -self.life,255),self)

        #increase life by 0.1
        self.life += 0.1
        
    #move particle by user specified values
    def moveby(self,r,t):
        self.r += r
        self.theta += t
     
stars = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    blanker = pygame.Surface((WIDTH,HEIGHT))

    #fill in a alpha background for a video feedbackesq effect
    blanker.set_alpha(10)
    blanker.fill((0,0,0))
    screen.blit(blanker,(0,0))


    star = Star(1,random.randint(0,360),3)
    stars.append(star)
    #checks the life of each star
    for lifecheck in stars:
        #if the stars life is over 200 KILL IT >:)
        if lifecheck.life > 200.0:
            stars.remove(lifecheck)
    #draw each star then move them (the move will be visible next iteration)
    for star in stars:
        star.draw("white",screen)
        star.moveby(random.randint(1,10)*0.1,0)


    pygame.display.flip()

    #clock.tick(60)

pygame.quit()