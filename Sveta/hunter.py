import pygame
import os
import sys
from player import Player
from player import Player_controller
from pygame.locals import *
from ball import BallModel
from collision import CollisionController
from quaffle import QuaffleModel

class Hunter(Player):
    def __init__(self,x,y,speed):
        Player.__init__(self,x,y,speed)
        
        self.type = 'hunter'
        #self.team = team
        self.image = pygame.Surface((10, 10))
   
        self.image=pygame.image.load('hunter.jpg')
        self.image.set_colorkey('black')
        self.acceleration = 1
        self.power = 10
        self.quaffle = None
        self.pos = pygame.math.Vector2(30,10)
        self.speed=pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect()

    def checkQuaffle(self, quaffle):
        if self.collision_Detection(quaffle):
            if quaffle.possession==False:
                self.quaffle=quaffle
                quaffle.possession=True
                quaffle.pos.x=self.pos.x
                quaffle.pos.y=self.pos.y
                print('check')

class Hunter_controller(Player_controller):
    def __init__(self,Hunter):
        Player_controller.__init__(self)
        self.hunter=Hunter
    
class Hunter_View:
    def __init__(self, hunter_controller):
        self.hunter_controller=hunter_controller
        self.image=pygame.image.load('hunter.jpg')
    def render(self,surface):
        surface.blit(self.image,(self.hunter_controller.get_Coord_x(),self.hunter_controller.get_Coord_y()))
