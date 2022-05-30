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
    def __init__(self,x,y,speed,acceleration,types,game):
        Player.__init__(self,x,y,speed,acceleration,types,game)
        self.type_name = 'seeker'
        #self.team = team
        #self.control=player\computer
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('player.png')
      
        self.gameStop = False
        self.acceleration = acceleration
        self.power = 0
        self.snitch = None
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.rect = self.image.get_rect()
        self.quaffle=None
        self.shoot_power=30
        self.type=types
        self.game=game 
        self.setup=self.game.setup
        self.health=100
        self.rotated=self.image
        self.rotated_computer=self.image
        self.flag_move=20
        self.next_pos_index=1
        self.i=1
        self.points=[]
        self.points_1=[]
    
class Seeker_View:
    def __init__(self):
        self.image=pygame.image.load('player.png')

class Seeker_controller(Player_controller):
    def __init__(self,player: Seeker, player_view: Seeker_View):
        Player_controller.__init__(self)
        self.player=player
        self.image=player_view.image

    def render_computer(self,surface):
        surface.blit(self.player.rotated_computer,(self.player.pos.x,self.player.pos.y))

    def render(self,surface):
        surface.blit(self.player.rotated,(self.player.pos.x,self.player.pos.y))

    def update(self,time):
        self.player.update(time)
    
    def computer_update(self,time):
        self.player.computer_update(time)