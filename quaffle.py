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
        self.radius=8
        self._speed = pygame.math.Vector2(speed,speed)
        self.possession = False
        self.quaffle_holder_type=None

    def change_holder_type(self,line):
        self.quaffle_holder_type=line
    #в контроллере вызывает при столкновении и меняет два параметра на другие
    def none_is_posessing(self):
        self._possession = False
        self.quaffle_holder_type=None
    #если клавиша, то игрок выпустил мяч и владение стало None collision controller

class QuaffleView(BallView):
    def __init__(self):
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/quaffle.png')
    def getImage(self):
        return self._image

class QuaffleController(BallController):
    def __init__(self,ball:QuaffleModel,ballview:QuaffleView):
        self.ball = ball
        self._image=ballview.getImage()
        self._hunter=None
        self.hunter2=None

    def is_caught_by_hunter(self,hunter):
        self._hunter=hunter
        self.ball.change_holder_type(self._hunter.type)

    def radius_of_hunters(self,hunter):
        self.hunter2=hunter

    def update(self,dt):
        if self.ball.possession==True:
            self.ball.set_Coord(self._hunter.get_Coord)

        if self.ball.quaffle_holder_type!=None:
            if self.hunter2!=None:
                self.ball.set_Coord(self.hunter2.get_Coord)
            else:
                self.ball.set_Coord_y(self.ball.get_Coord_y()+10)
                if self.ball.get_Coord_y() >=1080:
                    self.ball.set_Coord_y(0+100)
        else:
             self.ball.set_Coord_y(self.ball.get_Coord_y()+10)
             if self.ball.get_Coord_y() >=1080:
                self.ball.set_Coord_y(0+100)

    def render(self,surface):
        surface.blit(self._image,(self.ball.get_Coord_x(),self.ball.get_Coord_y(),32,32))