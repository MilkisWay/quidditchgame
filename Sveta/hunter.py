import pygame
import os
import sys
from player import Player
from pygame.locals import *
from ball import BallModel
#from collision import CollisionController

class Hunter(Player):
    def __init__(self,x,y,speed):
        Player.__init__(self,x,y,speed)
        
        self.type = 'chaser'
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('hunter.jpg')
        self.acceleration = 1
        self.power = 10
        self.quaffle = []
        self.pos = pygame.math.Vector2(30,10)
        self.speed=pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect()

class Hunter_controller:
    def __init__(self,Hunter):
        sel.hunter=hunter
    
    def update(self):
        self.checkQuaffle()

    def checkQuaffle(self):
         if self.quaffle.get_possession_statues() is None:
             if collision_Detection(self, self.quaffle):
                self.quaffle.set_possession_statues(self)

    def key_control(self, direction):
            if direction=="left":
                t=pygame.math.Vector2(-0.5, 0)
            elif direction=="right":
                t=pygame.math.Vector2(0.5, 0)
            elif direction== "up":
                t=pygame.math.Vector2(0, -0.5)
            elif direction== "down":
                t=pygame.math.Vector2 (0, 0.5)
            self.acceleration += 0.9
            self.speed+=t
   
class Hunter_View:
    def __init__(self, hunter_controller):
        self.hunter_controller=hunter_controller
        self.image=pygame.image.load('hunter.jpg')
    def render(self,surface):
        surface.blit(self.image,(self.hunter_controller.get_Coord_x(),self.hunter_controller.get_Coord_y()))

