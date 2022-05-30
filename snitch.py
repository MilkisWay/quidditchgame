from operator import truediv
import pygame
import os
import sys
import random
from pygame.locals import *
from ball import *
from mode import *

class SnitchModel(BallModel):
    def __init__(self, x,y, seeker1 =1, seeker2=1, speed =5):
        super(SnitchModel,self).__init__(x,y,speed)
        self.image = pygame.Surface((8,8)) 
        self.pos = pygame.math.Vector2(x,y)
        self.rect = self.image.get_rect(topleft = self._pos)
        self.rect = pygame.transform.scale(self.image,(8,8))
        self.radius=250
        self.gameStop = False
        self._speed = pygame.math.Vector2(speed,speed)
        self.result=0
        #self._mode = mode.get_Game_Mode()
        self.possession = False
        self.who_possess = None
        self.count=1

    def endGame(self,team):
        if self.possession==True:
            self.who_posses=team
            self.gameStop=True

    def set_Speed(self):
        self._speed=self._speed*self._mode
        return self._speed

    def get_Mode(self):
        return self._mode

    def set_who_possess(self,person):
        self.who_posses = person

    def get_who_posses(self):
        return self.who_possess

    def get_image(self):
        return self.image


class SnitchView(BallView):#not done
    def __init__(self):
        self._image=pygame.image.load('snitch.png')
    def getImage(self):
        return self._image
    

class SnitchController(BallController):
    def __init__(self,ball:SnitchModel,ballview:SnitchView):
        self.ball = ball
        self._image=ballview.getImage()

    def update(self,dt):
        if self.ball.possession!=True:
            num = random.randint(1,4)
            if 1920 <= self.ball.pos.x or self.ball.pos.x<=0 or 0>=self.ball.pos.y or self.ball.pos.y>=1080:
                self.ball.pos.x=500
                self.ball.pos.y=500
            elif num == 1:
                self.ball.pos.x=self.ball.pos.x + random.randint(1,100)
                self.ball.pos.y=self.ball.pos.y
            elif num == 2:
                self.ball.pos.x=self.ball.pos.x - random.randint(1,100)
                self.ball.pos.y=self.ball.pos.y
            elif num == 3:
                self.ball.pos.x=self.ball.pos.x
                self.ball.pos.y=self.ball.pos.y + random.randint(1,100)
            elif  num == 4:
                self.ball.pos.x=self.ball.pos.x
                self.ball.pos.y=self.ball.pos.y - random.randint(1,100)
            elif num == 5:
                self.ball.pos.x=self.ball.pos.x - random.randint(1,100)
                self.ball.pos.y=self.ball.pos.y + random.randint(1,100)
            elif num == 6:
                self.ball.pos.x=self.ball.pos.x + random.randint(1,100)
                self.ball.pos.y=self.ball.pos.y - random.randint(1,100)
            elif num == 7:
                self.ball.pos.x=random.randint(3,1900)
                self.ball.pos.y=random.randint(10,1050)

    def render(self, surface):
        if self.ball.possession!=True:
            surface.blit(self._image,(self.ball.pos.x,self.ball.pos.y))



