import pygame
import os
import sys
import math
import random
from pygame.locals import *
from ball import *
from mode import *


class QuaffleModel(BallModel):
    def __init__(self, x,y, speed):
        super(QuaffleModel,self).__init__(x,y, speed)
        self._pos = pygame.math.Vector2(x,y)
        self.image = pygame.Surface((8,8))
        self.rect = self.image.get_rect()
        self.rect = pygame.transform.scale(self.image,(8,8))
        self.radius=50
        self._speed = pygame.math.Vector2(speed,speed)
        self.possession = False
        self.quaffle_holder_type=None

    def change_holder_type(self,line):
        self.quaffle_holder_type=line

    def none_is_posessing(self):
        self.possession = False
        self.quaffle_holder_type=None


class QuaffleView(BallView):
    def __init__(self):
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/quaffle.png')
    def getImage(self):
        return self._image

class QuaffleController(BallController):
    def __init__(self,ball:QuaffleModel,ballview:QuaffleView):
        self.ball = ball
        self._image=ballview.getImage()
        self.hunter=None

    def is_caught_by_hunter(self,hunter):
        self.hunter=hunter
        self.ball.change_holder_type(self.hunter.type)
        self.ball.possession=True

    def radius_of_hunters(self,hunter):
        self.hunter2=hunter

    def update(self,dt):
        if self.ball.possession==True:
            if self.hunter!=None:
                self.ball.set_pos(self.hunter.pos)
        else:
             self.ball.set_Coord_y(self.ball.get_Coord_y()+10)
             if self.ball.get_Coord_y()>=1080:
                self.ball.set_Coord_y(0+100)

    def render(self,surface):
        surface.blit(self._image,(self.ball.get_Coord_x(),self.ball.get_Coord_y(),32,32))
        pygame.draw.circle(surface,255,(500,100),20)