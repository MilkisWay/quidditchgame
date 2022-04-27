import pygame 
import random
import math
from unit import Unit
from ball import BallController
from collision import CollisionController
#Нельзя так делать, только через контроллеры

class Player(Unit):
    def __init__(self,x,y,speed, acceleration,activity):
        Unit.__init__(self,x,y,speed)
        self.type = None
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed, speed)
        self.acceleration = acceleration
        self.pointer=1 
        self.rect = self.image.get_rect()
        self.activity=activity

    def update(self,time):

                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.speed.x = -3
                if keystate[pygame.K_RIGHT]:
                    self.speed.x = 3
                if keystate[pygame.K_UP]:
                    self.speed.y = -3
                if keystate[pygame.K_DOWN]:
                    self.speed.y = 3
                self.rect.x += self.speed.x
                self.rect.y+=self.speed.y
                if self.pos.x>1200:
                    self.pos.x-=10
                if self.pos.y>800:
                    self.pos.y-=10

    def computer_update(self,time):
            self.dy=random.randint(-1,1)
            self.dx=random.randint(-1,1) 
            self.rect.x+=self.dx*self.speed.x*time
            self.rect.y+=self.dy*self.speed.y*time

            if self.rect.y<0:
                self.rect.y+=10
            if self.rect.y>600:
                self.rect.y-=100
            if self.rect.x<0:
                self.rect.x+=100
            if self.rect.x>1000:
                self.rect.x-=100


            self.pos.x=self.rect.x
            self.pos.y=self.rect.y

    def search(self,  pos_2):
        min_dist = 25
        max_dist = 100
        target_vector=pygame.math.Vector2(self.pos)
        follower_vector=pygame.math.Vector2(pos_2)
        new_vector=pygame.math.Vector2(pos_2)

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
        if (self.pos.x==pos_2.x) and (self.pos.y==pos_2.y):
            pos_2.x=self.pos.x
            pos_2.y=self.pos_y

    def reset(player):
        player.set_speed(0,0)

    def direction_move(player): # показывает, в какую сторону повёрнут  игрок
        if  player.speed_x>= 0:#У селф нет скорости, обращение через гет из игрока
            player.pointer(1)
        else:
            player.pointer(-1)


class Player_controller:
    def __init__(self):
        self.players=[]
        self.collision_controller=CollisionController(Player)

    def add_player(self,Player):
        self.players.append(Player)


        
    def check_collision(player):
        collision_controller.collision_Detection(player)

class Player_View(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image)

    
    

