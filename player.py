import pygame 
import random
import numpy
from unit import Unit
from ball import BallController
from collision import CollisionController
#Нельзя так делать, только через контроллеры
class Player(Unit):
    def __init__(self,x,y,speed, acceleration,types,game):
        Unit.__init__(self,x,y,speed)
        self.pos = pygame.math.Vector2(x,y)
        self.speed=pygame.math.Vector2(speed,speed)
        self.acceleration = acceleration
        self.pointer=1 
        self.rect = self.image.get_rect()
        self.rect = pygame.transform.scale(self.image,(8,8))
        self.x=0
        self.y=0
        self.type = types
        self.health=100
        self.game=game
        self.setup=self.game.setup
        self.rotated=self.image
        self.rotated_computer=self.image
        self.flag_move=5
        self.next_pos_index=1
        self.i=1
        self.points=[]
        self.points_1=[]


    def search(self, pos,time):
        min_dist = 100
        max_dist = 100
        target_vector=pygame.math.Vector2(self.pos)
        follower_vector=pygame.math.Vector2(pos)
        new_vector=pygame.math.Vector2(pos)

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
       

    def update(self,time):

                t=0
                keystate = pygame.key.get_pressed()
                if keystate[pygame.K_LEFT]:
                    self.speed.x =- 10
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

                #self.rect.x+=self.speed.x
                #self.rect.y+=self.speed.y

                if self.pos.x>self.setup.screen_width:
                    self.pos.x=10
                if self.pos.y>self.setup.screen_height:
                    self.pos.y=10
                if self.pos.x<0:
                    self.pos.x=10
                if self.pos.y<0:
                    self.pos.y=10


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
            if flag==0 or flag==-1:
                self.rotated_computer=pygame.transform.flip(self.image,True,False)
                flag=1
            elif flag==1:
                self.rotated_computer=pygame.transform.flip(self.image,False,False)
                flag=1
        elif x<0:
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
        if self.rect.y>self.setup.screen_height:
                self.rect.y-=100
        if self.rect.x<0:
                self.rect.x=0
        if self.rect.x>self.setup.screen_height:
                self.rect.x-=100

        self.pos.y+=self.dy*self.speed.y*0.5
        self.pos.x+=self.dx*self.speed.x*0.5

        return self.rotated_computer

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
                    self.rotated_computer=pygame.transform.flip(self.image,True,False)
                    flag=1
                elif flag==1:
                    self.rotated_computer=pygame.transform.flip(self.image,False,False)
                    flag=1
            elif new_pos.x-self.pos.x<0:
                if flag==0:
                    self.rotated_computer=pygame.transform.flip(self.image,False,False)
                    flag=-1
                elif flag==1:
                    self.rotated_computer=pygame.transform.flip(self.image,True,False)
                    flag=-1
            self.pos.x, self.pos.y = (new_pos.x, new_pos.y)

    def computer_update_2(self, time):
        n=100
        x = numpy.zeros(n)
        y = numpy.zeros(n)
        for i in range(1, n):
            val = random.randint(1, 4)
            if val == 1:
                x[i] = x[i - 1] + 1
                y[i] = y[i - 1]
            elif val == 2:
                x[i] = x[i - 1] - 1
                y[i] = y[i - 1]
            elif val == 3:
                x[i] = x[i - 1]
                y[i] = y[i - 1] + 1
            else:
                x[i] = x[i - 1]
                y[i] = y[i - 1] - 1

            self.pos.x+=x[i]
            self.pos.y+=y[i]
            self.rect.x+=x[i]
            self.rect.y+=y[i]
    

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
        pass

class Player_View(pygame.sprite.Sprite):
    def __init__(self, image):
        self.image = pygame.image.load(image)

    

