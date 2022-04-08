import pygame
import os
import sys
from pygame.locals import *
from ball import *
from mode import *

class QuaffleModel(BallModel):
    def __init__(self, pos_x, pos_y, speed):
     super(QuaffleModel,self).__init__(pos_x, pos_y, speed)
     self.pos = pygame.math.Vector2(pos_x,pos_y)
     self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
     self.speed = pygame.math.Vector2(speed,speed)
     self.mass = Mode().mode
     self.g=9.8


class QuaffleController():
    def __init__(self):
        self.ball

    def initball(self,pos_x, pos_y, speed):
        self.ball = QuaffleModel(pos_x, pos_y, speed)

    def fly(self,time):#time from Chaserpower
        for i in range(1,time):
            self.pos.x=self.pos.x+self.speed.x*i
            self.pos.y=self.pos.y+self.speed.y*i - (self.g*(i**2))//2