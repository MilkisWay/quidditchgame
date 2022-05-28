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

    def __init__(self,x,y,speed,acceleration,activity,types):
        Player.__init__(self,x,y,speed,acceleration,activity,types)
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
        self.type=types
        self.main_radius=8
        self.head_radius=4
        self.dx1=5
        self.dy1=-3
        self.hand_radius=1
        self.dx2=4
        self.dy2=1
        self.count=0
    
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
 
            ball.update(time,ring)
            self.computer_update(time)

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
            self.player.count+=1
   
    def computer_update(self,time):
            self.player.computer_update(time)