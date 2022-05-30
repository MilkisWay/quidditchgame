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
        self.pos = pygame.math.Vector2(x,y)
        self.image = pygame.Surface((8,8))
        self.rect = self.image.get_rect()
        self.rect = pygame.transform.scale(self.image,(8,8))
        self.radius=100
        self._speed = pygame.math.Vector2(speed,speed)
        self.possession = False
        self.quaffle_holder_type=None

    def change_holder_type(self,line):
        self.quaffle_holder_type=line

    def none_is_possessing(self):
        self.possession = False
        self.quaffle_holder_type=None


class QuaffleView(BallView):
    def __init__(self):
        self._image=pygame.image.load('quaffle.png')
    def getImage(self):
        return self._image

class QuaffleController(BallController):
    def __init__(self,ball:QuaffleModel,ballview:QuaffleView):
        self.ball = ball
        self._image=ballview.getImage()
        self.hunter=None
        self.count=0

    def is_caught_by_hunter(self,hunter):
        self.hunter=hunter
        self.ball.change_holder_type(self.hunter.type)
        self.ball.possession=True

    def is_not_caught_by_hunter(self):
        self.ball.none_is_possessing()
        self.hunter==None

    def radius_of_hunters(self,hunter):
        self.hunter2=hunter

    def update_if_caught(self):
        if self.hunter!=None:
            self.ball.pos.x=self.hunter.pos.x
            self.ball.pos.y=self.hunter.pos.y
            self.count+=1

    def update_if_not_caught(self):
        self.ball.pos.y=self.ball.pos.y+10
        if self.ball.pos.y>=1080:
            self.ball.pos.y=100
        self.count+=1

    def update(self):
        if self.count==0:
            if self.hunter!=None:
                self.ball.pos.x=self.hunter.pos.x
                self.ball.pos.y=self.hunter.pos.y
            else:
                self.ball.pos.y=self.ball.pos.y+10
                if self.ball.pos.y>=1080:
                    self.ball.pos.y=100
        self.count=0

    def render(self,surface):
        surface.blit(self._image,(self.ball.pos.x,self.ball.pos.y))