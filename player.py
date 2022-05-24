import pygame 
import random
from unit import Unit
from ball import BallController
from collision import CollisionController
#Нельзя так делать, только через контроллеры
class Player(Unit):
    def __init__(self,x,y,speed, acceleration,activity,types):
        Unit.__init__(self,x,y,speed)
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed, speed)
        self.acceleration = acceleration
        self.pointer=1 
        self.rect = self.image.get_rect()
        self.activity=activity
        self.type = types
        self.health=100

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
            self.dy=random.randint(-1, 1)
            self.dx=random.randint(-1, 1) 
            self.rect.x+=self.dx*self.speed.x*time*0.5
            self.rect.y+=self.dy*self.speed.y*time*0.5

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

    

        #if (self.pos==pos_2.x) and (self.pos.y==pos_2.y):
            #print('круг пойман')
            #search(ball,ring_pos)
            #self.update(time)

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

    def add_player(self,Player):
        self.players.append(Player)


        
    def check_collision(player):
        collision_controller.collision_Detection(player)

class Player_View(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image)

    

