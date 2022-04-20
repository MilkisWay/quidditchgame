import pygame 
from unit import Unit
from ball import BallModel
#from collision import CollisionController

class Player(Unit):
    def __init__(self,x,y,speed):
        Unit.__init__(self,x,y,speed)

        self.type = None
        self.pos = pygame.math.Vector2(10,10)
        self.speed=pygame.math.Vector2(0, 0)
        self.acceleration = 0
        self.pointer=1 

    def update(self):
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
            self.pos.x=0
        if self.pos.y>800:
            self.pos.y=0

    def collision_Detection(self,object):
        b=0
        if pygame.sprite.collide_rect(self,object):
            collision_detected = 1
        else:
            collision_detected = 0
        b = collision_detected
        return b

class Player_controller:
    def __init__(self):
        self.players=[]

    def add_player(self,Player):
        all_players = pygame.sprite.Group()
        all_players.add(Player)
        return all_players

    def check_collision(self):
        pass

    def reset(self):
        self.speed =pygame.math.Vector2(0, 0)
        self.acceleration = 0

    def direction_move(self): # показывает, в какую сторону повёрнут  игрок
        if self.speed.x >= 0:
            self.pointer= 1
        else:
            self.pointer = -1

class Player_View:
    def __init__(self, playerController , image):
        self.Player_controller = player_controller
        self.image = pygame.image.load(image)
    def render(self,surface):
        for i in self.Player_controller.players:
            surface.blit(self.image,(i.get_Coord.x(),i.get_Coord.y()))
    

