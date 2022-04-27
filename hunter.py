﻿import pygame
import os
import math
import sys
import random 
from player import Player
from player import Player_controller
from pygame.locals import *
from collision import CollisionController
from quaffle import QuaffleController

class Hunter(Player):
    def __init__(self,x,y,speed,acceleration,activity):
        Player.__init__(self,x,y,speed,acceleration,activity)
        self.type = 'hunter'
        #self.team = team
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('player.png')
        self.activity=activity
        self.gameStop = False
        self.acceleration = acceleration
        self.power = 10
        self.quaffle = None
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.rect = self.image.get_rect()

    def checkQuaffle(self, quaffle):#Во-первых все взаимодействия в контроллере, во-вторых этим ты не управляешь
        pass

class Hunter_View:
    def __init__(self):
        self.image=pygame.image.load('player.png')

class Hunter_controller(Player_controller):
    def __init__(self,player: Hunter, player_view: Hunter_View):
        Player_controller.__init__(self)
        self.player=player
        self.image=player_view.image

    def render(self,surface):
        surface.blit(self.image,self.player.rect)

    def update(self,time):
            self.player.update(time)
    
   
    def computer_update(self,time):
            self.player.computer_update(time)
  
  
