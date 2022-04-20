import pygame
import os
import sys
from pygame.locals import *
from movableobject import Movable_Object

class BallModel(Movable_Object):
    _g=9.8
    def __init__ (self,x,y,speed):
        self._pos = pygame.math.Vector2(x,y)
        #self.sprite
        #self.rect = self.sprite.get_rect()
        self._speed = pygame.math.Vector2(speed,speed)
        self._possession = False           

    def get_g(self):
        return self._g

    def set_possession_statues(self,t:bool):
        self._possession = t

    def get_possession_statues(self):
        return self._possession

class BallController(object):
    def __init__(self):
        self.balls = []

    def addBall(self,x,y,speed):
        self.balls.append(BallModel(x,y,speed))

    def fly():
        pass

class BallView(pygame.sprite.Sprite):
    def __init__(self, ballController, img):
        self.BallController = ballController
        self.image = pygame.image.load(img)
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,(i.get_Coord.x()))
