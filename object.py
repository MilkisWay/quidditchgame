import pygame
import os
import sys
from pygame.locals import *

class Object(pygame.sprite.Sprite):
     def __init__ (self,x,y):
        self._pos = pygame.math.Vector2(x,y)
        self._startpos = pygame.math.Vector2(x,y)
        self.sprite
        self.rect = self.sprite.get_rect()

     def start_pos_x(self):
         return self._startpos.x

     def start_pos_y(self):
         return self._startpos.y

     def set_Coord(self,x,y):
         self._pos=[x,y]

     def get_Coord(self):
        return self._pos

     def set_Coord_x(self,x):
        self._pos.x=x

     def get_Coord_x(self):
        return self._pos.x

     def set_Coord_y(self,y):
        self._pos.y=y

     def get_Coord_y(self):
        return self._pos.y

     def get_distance(self,object1):
        return pygame.math.Vector2(self.get_Coord()).distance_to(object1.get_Coord())

class ObjectView(object):
    pass

class ObjectController(object):
    pass