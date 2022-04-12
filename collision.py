import pygame
import os
import sys
from pygame.locals import *
from interstitial import *
from object import Object
#add player, ball and so on

class CollisionController(object):
    def __init__(self,object1:Object,object2:Object):
        self._object1 = object1
        self._object2 = object2
        self._collision_detected = False

    def collision_Detection(self):
        b=False
        if self._object1.colliderect(self._object2):
            self._collision_detected = True
        b = self._collision_detected
        self.collision_detected = False
        return b