import pygame
import os
import sys
from pygame.locals import *

class BallModel(pygame.sprite.Sprite):
    _g=9.8
    def __init__ (self,pos,speed):
        self._pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self._speed = pygame.math.Vector2(speed)
        self._possession = False

    def set_Coord(self,pos):
        self._pos=pos

    def get_Coord(self):
        return self._pos

    def set_Speed(self,speed):
        self._speed = speed
    
    def get_Speed(self):
        return self._speed

    def get_g(self):
        return self._g

    def set_possession_statues(self,t:bool):
        self._possession = t

    def get_possession_statues(self):
        return 

class BallController(object):
    def __init__(self):
        self.balls = []

    def addBall(self,pos,speed):
        self.balls.append(BallModel(pos,speed))

    def fly():
        pass

class BallView(pygame.sprite.Sprite):
    def __init__(self, ballController, img):
        self.BallController = ballController
        self.image = pygame.image.load(img)
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,(i.get_Coord))
