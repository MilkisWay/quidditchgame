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
        self._pos = pygame.math.Vector2(x,y)
        self.rect = self.image.get_rect(topleft = self._pos)
        self.rect = pygame.transform.scale(self.image,(8,8))
        self.radius=50
        self._gameStop = False
        self._speed = pygame.math.Vector2(speed,speed)
        #self._mode = mode.get_Game_Mode()
        self._possession = False
        self._who_possess = None

    def endGame(self,team):
        if self._possession:
            self._who_posses=team
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

    def get_image(self):
        return self.image


class SnitchView(BallView):#not done
    def __init__(self):
        self._image=pygame.image.load('C:/Users/milan/Documents/Uni/Python/Game/GameUni/Photos/snitch_redone.png')
    def getImage(self):
        return self._image
    

class SnitchController(BallController):
    def __init__(self,ball:SnitchModel,ballview:SnitchView):
        self.ball = ball
        self._image=ballview.getImage()

    def update(self,dt):
        num = random.randint(1,4)
        if 1920 <= self.ball.get_Coord_x() or self.ball.get_Coord_x()<=0 or 0>=self.ball.get_Coord_y() or self.ball.get_Coord_y()>=1080:
            self.ball.set_Coord_x(500)
            self.ball.set_Coord_y(500)
        elif num == 1:
            self.ball.set_Coord_x(self.ball.get_Coord_x() + random.randint(1,100))
            self.ball.set_Coord_y(self.ball.get_Coord_y())
        elif num == 2:
            self.ball.set_Coord_x(self.ball.get_Coord_x() - random.randint(1,100))
            self.ball.set_Coord_y(self.ball.get_Coord_y())
        elif num == 3:
            self.ball.set_Coord_x(self.ball.get_Coord_x())
            self.ball.set_Coord_y(self.ball.get_Coord_y() + random.randint(1,100))
        elif  num == 4:
            self.ball.set_Coord_x(self.ball.get_Coord_x())
            self.ball.set_Coord_y(self.ball.get_Coord_y() - random.randint(1,100))
        elif num == 5:
            self.ball.set_Coord_x(self.ball.get_Coord_x() - random.randint(1,100))
            self.ball.set_Coord_y(self.ball.get_Coord_y() + random.randint(1,100))
        elif num == 6:
            self.ball.set_Coord_x(self.ball.get_Coord_x() + random.randint(1,100))
            self.ball.set_Coord_y(self.ball.get_Coord_y() - random.randint(1,100))
        elif num == 7:
            self.ball.set_Coord_x(random.randint(3,1900))
            self.ball.set_Coord_y(random.randint(10,1050))

    def render(self, surface):
        surface.blit(self._image,(self.ball.get_Coord_x(),self.ball.get_Coord_y(),32,32))
        pygame.draw.circle(surface,220,(200,100),20)
    



