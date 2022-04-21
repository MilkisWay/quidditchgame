import pygame
import os
import sys
from player import Player
from player import Player_controller
from pygame.locals import *
from ball import BallController #Доступ только через контроллер. К данным шара так доступа нет
from collision import CollisionController
from quaffle import QuaffleController

class Hunter(Player):
    def __init__(self,x,y,speed):
        Player.__init__(self,x,y,speed)
        self.type = 'hunter'
        #self.team = team
        self.image = pygame.Surface((10, 10))
        #self.image=pygame.image.load('hunter.jpg')#должно быть во вью
        self.acceleration = 1
        self.power = 10
        self.quaffle = None
        self.pos = pygame.math.Vector2(30,10)
        self.speed=pygame.math.Vector2(speed,speed)#Тоже, что и в охотнике
        self.rect = self.image.get_rect()

    def checkQuaffle(self, quaffle):
        pass
    def nearest_hunter()://distance to nearest hunter
        pass

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

