import pygame
import os
import sys
from pygame.locals import *
from interstitial import *
from object import Object
#add player, ball and so on

class CollisionController(object):
    def __init__(self):
        self._collision_detected = False

    def collision_Detection(self,object1,object2):
        if object1.get_distance(object2) <= 0:
            self.collision_detected = True
        return self._collision_detected

    def return_collision_detection_to_start_point(self):
        self.collision_detected = False