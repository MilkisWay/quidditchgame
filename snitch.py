from operator import truediv
import pygame
import os
import sys
import random
from pygame.locals import *
from ball import *
from mode import *

class SnitchModel(BallModel):
    def __init__(self, pos, speed=5, mode:Mode):
        super(SnitchModel,self).__init__(pos,speed)
        self._pos = pygame.math.Vector2(pos)
        self._gameStop = False
        self._disatnce = pygame.math.Vector2(0,0)
        self._speed=speed
        self._mode = mode.get_Game_Mode()
        self._possession = False

    def endGame(self):
        if self._possession:
            self._gameStop==True
        return self._gameStop

    def set_Speed(self):
        self._speed=self._speed*self._mode
        return self._speed

    def get_Mode(self):
        return self._mode

class SnitchController(object):
    def __init__(self,ball:SnitchModel):
        self.ball = ball

    def fly(self):
        while self.ball.disatnce>0: #change MISTAKE!
            #add here how ball should move
            self.ball.set_possession_statues(True)

class SnitchView(object):#not done
    def __init__(self, snitchController,imagelist):
        self.SnitchController = snitchController
        self.image = [self.image.append(imagelist)for i in range(10)]
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)

