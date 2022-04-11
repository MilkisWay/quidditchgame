import pygame
import os
import sys
from pygame.locals import *

class Object(pygame.sprite.Sprite):
     def __init__ (self,pos):
        self._pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)

    def set_Coord(self,pos):
        self._pos=pos

    def get_Coord(self):
        return self._pos

    def set_Coord_x(self,x):
        self._pos.x=x

    def get_Coord_x(self):
        return self._pos.x

    def set_Coord_y(self,y):
        self._pos.y=poy

    def get_Coord_y(self):
        return self._pos.y
