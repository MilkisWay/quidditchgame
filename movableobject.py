from object import *


class Movable_Object(Object):
    def __init__(self, pos, speed):
        super(Movable_Object,self).__init__(pos)
        self._pos = pygame.math.Vector2(pos)
        self.rect = pygame.Rect(self.pos.x,self.pos.y, 0, 0)
        self._speed = pygame.math.Vector2(speed)

    def set_Speed(self,speed):
        self._speed = speed
    
    def get_Speed(self):
        return self._speed