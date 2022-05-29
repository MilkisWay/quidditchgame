import pygame 
import random
from unit import Unit
from ball import BallController
from collision import CollisionController
#Нельзя так делать, только через контроллеры
class Player(Unit):
    def __init__(self,x,y,speed, acceleration,activity,types,type_name,game):
        Unit.__init__(self,x,y,speed)
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.acceleration = acceleration
        self.pointer=1 
        self.rect = self.image.get_rect()
        self.activity=activity
        self.type = types
        self.health=100
        self.game=game
        self.setup=self.game.setup
        self.rotated=self.image
        self.rotated_computer=self.image
        self.type_name=type_name

    def update(self,time):

                t=0
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.speed.x = -10
                    self.pos.x-=10
                    if t==0:
                        self.rotated=pygame.transform.flip(self.image,False,False)
                        t=-1
                    elif t==1:
                        self.rotated=pygame.transform.flip(self.image,True,False)
                        t=-1
                elif keystate[pygame.K_RIGHT]:
                    self.speed.x= 10
                    self.pos.x+=10
                    if t==0 or t==-1:
                        self.rotated=pygame.transform.flip(self.image,True,False)
                        t=1
                    elif t==1:
                        self.rotated=pygame.transform.flip(self.image,False,False)
                        t=1
                elif keystate[pygame.K_UP]:
                    self.speed.y = -10
                    self.pos.y-=10
                elif keystate[pygame.K_DOWN]:
                    self.speed.y = 10
                    self.pos.y+=10
                else:
                    self.speed.x=0
                    self.speed.y=0
                self.rect.x+=self.speed.x
                self.rect.y+=self.speed.y
                if self.pos.x>self.setup.screen_width:
                    self.pos.x-=10
                if self.pos.y>self.setup.screen_height:
                    self.pos.y-=10
                self.rect.clamp_ip(self.game.screen_rect)

                return self.rotated


    def computer_update(self,time):
        #self.angle = random.uniform(-1, 1)
        #self.dy = math.sin(self.angle * math.pi/2)
        #self.dx = math.cos(self.angle * math.pi/2)
        #x=self.dx*self.speed.x*time*0.5
        self.dy=random.randint(-1, 1)
        self.dx=random.randint(-1, 1) 
        x=self.dx*self.speed.x*time*0.5


        flag=0
        if x>0:
            print('1')
            if flag==0 or flag==-1:
                self.rotated_computer=pygame.transform.flip(self.image,True,False)
                flag=1
            elif flag==1:
                self.rotated_computer=pygame.transform.flip(self.image,False,False)
                flag=1
        elif x<0:
            print('2')
            if flag==0:
                self.rotated_computer=pygame.transform.flip(self.image,False,False)
                flag=-1
            elif flag==1:
                self.rotated_computer=pygame.transform.flip(self.image,True,False)
                flag=-1
        self.rect.y+=self.dy*self.speed.y*time*0.5
        self.rect.x+=self.dx*self.speed.x*time*0.5

        if self.rect.y<0:
                self.rect.y=0
        if self.rect.y>600:
                self.rect.y-=100
        if self.rect.x<0:
                self.rect.x=0
        if self.rect.x>1300:
                self.rect.x-=100
        self.rect.y+=self.dy*self.speed.y*time*0.5
        self.rect.x+=self.dx*self.speed.x*time*0.5
        self.pos.x+=self.rect.x
        self.pos.y+=self.rect.y
        self.rect.clamp_ip(self.game.screen_rect)
        return self.rotated_computer
            
    

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

    

