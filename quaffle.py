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
    def __init__(self, pos, speed, mode:Mode):
     super(QuaffleModel,self).__init__(pos, speed)
     self._pos = pygame.math.Vector2(pos)
     self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
     self._speed = pygame.math.Vector2(speed)
     self._mass = mode.get_Game_Mode()


class QuaffleController(object):
    def __init__(self,ball:QuaffleModel):
        self.ball = ball

    def fly(self,time,angle):#time from Chaserpower
        if self.ball.get_possession_statues is False:
            for i in range(1,time):
                self.ball.pos.x=self.ball.pos.x+self.ball.speed.x*i
                self.ball.pos.y=self.ball.pos.y+self.ball.speed.y*i*tan(angle) - (self.ball.g*(i**2))//2
                if self.ball.pos.y <=0:
                    self.ball.pos.y = screen_height-100
                    self.ball.pos.x = screen_width//2
                elif self.ball.pos.x <=0 and self.ball.pos.x>=1080:
                    self.ball.pos.x = screen_width//2
                    self.ball.pos.y = screen_height-100
                if self.ball.get_possession_statues == True:
                    break
    def got_caught(a):
        pass
