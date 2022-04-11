from random import random
from ball import *


class BludgerModel(BallModel):
    def __init__(self, pos, speed):
        super(BludgerModel,self).__init__(pos, speed)
        self._pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self._speed = pygame.math.Vector2(speed)
        self._possession = False
        self._hit_power = random(1,2)
        self._condition = 100

    def set_condition(self):
        self._condition = self._condition - 10

    def get_condition(self):
        return self._condition

    def get_hit_power(self):
        return self._hit_power
