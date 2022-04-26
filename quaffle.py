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
     self.rect = pygame.transform.scale(self.image,(8,8))
     self._speed = pygame.math.Vector2(speed,speed)
     self._possession = False 
     #self._mass = mode.get_Game_Mode()

class QuaffleView(BallView):#not done
    def __init__(self):
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/quaffle.png')
    def getImage(self):
        return self._image
    


class QuaffleController(BallController):
    def __init__(self,ball:QuaffleModel,ballview:QuaffleView):
        self._ball = ball
        self._image=ballview.getImage()

    def fly_from_throw(self,time,angle):#time from Chaserpower
        if self._ball.get_possession_statues is False:
            if 0<self._ball.get_Coord_x()<1920 and 0<self._ball.get_Coord_y()<1080:
                self._ball.set_Coord_x(self._ball.start_pos_x()+self._ball.get_Speed_x()*time*math.cos(angle))
                self._ball.set_Coord_y(self._ball.start_pos_y()+self._ball.get_Speed_y()*time*math.sin(angle) - (self._ball.get_g()*(time**2))//2)
        if self._ball.get_Coord_y()<0:
            self.updat2e(time)

    def update(self,dt):
         self._ball.set_Coord_y(self._ball.get_Coord_y()+10)
         if self._ball.get_Coord_y() >=1080:
                self._ball.set_Coord_y(0+100)

    def render(self,surface):
        surface.blit(self._image,(self._ball.get_Coord_x(),self._ball.get_Coord_y(),32,32))

    def got_caught(a):
        pass



   