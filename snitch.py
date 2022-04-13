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
    def __init__(self, x,y, seeker1 =1, seeker2=1, speed =5):
        super(SnitchModel,self).__init__(x,y,speed)
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect()
        self._pos = pygame.math.Vector2(x,y)
        self._gameStop = False
        self._speed = pygame.math.Vector2(speed,speed)
        #self._mode = mode.get_Game_Mode()
        self._possession = False
        self.player_seeker = seeker1
        self.computer_seeker = seeker2
        self._who_possess = None

    def endGame(self):
        if self._possession:
            self._gameStop=True
        return self._gameStop

    def set_Speed(self):
        self._speed=self._speed*self._mode
        return self._speed

    def get_Mode(self):
        return self._mode

    def set_who_possess(self,person):
        self._who_posses = person

    def get_who_posses(self):
        return self._who_possess

class SnitchController(object):
    def __init__(self,ball:SnitchModel):
        self._ball = ball

    def update(self,dt):
        self._ball.set_Coord_x(self._ball.get_Speed_x()*dt*random.randint(0,3))
        self._ball.set_Coord_y(self._ball.get_Speed_y()*dt*random.randint(0,2))
    
    def call_Collision_Controller(self):
        collision_Controller=CollisionController(self._ball,self.computer_seeker)
        if collision_Controller.collision_Detection() == True:
            self._ball.set_possession_statues(True)
            self._ball.set_who_possess(self.computer_seeker)

class SnitchView(object):#not done
    def __init__(self, snitchController):
        self._snitchcontroller = snitchController
        self._image=pygame.image.load('snitch.jpg')
    def render(self, surface):
        surface.blit(self._image,(self._snitchcontroller._ball.get_Coord_x(),self._snitchcontroller._ball.get_Coord_y(),32,32))

