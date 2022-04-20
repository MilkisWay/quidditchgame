import pygame
import os
import sys
from player import Player
from player import Player_controller
from pygame.locals import *
from ball import BallModel #Доступ только через контроллер. К данным шара так доступа нет
from collision import CollisionController
from quaffle import QuaffleModel #Тоже самое, что и выше

class Hunter(Player):
    def __init__(self,x,y,speed):
        Player.__init__(self,x,y,speed)
        
        self.type = 'hunter'
        #self.team = team
        self.image = pygame.Surface((10, 10))
      
        self.image=pygame.image.load('hunter.jpg')#должно быть во вью
     
        self.acceleration = 1
        self.power = 10
        self.quaffle = None
        self.pos = pygame.math.Vector2(30,10)
        self.speed=pygame.math.Vector2(0,0)#Тоже, что и в охотнике
        self.rect = self.image.get_rect()

    def checkQuaffle(self, quaffle):#Во-первых все взаимодействия в контроллере, во-вторых этим ты не управляешь
        if self.collision_Detection(quaffle):
            if quaffle.possession==False:
                self.quaffle=quaffle
                quaffle.possession=True
                quaffle.pos.x=self.pos.x
                quaffle.pos.y=self.pos.y
                quaffle.rect.x = self.rect.x
                quaffle.rect.y+=self.rect.y
              
                #print(quaffle.pos.x, quaffle.pos.y)
                print('check')

    def throw(self,quaffle):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


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

