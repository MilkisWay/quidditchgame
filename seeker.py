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
    def __init__(self,x,y,speed,acceleration,activity,types,type_name,game):
        Player.__init__(self,x,y,speed,acceleration,activity,types,type_name,game)
        self.type = 'seeker'
        #self.team = team
        #self.control=player\computer
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
        self.quaffle=None
        self.shoot_power=30
        self.type=types
        self.game=game 
        self.setup=self.game.setup
        self.health=100
        self.rotated=self.image
        self.rotated_computer=self.image
        self.type_name=type_name

    def search(self,  ball, time, ring):
        min_dist = 25
        max_dist = 100
        target_vector=pygame.math.Vector2(self.pos)
        follower_vector=pygame.math.Vector2(ball.pos)
        new_vector=pygame.math.Vector2(ball.pos)

        distance = follower_vector.distance_to(target_vector)
        if distance > min_dist:
            direction_vector= (target_vector - follower_vector) / distance 
            min_step = max(0, distance - max_dist)
            max_step = distance - min_dist
            step_distance= min_step + (max_step - min_step) 
            new_vector= (follower_vector + step_distance*direction_vector)
            self.pos.x=new_vector.x
            self.pos.y=new_vector.y

            self.rect.x=new_vector.x
            self.rect.y=new_vector.y
        
        if (self.pos.x==ball.pos.x or self.pos.y==ball.pos.y):
            ball.holder=self
            self.quaffle=ball
 
            ball.update(time)


class Seeker_View:
    def __init__(self):
        self.image=pygame.image.load('seeker.jpg')

class Seeker_controller(Player_controller):
    def __init__(self,player: Seeker, player_view: Seeker_View):
        Player_controller.__init__(self)
        self.player=player
        self.image=player_view.image

    def render_computer(self,surface):
        surface.blit(self.player.rotated_computer, self.player.rect)

    def render(self,surface):
        surface.blit(self.image,self.player.rect)

    def render(self,surface):
        surface.blit(self.player.rotated,self.player.rect)

    def shoot(self):
       pass

    def update(self,time):
            self.player.update(time)
    
    def computer_update(self,time):
            self.player.computer_update(time)
  
