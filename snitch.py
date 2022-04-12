from operator import truediv
import pygame
import os
import sys
import random
from pygame.locals import *
from ball import *
from mode import *
from collision import CollisionController

class SnitchModel(BallModel):
    def __init__(self, x,y, mode:Mode, seeker1, seeker2, speed =5):
        super(SnitchModel,self).__init__(x,y,speed)
        self._pos = pygame.math.Vector2(x,y)
        self._gameStop = False
        self._speed=speed
        self._mode = mode.get_Game_Mode()
        self._possession = False
        self.player_seeker = seeker1
        self.computer_seeker = seeker2
        self._who_possess = None

    def endGame(self):
        if self._possession:
            self._gameStop=True

    def set_Speed(self):
        self._speed=self._speed*self._mode
        return self._speed

    def get_Mode(self):
        return self._mode

    def set_who_posses(self,person):
        self._who_posses = person

class SnitchController(object):
    def __init__(self,ball:SnitchModel):
        self._ball = ball

    def fly(self):
        pass
    
    def call_Collision_Controller(self):
        collision_Controller=CollisionController(self._ball,self.computer_seeker)
        if collision_Controller.collision_Detection() == True:
            self._ball.set_possession_statues(True)
            self._ball.set_who_posses(self.computer_seeker)
            self._ball.endGame() #add how to call an end of a game


class SnitchView(object):#not done
    def __init__(self, snitchController,imagelist):
        self.SnitchController = snitchController
        self.image = [self.image.append(imagelist)for i in range(10)]
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)

