import pygame 
from object import Object
import random

class Ring(Object):
   def __init__(self, x,y):
        Object.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image=pygame.image.load('ring.jpg')
        self.pos = pygame.math.Vector2(1000,400)
        self.speed=pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect()
        self.rect.x = 100 
        self.rect.y = 600


class Ring_controller:
    def __init__(self, Rings):
        self.rings=[]

    def add_rings(self,ring):
        all_rings = pygame.sprite.Group()
        all_rings.add(ring)
        return all_rings
