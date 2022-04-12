import pygame
import os
import sys
import math
from pygame.locals import *
from ball import *
from mode import *
from mapp import *

#add mode to an object as an attribute and only access
class QuaffleModel(BallModel):
    def __init__(self, x,y, speed):
     super(QuaffleModel,self).__init__(x,y, speed)
     self._pos = pygame.math.Vector2(x,y)
     self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
     self._speed = pygame.math.Vector2(speed,speed)
     #self._mass = mode.get_Game_Mode()


class QuaffleController(object):
    def __init__(self,ball:QuaffleModel):
        self.ball = ball

    def fly_from_throw(self,time,angle):#time from Chaserpower
        if self.ball.get_possession_statues is False:
            self.ball.set_Coord_x(self.ball.get_Coord_x()+self.ball.get_Speed_x()*time)
            self.ball.set_Coord_y(self.ball.get_Coord_y()+self.ball.get_Speed_y()*time*math.tan(angle) - (self.ball.get_g()*(time**2))//2)
            if self.ball.get_Coord_y() <=0:
                self.ball.set_Coord_y(screen_height-100)
                self.ball.set_Coord_x(screen_width//2)
            elif self.ball.get_Coord_x() <=0 and self.ball.get_Coord_x()>=1080:
                self.ball.set_Coord_y(screen_height-100)
                self.ball.set_Coord_x(screen_width//2)

    def fly_without_throw(self):
        if self.ball.get_possession_statues is False:
            self.ball.set_Coord_y(self.ball.get_Coord_y()-1)


    def got_caught(a):
        pass
