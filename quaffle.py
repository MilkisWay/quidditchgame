import pygame
import os
import sys
import math
from pygame.locals import *
from ball import *
from mode import *


#add mode to an object as an attribute and only access
class QuaffleModel(BallModel):
    def __init__(self, x,y, speed):
     super(QuaffleModel,self).__init__(x,y, speed)
     self._pos = pygame.math.Vector2(x,y)
     self.image = pygame.Surface((8,8))
     self.rect = self.image.get_rect()
     self._speed = pygame.math.Vector2(speed,speed)
     self._possession = False 
     #self._mass = mode.get_Game_Mode()


class QuaffleController(object):
    def __init__(self,ball:QuaffleModel):
        self._ball = ball

    def fly_from_throw(self,time,angle):#time from Chaserpower
        if self._ball.get_possession_statues is False:
            self._ball.set_Coord_x(self._ball.get_Coord_x()+self._ball.get_Speed_x()*time)
            self._ball.set_Coord_y(self._ball.get_Coord_y()+self._ball.get_Speed_y()*time*math.tan(angle) - (self.ball.get_g()*(time**2))//2)
            if self._ball.get_Coord_y() <=0:
                self._ball.set_Coord_y(screen_height-100)
                self._ball.set_Coord_x(screen_width//2)
            elif self._ball.get_Coord_x() <=0 and self._ball.get_Coord_x()>=1080:
                self._ball.set_Coord_y(screen_height-100)#add 
                self._ball.set_Coord_x(screen_width//2)#add

    def update(self,dt):
        if self._ball.get_possession_statues == False:
            self._ball.set_Coord_y(self.ball.get_Coord_y()-10)


    def got_caught(a):
        pass

class QuaffleView(object):#not done
    def __init__(self, quaffleController):
        self._quafflecontroller = quaffleController
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/quaffle.png')
    def render(self, surface):
        surface.blit(self._image,(self._quafflecontroller._ball.get_Coord_x(),self._quafflecontroller._ball.get_Coord_y(),32,32))