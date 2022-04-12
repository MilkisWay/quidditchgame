from operator import truediv
import pygame
import os
import sys
import random
from pygame.locals import *
from ball import *
from mode import *

class SnitchModel(BallModel):
    def __init__(self, x,y, mode:Mode, seeker1, seeker2, speed =5):
        super(SnitchModel,self).__init__(x,y,speed)
        self._pos = pygame.math.Vector2(x,y)
        self._gameStop = False
        self._speed=speed
        self._mode = mode.get_Game_Mode()
        self._possession = False
        self._player_seeker = seeker1
        self._computer_seeker = seeker2

    def endGame(self):
        if self._possession:
            self._gameStop=True
        return self._game

    def set_Speed(self):
        self._speed=self._speed*self._mode
        return self._speed

    def get_Mode(self):
        return self._mode

class SnitchController(object):
    def __init__(self,ball:SnitchModel):
        self.ball = ball

    def fly(self):
        if

class SnitchView(object):#not done
    def __init__(self, snitchController,imagelist):
        self.SnitchController = snitchController
        self.image = [self.image.append(imagelist)for i in range(10)]
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)

