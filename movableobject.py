from object import *


class Movable_Object(Object):
    def __init__(self,x,y,speed):
        super(Movable_Object,self).__init__(x,y)
        self._pos = pygame.math.Vector2(x,y)
        self.rect = pygame.Rect(self._pos.x,self._pos.y, 0, 0)
        self._speed = pygame.math.Vector2(speed)

    def set_Speed(self,speed):
        self._speed = [speed,speed]
    
    def get_Speed(self):
        return self._speed

    def set_Speed_y(self,speed):
        self._speed.y = speed
    
    def get_Speed_y(self):
        return self._speed.y

    def set_Speed_x(self,speed):
        self._speed.x = speed
    
    def get_Speed_x(self):
        return self._speed.x