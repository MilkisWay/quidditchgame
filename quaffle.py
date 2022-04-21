import pygame
import os
import sys
import math
from pygame.locals import *
from ball import *
from mode import *
import random


#add mode to an object as an attribute and only access
class QuaffleModel(BallModel):
    def __init__(self, x,y, speed):
     super(QuaffleModel,self).__init__(x,y, speed)
     self._pos = pygame.math.Vector2(x,y)
     self.image = pygame.Surface((8,8))
     self.rect = self.image.get_rect()
     self.rect = pygame.transform.scale(self.image,(8,8))
     self._speed = pygame.math.Vector2(speed,speed)
     self._possession = False 
     #self._mass = mode.get_Game_Mode()


class QuaffleController(object):
    def __init__(self,ball:QuaffleModel):
        self._ball = ball

    def update(self,time):#time from Chaserpower
        angle = 45
        self._ball.set_Coord_x(self._ball.get_Coord_x()+1)#self._ball.get_Speed_x()*time)
        self._ball.set_Coord_y(self._ball.get_Coord_y()+self._ball.get_Speed_y()*time*math.tan(angle) - (self._ball.get_g()*(time**2))//2)
        if self._ball.get_Coord_y() >=1080 or self._ball.get_Coord_y()<=0:
            self._ball.set_Coord_y(0+100)
            self._ball.set_Coord_x(1920//2)
        elif self._ball.get_Coord_x() <=0 or self._ball.get_Coord_x()>=1920:
            self._ball.set_Coord_y(0+100)
            self._ball.set_Coord_x(1920//2)
        print(self._ball.get_Coord_x())
        print(self._ball.get_Coord_y())
        angle=angle-1

    def updat2e(self,dt):
         self._ball.set_Coord_y(self._ball.get_Coord_y()+10)
         if self._ball.get_Coord_y() >=1080:
                self._ball.set_Coord_y(0+100)


    def got_caught(a):
        pass

class QuaffleView(object):#not done
    def __init__(self, quaffleController):
        self._quafflecontroller = quaffleController
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/quaffle.png')
    def render(self, surface):
        surface.blit(self._image,(self._quafflecontroller._ball.get_Coord_x(),self._quafflecontroller._ball.get_Coord_y(),32,32))