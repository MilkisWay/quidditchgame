from random import random
from ball import *


class BludgerModel(BallModel):
    def __init__(self, x,y, speed):
        super(BludgerModel,self).__init__(x,y, speed)
        self._pos = pygame.math.Vector2(x,y)
        self.sprite
        self.rect = self.sprite.get_rect()
        self._speed = pygame.math.Vector2(speed,speed)
        self._hit_power = random(1,2)
        self._condition = 100

    def set_condition(self):
        self._condition = self._condition - 10

    def get_condition(self):
        return self._condition

    def get_hit_power(self):
        return self._hit_power

class BludgerController(object):
    def __init__(self):
        self._balls = []

    def addBall(self,x,y,speed):
        self._balls.append(BludgerModel(x,y,speed))
    def fly(self,object):
        for i in self._balls:
            if self._balls[i].get_distance(object) <5:
                self._balls[i].set_Coord(object.get_Coord())
                self._balls[i].attack(object)

    def attack(self,object):
        pass