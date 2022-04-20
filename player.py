import pygame 
from unit import Unit
from ball import BallController
from collision import CollisionController
#Нельзя так делать, только через контроллеры
class Player(Unit):
    def __init__(self,x,y,speed):
        Unit.__init__(self,x,y,speed)
        self.type = None
        self._pos = pygame.math.Vector2(10,10)
        self._speed=pygame.math.Vector2(speed, speed)
        self.acceleration = 0
        self._pointer=1 
        self.rect = self.image.get_rect()

    def set_speed(self,x,y):
         self._speed=pygame.math.Vector2(x, y)

    def get_speed(self):
        return self._speed

    def set_speed_x(self,x):
        self._speed.x=x

    def get_speed_x(self):
        return self._speed.x

    def set_speed_y(self,y):
        self._speed.y=y

    def get_speed_y(self):
        return self._speed.y

    def set_pointer(self,y):
        self._pointer=y

    def get_pointer(self):
        return self._pointer

    def set_speed_x(self,x):
        self._speed.x=x

    def get_speed_x(self):
        return self._speed.x

class Player_controller:
    def __init__(self,Player):
        self.players=[]
        self.collision_controller=CollisionController(Player)

    def add_player(self,Player):
        all_players = pygame.sprite.Group()
        all_players.add(Player)
        self.players=all_players

    def update(player): #Это в контроллере, и обращение через get
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            player.set_speed_x(-3)
        if keystate[pygame.K_RIGHT]:
            player.set_speed_x(3)
        if keystate[pygame.K_UP]:
            player.set_speed_y(-3)
        if keystate[pygame.K_DOWN]:
            player.set_speed_y(3)

        player.rect.x += player.speed.x
        player.rect.y+=player.speed.y
        
        if player.get_Coord_x>1200:
           player.set_Coord_x(0)
        if player.get_Coord_y>800:
           player.set_Coord_y(0)
        
    def check_collision(player):
        collision_controller.collision_Detection(player)

    def reset(player):
        player.set_speed(0,0)

    def direction_move(player): # показывает, в какую сторону повёрнут  игрок
        if  player.get_speed_x>= 0:#У селф нет скорости, обращение через гет из игрока
            player.set_pointer(1)
        else:
            player.set_pointer(-1)

class Player_View:
    def __init__(self, playerController , image):
        self.Player_controller = player_controller
        self.image = pygame.image.load(image)

    def render(self,surface):
        for i in self.Player_controller.players:
            surface.blit(self.image,(i.get_Coord.x(),i.get_Coord.y()))

    

