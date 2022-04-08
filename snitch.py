import pygame
import os
import sys
import random
from pygame.locals import *
from ball import *
from mode import *

class SnitchModel(BallModel):
    def __init__(self,pos_x,pos_y):
        super(SnitchModel,self).__init__(pos_x,pos_y)
        self.pos = pygame.math.Vector2(pos_x,pos_y)
        self.gameStop = False
        self.disatnce = pygame.math.Vector2.distance_to(self.pos)#need Sveta`s code to add sicker
        self.speed=5

class SnitchController(object):
    def __init__(self):
        self.mode = Mode().mode
        self.ball

    def initball(self,pos_x,pos_y):
        self.ball = SnitchModel(pos_x,pos_y)

    def changeSpeed(self):
        self.ball.speed = self.ball.speed*self.mode

    def fly(self):
        while self.ball.disatnce>0:
            self.ball.pos.x += self.ball.speed * (random.randint(self.mode.mode_A,self.mode.mode_B))#redo
            self.ball.pos.y += self.ball.speed * (random.randint(self.mode.mode_A,self.mode.mode_B))#redo
        if self.distance==0:
            self.ball.gameStop==True #snitch is caught
class SnitchView(object):#not done
    def __init__(self, snitchController,imagelist):
        self.SnitchController = snitchController
        self.image = [self.image.append(imagelist)for i in range(10)]
    def render(self, surface):
        for i in self.BallController.balls:
            surface.blit(self.image,self.BallController.balls[i].pos)

