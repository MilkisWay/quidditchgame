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
    def __init__(self,x,y,speed,acceleration,types,game,image1):
        Player.__init__(self,x,y,speed,acceleration,types,game)
        self.type_name = 'seeker'
        #self.team = team
        #self.control=player\computer
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load(image1)
      
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

    def search(self,  ball, ring):
        min_dist = 5
        max_dist = 100
        target_vector=pygame.math.Vector2(self.pos)
        follower_vector=pygame.math.Vector2(ball.pos)
        new_vector=pygame.math.Vector2(ball.pos)

        distance = follower_vector.distance_to(target_vector)
        if distance > min_dist and ball.possession==False:

            direction_vector= (target_vector - follower_vector) / distance 
            min_step = max(0, distance - max_dist)
            max_step = distance - min_dist
            step_distance= min_step + (max_step - min_step) 
            new_vector= (follower_vector + step_distance*direction_vector)
            self.pos.x=new_vector.x
            self.pos.y=new_vector.y

            self.rect.x=new_vector.x
            self.rect.y=new_vector.y

            if self.pos==ball.pos:
                self.search(self, ring)

    def computer_update_3(self,time):
        w=self.setup.screen_width
        h=self.setup.screen_height
        t=0

        for i in range(0,200):
            x=random.randint(0,w)
            y=random.randint(0,h)
            position=(x,y)
            self.points.append(position)
  
        dir = pygame.math.Vector2(self.points[self.i]) - (self.pos.x, self.pos.y)
        if dir.length() < self.flag_move :
           
            self.pos.x, self.pos.y = self.points[self.i]
            self.i = (self.i + 1) % len(self.points)

        else:
            dir.scale_to_length(self.flag_move)
            new_pos = pygame.math.Vector2(self.pos.x, self.pos.y) + dir*2
            flag=0
            if new_pos.x-self.pos.x>0:
                if flag==0 or flag==-1:
                    self.rotated=pygame.transform.flip(self.image,True,False)
                    flag=1
                elif flag==1:
                    self.rotated=pygame.transform.flip(self.image,False,False)
                    flag=1
            elif new_pos.x-self.pos.x<0:
                if flag==0:
                    self.rotated=pygame.transform.flip(self.image,False,False)
                    flag=-1
                elif flag==1:
                    self.rotated=pygame.transform.flip(self.image,True,False)
                    flag=-1
            self.pos.x, self.pos.y = (new_pos.x, new_pos.y) 
    
class Seeker_View:
    def __init__(self,image1):
        self.image=pygame.image.load(image1)

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