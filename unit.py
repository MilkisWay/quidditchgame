import pygame
from object import Object 
import pygame.locals as local

class Unit(Object):
    def __init__(self, x,y):
        Object.__init__(self)
        self.pos = pygame.math.Vector2(x,y)
        self._speed = pygame.math.Vector2(speed,speed)

class Unit_Controller:
    def __init__(self,units):
        self.units=[]


class UnitView:
    def __init__(self,Unit_Controller,image):
        self.Unit_Controller = Unit_Controller
        self.image = pygame.image.load(image)
    def render(self, surface):
        for i in self.Unit_Controller.units:
            surface.blit(self.image,(i.get_Coord.x()))