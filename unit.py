import pygame
from object import Object 
import pygame.locals as local

class Unit(Object):
    def __init__(self, x,y,speed):
        Object.__init__(self,x,y)
        self.pos = pygame.math.Vector2(x,y)
        self.speed = pygame.math.Vector2(speed,speed)

class Unit_Controller:
    def __init__(self,units):
        self.units=[]

