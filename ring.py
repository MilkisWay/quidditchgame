import pygame
import os
import math
import sys
import random 
from nonmovableobject import *
from pygame.locals import *

class Ring(NonMovableObject):
    def __init__(self,x,y):
        super(Ring,self).__init__(x,y)
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('ring.png')
        self.gameStop = False
        self.pos = pygame.math.Vector2(x,y)
        #self.rect = self.image.get_rect()
        self.rect.x=500
        self.rect.y=500
        self.pos.x=self.rect.x
        self.pos.y=self.rect.y


class Ring_View(NonMovableObjectView):
    def __init__(self):
        super(NonMovableObjectView,self).__init__()
        self.image=pygame.image.load('ring.png')

class Ring_controller(NonMovableObjectController):
    def __init__(self,ring: Ring, ring_view: Ring_View):
        super(NonMovableObjectController,self).__init__()
        self.ring=ring
        self.image=ring_view.image

    def update(self,gameTime):
        pass
    def render(self,surface):
        surface.blit(self.image,self.ring.rect)
