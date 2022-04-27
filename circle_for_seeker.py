import pygame
import os
import math
import sys
import random 
from pygame.locals import *
from ball import *

class Circle(BallModel):
    def __init__(self,x,y,speed):
        BallModel.__init__(self,x,y,speed)
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('balls.jpg')
        self.dx=2
        self.dy=2
        self.gameStop = False
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.rect = self.image.get_rect()

    def update(self,time):
            self.dy=random.randint(-1,1)
            self.dx=random.randint(-1,1) 
            self.rect.x+=self.dx*self.speed.x*time
            self.rect.y+=self.dy*self.speed.y*time

            if self.rect.y<0:
                self.rect.y+=10
            if self.rect.y>600:
                self.rect.y-=10
            if self.rect.x<0:
                self.rect.x+=10

            self.pos.x=self.rect.x
            self.pos.y=self.rect.y

class Circle_View:
    def __init__(self):
        self.image=pygame.image.load('balls.jpg')

class Circle_controller:
    def __init__(self,circle: Circle, circle_view: Circle_View):
        self.circle=circle
        self.image=circle_view.image

    def render(self,surface):
        surface.blit(self.image,self.circle.rect)

    def update(self,time):
        self.circle.update(time)