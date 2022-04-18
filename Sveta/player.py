import pygame 
from unit import Unit
from collision import CollisionController

class Player(Unit):
    def __init__(self,x,y,speed):
        Unit.__init__(self,x,y,speed)

        self.type = None
        self.pos = pygame.math.Vector2(10,10)
        self.speed=pygame.math.Vector2(0, 0)
        self.acceleration = 0
        self.pointer=1 

class Player_controller:
    def __init__(self):
        self.players=[]

    def player_control(self, direction):
            if direction=="left":
                t=pygame.math.Vector2(-0.5, 0)
            elif direction=="right":
                t=pygame.math.Vector2(0.5, 0)
            elif direction== "up":
                t=pygame.math.Vector2(0, -0.5)
            elif direction== "down":
                t=pygame.math.Vector2 (0, 0.5)
            self.acceleration += 0.9
            self.speed+=t

    def _update(self):
        collision_Detection()

    def direction_move(self): # показывает, в какую сторону повёрнут  игрок
        if self.speed.x >= 0:
            self.pointer= 1
        else:
            self.pointer = -1

    def reset(self):
        self.speed =pygame.math.Vector2(0, 0)
        self.acceleration = 0

    def add_player(self,x,y,speed):
        self.players.append(Player(x,y,speed))

class Player_View:
    def __init__(self, playerController , image):
        self.Player_controller = player_controller
        self.image = pygame.image.load(image)
    def render(self,surface):
        for i in self.Player_controller.players:
            surface.blit(self.image,(i.get_Coord.x(),i.get_Coord.y()))

    

