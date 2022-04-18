import pygame
from player import Player
from player import Player_controller
from collision import CollisionController

class Seeker(Player):
     def __init__(self, x,y,speed):
        Player.__init__(self,x,y,speed)

        self.seg_radius=1
        self.type = 'seeker'
        self.image = pygame.Surface((10, 10))
        self.image=pygame.image.load('seeker.jpg')
        self.acceleration = 3
        self.power = 1
        self.snitch = None 
        self.pos = pygame.math.Vector2(30,10)
        self.speed=pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect()

     def seek(self, target,seg_radius):
        print ('seek')
        dist=get_distance(self,target)

        if (dist <= seg_radius):
            self.speed=self.speed*2
            self.acceleration =self.acceleration * 1.5
            if collision_Detection(self):
                self.snitch=1


class Seeker_controller(Player_controller):
    def __init__(self,Seeker):
        Player_controller.__init__(self)
        self.seeker=seeker
        

class Seeker_View:
    def __init__(self, seeker_controller):
        self.seeker_controller=seeker_controller
        self.image=pygame.image.load('seeker.jpg')
    
    def render(self,surface):
        surface.blit(self.image,(self.seeker_controller.get_Coord_x(),self.sekeer_controller.get_Coord_y()))
