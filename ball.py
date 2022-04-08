import pygame
import os
import sys
from pygame.locals import *

class BallModel(object):
    def __init__ (self,pos_x,pos_y,speed):
        self.pos = pygame.math.Vector2(pos_x,pos_y)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self.speed = pygame.math.Vector2(speed,speed)
        self.g=9.8

class BallController(object):
    def __init__(self):
        self.balls = []

    def addBall(self,pos,speed):
        self.balls.append(BallModel(pos,speed))

    def fly():
        pass

class BallView(object):
    def __init__(self, ballController, img):
        self.BallController = ballController
        self.image = pygame.image.load(img)
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)
