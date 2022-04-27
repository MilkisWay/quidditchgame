import pygame
import os
import math
import sys
import random 
from player import Player
from player import Player_controller
from pygame.locals import *
from collision import CollisionController
from quaffle import QuaffleController

class Seeker(Player):
    def __init__(self,x,y,speed,acceleration,activity):
        Player.__init__(self,x,y,speed,acceleration,activity)
        self.type = 'seeker'
        #self.team = team
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('seeker.jpg')
        self.activity=activity
        self.gameStop = False
        self.acceleration = acceleration
        self.power = 0
        self.snitch = None
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.rect = self.image.get_rect()
        #self.rect.x=500
        #self.rect.y=400

    #def update(self,time):
       #self.dy=2
       #self.dx=2
       #self.rect.x+=self.dx*self.speed.x*time
       #self.rect.y+=self.dy*self.speed.y*time

       #if self.rect.y<0:
           #self.rect.y+=10
       #if self.rect.y>600:
           #self.rect.y-=10
       #if self.rect.x<0:
           #self.rect.x+=10

       #self.pos.x=self.rect.x
       #self.pos.y=self.rect.y


class Seeker_View:
    def __init__(self):
        self.image=pygame.image.load('seeker.jpg')

class Seeker_controller(Player_controller):
    def __init__(self,player: Seeker, player_view: Seeker_View):
        Player_controller.__init__(self)
        self.player=player
        self.image=player_view.image

    def render(self,surface):
        surface.blit(self.image,self.player.rect)

    def update(self,time):
            print('seeker key update')
            self.player.update(time)
    
    def computer_update(self,time):
        
            self.player.computer_update(time)
  